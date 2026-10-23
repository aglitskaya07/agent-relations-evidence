# UNIT: agentloopkit | npm v1.2.0 (published 2026-07-14T12:35:47.577Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (встроенный в CLI-пакет)

Пакет — прежде всего CLI-тулкит («drop-in engineering loop for software agents», bin: `agentloop`/`agentloopkit`), но содержит полноценный stdio MCP-сервер: `dist/cli/index.js` содержит `startAgentLoopMcpServer` (`// src/mcp/server.ts`), `new Server(...)` из `@modelcontextprotocol/sdk` с обработчиками `ListToolsRequestSchema`/`CallToolRequestSchema`. Есть `server.json` (MCP registry manifest, `io.github.abhiyoheswaran1/agentloopkit`, transport stdio). Сервер read-only, работает поверх локальных артефактов `.agentloop/` в репозитории.

## CHANNEL: instructions, npm (static, 530 chars)

Передаётся конструктору `Server` (dist/cli/index.js, строка 16552):

> Read-only AgentLoopKit server. Exposes local task contracts, policies, policy template status, verification reports, ship reports, artifact inventory metadata, run ledger summaries and details, file intent matches, maintainer reviewability checks, gate status, handoffs, status, next action, start briefings, context budgets, context handle inventories, context packs, and context source-handle expansion. It does not run verification commands, read env file contents, call external APIs, upload files, or mutate repository files.

Оценка стиринга: нейтрально-описательная, без императивов в адрес модели, без «primary/precedence/always use». Честно декларирует ограничения (не читает env, не мутирует файлы).

## CHANNEL: tool descriptions, npm (static, coverage=full)

23 инструмента; `listMcpTools()` возвращает статический массив `tools` (строка 16217: `return [...tools];`), динамической генерации нет. Все описания дословно:

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

Маркер-скан по стиринговым регексам: 0 совпадений в описаниях инструментов. Все описания — сухие «Read/List …», без сравнительных или командных формулировок.

## NOTES

- Код в dist — tsup-бандл, НЕ минифицирован (читаемые имена, комментарии с путями исходников), есть sourcemaps.
- Риск динамической сборки строк: низкий. instructions — один литерал в конструкторе; tools — статический массив объектных литералов; несколько описаний параметров используют template-литералы только для числовых дефолтов (`Defaults to ${FILE_INTENT_DEFAULT_SCAN_LIMIT}`).
- Пакет также ставит на диск агентские инструкции-шаблоны (`dist/templates/agents/*.md` для claude-code/cursor/codex и др., политики, гейты, AGENTS.md) — это отдельный канал влияния через файлы в репозитории пользователя, а не через MCP-протокол; в этом досье не разбирался построчно.
- Файлов просмотрено: package.json, server.json, dist/cli/index.js (целевые срезы: конструктор сервера, блок tools ~15930–16230, listMcpTools), листинг дерева (~70+ файлов, в основном md-шаблоны).
