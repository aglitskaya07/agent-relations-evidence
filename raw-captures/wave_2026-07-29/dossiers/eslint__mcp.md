# UNIT: @eslint/mcp | npm v0.3.10 (published 2026-07-27T21:55:12.344Z) | frames: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

Verified MCP server: `new McpServer({ name: "ESLint", version: "0.3.10" })` from `@modelcontextprotocol/sdk/server/mcp.js`, stdio transport (`src/mcp-cli.js`), bin in package.json. Official ESLint package (repo eslint/rewrite, packages/mcp), author Nicholas C. Zakas.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name` and `version` are passed to the McpServer constructor — there is no `instructions` field; there is no custom initialize handler.

## CHANNEL: tool descriptions, npm (static, coverage=full)

A total of 1 tool.

### lint-files
> Lint files using ESLint. You must provide a list of absolute file paths to the files you want to lint. The absolute file paths should be in the correct format for your operating system (e.g., forward slashes on Unix-like systems, backslashes on Windows).

inputSchema: `{ filePaths: z.array(z.string().min(1)).nonempty() }` (without `.describe()` — comment in code: Cursor breaks on describe in schema).

## NOTE: steering in runtime tool results (not in the description)

In the `lint-files` handler (src/mcp-server.js:49-56), two imperative text blocks are appended to the lint results, which the model receives as the tool response content:

> "Here are the results of running ESLint on the provided files. Before doing anything else, you must display the full list to the user:"

> "If the user asked to fix any issues found, proceed in fixing them. If the user did not ask to fix issues found, you must ask the user for confirmation before attempting to fix the issues found."

This is agent behavior management through the tool-result channel, not through description/instructions. The character is conservative/protective (show everything to the user, ask for confirmation before fixes), not competitively displacing.

## NOTES
- The code is not minified, readable source with comments (src/ is shipped as is, files: ["src"]).
- Risk of dynamic string construction: absent — all strings are literals, with no concatenation/templates in descriptions.
- Reviewed files: 5 of 5 in the package (package.json, README.md, LICENSE, src/mcp-server.js, src/mcp-cli.js); analysis complete.
