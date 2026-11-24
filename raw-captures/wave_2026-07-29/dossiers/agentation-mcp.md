# UNIT: agentation-mcp | npm v1.2.0 (published 2026-02-15T20:37:04.456Z) | scope: npm-top | captured 2026-07-29 (static, tarball)

Verified MCP server: stdio server (`new Server({name: "agentation", version: "0.0.1"}, {capabilities: {tools: {}}})` + `StdioServerTransport`, dist/index.mjs:1434-1458) and an additional Streamable HTTP variant (`createMcpSession`, dist/index.mjs:1704-1723). Dependency `@modelcontextprotocol/sdk`. Purpose: visual feedback (annotations in the browser) for AI coding agents; SQLite/in-memory store, webhooks.

## CHANNEL: instructions, npm (static)
(not found statically)

Both Server constructors receive only `{name, version}` and `{capabilities: {tools: {}}}` — the `instructions` field is never passed anywhere; grep for the word `instructions` across all three bundles (cli.js, index.js, index.mjs) yields 0 matches.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Static array `TOOLS` (dist/index.mjs:982-1119), returned as is in ListTools by both transports. 9 tools, all verbatim:

1. **agentation_list_sessions** — "List all active annotation sessions"
2. **agentation_get_session** — "Get a session with all its annotations"
3. **agentation_get_pending** — "Get all pending (unacknowledged) annotations for a session. Use this to see what feedback the human has given that needs attention."
4. **agentation_get_all_pending** — "Get all pending annotations across ALL sessions. Use this to see all unaddressed feedback from the human across all pages they've visited."
5. **agentation_acknowledge** — "Mark an annotation as acknowledged. Use this to let the human know you've seen their feedback and will address it."
6. **agentation_resolve** — "Mark an annotation as resolved. Use this after you've addressed the feedback. Optionally include a summary of what you did."
7. **agentation_dismiss** — "Dismiss an annotation. Use this when you've decided not to address the feedback, with a reason why."
8. **agentation_reply** — "Add a reply to an annotation's thread. Use this to ask clarifying questions or provide updates to the human."
9. **agentation_watch_annotations** — "Block until new annotations appear, then collect a batch and return them. Triggers automatically when annotations are created — the user just annotates in the browser and the agent picks them up. After detecting the first new annotation, waits for a batch window to collect more before returning. Use in a loop for hands-free processing. After addressing each annotation, call agentation_resolve with the annotation ID and a summary of what you did. Only resolve annotations the user accepted — if the user rejects your change, leave the annotation open."

Steering markers: soft behavioral directives in No. 9 ("Use in a loop for hands-free processing", "After addressing each annotation, call agentation_resolve…", "Only resolve annotations the user accepted") and the "Use this to/when/after" pattern in No. 3-8 — a workflow guide, not cross-tool displacement of competitors; there are no markers like "instead of built-in / takes precedence / MUST use".

## NOTES
- The code is a tsup bundle, readable (not minified); sourcemaps are included.
- TOOLS — a static literal; there is no dynamic construction of description strings, dynamic risk is low. The descriptions in cli.js and index.mjs match byte for byte (diff on the extracted description — identical).
- Reviewed: package.json, README.md (heading), dist/cli.js, dist/index.js, dist/index.mjs (~256 KB of text; .d.ts and .map — tangentially).
- Version mismatch: package.json v1.2.0, but in the Server constructor version "0.0.1" is hardcoded.
