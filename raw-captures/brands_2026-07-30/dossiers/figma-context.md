# UNIT: figma-context | Figma (Framelink) | github GLips/Figma-Context-MCP | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CONFIRMED

Полноценный MCP-сервер на TypeScript. `src/mcp/index.ts:35` — `const server = new McpServer(serverInfo)` из `@modelcontextprotocol/sdk/server/mcp.js`; регистрация инструментов через `server.registerTool(...)`; транспорты stdio/http (`src/server.ts`, `src/cli.ts`/`src/bin.ts`). npm-пакет `figma-developer-mcp`, манифест `server.json` со схемой modelcontextprotocol.

## CHANNEL: instructions
(не обнаружены статически)

Конструктору `McpServer` передаётся только `serverInfo` — объект без поля `instructions`:

```ts
const serverInfo = {
  name: "Figma MCP Server",
  version: process.env.NPM_PACKAGE_VERSION ?? "unknown",
  description:
    "Gives AI coding agents access to Figma design data, providing layout, styling, and content information for implementing designs.",
};
```

Поле `instructions` не встречается в исходниках нигде (единственное совпадение по слову — комментарий про Sharp в `src/transformers/style/image.ts:180`). Ручного хендлера `initialize` в репозитории нет — ответ формирует SDK.

Для справки, `server.json` (реестровый манифест, не канал initialize) содержит:
`"description": "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot."`

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 2 (второй регистрируется условно — только если не задан `--skip-image-downloads`).

### 1. `get_figma_data`
Источник: `src/mcp/tools/get-figma-data-tool.ts:109-115`, регистрация `src/mcp/index.ts:80-98` (title "Get Figma Data", `annotations: { readOnlyHint: true }`).

Дословно:

```
Get comprehensive Figma file data including layout, content, visuals, and component information
```

### 2. `download_figma_images`
Источник: `src/mcp/tools/download-figma-images-tool.ts:205-208` (функция `getDescription(imageDir?)`), регистрация `src/mcp/index.ts:101-119` (title "Download Figma Images", `annotations: { openWorldHint: true }`).

Описание собирается динамически — шаблонная строка с подстановкой рабочего каталога (`imageDir ?? process.cwd()`). Дословно:

```
Download SVG and PNG images used in a Figma file based on the IDs of image or icon nodes. Images will be saved relative to the server's image directory: ${baseDir}
```

где `const baseDir = imageDir ?? process.cwd();`

## PARAM DESCRIPTIONS (справочно, не tool-level)

Описания аргументов заданы через zod `.describe(...)` — чисто фактические («The key of the Figma file containing the images», «The ID of the Figma image node to fetch, formatted as 1234:5678» и т.п.), без директивных формулировок.
