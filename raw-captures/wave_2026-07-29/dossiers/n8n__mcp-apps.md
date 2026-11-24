# UNIT: @n8n/mcp-apps | npm v0.9.0 (published 2026-07-21T07:29:18.713Z) | frames: npm-top | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

The package is a helper library ("UI resources and server helpers for n8n"), not a standalone MCP server:

- There is no server construction anywhere in `dist/`: grep for `new Server|new McpServer|createServer|instructions` — zero matches. `@modelcontextprotocol/sdk` — only as a peerDependency.
- The `@n8n/mcp-apps/server` export (`dist/server/index.js`) returns helpers that are called by code in `packages/cli` of the main n8n on top of an ALREADY created server:
  - `registerMcpAppTool(server, name, config, handler)` — a thin wrapper over `server.registerTool`, the only logic is `_meta` normalization (synchronization of `ui.resourceUri` and the legacy key `'ui/resourceUri'`). It does not set either the tool name or the description — everything comes from outside.
  - `registerWorkflowPreviewApp(server, options)` — registers ONE MCP resource (not a tool): `ui://workflow-preview/workflow-preview.html`, mime `text/html;profile=mcp-app`, description verbatim: `'Workflow preview shown after creating a workflow from code'`. Returns a prebuilt inline HTML (Vue application MCP Apps / ext-apps) with telemetry config injection (RudderStack CDN origin).
- README confirms: this is the UI part (MCP Apps via the `@modelcontextprotocol/ext-apps` extension) for rendering workflow previews after the `create_workflow_from_code` tool, which lives in n8n core.

## CHANNEL: instructions, npm (static)
(not found statically — the package does not construct a server, the string instructions is nowhere in dist)

## CHANNEL: tool descriptions, npm (static, coverage=none)
The package does not define tools (0). The only text that reaches the MCP surface is the resource description:

- resource `workflow-preview` (`ui://workflow-preview/workflow-preview.html`): "Workflow preview shown after creating a workflow from code"

Marker scan of steering regexes across the entire dist — no matches.

## NOTES
- The code is not minified (tsc output with sourcemaps), fully readable; exception — `dist/apps/workflow-preview.html` (inline-built Vite/Vue bundle, minified, but this is a UI artifact, not server strings).
- Risk of dynamic string assembly: low. The only dynamic part is `injectTelemetryConfig`, which inserts `<script>window.<GLOBAL>=<json></script>` into the resource HTML; descriptions/instructions are not assembled by concatenation.
- Reviewed: all 12 JS/JSON/MD files of the server part (package.json, README, dist/server/*.js, dist/apps-manifest.js, dist/telemetry-contract.js) + grep across all ~30 files in the package.
