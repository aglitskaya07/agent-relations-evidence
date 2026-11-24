# UNIT: @adeze/raindrop-mcp | npm v2.4.5 (published 2026-03-11T06:15:52.834Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

A full-fledged MCP server for Raindrop.io (bookmarks). Two entry points: `build/index.js` (stdio, bin `raindrop-mcp`) and `build/server.js` (HTTP/Express). Inside — `new McpServer(...)` from `@modelcontextprotocol/sdk` (class `RaindropMCPService`, src/services/raindropmcp.service.ts according to sourcemaps), registration of tools via `server.registerTool(...)` in a loop over the declarative array `toolConfigs`, plus resources, prompts, and experimental elicitation capability.

## CHANNEL: instructions, npm (static)
(not found statically)

The `McpServer` constructor receives only `{ name: "raindrop-mcp", version, description: "MCP Server for Raindrop.io with advanced interactive capabilities" }` — the `instructions` field is not passed either in index.js (line ~41156) or in server.js (line ~55910). There is no separate text in initialize either.

## CHANNEL: tool descriptions, npm (static, coverage=full)

17 tools, all descriptions are static string literals, given verbatim:

1. **diagnostics** — "Diagnostics resource and runtime metadata."
2. **collection_list** — "Lists all Raindrop.io collections as a flat list."
3. **get_collection_tree** — "Returns a hierarchical view of all collections with full breadcrumb paths."
4. **collection_manage** — "Creates, updates, or deletes a collection. Use the operation parameter to specify the action."
5. **bookmark_search** — "Searches bookmarks with advanced filters, tags, and full-text search."
6. **bookmark_manage** — "Creates, updates, or deletes bookmarks. Use the operation parameter to specify the action."
7. **get_raindrop** — "Fetch a single Raindrop.io bookmark by ID."
8. **list_raindrops** — "List Raindrop.io bookmarks for a collection with pagination."
9. **bulk_edit_raindrops** — "Bulk update, move, or remove bookmarks in a specific collection."
10. **tag_manage** — "Renames, merges, or deletes tags. Use the operation parameter to specify the action."
11. **highlight_manage** — "Creates, updates, or deletes highlights. Use the operation parameter to specify the action."
12. **library_audit** — "Scans the entire library for broken links and duplicate bookmarks."
13. **empty_trash** — "Permanently delete all bookmarks currently in the trash collection. Requires 'confirm: true' to execute."
14. **cleanup_collections** — "Remove all collections that do not contain any bookmarks. Requires 'confirm: true' to execute."
15. **remove_duplicates** — "Optimized duplicate deletion pattern. Scans all collections and removes duplicates in batches of 50 to minimize round-trips. Supports dry run to report counts without deleting."
16. **get_suggestions** — "Get AI-powered suggestions for tags and collections for a specific URL or existing bookmark."
17. **suggest_tags** — "Uses AI to suggest relevant tags based on bookmark metadata (title, URL, description)."

Steering marker patterns (instead of built-in / prefer / primary / MUST use / takes precedence, etc.) do NOT appear in the descriptions. The tone is neutrally functional; the only imperatives are protective ("Requires 'confirm: true' to execute").

## Other channels

- **Prompts (3):** organize_by_topic, find_duplicates, export_markdown — neutral system prompts about organizing bookmarks, without steering toward the server.
- **Sampling model hints** in suggestion tools: `hints: [{ name: "claude-3-5-sonnet" }, { name: "gpt-4o" }]` — model preferences for MCP sampling, not steering the agent.
- **Resources:** mcp://user/profile, diagnostics://server — static JSON stubs.

## NOTES

- The code is NOT minified: bun ESM bundle with sourcemaps, names and structure are readable; node_modules (SDK, axios, express, keyv, openai, etc.) are bundled into the same files (~1.9 MB server.js, ~1.4 MB index.js).
- Risk of dynamic construction of descriptions is low: all description values are literals in declarative tool configs; the only dynamic part is title (generated from name by capitalization).
- Reviewed files: 3 substantively (package.json, build/index.js, build/server.js); 7 total in the tarball (plus LICENSE, README.md, 2 source maps).
