# UNIT: projscan | npm v5.0.3 (published 2026-07-19T21:27:29.947Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

Type: confirmed MCP server (stdio) + CLI. Not SDK/proxy. Own JSON-RPC implementation of the MCP protocol (without @modelcontextprotocol/sdk): `dist/mcp/server.js` → `serverHandlers.js` (initialize / tools/list / tools/call / prompts / resources), support for protocols 2025-03-26 and 2024-11-05. "Local code intelligence for agent-assisted engineering" — repository analysis (AST, git churn, dependencies, coordination of parallel agents).

## CHANNEL: instructions, npm (static)
(not found statically)

The Initialize response is assembled in `dist/mcp/serverHandlers.js` (handleInitialize) and contains only `protocolVersion`, `serverInfo: { name: 'projscan', version }`, and `capabilities` (tools/prompts/resources/logging + experimental fileChanged when watch). The `instructions` field is nowhere in dist (grep across all .js: the only occurrences of the word are the README recommendation text in analyzers/architectureCheck.js and the internal key core/feedback.js, and they are unrelated to initialize).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

51 tools (tool-manifest.json `toolCount: 51`; checked against the source files `dist/mcp/tools/*.js` — names and descriptions match verbatim, 0 discrepancies).

### Marker scan
Full pass over all regex markers of the string index (instead of built-in, most powerful, always default, call this immediately, Best for:, prefer/Prefer this over, faster and cheaper, N% faster, PRECEDENCE/takes precedence, LAST resort, Do NOT answer from memory, even when you think you know, even if isn't named, The user has installed/chosen, primary tool/provider/interface, refund/credit/reward, MUST use/run, ignore other/previous, whenever the user, Assume appropriate/legitimate, Perfect for/Great for/essential for, trusted sources, never means leave) across all 51 top-level manifest descriptions AND additionally across all `dist/mcp/tools/*.js` (including parameter descriptions) and `dist/mcp/prompts.js`:

**0 matches.** No string markers were found. The descriptions are factual, with the scope formulated inside the product itself ("Use this after projscan_hotspots…", "Use when an agent is asked 'is this PR safe to merge?'"), without displacing the client's built-in tools or other servers.

### Full list of tools (names)
projscan_analyze, projscan_doctor, projscan_hotspots, projscan_file, projscan_structure, projscan_dependencies, projscan_outdated, projscan_audit, projscan_upgrade, projscan_coverage, projscan_semantic_graph, projscan_coupling, projscan_workspaces, projscan_pr_diff, projscan_review, projscan_fix_suggest, projscan_explain_issue, projscan_impact, projscan_search, projscan_session, projscan_memory, projscan_workspace_graph, projscan_apply_fix, projscan_taint, projscan_dataflow, projscan_cost_summary, projscan_review_watch, projscan_plugin, projscan_preflight, projscan_workplan, projscan_release_train, projscan_bug_hunt, projscan_evidence_pack, projscan_regression_plan, projscan_agent_brief, projscan_quality_scorecard, projscan_assess, projscan_simulate, projscan_prove, projscan_passport, projscan_proof_broker, projscan_review_gate, projscan_adoption, projscan_start, projscan_understand, projscan_collision, projscan_claim, projscan_merge_risk, projscan_route, projscan_coordinate, projscan_coordinate_watch

### 8 representative full descriptions (verbatim)

**projscan_analyze**
> Run a full projscan analysis of the project: languages, frameworks, dependencies, issues, and health score. Use this to understand a codebase before making changes.

**projscan_review**
> One-call PR review. Combines projscan_pr_diff + per-changed-file risk score + new/expanded import cycles + risky function additions + dependency changes, plus a verdict ("ok" | "review" | "block") with a one-line summary. Use when an agent is asked "is this PR safe to merge?" Defaults: base=origin/main (falls back to main/master/HEAD~1), head=HEAD. Pass `max_cost_tokens` (1.5+) to get a budget-shaped response: <3000 returns verdict-only, <7000 returns a summary, otherwise the full review. 1.9+: pass `intent` (a free-text PR description like "refactor auth middleware" or "docs: fix codex setup") to get an intent-grounded review — each finding is labelled expected / unexpected / out-of-scope against the stated intent. Verdict is unchanged; this is an extra narration layer.

**projscan_cost_summary**
> Aggregate token-cost analytics from the current session's tool-call history. action:"snapshot" (default) returns total tokens spent, top spenders, per-tool typical/p95 estimates, and a static expected-cost catalog so the agent can budget pre-call. 1.10+: action:"start_stream" / "stop_stream" / "list_streams" turns this into a live cost dashboard — the server polls the session log on an interval and emits notifications/projscan/cost_delta whenever new tool calls have accrued, with the per-tool deltas and the new cumulative totals inline. Pairs with the `_cost` sidecar attached to every tool result. Read-only. Note: the session event log is bounded at 500 entries — for long-running sessions, older calls are dropped from the snapshot.

**projscan_search**
> Ranked search across the project. Lexical (BM25) by default; optional semantic (vector) and hybrid (RRF fusion) modes available when the @xenova/transformers peer dependency is installed. Scope controls what to search: "auto"/"content" (ranked content matches with excerpts), "symbols" (exported names), "files" (path substring).

**projscan_prove**
> Create, record, or replay a local Proof Contract for a change. Returns allowed files, forbidden files, proof commands, ledger evidence, scope drift, a reviewer-ready Proof Receipt, and verifiedWorkflow status for agent handoff.

**projscan_route**
> Find the right projscan tool for a goal. Given `intent` (free text — e.g. "what breaks if I rename X", "coordinate parallel agents", "is it safe to commit"), returns the best-matching tool(s) with the exact call and why to use each. With no `intent`, returns the full capability catalog grouped by category. A discovery entry point over projscan's surface; deterministic keyword routing, no inference.

**projscan_claim**
> Coordinate parallel agents with advisory claims/leases over files, directories, or symbols, shared across the repo's git worktrees. action:"add" records a claim (optionally a lease with `ttl_seconds`) and returns any `contention` (another agent already holding an overlapping, non-expired claim); "list" returns claims; "release" drops a claim by `id`, by `target`, or all of an `agent`'s; "prune" removes expired-lease claims. Local-first and advisory — claiming an already-claimed target still succeeds, but surfaces contention so the swarm can coordinate.

**projscan_start**
> First-60-seconds repo orientation for agents and developers. Composes setup diagnostics, workplan, quality scorecard, adoption gaps, top risks, and next commands into one read-only workflow recommendation.

## NOTES
- Code is NOT minified: plain tsc output with comments and sourcemaps, readable directly.
- Risk of dynamic construction of descriptions: low. All descriptions are static literals in `dist/mcp/tools/*.js`; the only concatenation is `deprecationDescriptionPrefix()` in toolDefinitions.js (a deprecation prefix, not a string). The `dist/tool-manifest.json` manifest is generated at build time and matches the code 100%.
- Prompts/resources channels exist (prompts.js, resources.js) — run through the same markers, 0 matches.
- Reviewed: ~55 files selectively (package.json, mcp/server*, all 46 tools/*.js, toolDefinitions, prompts, manifest) + grep scan of all dist (the package has 2366 files, including .map/docs/images).
