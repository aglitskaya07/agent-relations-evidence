# UNIT: kagi | Kagi Search | github kagisearch/kagimcp | author type: official | captured 2026-07-29 (static source)

Confirmed: this is an MCP server. `src/kagimcp/server.py` creates `mcp = FastMCP("kagimcp", auth=_KagiKeyPassthroughVerifier())`, registers tools via `@mcp.tool()`, runs in stdio or streamable-http (`mcp.run(...)`).

## CHANNEL: instructions
(not found statically)

The constructor `FastMCP("kagimcp", auth=...)` is called without the `instructions` parameter; there is not a single mention of `instructions` in the repository code (the only match is the word in README prose about installation).

## CHANNEL: tool descriptions (coverage=full)

A total of 2 tools.

### 1. `kagi_search_fetch`

Description (docstring):

> Fetch web results for a query using the Kagi Search API. Use for general search and when the user explicitly tells you to 'fetch' results/information. Results are numbered so that a user may refer to a result by a specific number.

Parameter descriptions (verbatim):

- `query`: "A concise, keyword-focused search query. Include essential context for standalone use."
- `workflow`: "Type of results to return. Use 'news' for current events and recent reporting, 'videos' for video content (e.g. tutorials, talks), 'podcasts' for audio shows, 'images' for image results, or the default 'search' for general web results. Note that 'search' may return a mix of categories (web, news, videos, images) in one response, like a typical SERP; the other workflows return only their single category."
- `extract_count`: "Number of top results to fetch full page content for, inline as markdown."
- `limit`: "Maximum number of results per category. In the mixed 'search' workflow this caps each category independently, so the total can exceed this number; in single-category workflows it caps total results."
- `include_domains`: "Restrict results to these domains (e.g., ['docs.python.org', 'github.com']). Overrides any 'site:' operators in the query."
- `exclude_domains`: "Exclude results from these domains (e.g., ['pinterest.com', 'quora.com']). Overrides any 'site:' operators in the query."
- `time_relative`: "Restrict to results published/updated within the last day, week, or month, evaluated server-side. Mutually exclusive with 'after'/'before'."
- `after`: "Only include results published/updated on or after this date (ISO format, e.g., '2024-01-15')."
- `before`: "Only include results published/updated on or before this date (ISO format, e.g., '2024-12-31')."
- `file_type`: "Restrict to results with this file type (e.g., 'pdf', 'docx', 'xlsx'). Specify the extension without a leading dot."
- `lens_id`: "Apply a Kagi lens to narrow the search to a curated set of sources. Built-in lens IDs: '2' (Academic — education/.edu domains), '1' (Forums — discussion forums across the web), '15' (Programming — official programming language sites and forums), '29' (News 360 — multi-perspective coverage of global news), '120' (Recipes — high-quality recipe sites, English), '107' (Small Web — noncommercial domains and topics). You may also pass a custom lens ID or full URL from https://kagi.com/settings/lenses (only shareable lenses work). Mutually exclusive with 'include_domains', 'exclude_domains', 'time_relative', and 'file_type'; use those args or 'lens_id', not both."

### 2. `kagi_extract`

Description (docstring):

> Extract the content of a web page as markdown using the Kagi Extract API. Use this to read the full content of a page when needed.

Parameter descriptions (verbatim):

- `url`: "The HTTPS URL of the page to extract content from."

## Other static observations

- The deployment operator can hide part of the `kagi_search_fetch` parameters from the model via env `KAGI_HIDDEN_PARAMS` (`ToolTransform` / `ArgTransformConfig(hide=True)`) — this changes the schema visible to the model, but not the text of tool descriptions.
- Tool names and descriptions are given as literals in the source; there is no dynamic assembly of description strings.
