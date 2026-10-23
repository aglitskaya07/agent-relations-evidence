# UNIT: @claude-flow/mcp | npm v3.0.0-alpha.9 (published 2026-05-09T18:31:20.248Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: server-framework (library) с встроенным серверным кодом MCP

Пакет — standalone-реализация MCP-сервера (часть claude-flow v3, ruvnet): полный серверный код (initialize/tools/resources/prompts/tasks, транспорты stdio/HTTP/WebSocket) в `src/server.ts` (1131 строка) + tool-registry. Это НЕ клиент и НЕ прокси, но и не готовый продуктовый сервер: в package.json нет `bin`, пакет предназначен для встраивания (`quickStart` + `registerTool(defineTool(...))` из README). Прикладные инструменты определяет хост-приложение; сам пакет регистрирует только 4 встроенных system-инструмента (`registerBuiltInTools()`, src/server.ts:1033). Классифицирован как сервер (серверный код есть), с оговоркой «framework».

## CHANNEL: instructions, npm (static, 50 chars)

Передаётся в результате `initialize` (src/server.ts:492, идентично в dist/server.js:370):

```
Claude-Flow MCP Server V3 ready for tool execution
```

Нейтральная строка-статус, никакого steering-содержания (нет приоритетов, «primary», принуждения к использованию).

## CHANNEL: tool descriptions, npm (static, coverage=full)

Встроенных инструментов: 4 (src/server.ts:1033–1090; dist/server.js совпадает). Все описания дословно:

1. **system/info** — `Get system information`
2. **system/health** — `Get system health status`
3. **system/metrics** — `Get server metrics`
4. **tools/list-detailed** — `List all registered tools with details`
   - параметр `category`: `Filter by category`

Маркеров манипуляции (precedence/primary/instead of/MUST use и т.п.) в описаниях нет — все четыре описания предельно нейтральные, по 3–6 слов.

## NOTES

- Код не минифицирован: в tarball и `src/*.ts` (исходники), и `dist/*.js` (tsc-транспиляция с sourcemaps); src и dist сверены, расхождений по instructions/описаниям нет.
- Риск динамической сборки строк: низкий. instructions — статический литерал; описания встроенных инструментов — статические литералы. Динамика есть только в том смысле, что прикладные инструменты регистрируются хост-кодом извне пакета (framework by design) — их описания вне рамок этого tarball.
- Просмотрено: структура из 318 файлов, целиком/фрагментами прочитаны package.json, README.md, src/server.ts (ключевые блоки), grep по всему src/ и dist/ на instructions/registerTool/description (~30 файлов затронуто grep-ом).
- Побочное наблюдение: в tarball также лежат `.claude/` (settings.json, commands, helpers-скрипты) и CLAUDE.md — материал для канала «files in package», вне заявленных здесь каналов.
