# UNIT: @mcp-use/cli | npm v3.6.6 (published 2026-07-20T22:22:13.507Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

@mcp-use/cli — это командная утилита (bin `mcp-use`, построена на `commander`) для **сборки, разработки и деплоя** MCP-серверов на облако Manufact, плюс MCP-**клиент** для подключения к чужим серверам. Сам пакет серверного MCP-кода не содержит.

Обоснование (статический анализ dist/index.js, 10 102 строки, и dist/index.cjs):

- package.json: `"description": "The mcp-use CLI is a tool for building and deploying MCP servers..."`, `"bin": {"mcp-use": "./dist/index.cjs"}`. Зависимости — vite, esbuild, tsx, commander, tar, chokidar и т.п. (build-тулчейн), а не MCP SDK-сервер.
- В коде нет ни одного вызова `new Server(...)`, `McpServer`, `FastMCP`, `createMCPServer`, `registerTool`, `addTool`, `server.tool(...)`, `setRequestHandler`, `StdioServerTransport`. Единственное упоминание `@modelcontextprotocol/sdk` (строка 4994 index.js) — проверка, есть ли эта зависимость в *пользовательском* проекте, который CLI собирается деплоить.
- Все совпадения по слову "McpServer" — хелперы `getMcpServerUrl()` / `getMcpServerUrlForCloudServer()`, которые формируют URL задеплоенного сервера для вывода в консоль.
- Структура — команды commander: `build`, `dev`, `start`, `login`, `logout`, `whoami`, `deployments *`, `servers *`, `env *`, `org *`, `skills add/install`, `client connect/list/remove` и per-server субкоманды `tools list/call/describe`, `resources list/read/subscribe`, `prompts list/get`, `auth status/refresh/logout` — это CLI-обёртка MCP-*клиента* и деплой-панели, не серверные инструменты.
- `instructions` для конструктора сервера отсутствуют (нечему их передавать).

## CHANNEL: instructions, npm (static)
(не обнаружены статически — в пакете нет серверного кода)

## CHANNEL: tool descriptions, npm (static, coverage=none)
Нет зарегистрированных MCP-инструментов. Строки `.description(...)` в коде — это help-тексты commander для человека в терминале, а не tool descriptions для LLM.

## NOTES
- Код бандлирован tsup/esbuild, но не минифицирован (читаемые имена, 10k строк).
- Риск динамической сборки строк для MCP-канала: неприменим — канала нет.
- Просмотрено: package.json, README.md, dist/index.js (грепы по всему файлу), dist/index.cjs (грепы), список всех 68 файлов пакета (остальное — .d.ts/.map/шимы).
