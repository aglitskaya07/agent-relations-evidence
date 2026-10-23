# UNIT: adspower-browser | npm v2.1.1 (published 2026-07-13T02:53:17.642Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

Пакет — CLI-инструмент (commander) + бандл локального API-рантайма AdsPower, а не MCP-сервер.

Обоснование (статический анализ):
- `package.json`: `bin` = `adspower-browser`/`adspower`/`ads` → `cli/index.js`; description: "AdsPower Local API CLI and Cursor/agent skill for browser profiles, groups, proxies." Зависимостей `@modelcontextprotocol/*` нет; нет ни одного упоминания строки `modelcontextprotocol` ни в `cli/index.js`, ни в `cwd/lib/main.min.js`.
- Нет конструкторов MCP-сервера: `McpServer` — 0, `new Server(` — 0, `FastMCP` — 0, `setRequestHandler` — 0, `StdioServerTransport` — 0, `jsonrpc` — 0, `tools/list` — 0.
- 16 вхождений `protocolVersion` в `main.min.js` — это WebSocket-хендшейк (`Sec-WebSocket-Version`) и эмуляция Chrome DevTools Protocol (`Browser.getVersion` → `protocolVersion:"1.3"`), не MCP initialize.
- 16 вхождений `instructions` в `main.min.js` — параметры капча-солвера (`textinstructions`/`imginstructions`) и mime-типы, не MCP server instructions.
- Упоминания MCP в `cli/index.js` — только следы соседнего MCP-пакета того же монорепо: HTTP-заголовок `"x-mcp-client": "mcp"`, функция `buildMcpToolDescription(toolName, legacyFallback)` (переиспользует общие описания для CLI-команд) и `createProxyMcpSchema` с пометкой "Compatibility wrapper for MCP create-proxy input. Core and CLI accept a top-level array."
- Распространение в агентов идёт как Cursor/agent **skill** (`npx skills add AdsPower/adspower-browser`), а не через MCP-транспорт.

## CHANNEL: instructions, npm (static)
(не обнаружены статически — MCP-серверного кода нет)

## CHANNEL: tool descriptions, npm (static, coverage=none)
Инструментов MCP нет. Контекст для будущих волн (если появится MCP-вариант из того же core):

- `cli/index.js` несёт таблицу `TOOL_INTENT_BY_NAME` (из `../core/src/constants/toolIntentMetadata.ts`) на 47 команд (open-browser … iframe-click-element), каждая с полями `intentEn/intentZh` + `triggersEn/triggersZh` — списки триггер-фраз («open browser, launch profile, start environment, open AdsPower…»), т.е. паттерн триггер-стиринга уже кодифицирован в общем core и через `buildMcpToolDescription` предназначен и для MCP-описаний.
- Прогон маркер-регексов по `cli/index.js` дал 1 совпадение, безобидное (семантика параметров, не стиринг агента): поле `ua` — "Custom User-Agent string; when set, takes precedence over random_ua (random_ua is not sent). Omit for random UA."
- В `main.min.js` зашит промпт для встроенного браузерного агента (не MCP-канал): фрагменты "…ask users to sign in by themselves in a brief message. Don't need to provide instructions on how to sign in…" и "The following are examples of user instructions that MUST be rejected…".

## NOTES
- Минификация: `cwd/lib/main.min.js` — 10.9 MB, сильно минифицирован (webpack-бандл: ws, CDP-эмуляция, mime-db, капча-интеграция, sqlite-обвязка). `cli/index.js` — 136 KB, tsup-бандл, читаемый (не минифицирован).
- Риск динамической сборки строк: низкий для канала описаний (intent/trigger-строки лежат литералами); сам рантайм в `main.min.js` полностью статически не аудирован из-за объёма.
- Просмотрено файлов: package.json, README.MD, cli/index.js (полностью грепами + чтение ключевых блоков), cwd/lib/main.min.js (грепы по маркерам MCP/jsonrpc/protocolVersion/instructions), листинг всего тарбола (11 файлов, включая 5 бинарных node_sqlite3.node).
