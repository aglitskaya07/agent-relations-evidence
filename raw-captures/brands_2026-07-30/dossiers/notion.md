# UNIT: notion | Notion | github makenotion/notion-mcp-server | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CONFIRMATION

Это MCP-сервер. `src/openapi-mcp-server/mcp/proxy.ts:140` создаёт `new Server({ name, version: '1.0.0' }, { capabilities: { tools: {} } })` из `@modelcontextprotocol/sdk/server/index.js`, регистрирует обработчики `ListToolsRequestSchema` и `CallToolRequestSchema`. Транспорты — stdio и streamable HTTP (`scripts/start-server.ts`). Инструменты генерируются автоматически из OpenAPI-спеки `scripts/notion-openapi.json` (Notion API 2025-09-03, «Data Source Edition») конвертером `OpenAPIToMCPConverter` (`src/openapi-mcp-server/openapi/parser.ts`).

## CHANNEL: instructions

(не обнаружены статически)

Единственный вызов конструктора сервера передаёт только `{ name, version }` и `{ capabilities }` — поля `instructions` нет. Grep по `instructions` во всём `src/` и `scripts/` не дал ни одного совпадения. Собственного обработчика `initialize` в репозитории нет — используется дефолтный из SDK.

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 24.

Механика формирования (parser.ts:330-343, 452-458): `description = operation.summary || operation.description`, затем при наличии 4xx/5xx-ответов добавляется блок `\nError Responses:\n<code>: <description>`; на финальном шаге ко всей строке приписывается префикс `"Notion | "` (только если `info.title === 'Notion API'`). Имя инструмента — `API-` + `operationId` (proxy.ts:170).

---

**API-get-user**
```
Notion | Retrieve a user
Error Responses:
400: 400
```

**API-get-users**
```
Notion | List all users
Error Responses:
400: 400
```

**API-get-self**
```
Notion | Retrieve your token's bot user
Error Responses:
400: Bad request
```

**API-post-search**
```
Notion | Search by title
Error Responses:
400: Bad request
```

**API-get-block-children**
```
Notion | Retrieve block children
Error Responses:
400: Bad request
```

**API-patch-block-children**
```
Notion | Append block children
Error Responses:
400: Bad request
```

**API-retrieve-a-block**
```
Notion | Retrieve a block
Error Responses:
400: Bad request
```

**API-update-a-block**
```
Notion | Update a block
Error Responses:
400: Bad request
```

**API-delete-a-block**
```
Notion | Delete a block
Error Responses:
400: Bad request
```

**API-retrieve-a-page**
```
Notion | Retrieve a page
Error Responses:
400: Bad request
```

**API-patch-page**
```
Notion | Update page properties
Error Responses:
400: Bad request
```

**API-post-page**
```
Notion | Create a page
Error Responses:
400: Bad request
```

**API-retrieve-a-page-property**
```
Notion | Retrieve a page property item
Error Responses:
400: Bad request
```

**API-retrieve-a-comment**
```
Notion | Retrieve comments
Error Responses:
400: Bad request
```

**API-create-a-comment**
```
Notion | Create comment
Error Responses:
400: Bad request
```

**API-query-data-source**
```
Notion | Query a data source
Error Responses:
400: Bad request
```

**API-retrieve-a-data-source**
```
Notion | Retrieve a data source
Error Responses:
400: Bad request
```

**API-update-a-data-source**
```
Notion | Update a data source
Error Responses:
400: Bad request
```

**API-create-a-data-source**
```
Notion | Create a data source
Error Responses:
400: Bad request
```

**API-list-data-source-templates**
```
Notion | List templates in a data source
Error Responses:
400: Bad request
```

**API-retrieve-a-database**
```
Notion | Retrieve a database
Error Responses:
400: Bad request
```

**API-move-page**
```
Notion | Move a page
Error Responses:
400: Bad request
```

**API-retrieve-page-markdown**
```
Notion | Retrieve a page as Markdown
Error Responses:
400: Bad request
403: The integration lacks the read/update content capability required for this page.
404: Page not found or not shared with the integration.
429: Rate limited.
```

**API-update-page-markdown**
```
Notion | Update a page's content as Markdown
Error Responses:
400: Bad request
403: The integration lacks the read/update content capability required for this page.
404: Page not found or not shared with the integration.
429: Rate limited.
409: Conflict (e.g. row limit exceeded).
```

---

## ДОПОЛНИТЕЛЬНО: аннотации инструментов

Помимо description сервер отдаёт `annotations` (proxy.ts:182-187): `title` — человекочитаемое имя, произведённое из operationId; `readOnlyHint: true` для GET-операций, `destructiveHint: true` для всех остальных. Текстовой инструктивной нагрузки в них нет.
