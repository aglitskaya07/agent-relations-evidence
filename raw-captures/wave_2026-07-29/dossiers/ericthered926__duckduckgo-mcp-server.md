# UNIT: @ericthered926/duckduckgo-mcp-server | npm v0.6.0 (published 2025-12-18T06:08:25.603Z) | frames: npm-top | captured 2026-07-29 (static, tarball)

This is a confirmed MCP server: `build/index.js` imports `Server` from `@modelcontextprotocol/sdk/server/index.js`, starts `StdioServerTransport`, registers `ListToolsRequestSchema` / `CallToolRequestSchema` handlers. Two DuckDuckGo search tools (via the `duck-duck-scrape` library).

## CHANNEL: instructions, npm (static)
(not found statically)

Constructor: `new Server(CONFIG.server, { capabilities: { tools: {} } })` — the second argument contains only capabilities, there is no `instructions` field anywhere in the package (grep for `instructions` in build/ and package.json is empty, except README installation sections).

## CHANNEL: tool descriptions, npm (static, coverage=full)

A total of 2 tools. Descriptions are assembled from configuration as template strings (env variables with defaults), values are deterministic in the default environment. Below is the verbatim template + value with defaults.

### 1. duckduckgo_web_search
Template (index.js:131-132):
```
`Web search via DuckDuckGo. Returns max ${CONFIG.search.defaultResults} results with ${CONFIG.search.maxSnippetLength}-char snippets. ` +
`Use 'limit' param to override (1-${CONFIG.search.maxResults}). Supports region/time filters.`
```
At defaults (defaultResults=3, maxSnippetLength=150, maxResults=20):
> Web search via DuckDuckGo. Returns max 3 results with 150-char snippets. Use 'limit' param to override (1-20). Supports region/time filters.

Parameters (descriptions verbatim):
- query: "Search query (max 400 chars)" (template: `Search query (max ${CONFIG.search.maxQueryLength} chars)` )
- limit: "Override default result limit (1-20, default: 3)"
- count: "[DEPRECATED: use 'limit'] Number of results"
- safeSearch: "Content filtering level"
- region: "Region for localized results. Examples: 'us-en' (US), 'uk-en' (UK), 'de-de' (Germany), 'wt-wt' (worldwide, default)"
- time: "Time range filter for results"

### 2. duckduckgo_news_search
Template (index.js:176-177):
```
`News search via DuckDuckGo. Returns max ${CONFIG.search.defaultResults} articles with ${CONFIG.search.maxSnippetLength}-char excerpts. ` +
`Use 'limit' param to override (1-${CONFIG.search.maxResults}).`
```
At defaults:
> News search via DuckDuckGo. Returns max 3 articles with 150-char excerpts. Use 'limit' param to override (1-20).

Parameters (descriptions verbatim):
- query: "News search query (max 400 chars)"
- limit: "Override default result limit (1-20, default: 3)"
- count: "[DEPRECATED: use 'limit'] Number of results"
- safeSearch: "Content filtering level"
- time: "Time range for news articles"

## STEERING-MARKERS
Marker scan for research regexes (instead of built-in, most powerful, always default, primary, PRECEDENCE, LAST resort, MUST use, whenever the user, Do NOT answer from memory, etc.) in the tool descriptions: no matches. The descriptions are dry, functional, with no attempt to seize priority from built-in search.

## NOTES
- The code is NOT minified — readable tsc output with comments, full review of all 512 lines.
- Tool descriptions are assembled dynamically from template literals with env config (DDG_MAX_RESULTS 1-20, DDG_MAX_SNIPPET_LENGTH 50-500), but the substitutions are only numbers; the text part is static, and there is no risk of hidden dynamic assembly of steering strings.
- Files examined: package.json, build/index.js (fully), README.md (bytes), listing of all 7 package files; build/index.d.ts is an empty type export, .map is a sourcemap.
- Version mismatch: package.json v0.6.0, but CONFIG.server.version = "0.3.0" (the server presents itself to the client as 0.3.0).
