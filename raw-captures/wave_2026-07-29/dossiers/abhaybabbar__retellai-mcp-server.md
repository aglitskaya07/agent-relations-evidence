# UNIT: @abhaybabbar/retellai-mcp-server | npm v1.0.4 (published 2026-04-09T22:28:23.696Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Настоящий MCP-сервер на TypeScript: `src/index.ts` создаёт `new McpServer({ name: "Retell MCP", version: "0.1.0" })` из `@modelcontextprotocol/sdk`, подключает `StdioServerTransport`, регистрирует инструменты через `registerAllTools`. Обёртка над Retell AI API (голосовые агенты/звонки), ключ `RETELL_API_KEY` из env.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаются только `name` и `version`; grep по `instructions` в `src/` и `build/` — 0 совпадений.

## CHANNEL: tool descriptions, npm (static, coverage=full)

24 инструмента, все регистрируются как `server.tool(name, description, schema, handler)`. Описания дословно:

### call.ts (6)
1. `create_phone_call` — "Creates a new phone call"
2. `create_web_call` — "Creates a new web call"
3. `get_call` — "Gets a call by ID"
4. `list_calls` — "Lists all calls"
5. `update_call` — "Updates an existing call"
6. `delete_call` — "Deletes a call"

### agent.ts (6)
7. `list_agents` — "Lists all Retell agents"
8. `create_agent` — "Creates a new Retell agent"
9. `get_agent` — "Gets a Retell agent by ID"
10. `update_agent` — "Updates an existing Retell agent"
11. `delete_agent` — "Deletes a Retell agent"
12. `get_agent_versions` — "Gets all versions of a Retell agent"

### retell-llm.ts (5)
13. `list_retell_llms` — "Lists all Retell LLMs"
14. `create_retell_llm` — "Creates a new Retell LLM"
15. `get_retell_llm` — "Gets a Retell LLM by ID"
16. `update_retell_llm` — "Updates an existing Retell LLM"
17. `delete_retell_llm` — "Deletes a Retell LLM"

### phone-number.ts (5)
18. `list_phone_numbers` — "Lists all Retell phone numbers"
19. `create_phone_number` — "Creates a new phone number"
20. `get_phone_number` — "Gets details of a specific phone number"
21. `update_phone_number` — "Updates a phone number"
22. `delete_phone_number` — "Deletes a phone number"

### voice.ts (2)
23. `list_voices` — "Lists all available Retell voices"
24. `get_voice` — "Gets details of a specific voice"

## MARKER SCAN

Ни одно описание не содержит steering-маркеров (instead of / prefer / MUST / primary / precedence / whenever the user и т.д.). Все описания — нейтральные CRUD-однострочники.

## NOTES

- Код не минифицирован: в тарболе и src/*.ts, и build/*.js (читаемый tsc-выход); build зеркалит src, число регистраций совпадает (24/24).
- Риск динамической сборки строк описаний: низкий — все имена и описания заданы строковыми литералами прямо в вызовах `server.tool(...)`.
- В корне package/ лежит вложенный тарбол предыдущей версии `abhaybabbar-retellai-mcp-server-1.0.3.tgz` (не анализировался как отдельный юнит, не исполнялся).
- Просмотрено файлов: ~12 текстовых (package.json, README.md, src/index.ts, src/client.ts, src/tools/*.ts ×7, плюс grep по build/ ×9).
- Расхождение метаданных: package.json version 1.0.4, но в конструктор McpServer зашито version "0.1.0".
