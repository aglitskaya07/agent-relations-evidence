#!/usr/bin/env python3
"""Assembles the unit group from Jev's per-sentence answers and compares it with the LLM raters' labels.

Codebook rule: unit group = worst technique. For Jev, a technique counts if the
sum of probabilities of that group's options in a sentence is >= the threshold. A+ is assigned if
there is no B, C or D and there is a protective sentence above the threshold.

python compare.py pilot|full|units [--show unit]
"""
import json, os, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = ROOT  # inputs/outputs sit next to the scripts
sys.path.insert(0, ROOT)
from run_jev import GROUP_OF, RANK

mode = sys.argv[1]
show = sys.argv[sys.argv.index("--show") + 1] if "--show" in sys.argv else None
rows = [json.loads(l) for l in open(os.path.join(OUT, f"sentences_{mode}.jsonl"), encoding="utf-8")]
units = json.load(open(os.path.join(OUT, f"units_{mode}.json"), encoding="utf-8"))
by_unit = defaultdict(list)
for r in rows:
    by_unit[r["unit"]].append(r)


def group_mass(r):
    m = Counter()
    for opt, p in (r["probabilities"] or {}).items():
        m[GROUP_OF[opt]] += p
    return m


def unit_group(sents, t):
    worst, protective = "A", False
    for r in sents:
        m = group_mass(r)
        for g in ("D", "C", "B"):
            if m[g] >= t and RANK[g] > RANK[worst]:
                worst = g
        if m["A+"] >= t:
            protective = True
    if worst == "A" and protective:
        return "A+"
    return worst


def coarse(g):  # hard / soft / clean
    return {"D": "hard", "C": "hard", "B": "soft", "A": "clean", "A+": "clean"}[g]


def kappa(pairs):
    labs = sorted({x for p in pairs for x in p})
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[l] * cb[l] for l in labs) / n / n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


report = {"mode": mode, "units": len(units), "thresholds": []}
print(f"units {len(units)}, sentences {len(rows)}")
print("threshold | exact group match | kappa | hard/soft/clean match | hard for Jev / for LLM")
for t in (0.5, 0.6, 0.7, 0.8, 0.9, 0.95):
    pairs = [(u["label"], unit_group(by_unit.get(u["unit"], []), t)) for u in units]
    exact = sum(a == b for a, b in pairs) / len(pairs)
    cpairs = [(coarse(a), coarse(b)) for a, b in pairs]
    cexact = sum(a == b for a, b in cpairs) / len(cpairs)
    hard_j = sum(coarse(b) == "hard" for _, b in pairs)
    hard_l = sum(coarse(a) == "hard" for a, _ in pairs)
    print(f"{t:.2f} | {exact:.1%} | {kappa(pairs):.2f} | {cexact:.1%} | {hard_j} / {hard_l}")
    report["thresholds"].append({"t": t, "exact": round(exact, 3), "kappa": round(kappa(pairs), 3),
                                 "coarse_exact": round(cexact, 3), "hard_jev": hard_j, "hard_llm": hard_l,
                                 "confusion": Counter(f"{a}->{b}" for a, b in pairs)})

best = max(report["thresholds"], key=lambda x: x["kappa"])
t = best["t"]
print(f"\nbest threshold by kappa: {t}; LLM->Jev matrix:", dict(best["confusion"]))
diff = []
for u in units:
    j = unit_group(by_unit.get(u["unit"], []), t)
    if j != u["label"]:
        top = sorted(by_unit.get(u["unit"], []), key=lambda r: -max(group_mass(r)[g] for g in ("D", "C", "B")))[:3]
        diff.append({"unit": u["unit"], "frame": u["frame"], "llm": u["label"], "jev": j,
                     "top_sentences": [{"choice": r["choice"], "conf": r["confidence"], "sentence": r["sentence"][:220]} for r in top]})
report["best_t"] = t
report["disagreements"] = diff
json.dump(report, open(os.path.join(OUT, f"compare_{mode}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=dict)
print(f"disagreements at threshold {t}: {len(diff)}")
for d in diff[:40]:
    print(f"- {d['unit']} [{d['frame']}]: LLM {d['llm']} → Jev {d['jev']}")
    for s in d["top_sentences"][:2]:
        print(f"    {s['choice']} ({s['conf']:.2f}): {s['sentence']}")

if show:
    print(f"\n== {show}")
    for r in sorted(by_unit[show], key=lambda r: -max(group_mass(r)[g] for g in ('D', 'C', 'B')))[:15]:
        print(f"  {r['choice']} {r['confidence']:.2f} | {r['sentence'][:200]}")
