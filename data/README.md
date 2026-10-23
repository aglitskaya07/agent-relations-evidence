# Data

Three labeled samples, one JSON object per line. Together they cover 138 MCP servers.

| File | Rows | Labeled servers | Sample |
|---|---:|---:|---|
| `dataset-pilot-2026-07-29.jsonl` | 13 | 11 | Pilot. Picked by hand and deliberately including known poles, to check that the scale discriminates. |
| `dataset-wave-2026-07-29.jsonl` | 106 | 80 | Broad wave from the official registry, npm download tops, PulseMCP, Smithery, Docker, claude.ai connectors. |
| `dataset-brands-2026-07-30.jsonl` | 50 | 47 | Well-known brands: Docker MCP Catalog and the most-starred GitHub repositories. |

Rows without a group are units that were dropped: not actually an MCP server (`not-a-server`), a binary wrapper, a missing path, or a server that refused access without a key. 11 non-servers and 18 key-gated servers are excluded from all statistics.

Final distribution across the 138 servers:

| Group | Meaning | Pilot | Wave | Brands | Total |
|---|---|---:|---:|---:|---:|
| D | manipulates | 1 | 1 | 0 | 2 |
| C | captures (hard push) | 3 | 14 | 10 | 27 |
| B | promotes itself | 2 | 10 | 7 | 19 |
| A | informs | 3 | 53 | 27 | 83 |
| A+ | protects the user | 2 | 2 | 3 | 7 |
| | hard push (C + D) | 36% | 19% | 21% | 21% |

The pilot share is high on purpose: it was seeded with the poles.

## Fields

Not every file has every field; the pilot was labeled before the main protocol was fixed.

| Field | What it holds |
|---|---|
| `unit` | Server identifier as captured (npm package, registry name, connector name or repository). |
| `title`, `server`, `version`, `repo`, `stars`, `npm`, `hosted_url`, `popularity` | Identification and popularity signals at capture time. |
| `date` | Capture date. |
| `codebook` | Codebook version used (`v1.0` for the wave and brands, `v0.1` for the pilot). |
| `source_frame(s)` | Which sampling frame the server came from. Frame snapshots are in `../raw-captures/wave_2026-07-29/sampling-frames_2026-07-29.tgz` and `../raw-captures/brands_2026-07-30/sample50_frame.json`. |
| `category`, `vendor_type`, `transport` | Topic category, official vendor vs community wrapper vs platform connector, and how the server was reached. Categories were assigned by the author by hand. |
| `dossier_file`, `dossier_chars` | Path to the dossier with the exact vendor text the raters saw (instructions block and tool descriptions), and its length. |
| `skipped` | Why the unit was dropped, if it was. |
| `extraction`, `extraction_notes` | How the text was obtained and whether coverage was complete. |
| `votes` | Groups given by the three independent raters. |
| `votes_run2_reliability` | Pilot only: a second rating run to check stability. |
| `consensus_group` | Majority group. |
| `adjudication_needed`, `final_group` | Whether raters fully disagreed, and the group after adjudication and the skeptic pass. |
| `verdicts` | Each rater's group plus the techniques found, each with a verbatim `quote` and the `channel` it came from (`instructions` or `tool_description:<tool>`). |
| `skeptic` | The skeptic's pass on hard findings: per technique `confirmed` or not, a reason, and an `uphold` / `downgrade` recommendation. |

**Language.** Quotes from servers are verbatim English. The raters' and skeptic's own annotations (technique names, reasons, notes) were written in Russian and are kept as recorded, untranslated, so the data stays raw. The codebook explains every technique in English: `../codebook/codebook-v1.0.md`.

Raters and skeptics were language models. See the main README for limitations.

## Formulations catalog

`formulations-catalog-2026-07-30.json` groups the hard formulations into eight classes, with one representative verbatim quote per server and class (51 quotes in total). `label_en` is the English class name, `label` the original Russian one. Every quote was machine-checked against the captured dossiers. The full set of findings is in the `verdicts` of the three datasets.
