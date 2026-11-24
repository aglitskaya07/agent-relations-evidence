# UNIT: @notionhq/notion-mcp-server | npm v2.5.1 (published 2026-07-25T16:20:34.018Z) | scopes: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (yes)

True MCP server: `src/openapi-mcp-server/mcp/proxy.ts` creates `new Server({ name: 'Notion API', version: '1.0.0' }, { capabilities: { tools: {} } })` from `@modelcontextprotocol/sdk` and registers `ListToolsRequestSchema` / `CallToolRequestSchema` handlers. Architecture: OpenAPI→MCP proxy: tools are generated from `scripts/notion-openapi.json` by the `OpenAPIToMCPConverter` (`src/openapi-mcp-server/openapi/parser.ts`). Transports stdio and streamable-HTTP (`scripts/start-server.ts`).

## CHANNEL: instructions, npm (static)

(not found statically)

The `Server` constructor receives only `{ name, version }` and `{ capabilities: { tools: {} } }` — the `instructions` field is not passed anywhere in `src/`. In the `bin/cli.mjs` bundle, the string `instructions&&{instructions:this._instructions}` is generic MCP SDK plumbing, not a value from Notion.

## CHANNEL: tool descriptions, npm (static, coverage=full)

24 tools (all). Name = `API-<operationId>` (truncated to 64 chars in `truncateToolName`). The description is assembled in `parser.ts`: `"Notion | " + (summary || description)` + an appended `Error Responses:` block from the spec's 4xx/5xx responses. Below are the final descriptions verbatim (as the client will see them in tools/list).

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
(the spec `description` field, not included in the final result because summary has priority: "Retrieves a list of un-resolved [Comment objects](ref:comment-object) from a page or block.")

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

Steering markers are practically absent. The only near-hit: "Prefer `replace_content` … or `update_content` for targeted find-and-replace edits" in spec-description update-page-markdown — but this is an internal recommendation about parameters of its own tool, not the displacing of other tools; moreover, the description field of this op object does NOT make it into the final description (summary has priority in `parser.ts:330`). There is no "instead of built-in", "takes precedence", "MUST use", "primary interface", etc. Annotations: GET → readOnlyHint, everything else → destructiveHint (neutral-honest labeling).

## METHOD / OPSEC

Static analysis, code was not executed. The source of descriptions is `scripts/notion-openapi.json` (24 operations), the build logic is `src/openapi-mcp-server/openapi/parser.ts` (getDescription: prefix "Notion | " when title=="Notion API"; error responses are appended) and `src/openapi-mcp-server/mcp/proxy.ts` (name `API-x`, truncate 64, annotations).

- Minification: `src/` — readable TypeScript; `bin/cli.mjs` (~1.4 MB) — a minified esbuild bundle of the same code + SDK/zod. Analysis was done on src, the bundle was checked with grep for "instructions".
- Risk of dynamic string assembly: low-medium. Descriptions are assembled dynamically from an OpenAPI file (prefix concatenation + error responses), but the input JSON is inside the package and static; the CLI allows supplying a different spec file (`--spec-path`?/positional path in init-server), then the tool set and texts change. The spec base URL can be overridden (`baseUrl` in initProxy).
- Reviewed ~10 text files (init-server.ts, proxy.ts, parser.ts, start-server.ts (grep), notion-openapi.json, package.json, cli.mjs (grep), README (skimming)); 51 files total in the package, of which 5 are png documentation images.
