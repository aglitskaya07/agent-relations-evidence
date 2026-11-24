# UNIT: airtable | Airtable | github domdomegg/airtable-mcp-server | author type: community | captured 2026-07-29 (static source)

## SERVER CONFIRMED
TypeScript MCP server on `@modelcontextprotocol/sdk`. `src/index.ts` → `createServer()` creates `new McpServer({name: 'airtable-mcp-server', version})`; `src/main.ts` connects stdio or StreamableHTTP transport. Tools are registered via `server.registerTool(...)` in `src/tools/*.ts`, aggregation in `src/tools/index.ts` (`registerAll`).

## CHANNEL: instructions
(not found statically)

The `McpServer` constructor receives only `{name, version}` — there is no `instructions` field; there is no manual `initialize` handler in the repository, nor an `instructions` string in the code (the only occurrence of the word is prose text in the README).

## CHANNEL: tool descriptions (coverage=full)

There are 16 tools in total (all included, verbatim).

1. **list_records** — `List records from a table`
2. **search_records** — `Search for records containing specific text`
3. **list_bases** — `List all accessible Airtable bases`
4. **list_tables** — `List all tables in a specific base`
5. **describe_table** — `Get detailed information about a specific table`
6. **get_record** — `Get a specific record by ID`
7. **create_record** — `Create a new record in a table`
8. **update_records** — `Update up to 10 records in a table`
9. **delete_records** — `Delete records from a table`
10. **create_table** — `Create a new table in a base`
11. **update_table** — `Update a table's name or description`
12. **create_field** — `Create a new field in a table`
13. **update_field** — `Update a field's name or description`
14. **create_comment** — `Create a comment on a record`
15. **list_comments** — `List comments on a record`
16. **upload_attachment** — `Upload a file directly to an attachment field on an existing record using Airtable's upload API. Supports files up to 5 MB. For larger files, use create_record or update_records with a public URL. The record must already exist.`

### Notes on the channel
- All descriptions are a single phrase with the actual action; the only multi-part description is for `upload_attachment` (5 MB limit + reference to alternative tools, purely operational).
- `annotations` are present (`readOnlyHint`, `destructiveHint`) — machine-readable hints, not textual directives.
- There is neither `registerResource` nor `registerPrompt` — there are no other text channels in the server.
