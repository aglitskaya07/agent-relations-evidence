# UNIT: @claude-flow/mcp | npm v3.0.0-alpha.9 (published 2026-05-09T18:31:20.248Z) | frames: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: server-framework (library) with built-in MCP server code

Package — standalone implementation of an MCP server (part of claude-flow v3, ruvnet): full server code (initialize/tools/resources/prompts/tasks, stdio/HTTP/WebSocket transports) in `src/server.ts` (1131 lines) + tool-registry. This is NOT a client and NOT a proxy, but also not a ready-made production server: package.json has no `bin`, the package is intended for embedding (`quickStart` + `registerTool(defineTool(...))` from README). Application tools are defined by the host application; the package itself registers only 4 built-in system tools (`registerBuiltInTools()`, src/server.ts:1033). Classified as a server (server code exists), with the caveat "framework".

## CHANNEL: instructions, npm (static, 50 chars)

Passed in the result of `initialize` (src/server.ts:492, identical in dist/server.js:370):

```
Claude-Flow MCP Server V3 ready for tool execution
```

A neutral status line, no steering content whatsoever (no priorities, no "primary", no coercion to use).

## CHANNEL: tool descriptions, npm (static, coverage=full)

Built-in tools: 4 (src/server.ts:1033–1090; dist/server.js matches). All descriptions verbatim:

1. **system/info** — `Get system information`
2. **system/health** — `Get system health status`
3. **system/metrics** — `Get server metrics`
4. **tools/list-detailed** — `List all registered tools with details`
   - parameter `category`: `Filter by category`

There are no manipulation markers (precedence/primary/instead of/MUST use, etc.) in the descriptions — all four descriptions are extremely neutral, 3–6 words each.

## NOTES

- The code is not minified: the tarball contains both `src/*.ts` (sources) and `dist/*.js` (tsc transpilation with sourcemaps); src and dist were compared, no discrepancies in instructions/descriptions were found.
- Risk of dynamic string assembly: low. instructions — a static literal; built-in tool descriptions — static literals. The only dynamic aspect is that application tools are registered by host code from outside the package (framework by design) — their descriptions are outside the scope of this tarball.
- Reviewed: structure of 318 files, package.json, README.md, src/server.ts (key blocks) read in full/fragmentary form, grep across all src/ and dist/ for instructions/registerTool/description (~30 files affected by grep).
- Side observation: the tarball also contains `.claude/` (settings.json, commands, helpers scripts) and CLAUDE.md — material for the "files in package" channel, outside the channels claimed here.
