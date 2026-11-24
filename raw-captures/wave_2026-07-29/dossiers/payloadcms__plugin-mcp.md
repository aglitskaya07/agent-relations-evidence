# UNIT: @payloadcms/plugin-mcp | npm v3.86.0 (published 2026-07-10T15:42:43.512Z) | scopes: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (plugin)

This is an MCP server: a plugin for Payload CMS that mounts an MCP endpoint inside a Payload application via `createMcpHandler` from the `mcp-handler` package (`src/mcp/getMcpHandler.ts:109`) and registers tools via `server.registerTool(...)`. Not a standalone binary, but an embedded server: HTTP transport (basePath = Payload API route, SSE disabled by default), authorization by API keys (`payload-mcp-api-keys` collection).

## CHANNEL: instructions, npm (static)
(not found statically)

The `instructions` field exists, but it is a pass-through of user configuration, not a hardcoded string: the type `MCPServerOptions.instructions?: string` (`src/types.ts:377-379`, JSDoc: "Optional instructions describing how to use the server and its features.") is passed to `createMcpHandler(..., { instructions: serverOptions.instructions, ... })` (`src/mcp/getMcpHandler.ts:530`). There is no default value in the package — if the integrator did not set anything, instructions are absent.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Generation feature: tool names are dynamic — for each enabled collection, `create{Slug}` / `update{Slug}` / `find{Slug}` / `delete{Slug}` are created (for example `findPosts`), for globals — `find{GlobalSlug}` / `update{GlobalSlug}`. The description is taken from the user's `collections[slug].description`, and if absent — from the static template in `src/mcp/tools/schemas.ts` (for globals — template + user description via `\n\n`). Below are ALL 21 static description templates, verbatim:

Basic (CRUD, generated from slugs):
1. `find{Global}` (findGlobal): "Find a Payload global singleton configuration."
2. `find{Collection}` (findResources): "Find documents in a collection by ID or where clause using Find or FindByID."
3. `create{Collection}` (createResource): "Create a document in a collection."
4. `update{Collection}` (updateResource): "Update documents in a collection by ID or where clause."
5. `delete{Collection}` (deleteResource): "Delete documents in a collection by ID or where clause."
6. `update{Global}` (updateGlobal): "Update a Payload global singleton configuration."

Experimental (fixed names; most only with NODE_ENV=development + explicit opt-in):
7. `createCollection`: "Creates a new collection with specified fields and configuration."
8. `findCollections`: "Finds and lists collections with optional content and document counts."
9. `updateCollection`: "Updates an existing collection with new fields, modifications, or configuration changes."
10. `deleteCollection`: "Deletes a collection and optionally updates the configuration."
11. `findConfig`: "Reads and displays the current configuration file."
12. `updateConfig`: "Updates the configuration file with various modifications."
13. `auth`: "Checks authentication status for the current user."
14. `login`: "Authenticates a user with email and password."
15. `verify`: "Verifies a user email with a verification token."
16. `resetPassword`: "Resets a user password with a reset token."
17. `forgotPassword`: "Sends a password reset email to a user."
18. `unlock`: "Unlocks a user account that has been locked due to failed login attempts."
19. `createJob`: "Creates a new job (task or workflow) with specified configuration."
20. `updateJob`: "Updates an existing job with new configuration, schema, or handler code."
21. `runJob`: "Runs a job with specified input data and queue options."

Marker scan of displacement/capture formulations (PRECEDENCE, "always default", "instead of built-in", "MUST use", "primary tool", "whenever the user", etc.) in src/ and README: 0 matches. All descriptions are dry functional one-liners without agent steering.

## NOTES
- The code is NOT minified: both src/ (TypeScript) and dist/ (readable ESM with sourcemaps) are in the tarball.
- Risk of dynamic string construction: moderate and by design. Tool names are assembled from collection slugs at runtime; descriptions and instructions can be fully overridden by the integrator config (`collections[slug].description`, `serverOptions.instructions`, plus arbitrary custom tools/prompts/resources via `pluginOptions.mcp`). In other words, the actual steering of a specific installation is determined by the integrator, not by the package — the package itself is neutral.
- Reviewed: ~12 files in depth (getMcpHandler.ts, registerTool.ts, schemas.ts, types.ts, index.ts, defaults.ts, tools/resource/*, tools/global/find.ts, README.md, package.json surroundings) + grep scan of all src/ and README (in total there are ~40 source .ts files + a duplicate dist).
