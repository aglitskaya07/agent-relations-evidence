# UNIT: nothumanallowed | npm v16.0.64 (published 2026-05-23T07:49:19.717Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

The package is a CLI launcher/bootstrapper for a local AI assistant "NHA", not an MCP server. Rationale:

1. **There is no MCP server code in the tarball.** There is no `@modelcontextprotocol/sdk` dependency (deps: acorn, imapflow, mailparser, typescript, ws, better-sqlite3). Grep across all 73 .mjs files does not find `new Server(`, `McpServer`, `FastMCP`, `registerTool`, `server.tool(`, `ListTools` — only ordinary `http.createServer` for the local Web UI and OAuth callbacks.
2. **The `nha mcp` command launches CODE THAT IS NOT IN THE PACKAGE.** `src/cli.mjs:171-172`: `case 'mcp': return spawnCore('pif', ['mcp']);` — spawnCore (`src/spawn.mjs`) executes `~/.nha/core/pif.mjs`. This file is downloaded on first run from `https://nothumanallowed.com/cli/pif.mjs` (see `src/bootstrap.mjs:66-67`, `BASE_URL` in `src/constants.mjs:9`). `legion-x.mjs` and 38 agent files are downloaded similarly. The real MCP server is a remote runtime artifact, statically unobservable.
3. **Internal "80 tools" are not MCP registrations.** `src/services/tool-executor.mjs` (5598 lines) contains a text system prompt for the LLM listing tools of the form `14. calendar_create(summary, start, end, ...)` — this is the local assistant's own prompt-based tool-calling, not MCP `tools/list`. How these tools are exposed in MCP mode is determined by the downloaded pif.mjs.

## CHANNEL: instructions, npm (static)
(not found statically — there is no MCP server constructor in the package)

## CHANNEL: tool descriptions, npm (static, coverage=none)
(There are no MCP tool registrations in the package; tool descriptions exist only as the LLM prompt of the internal assistant in tool-executor.mjs and as unknown content of the downloaded pif.mjs)

## NOTES
- The code is not minified (readable ESM with comments), except for the Web UI bundle `src/ui-dist/assets/index-DNzlAbYu.js`.
- **High risk of dynamics:** all server logic (legion-x.mjs, pif.mjs, agents, extensions) is pulled from nothumanallowed.com at bootstrap and updated by the `nha update` command — MCP channel behavior can change without publishing a new npm version. To assess the steering content, a separate (non-static) stage is needed to capture https://nothumanallowed.com/cli/pif.mjs.
- Reviewed: package.json, README.md, bin/, all key src/*.mjs (constants, bootstrap, spawn, cli, downloader), grep across all 89 files in the package.
