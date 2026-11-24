# UNIT: agentloopkit | npm v1.2.0 (published 2026-07-14T12:35:47.577Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (built into the CLI package)

Package — primarily a CLI toolkit ("drop-in engineering loop for software agents", bin: `agentloop`/`agentloopkit`), but contains a full stdio MCP server: `dist/cli/index.js` contains `startAgentLoopMcpServer` (`// src/mcp/server.ts`), `new Server(...)` from `@modelcontextprotocol/sdk` with handlers for `ListToolsRequestSchema`/`CallToolRequestSchema`. There is `server.json` (MCP registry manifest, `io.github.abhiyoheswaran1/agentloopkit`, transport stdio). The server is read-only, works on top of local artifacts `.agentloop/` in the repository.

## CHANNEL: instructions, npm (static, 530 chars)

Passed into the `Server` constructor (dist/cli/index.js, line 16552):

> Read-only AgentLoopKit server. Exposes local task contracts, policies, policy template status, verification reports, ship reports, artifact inventory metadata, run ledger summaries and details, file intent matches, maintainer reviewability checks, gate status, handoffs, status, next action, start briefings, context budgets, context handle inventories, context packs, and context source-handle expansion. It does not run verification commands, read env file contents, call external APIs, upload files, or mutate repository files.

Assessment of steering: neutrally descriptive, without imperatives addressed to the model, without "primary/precedence/always use". It honestly declares limitations (does not read env, does not mutate files).

## CHANNEL: tool descriptions, npm (static, coverage=full)

23 tools; `listMcpTools()` returns the static array `tools` (line 16217: `return [...tools];`), there is no dynamic generation. All descriptions verbatim:

| # | name | description |
|---|------|-------------|
| 1 | agentloop_status | Read AgentLoopKit status, active task, latest verification, git state, and next action. |
| 2 | agentloop_next | Read only the next recommended AgentLoopKit action and reason. |
| 3 | agentloop_list_tasks | List local task contracts under the configured AgentLoopKit task directory. |
| 4 | agentloop_show_active_task | Read the active task contract content when one is pinned. |
| 5 | agentloop_list_policies | List local AgentLoopKit safety policy files. |
| 6 | agentloop_read_policy | Read one local AgentLoopKit policy by policy name. |
| 7 | agentloop_policy_status | Read local AgentLoopKit policy template status, including current, modified, missing, and extra policies. |
| 8 | agentloop_latest_verification_report | Read the latest local verification report metadata and Markdown content. |
| 9 | agentloop_latest_ship_report | Read the latest local ship report metadata and Markdown content. |
| 10 | agentloop_list_runs | List recent local AgentLoopKit run ledger entries. |
| 11 | agentloop_show_run | Read one local AgentLoopKit run ledger entry by run id. |
| 12 | agentloop_file_intent | Read local run ledger matches for one repo-relative file path. |
| 13 | agentloop_maintainer_check | Read local maintainer reviewability checks for agent-assisted changes. |
| 14 | agentloop_check_gates | Read local review gate status for task, verification, handoff, harness, policy, and git evidence. |
| 15 | agentloop_artifacts | Read local AgentLoopKit artifact inventory metadata without artifact contents. |
| 16 | agentloop_review_context | Read one local reviewability snapshot for agents, without running commands or returning artifact bodies. |
| 17 | agentloop_start | Read a compact software-agent start briefing with task, evidence, risk, context routing, and impact metrics. |
| 18 | agentloop_context_budget | Read local context pressure and compact-pack savings guidance without running commands. |
| 19 | agentloop_context_handles | List local context source handles with availability, reasons, and expansion commands. |
| 20 | agentloop_context_pack | Read an auditable local context pack with receipts, context-budget estimates, and source handles. |
| 21 | agentloop_context_show | Expand one local context source handle, such as task:active or evidence-map:current. |
| 22 | agentloop_list_handoffs | List recent local reviewer handoff summaries. |
| 23 | agentloop_latest_handoff | Read the latest local reviewer handoff summary Markdown content. |

Marker scan for steering regexes: 0 matches in the tool descriptions. All descriptions are dry "Read/List …", without comparative or imperative formulations.

## NOTES

- Code in dist is a tsup bundle, NOT minified (readable names, comments with source paths), sourcemaps are present.
- Risk of dynamic string assembly: low. instructions — one literal in the constructor; tools — a static array of object literals; several parameter descriptions use template literals only for numeric defaults (`Defaults to ${FILE_INTENT_DEFAULT_SCAN_LIMIT}`).
- The package also writes agent instruction templates to disk (`dist/templates/agents/*.md` for claude-code/cursor/codex and others, policies, gates, AGENTS.md) — this is a separate influence channel through files in the user's repository, not through the MCP protocol; in this dossier it was not analyzed line by line.
- Files reviewed: package.json, server.json, dist/cli/index.js (target slices: server constructor, tools block ~15930–16230, listMcpTools), tree listing (~70+ files, mostly md templates).
