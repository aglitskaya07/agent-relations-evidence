# UNIT: git-mcp | GitMCP | github idosal/git-mcp | author type: community | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript / Cloudflare Workers. `src/index.ts` — `export class MyMCP extends McpAgent { server = new McpServer({ name: "GitMCP", version: "1.1.0" }); ... }`; tools are registered via `this.server.tool(tool.name, tool.description, tool.paramsSchema, cb, { annotations })`. Transport — SSE/streamable HTTP via `MyMCP.serve("/*")`. This is an MCP server (remote, per-repo dynamic tooling).

The toolset depends on the URL used to connect: `getHandlerByRepoData()` chooses a handler (`default`, `generic` for `docs/`, `threejs` for `mrdoob/three.js`, `react-router` for `remix-run/react-router`). Below are all statically defined descriptions for all handlers.

## CHANNEL: instructions
(not found statically)

The `McpServer` constructor receives only `{ name, version }` — there is no `instructions` field; there is no custom `initialize` handler in the repository.

## CHANNEL: tool descriptions (coverage=full)

A total of 12 tools were statically defined (unique by name/description).

### A. DefaultRepoHandler (`src/api/tools/repoHandlers/DefaultRepoHandler.ts`), descriptions are assembled by generators from `src/api/tools/commonTools.ts`

Names are dynamic: `fetch_<repo>_documentation`, `search_<repo>_documentation`, `search_<repo>_code` (otherwise fallback `fetch_documentation` / `search_documentation` / `search_code`).

1. **`fetch_<repo>_documentation`** (`generateFetchToolDescription`) — three branches:
   - urlType == "subdomain": `Fetch entire documentation file from the ${owner}/${repo} GitHub Pages. Useful for general questions. Always call this tool first if asked about ${owner}/${repo}.`
   - urlType == "github": `Fetch entire documentation file from GitHub repository: ${owner}/${repo}. Useful for general questions. Always call this tool first if asked about ${owner}/${repo}.`
   - default: `Fetch entire documentation for the current repository.`
   - catch-fallback: `Fetch documentation for the current repository.`

2. **`search_<repo>_documentation`** (`generateSearchToolDescription`) — three branches:
   - urlType == "subdomain": `Semantically search within the fetched documentation from the ${owner}/${repo} GitHub Pages. Useful for specific queries.`
   - urlType == "github": `Semantically search within the fetched documentation from GitHub repository: ${owner}/${repo}. Useful for specific queries.`
   - default: `Semantically search within the fetched documentation for the current repository.`
   - catch-fallback: `Search documentation for the current repository.`

3. **`search_<repo>_code`** (`generateCodeSearchToolDescription`):
   `Search for code within the GitHub repository: "${owner}/${repo}" using the GitHub Search API (exact match). Returns matching files for you to query further if relevant.`

### B. Universal tool (`src/api/tools/index.ts`), added to ANY handler

4. **`fetch_generic_url_content`**
   `Generic tool to fetch content from any absolute URL, respecting robots.txt rules. Use this to retrieve referenced urls (absolute urls) that were mentioned in previously fetched documentation.`

### C. GenericRepoHandler (`src/api/tools/repoHandlers/GenericRepoHandler.ts`) — active for `docs/`

5. **`match_common_libs_owner_repo_mapping`**
   `Match a library name to an owner/repo. Don't use it if you have an owner and repo already. Use this first if only a library name was provided. If found - you can use owner and repo to call other tools. If not found - try to use the library name directly in other tools.`

6. **`fetch_generic_documentation`**
   `Fetch documentation for any GitHub repository by providing owner and project name`

7. **`search_generic_documentation`**
   `Semantically search in documentation for any GitHub repository by providing owner, project name, and search query. Useful for specific queries.`

8. **`search_generic_code`**
   `Search for code in any GitHub repository by providing owner, project name, and search query. Returns matching files. Supports pagination with 30 results per page.`

### D. ThreejsRepoHandler (`src/api/tools/repoHandlers/ThreejsRepoHandler.ts`) — active for `mrdoob/three.js`

9. **`get_threejs_reference_docs_list`**
   `Get the reference docs list. This should be the first step. It will return a list of all the reference docs and manuals and their corresponding urls.`

10. **`get_threejs_specific_docs_content`**
    `Get the content of specific docs or manuals. This should be the second step. It will return the content of the specific docs or manuals. You can pass in a list of document or manual names.`

11. **`search_threejs_documentation`**
    `Semantically search the repository documentation for the given query. Use this if you need to find information you don't have in the reference docs.`

12. **`fetch_threejs_urls_inside_docs`**
    `Fetch content from URLs that are inside the reference docs. Usually contains '#' in the url. Returns the content of the pages as markdown.`

### E. ReactRouterRepoHandler (`src/api/tools/repoHandlers/ReactRouterRepoHandler.ts`)

Takes all DefaultRepoHandler tools and replaces the search tool with its own implementation with the SAME name (`generateSearchToolName`) and the SAME description (`generateSearchToolDescription`) — no new descriptions are introduced.

### F. Other text included for the agent (not description, but response content)

`ThreejsRepoHandler.noopFallbackSearch` returns as text:
`Please use the ${GET_REFERENCE_DOCS_LIST_TOOL_NAME} tool first to get the list of reference docs and manuals, and then use the ${GET_SPECIFIC_DOCS_CONTENT_TOOL_NAME} tool to get the content of the specific docs or manuals.`
(substituted `get_threejs_reference_docs_list` and `get_threejs_specific_docs_content`)

### Annotations (title / readOnlyHint)

All 12 tools are marked `readOnlyHint: true`, with human-readable title: Fetch Documentation, Search Documentation, Search Code, Fetch URL Content, Match Library to Repository, Fetch Generic Documentation, Search Generic Documentation, Search Generic Code, Get Three.js Reference Docs List, Get Three.js Specific Docs Content, Search Three.js Documentation, Fetch Three.js URLs Inside Docs.

## NOTES (static-extraction caveats)

- Repository language: TypeScript (Cloudflare Workers + React Router UI); MCP SDK `@modelcontextprotocol/sdk/server/mcp.js` + `agents/mcp`.
- Definitions were found in: `src/index.ts` (server constructor), `src/api/tools/index.ts`, `src/api/tools/commonTools.ts` (name and description generators, pp. ~861–999), `src/api/tools/repoHandlers/{DefaultRepoHandler,GenericRepoHandler,ThreejsRepoHandler,ReactRouterRepoHandler,handlers,RepoHandler}.ts`.
- Risk of dynamic string assembly: HIGH in form, low in substance. The names and descriptions of the three main tools are assembled at runtime from `owner`/`repo`, computed from the request host/URL, plus the name is truncated by `enforceToolNameLengthLimit` to 55 characters. The resulting text the client sees is not statically fixed in any single literal in full — it is reconstructed from template strings. The tool set is also runtime-dependent: connecting to `docs/`, `mrdoob/three.js` or `remix-run/react-router` yields a different set.
- `dist/server.js` and `dist/tools/index.js` — an outdated compiled artifact of the previous stdio version (there `mcp.tool(...)`, descriptions like `Fetch documentation from GitHub repository: ...` without "Always call this tool first"). I did not use it as a source of truth in the dossier: the current code is `src/`. I note the discrepancy as a signal that descriptions in the repo were strengthened over time.
- Reviewed ~12 (7 TS files read in full; grep across all 57 TS/TSX in `src/` + `app/` for `description:` / `new McpServer` / `instructions`; `src/api/tools/repoHandlers/generic/static-mapping.json` — library table, not tool descriptions; `dist/` directory inspected with grep).
- The code was not executed.
