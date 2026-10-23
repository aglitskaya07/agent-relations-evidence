# Raw captures, July 2026

What each server sent to an agent, captured 27–30 July 2026.

- `*_hosted*_run1.json`, `*_run2.json` — handshakes with hosted servers (`initialize` + `tools/list`), two independent runs. Each file records the URL, capture time in UTC, the client name used, whether a key was used (`auth`), every protocol step, `instructions` and `tools`. Keys are never stored.
- `hosted-mcp-firecrawl-dev_instructions_2026-07-27.txt` and `…_2026-07-29.txt` — the Firecrawl hosted `instructions` before and after the July 29 rewrite.
- `*_session-copy*.md` — the block a real client session (Claude Code, claude.ai) received, copied verbatim from the agent's system prompt. Headers are in Russian.
- `dossiers_2026-07-29/`, `wave_2026-07-29/dossiers/`, `brands_2026-07-30/dossiers/` — one dossier per server with the exact vendor text the raters saw. Datasets point to them via `dossier_file`.
- `wave_2026-07-29/sampling-frames_2026-07-29.tgz`, `brands_2026-07-30/sample50_frame.json` — snapshots of the catalogs the samples were drawn from.
- `firecrawl_hosted_2026-09-14_keyless.json` — a later Firecrawl capture.

Researcher notes inside dossiers and session copies are in Russian; vendor texts are verbatim.
