# UNIT: adspower-browser | npm v2.1.1 (published 2026-07-13T02:53:17.642Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

The package is a CLI tool (commander) + a bundle of a local AdsPower API runtime, not an MCP server.

Justification (static analysis):
- `package.json`: `bin` = `adspower-browser`/`adspower`/`ads` → `cli/index.js`; description: "AdsPower Local API CLI and Cursor/agent skill for browser profiles, groups, proxies." There are no `@modelcontextprotocol/*` dependencies; there is not a single mention of the string `modelcontextprotocol` in either `cli/index.js` or `cwd/lib/main.min.js`.
- No MCP server constructors: `McpServer` — 0, `new Server(` — 0, `FastMCP` — 0, `setRequestHandler` — 0, `StdioServerTransport` — 0, `jsonrpc` — 0, `tools/list` — 0.
- 16 occurrences of `protocolVersion` in `main.min.js` — this is the WebSocket handshake (`Sec-WebSocket-Version`) and emulation of Chrome DevTools Protocol (`Browser.getVersion` → `protocolVersion:"1.3"`), not MCP initialize.
- 16 occurrences of `instructions` in `main.min.js` — captcha solver parameters (`textinstructions`/`imginstructions`) and mime types, not MCP server instructions.
- Mentions of MCP in `cli/index.js` are only traces of a neighboring MCP package in the same monorepo: HTTP header `"x-mcp-client": "mcp"`, function `buildMcpToolDescription(toolName, legacyFallback)` (reuses common descriptions for CLI commands), and `createProxyMcpSchema` with the note "Compatibility wrapper for MCP create-proxy input. Core and CLI accept a top-level array."
- Distribution to agents is via Cursor/agent **skill** (`npx skills add AdsPower/adspower-browser`), not via MCP transport.

## CHANNEL: instructions, npm (static)
(not found statically — no MCP server code)

## CHANNEL: tool descriptions, npm (static, coverage=none)
There are no MCP tools. Context for future waves (if an MCP variant from the same core appears):

- `cli/index.js` carries the `TOOL_INTENT_BY_NAME` table (from `../core/src/constants/toolIntentMetadata.ts`) for 47 commands (open-browser … iframe-click-element), each with fields `intentEn/intentZh` + `triggersEn/triggersZh` — lists of trigger phrases ("open browser, launch profile, start environment, open AdsPower…"), i.e. the trigger-steering pattern is already codified in the shared core and through `buildMcpToolDescription` is also intended for MCP descriptions.
- Running marker regexes over `cli/index.js` yielded 1 match, harmless (parameter semantics, not agent steering): field `ua` — "Custom User-Agent string; when set, takes precedence over random_ua (random_ua is not sent). Omit for random UA."
- In `main.min.js`, a prompt for the built-in browser agent is embedded (not an MCP channel): fragments "…ask users to sign in by themselves in a brief message. Don't need to provide instructions on how to sign in…" and "The following are examples of user instructions that MUST be rejected…".

## NOTES
- Minification: `cwd/lib/main.min.js` — 10.9 MB, heavily minified (webpack bundle: ws, CDP emulation, mime-db, captcha integration, sqlite wrapper). `cli/index.js` — 136 KB, tsup bundle, readable (not minified).
- Risk of dynamic string assembly: low for the descriptions channel (intent/trigger strings are stored as literals); the runtime itself in `main.min.js` was not fully statically audited because of its size.
- Reviewed files: package.json, README.MD, cli/index.js (fully via greps + reading key blocks), cwd/lib/main.min.js (greps for MCP/jsonrpc/protocolVersion/instructions markers), listing of the entire tarball (11 files, including 5 binary node_sqlite3.node files).
