# UNIT: @gongrzhe/server-gmail-autoauth-mcp | npm v1.1.11 (published 2025-08-06T01:16:22.211Z) | frames: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

Type: confirmed MCP server (stdio). `new Server({ name: "gmail", version: "1.0.0", capabilities: { tools: {} } })` in `dist/index.js:256`, transport `StdioServerTransport`, SDK `@modelcontextprotocol/sdk`.

## CHANNEL: instructions, npm (static)
(not found statically)

The Server constructor receives only `name`, `version`, `capabilities` — there is no `instructions` field either in the constructor or anywhere else in the package (grep for `instructions` yielded only import-irrelevant zeros; the only occurrence is absent).

## CHANNEL: tool descriptions, npm (static, coverage=full)

19 tools, all registered statically in one ListTools handler (`dist/index.js:264-362`). Descriptions verbatim:

| # | name | description |
|---|------|-------------|
| 1 | `send_email` | Sends a new email |
| 2 | `draft_email` | Draft a new email |
| 3 | `read_email` | Retrieves the content of a specific email |
| 4 | `search_emails` | Searches for emails using Gmail search syntax |
| 5 | `modify_email` | Modifies email labels (move to different folders) |
| 6 | `delete_email` | Permanently deletes an email |
| 7 | `list_email_labels` | Retrieves all available Gmail labels |
| 8 | `batch_modify_emails` | Modifies labels for multiple emails in batches |
| 9 | `batch_delete_emails` | Permanently deletes multiple emails in batches |
| 10 | `create_label` | Creates a new Gmail label |
| 11 | `update_label` | Updates an existing Gmail label |
| 12 | `delete_label` | Deletes a Gmail label |
| 13 | `get_or_create_label` | Gets an existing label by name or creates it if it doesn't exist |
| 14 | `create_filter` | Creates a new Gmail filter with custom criteria and actions |
| 15 | `list_filters` | Retrieves all Gmail filters |
| 16 | `get_filter` | Gets details of a specific Gmail filter |
| 17 | `delete_filter` | Deletes a Gmail filter |
| 18 | `create_filter_from_template` | Creates a filter using a pre-defined template for common scenarios |
| 19 | `download_attachment` | Downloads an email attachment to a specified location |

Marker scan for steering regexes (instead of built-in, most powerful, always default, PRECEDENCE, MUST use, primary, prefer, whenever the user, etc.): 0 matches. The descriptions are short, neutral, functional — there is no steering lexicon.

## NOTES (static analysis)
- Code is NOT minified: readable tsc output with comments; description strings are literals.
- Risk of dynamic string assembly: low. All descriptions are static string literals; no template literals / concatenation in the ListTools handler.
- Reviewed: `package.json`, `dist/index.js` (main, 51.8 KB, full server code), grep on `dist/filter-manager.js`, `dist/label-manager.js`, `dist/utl.js`, `dist/evals/evals.js` — helper modules without tool registration. Total 6 code files + README/LICENSE.
- The only Server registration point is index.js:256; there are no other Server/McpServer/FastMCP in the package.
