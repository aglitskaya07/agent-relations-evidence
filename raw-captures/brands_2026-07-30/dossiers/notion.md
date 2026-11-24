# UNIT: notion | Notion | github makenotion/notion-mcp-server | author type: official | captured 2026-07-29 (static source)

## SERVER CONFIRMATION

This is an MCP server. `src/openapi-mcp-server/mcp/proxy.ts:140` creates `new Server({ name, version: '1.0.0' }, { capabilities: { tools: {} } })` from `@modelcontextprotocol/sdk/server/index.js`, registers `ListToolsRequestSchema` and `CallToolRequestSchema` handlers. Transports — stdio and streamable HTTP (`scripts/start-server.ts`). Tools are generated automatically from the OpenAPI spec `scripts/notion-openapi.json` (Notion API 2025-09-03, "Data Source Edition") by the `OpenAPIToMCPConverter` (`src/openapi-mcp-server/openapi/parser.ts`).

## CHANNEL: instructions

(not found statically)

The only server-constructor call passes only `{ name, version }` and `{ capabilities }` — there is no `instructions` field. Grep for `instructions` across all of `src/` and `scripts/` found no matches. There is no custom `initialize` handler in the repository — the SDK default is used.

## CHANNEL: tool descriptions (coverage=full)

Total tools: 24.

Formation mechanics (parser.ts:330-343, 452-458): `description = operation.summary || operation.description`, then if there are 4xx/5xx responses a block is added `\nError Responses:\n<code>: <description>`; at the final step a prefix `"Notion | "` is appended to the whole string (only if `info.title === 'Notion API'`). The tool name is `API-` + `operationId` (proxy.ts:170).

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

## ADDITIONAL: tool annotations

In addition to description the server returns `annotations` (proxy.ts:182-187): `title` is a human-readable name derived from operationId; `readOnlyHint: true` for GET operations, `destructiveHint: true` for all others. There is no textual instructional load in them.
