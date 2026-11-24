# UNIT: tavily | Tavily | github tavily-ai/tavily-mcp | author type: official | captured 2026-07-29 (static source)

## SERVER CHECK
This is an MCP server. `src/index.ts:85-95`: `new Server({ name: "tavily-mcp", version: "0.2.21" }, { capabilities: { tools: {} } })` from `@modelcontextprotocol/sdk` 1.26.0, handlers `ListToolsRequestSchema` (line 165) and `CallToolRequestSchema` (line 445), stdio transport. The entire code is in one file `src/index.ts` (1070 lines), there are no other source files in the repository.

## CHANNEL: instructions
(not found statically)

The second argument to the `Server` constructor contains only `capabilities: { tools: {} }` — there is no `instructions` field. There is no custom `initialize` handler in the repository. The token `instructions` appears in the file only as the name of the tool parameter for `tavily_crawl` / `tavily_map` (natural language instructions for the crawler) and when passing `args.instructions` into the API request.

## CHANNEL: tool descriptions (coverage=full)

Source: `src/index.ts`, the `const tools: Tool[]` array inside `setupToolHandlers()` (lines ~166–443). 5 tools.

### tavily_search
Search the web for current information on any topic. Use for news, facts, or data beyond your knowledge cutoff. Returns snippets and source URLs.

### tavily_extract
Extract content from URLs. Returns raw page content in markdown or text format.

### tavily_crawl
Crawl a website starting from a URL. Extracts content from pages with configurable depth and breadth.

### tavily_map
Map a website's structure. Returns a list of URLs found starting from the base URL.

### tavily_research
Perform comprehensive research on a given topic or question. Use this tool when you need to gather information from multiple sources to answer a question or complete a task. Returns a detailed response based on the research findings. Rate limit: 20 requests per minute.

## SECONDARY: CLI `--list-tools` descriptions (not exposed via MCP)

The `listTools()` function (lines ~1014–1044) prints to stdout a different, more expanded set of descriptions. It does NOT participate in the `tools/list` response and does not reach the model via the protocol; included for completeness.

- **tavily_search** — A real-time web search tool powered by Tavily's AI engine. Features include customizable search depth (basic/advanced/fast/ultra-fast), domain filtering, time-based filtering, and support for both general and news-specific searches. Returns comprehensive results with titles, URLs, content snippets, and optional image results.
- **tavily_extract** — Extracts and processes content from specified URLs with advanced parsing capabilities. Supports both basic and advanced extraction modes, with the latter providing enhanced data retrieval including tables and embedded content. Ideal for data collection, content analysis, and research tasks.
- **tavily_crawl** — A sophisticated web crawler that systematically explores websites starting from a base URL. Features include configurable depth and breadth limits, domain filtering, path pattern matching, and category-based filtering. Perfect for comprehensive site analysis, content discovery, and structured data collection.
- **tavily_map** — Creates detailed site maps by analyzing website structure and navigation paths. Offers configurable exploration depth, domain restrictions, and category filtering. Ideal for site audits, content organization analysis, and understanding website architecture and navigation patterns.
- **tavily_research** — Performs comprehensive research on any topic or question by gathering information from multiple sources. Supports different research depths ('mini' for narrow tasks, 'pro' for broad research, 'auto' for automatic selection). Ideal for in-depth analysis, report generation, and answering complex questions requiring synthesis of multiple sources.

## PARAMETER-LEVEL NOTE
The parameter descriptions are also static string literals. Separately, I note `tavily_search.include_domains`: “A list of domains to specifically include in the search results, if the user asks to search on specific sites set this to the domain of the site” — a behavioral instruction inside the parameter description, not only a type description.

## DYNAMIC-ASSEMBLY RISK
Low. All `name`/`description` values are literals in one array, with no template substitutions, concatenation, or conditional branching. The only dynamic behavior is keyless mode: when `TAVILY_API_KEY` is absent, some tools return a runtime message about needing a key, but the tool list and their descriptions do not change.
