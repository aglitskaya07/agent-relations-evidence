# UNIT: @notionhq/notion-mcp-server | npm v2.5.1 (published 2026-07-25T16:20:34.018Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (да)

Подлинный MCP-сервер: `src/openapi-mcp-server/mcp/proxy.ts` создаёт `new Server({ name: 'Notion API', version: '1.0.0' }, { capabilities: { tools: {} } })` из `@modelcontextprotocol/sdk` и регистрирует хендлеры `ListToolsRequestSchema` / `CallToolRequestSchema`. Архитектура — OpenAPI→MCP прокси: инструменты генерируются из `scripts/notion-openapi.json` конвертером `OpenAPIToMCPConverter` (`src/openapi-mcp-server/openapi/parser.ts`). Транспорты stdio и streamable-HTTP (`scripts/start-server.ts`).

## CHANNEL: instructions, npm (static)

(не обнаружены статически)

Конструктор `Server` получает только `{ name, version }` и `{ capabilities: { tools: {} } }` — поле `instructions` не передаётся нигде в `src/`. В бандле `bin/cli.mjs` строка `instructions&&{instructions:this._instructions}` — это generic-пламбинг MCP SDK, а не значение от Notion.

## CHANNEL: tool descriptions, npm (static, coverage=full)

24 инструмента (все). Имя = `API-<operationId>` (обрезка до 64 симв. в `truncateToolName`). Описание собирается в `parser.ts`: `"Notion | " + (summary || description)` + приложенный блок `Error Responses:` из 4xx/5xx-ответов спеки. Ниже — итоговые описания дословно (как их увидит клиент в tools/list).

### API-get-user
```
Notion | Retrieve a user
Error Responses:
- 400: 400
```

### API-get-users
```
Notion | List all users
Error Responses:
- 400: 400
```

### API-get-self
```
Notion | Retrieve your token's bot user
Error Responses:
- 400: Bad request
```

### API-post-search
```
Notion | Search by title
Error Responses:
- 400: Bad request
```

### API-get-block-children
```
Notion | Retrieve block children
Error Responses:
- 400: Bad request
```

### API-patch-block-children
```
Notion | Append block children
Error Responses:
- 400: Bad request
```

### API-retrieve-a-block
```
Notion | Retrieve a block
Error Responses:
- 400: Bad request
```

### API-update-a-block
```
Notion | Update a block
Error Responses:
- 400: Bad request
```

### API-delete-a-block
```
Notion | Delete a block
Error Responses:
- 400: Bad request
```

### API-retrieve-a-page
```
Notion | Retrieve a page
Error Responses:
- 400: Bad request
```

### API-patch-page
```
Notion | Update page properties
Error Responses:
- 400: Bad request
```

### API-post-page
```
Notion | Create a page
Error Responses:
- 400: Bad request
```

### API-retrieve-a-page-property
```
Notion | Retrieve a page property item
Error Responses:
- 400: Bad request
```

### API-retrieve-a-comment
```
Notion | Retrieve comments
Error Responses:
- 400: Bad request
```
(поле `description` спеки, не попадает в итог, т.к. summary приоритетнее: "Retrieves a list of un-resolved [Comment objects](ref:comment-object) from a page or block.")

### API-create-a-comment
```
Notion | Create comment
Error Responses:
- 400: Bad request
```
(spec description: "Creates a comment in a page or existing discussion thread.")

### API-query-data-source
```
Notion | Query a data source
Error Responses:
- 400: Bad request
```
(spec description: "Query a data source (database) using filters and sorts")

### API-retrieve-a-data-source
```
Notion | Retrieve a data source
Error Responses:
- 400: Bad request
```
(spec description: "Retrieve metadata and schema for a data source")

### API-update-a-data-source
```
Notion | Update a data source
Error Responses:
- 400: Bad request
```
(spec description: "Update properties of a data source")

### API-create-a-data-source
```
Notion | Create a data source
Error Responses:
- 400: Bad request
```
(spec description: "Create a new data source (database)")

### API-list-data-source-templates
```
Notion | List templates in a data source
Error Responses:
- 400: Bad request
```
(spec description: "List available templates for a data source")

### API-retrieve-a-database
```
Notion | Retrieve a database
Error Responses:
- 400: Bad request
```
(spec description: "Retrieves a database object using the ID specified. Returns database metadata including the list of data source IDs contained in the database.")

### API-move-page
```
Notion | Move a page
Error Responses:
- 400: Bad request
```
(spec description: "Move a page to a different parent location")

### API-retrieve-page-markdown
```
Notion | Retrieve a page as Markdown
Error Responses:
- 400: Bad request
- 403: The integration lacks the read/update content capability required for this page.
- 404: Page not found or not shared with the integration.
- 429: Rate limited.
```
(spec description: "Retrieve the full content of a Notion page rendered as enhanced Markdown. Designed for agentic and developer tools that work natively with Markdown instead of the block JSON returned by Retrieve block children.")

### API-update-page-markdown
```
Notion | Update a page's content as Markdown
Error Responses:
- 400: Bad request
- 403: The integration lacks the read/update content capability required for this page.
- 404: Page not found or not shared with the integration.
- 429: Rate limited.
- 409: Conflict (e.g. row limit exceeded).
```
(spec description: "Update the content of a Notion page using enhanced Markdown. Prefer `replace_content` to overwrite the whole page or `update_content` for targeted find-and-replace edits.")

## MARKER NOTES

Steering-маркеры практически отсутствуют. Единственное near-hit: "Prefer `replace_content` … or `update_content` for targeted find-and-replace edits" в spec-description update-page-markdown — но это внутренняя рекомендация по параметрам своего же инструмента, не вытеснение чужих инструментов; к тому же поле description этого оп-объекта в итоговый description НЕ попадает (summary имеет приоритет в `parser.ts:330`). Нет "instead of built-in", "takes precedence", "MUST use", "primary interface" и т.п. Annotations: GET → readOnlyHint, остальное → destructiveHint (нейтрально-честная разметка).

## METHOD / OPSEC

Статический анализ, код не исполнялся. Источник описаний — `scripts/notion-openapi.json` (24 операции), логика сборки — `src/openapi-mcp-server/openapi/parser.ts` (getDescription: префикс "Notion | " при title=="Notion API"; error responses дописываются) и `src/openapi-mcp-server/mcp/proxy.ts` (имя `API-x`, truncate 64, annotations).

- Минификация: `src/` — читаемый TypeScript; `bin/cli.mjs` (~1.4 MB) — минифицированный esbuild-бандл того же кода + SDK/zod. Анализ вёлся по src, бандл проверен grep'ом на "instructions".
- Риск динамической сборки строк: низко-средний. Описания собираются динамически из OpenAPI-файла (конкатенация префикса + error responses), но входной JSON лежит в пакете и статичен; CLI позволяет подсунуть другой spec-файл (`--spec-path`?/позиционный путь в init-server), тогда набор инструментов и тексты меняются. Base URL спеки можно переопределить (`baseUrl` в initProxy).
- Просмотрено файлов: ~10 текстовых (init-server.ts, proxy.ts, parser.ts, start-server.ts (grep), notion-openapi.json, package.json, cli.mjs (grep), README (по диагонали)); всего в пакете 51 файл, из них 5 — png-картинки документации.
