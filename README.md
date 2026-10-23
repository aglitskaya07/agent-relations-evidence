# Agent relations: evidence pack

Data behind the study **«Мелкий шрифт, который читаю не я: как MCP-коннекторы манипулируют нашими агентами»** (*Fine print I don't read: how MCP connectors manipulate our agents*), Nailia Aglitskaya, October 2026.
Article (Russian): https://nailia.work/agent-relations/

When you connect an MCP server to an AI agent, the server sends the agent two texts the user never sees: an `instructions` block and a description for every tool. Both sit next to the system prompt in every session. This pack documents how vendors use that channel to promote themselves to the agent, from plain description to steering and manipulation, and contains everything needed to check the findings.

## Key findings

| | |
|---|---|
| Servers labeled | 138 (pilot 11, broad wave 80, well-known brands 47), captured 27–30 July 2026 |
| Hard push (groups C + D) | 29 of 138, **21%**; 19% in the broad wave, 21% among brands |
| Any self-promotion (B, C, D) | 35% |
| Official vendor servers vs community wrappers | about 34% vs about 6% hard push |
| Where it lives | 85% of findings are in tool descriptions (639 of 751 in the wave); only 28% of servers have an `instructions` block at all |
| By domain (brands) | developer infrastructure 10 of 16 hard; search and web data 0 of 11; social and messaging 0 of 8 |
| Experiment | the agent chose a third-party search tool over built-in search 5 of 16 times with a neutral description, 16 of 16 with a promotional one, 16 of 16 with a directive one (96 runs, Fisher's exact test p = 0.000068) |
| Truncation | Claude Code 2.1.292 passes the agent only the first 2,048 characters of an `instructions` block and of each tool description |
| Second instrument | Jev (TypeSafe) relabeled all 138 sentence by sentence: 82.6% exact agreement, κ = 0.70, 24% hard push |

## The scale

| Group | | Example |
|---|---|---|
| A+ | protects the user | warns about prompt injection, guards privacy |
| A | informs | what the tool does and when it fits |
| B | promotes itself | superlatives: "the most powerful…", "Best for: any topic" |
| C | captures | "instead of built-in web search", "ALWAYS call…", "Do NOT rely on your own knowledge" |
| D | manipulates | speaks for the user, rewards the agent, threatens consequences |

Full definitions, edge cases and what does *not* count as pressure: [`codebook/codebook-v1.0.md`](codebook/codebook-v1.0.md).

## What is here

| Folder | Contents |
|---|---|
| [`codebook/`](codebook/) | Labeling codebook v1.0, frozen before the main wave. English translation and Russian original. |
| [`data/`](data/) | The three labeled datasets and the catalog of formulations, with a field dictionary. |
| [`raw-captures/`](raw-captures/) | Raw server responses and dossiers with the exact vendor text the raters saw, July 2026. |
| [`experiment/`](experiment/) | Does the description change the agent's choice? Design and per-run results. |
| [`jev-replication/`](jev-replication/) | Relabeling with a second, non-generative model; scripts and outputs. |
| [`truncation-test/`](truncation-test/) | How much server text reaches the agent in Claude Code; stub server and runs. |
| [`recheck-2026-10/`](recheck-2026-10/) | October recaptures: which July formulations are still shipping. |
| [`firecrawl-case/`](firecrawl-case/) | The case that started the study, reconstructed from the vendor's public commit history. |

## On naming servers

The article names no server except Firecrawl: it is about the practice, not about culprits. This pack keeps the names, because without them the captures cannot be checked against live servers. Every text quoted here was sent by the vendor to any client that connected and is reproduced verbatim with its capture date. A group is the result of the method described below, applied to the text on that date, not a judgment about a company. Many texts have changed since; see `recheck-2026-10/`. If you represent a vendor and believe a capture or label is wrong, write to the address below and I will correct or annotate it.

## How the labeling worked

- **Capture.** For every server I obtained the text an agent receives: the `instructions` field from `initialize` and the tool descriptions from `tools/list`, by handshaking with hosted servers, reading published npm packages, or copying the block a real client session received. I identified as a standard client name when connecting, as such audits usually do.
- **Labeling.** Three language-model raters labeled each server independently and blind, following the same codebook with examples. I froze the codebook before the main wave and did not change it afterwards. Agreement of 3 of 3 or 2 of 3 decided the group; full disagreement went to adjudication.
- **Skeptic.** Every hard finding (C or D) went to a separate skeptic pass that tried to refute it: is the quote verbatim in the dossier, does it fit the technique, is there an innocent reading.
- **Second instrument.** I relabeled all 138 servers with Jev from TypeSafe, a model that does not write text but only chooses a class for each sentence. See `jev-replication/`.
- **Human check.** I re-read the key findings myself against the raw captures. All quotes were machine-checked for verbatim presence in the dossiers.

## Limitations

- **The raters are language models.** The pilot was labeled by models of one family, the wave and brands by another. Jev agreed with the original labels in 82.6% of cases (κ = 0.70) and was stricter, with 24% hard push instead of 21%. That is agreement between two instruments, not proof of correctness. Beyond my own re-reading of the key findings, there has been no systematic human labeling of a subsample.
- **Four brand findings did not get through the skeptic**, because the skeptic runs failed on service errors. The other six that were checked held up.
- **The sample leans toward popular servers** from npm, GitHub and catalogs. The Python part of the ecosystem is barely represented. 18 servers refused access without a key and are not in the statistics.
- **npm package texts were read from the package code**, not requested from a running server.
- **The experiment fed descriptions in the prompt**, not through a real MCP server, on one model, 16 runs per condition. That delivery is weaker than the real one, so the 69-point shift is more likely a lower bound of the effect. The runs were executed as subagents inside the author's own Claude Code session, whose global instructions rank Firecrawl first for web search; 2 of the 48 second-version justifications refer to "the user's priorities". This may raise the vendor share in all three conditions. It does not explain the gap between them, but the absolute levels are not clean.
- **The truncation test** covers one version of Claude Code (2.1.292). Other clients were not measured.
- **I do not claim causality** between my audit and Firecrawl's rollback. The vendor documented its own reason.
- **Some pull requests referenced in the Firecrawl case are unmerged.** They are the team's working experiments, not company policy.

## Check it yourself

Any stdio MCP server can be asked for exactly what an agent receives:

```bash
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"audit","version":"1.0"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
| npx -y <npm-package-of-the-server>
```

The first response carries `instructions`, the second the tool descriptions. Some servers need an API key in the environment just to start. A step-by-step reproduction for Firecrawl, including the hosted server, is in [`firecrawl-case/`](firecrawl-case/).

To audit the servers connected to your own agent, use the prompt in the "для агента" mode of the article.

## License and citation

Text, data and code in this repository: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quoted server texts belong to their vendors and are reproduced for research and criticism.

> Aglitskaya, N. (2026). *Agent relations: how MCP servers steer AI agents. Evidence pack.* https://nailia.work/agent-relations/

Contact: Nailia Aglitskaya · pr.aglickaya@gmail.com
