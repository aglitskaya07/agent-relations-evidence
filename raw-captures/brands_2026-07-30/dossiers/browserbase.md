# UNIT: browserbase | Browserbase | github browserbase/mcp-server-browserbase | тип автора: официальный | captured 2026-07-29 (static source)

Подтверждение: это MCP-сервер. `src/index.ts` создаёт `new McpServer(...)` из `@modelcontextprotocol/sdk/server/mcp.js`, регистрирует инструменты через `server.tool(...)` и обработчики `ListResourcesRequestSchema` / `ReadResourceRequestSchema` / `ListResourceTemplatesRequestSchema`.

## CHANNEL: instructions
(не обнаружены статически)

Поле `instructions` конструктору сервера не передаётся (грепа по `instructions` в `src/`, `evals/`, `tests/`, корневых `*.ts|*.js|*.json` — ни одного вхождения; слово `instruction` встречается только как имя параметра инструментов `extract`/`observe`). Ответ `initialize` формируется SDK по умолчанию.

Рядом (не канал instructions, но серверная строка-описание в опциях конструктора `McpServer`, `src/index.ts`):
> Cloud browser automation server powered by Browserbase and Stagehand. Enables LLMs to navigate websites, interact with elements, extract data, and capture screenshots using natural language commands.

Также `server.json` (метаданные реестра, не MCP-канал):
> MCP server for AI web browser automation using Browserbase and Stagehand

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 6. Источник — `src/tools/index.ts` (массив `TOOLS`: `...sessionTools, navigateTool, actTool, observeTool, extractTool`), определения в `src/tools/session.ts`, `navigate.ts`, `act.ts`, `observe.ts`, `extract.ts`. Порядок ниже — порядок регистрации.

1. **start**
> Create or reuse a Browserbase session

2. **end**
> Close the current Browserbase session

3. **navigate**
> Navigate to a URL

4. **act**
> Perform an action on the page

5. **observe**
> Observe actionable elements on the page

6. **extract**
> Extract data from the page

Комментарий в `src/tools/index.ts` рядом с массивом: `// Export all tools as array — matches hosted MCP server at mcp.browserbase.com`.
