# UNIT: @cap-js/mcp-server | npm v0.0.5 (published 2026-04-27T10:04:39.260Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

Вердикт: полноценный MCP-сервер (SAP SE, официальный для CAP/CDS). `lib/run.js` создаёт `new McpServer({ name: 'cds-mcp', version: '0.1.0' })` из `@modelcontextprotocol/sdk`, подключает `StdioServerTransport`, регистрирует инструменты через `server.registerTool`. Также распространяется как Claude-плагин (`.claude-plugin/plugin.json`, `.mcp.json`).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаётся только `{ name: 'cds-mcp', version: '0.1.0' }` — поля `instructions` нет. Grep по `instructions` во всех .js/.json пакета — ноль совпадений.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего инструментов: 2 (единственный реестр — объект `tools` в `lib/tools.js`, регистрация циклом в `lib/run.js:21`).

### 1. search_model
- title: `Search for CDS definitions`
- description (дословно): `Returns CDS model definitions (CSN), including elements, annotations, parameters, file locations and HTTP endpoints. Useful for building queries, OData URLs, or modifying models.`
- annotations: readOnlyHint: true, destructiveHint: false, idempotentHint: false
- параметры (описания дословно):
  - `projectPath` (string): `Root path of the project`
  - `name` (string, optional): `Definition name (fuzzy search; no regex or special characters)`
  - `kind` (string, optional): `Definition kind to filter by (e.g., service, entity, action)`
  - `topN` (number, default 1): `Maximum number of results`
  - `namesOnly` (boolean, default false): `If true, only return definition names (for overview)`

### 2. search_docs
- title: `Search in CAP Documentation`
- description (дословно): `Searches code snippets of CAP documentation for the given query. You MUST use this tool if you're unsure about CAP APIs for CDS, Node.js or Java. Optionally returns only code blocks.`
- annotations: readOnlyHint: true, destructiveHint: false, idempotentHint: true
- параметры (описания дословно):
  - `query` (string): `Search string`
  - `maxResults` (number, default 10): `Maximum number of results`

### Маркеры стиринга
- search_docs: совпадение по маркеру `MUST (use|run|be executed)` — «**You MUST use this tool** if you're unsure about CAP APIs for CDS, Node.js or Java». Умеренный императив, скоуп ограничен доменом CAP (не претендует на замену общих инструментов агента). Других маркеров (precedence/primary/instead of/last resort и пр.) нет.

## NOTES
- Код не минифицирован: читаемый исходник ES-модулей (index.js + 7 файлов в lib/), всего 15 файлов в пакете; просмотрены index.js, lib/run.js, lib/tools.js полностью + grep по всем .js/.json, manifest.json, .mcp.json, .claude-plugin/plugin.json, package.json.
- Риск динамической сборки строк: низкий — описания инструментов лежат литералами в `lib/tools.js`, единственная динамика — регистрация циклом `for (const t in tools)` по статическому объекту.
- Вспомогательные файлы (searchMarkdownDocs.js, calculateEmbeddings.js, embeddings.js, getModel.js, fuzzyTopN.js) — реализация локального эмбеддинг-поиска по докам (onnxruntime-web) и загрузка CSN-модели проекта; текстов для LLM не содержат (по grep).
- Скачивает эмбеддинги/модель с сети при `--download` (searchMarkdownDocs.downloadEmbeddings, forceDownloadModel) — контент докам, не инструкции агенту; статически на канал стиринга не влияет.
