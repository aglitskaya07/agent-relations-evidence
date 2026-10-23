# UNIT: @eslint/mcp | npm v0.3.10 (published 2026-07-27T21:55:12.344Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

Верифицированный MCP-сервер: `new McpServer({ name: "ESLint", version: "0.3.10" })` из `@modelcontextprotocol/sdk/server/mcp.js`, stdio-транспорт (`src/mcp-cli.js`), bin в package.json. Официальный пакет ESLint (repo eslint/rewrite, packages/mcp), автор Nicholas C. Zakas.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору McpServer передаются только `name` и `version` — поля `instructions` нет; кастомного initialize-хендлера нет.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего инструментов: 1.

### lint-files
> Lint files using ESLint. You must provide a list of absolute file paths to the files you want to lint. The absolute file paths should be in the correct format for your operating system (e.g., forward slashes on Unix-like systems, backslashes on Windows).

inputSchema: `{ filePaths: z.array(z.string().min(1)).nonempty() }` (без `.describe()` — комментарий в коде: Cursor ломается на describe в схеме).

## NOTE: steering в runtime tool results (не в описании)

В хендлере `lint-files` (src/mcp-server.js:49-56) к результатам линтинга приклеиваются два императивных текстовых блока, которые модель получает как содержимое ответа инструмента:

> "Here are the results of running ESLint on the provided files. Before doing anything else, you must display the full list to the user:"

> "If the user asked to fix any issues found, proceed in fixing them. If the user did not ask to fix issues found, you must ask the user for confirmation before attempting to fix the issues found."

Это управление поведением агента через канал tool-result, а не через description/instructions. Характер — консервативный/защитный (показать всё пользователю, спрашивать подтверждение перед фиксами), не конкурентно-вытесняющий.

## NOTES
- Код не минифицирован, читаемый исходник с комментариями (src/ поставляется как есть, files: ["src"]).
- Риск динамической сборки строк: отсутствует — все строки литеральные, никакой конкатенации/шаблонов в описаниях.
- Просмотрено файлов: 5 из 5 в пакете (package.json, README.md, LICENSE, src/mcp-server.js, src/mcp-cli.js); анализ полный.
