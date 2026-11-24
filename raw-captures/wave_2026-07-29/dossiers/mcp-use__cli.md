# UNIT: @mcp-use/cli | npm v3.6.6 (published 2026-07-20T22:22:13.507Z) | frames: npm-top | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

@mcp-use/cli is a command-line utility (bin `mcp-use`, built on `commander`) for **building, developing, and deploying** MCP servers to Manufact cloud, plus an MCP-**client** for connecting to other servers. The package itself does not include server-side MCP code.

Justification (static analysis of dist/index.js, 10 102 lines, and dist/index.cjs):

- package.json: `"description": "The mcp-use CLI is a tool for building and deploying MCP servers..."`, `"bin": {"mcp-use": "./dist/index.cjs"}`. Dependencies are vite, esbuild, tsx, commander, tar, chokidar, etc. (build toolchain), not an MCP SDK server.
- In the code there is not a single call to `new Server(...)`, `McpServer`, `FastMCP`, `createMCPServer`, `registerTool`, `addTool`, `server.tool(...)`, `setRequestHandler`, `StdioServerTransport`. The only mention of `@modelcontextprotocol/sdk` (line 4994 index.js) is a check whether this dependency exists in the *user* project that the CLI is going to deploy.
- All matches for the word "McpServer" are helpers `getMcpServerUrl()` / `getMcpServerUrlForCloudServer()`, which form the URL of the deployed server for output to the console.
- The structure is commander commands: `build`, `dev`, `start`, `login`, `logout`, `whoami`, `deployments *`, `servers *`, `env *`, `org *`, `skills add/install`, `client connect/list/remove`, and per-server subcommands `tools list/call/describe`, `resources list/read/subscribe`, `prompts list/get`, `auth status/refresh/logout` — this is a CLI wrapper for an MCP *client* and a deployment panel, not server tools.
- `instructions` for the server constructor are absent (there is nothing to pass them to).

## CHANNEL: instructions, npm (static)
(not found statically — there is no server code in the package)

## CHANNEL: tool descriptions, npm (static, coverage=none)
No MCP tools are registered. The `.description(...)` strings in the code are commander help texts for a human in the terminal, not tool descriptions for an LLM.

## NOTES
- Code is bundled with tsup/esbuild, but not minified (readable names, 10k lines).
- Risk of dynamic construction of strings for the MCP channel: not applicable — there is no channel.
- Reviewed: package.json, README.md, dist/index.js (grep across the whole file), dist/index.cjs (grep), list of all 68 files in the package (the rest are .d.ts/.map/shims).
