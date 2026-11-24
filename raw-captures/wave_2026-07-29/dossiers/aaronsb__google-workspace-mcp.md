# UNIT: @aaronsb/google-workspace-mcp | npm v4.0.1 (published 2026-07-12T21:51:22.133Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Yes, this is an MCP server. `build/server/server.js` creates `new Server({name: '@aaronsb/google-workspace-mcp', version: VERSION}, {capabilities: {tools: {}, resources: {}}})` from `@modelcontextprotocol/sdk/server/index.js`, attaches `StdioServerTransport`, registers ListTools/CallTool/ListResources/ReadResource handlers. Entry point — `bin: google-workspace-mcp -> ./build/index.js`.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name`/`version` and capabilities are passed to the `Server` constructor — there is no `instructions` field anywhere in `build/` (grep for "instructions" returned only unrelated mentions). The server-instructions channel is not used.

## CHANNEL: tool descriptions, npm (static, coverage=full)

A total of 11 tools (4 hand-coded in `build/server/tools.js` + 7 factory-generated from YAML manifests `build/factory/manifest/*.yaml`; the top-level `description` of each YAML becomes the tool description without modifications — verified by `generateSchema` in `build/factory/generator.js`).

1. **manage_accounts** — "Manage Google Workspace account lifecycle: list, authenticate, check status, refresh credentials, update scopes, or remove accounts."
2. **manage_workspace** — "Manage files and directories in the workspace sandbox. Supports nested paths (e.g. \"reports/q1/summary.csv\"). The workspace is the exchange point for file operations (attachments, downloads, exports)."
3. **manage_scratchpad** — "Compose, edit, and deliver text content. Use for any multi-line content: emails, documents, descriptions. Compose in the scratchpad, edit by line or JSON path, attach files, then send to any target. For short one-liners, use the service tool directly instead."
4. **queue_operations** — "Execute multiple operations in sequence. Operations run in order with result references ($0.field) to chain outputs. Use for multi-step workflows."
5. **manage_calendar** — "List events, view agenda, check availability, or manage calendar events." (9 operations)
6. **manage_docs** — "Read, write, insert, and find-replace text in Google Docs documents." (5 operations)
7. **manage_drive** — "Search, upload, download, share, comment on, or manage files in Google Drive." (17 operations)
8. **manage_email** — "Search, read, send, forward, or manage emails in a Google Workspace account. Supports Gmail search syntax." (15 operations)
9. **manage_meet** — "Browse past Google Meet conferences, participants, transcripts, recordings, and AI-generated smart notes. Requires Workspace Business Standard+ for transcripts/recordings." (11 operations)
10. **manage_sheets** — "Read, write, and manage Google Sheets spreadsheets." (13 operations)
11. **manage_tasks** — "Manage task lists and tasks in Google Tasks." (10 operations)

Marker scan of steering regexes in the manifests and tools.js: 0 matches. The descriptions are purely functional, without self-promotion, priority directives, or attempts to displace built-in tools. The only mild steering is in manage_scratchpad ("Use for any multi-line content… For short one-liners, use the service tool directly instead") — internal routing between the server's own tools, not against others.

Additionally: the server publishes 4 MCP resources (gws://safety/policies, gws://config/services, gws://config/workspace, gws://config/version) — metadata, without instructional text for the model.

## NOTES

- The code is not minified: clean tsc output with comments and sourcemaps, readable directly.
- Risk of dynamic string assembly: low. Tool descriptions are static strings in tools.js or top-level `description` from YAML; the only concatenation is the description enum parameter `operation`, built from per-operation descriptions in the manifest ("op: desc | op: desc"), deterministically from static YAML, without env/network sources.
- Reviewed ~12 files: package.json, build/server/{server,tools}.js, build/factory/{registry,generator,patches}.js, 7 YAML manifests; plus grep over all build/ (72 JS files) for instructions/registerTool/steering markers.
