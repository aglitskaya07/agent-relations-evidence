# UNIT: tavily-mcp | npm v0.2.21 (published 2026-07-10T20:14:27.492Z) | scope: npm-top,docker-catalog | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

A real stdio MCP server: `new Server({name: "tavily-mcp", version: "0.2.21"}, {capabilities: {tools: {}}})` + `StdioServerTransport` (build/index.js:35–42, 507–511). SDK `@modelcontextprotocol/sdk@1.26.0`. A proxy to api.tavily.com (search/extract/crawl/map/research).

## CHANNEL: instructions, npm (static)

(not found statically)

Only `name`/`version` and `capabilities: {tools: {}}` are passed to the `Server` constructor — there is no `instructions` field anywhere in the package. Grep for `instructions` finds only the tool parameter `instructions` in tavily_crawl/tavily_map (instructions for the crawler, not for the model).

## CHANNEL: tool descriptions, npm (static, coverage=full)

5 tools, registered statically in the ListTools handler (build/index.js:103–377). Descriptions verbatim:

1. **tavily_search** — "Search the web for current information on any topic. Use for news, facts, or data beyond your knowledge cutoff. Returns snippets and source URLs."
2. **tavily_extract** — "Extract content from URLs. Returns raw page content in markdown or text format."
3. **tavily_crawl** — "Crawl a website starting from a URL. Extracts content from pages with configurable depth and breadth."
4. **tavily_map** — "Map a website's structure. Returns a list of URLs found starting from the base URL."
5. **tavily_research** — "Perform comprehensive research on a given topic or question. Use this tool when you need to gather information from multiple sources to answer a question or complete a task. Returns a detailed response based on the research findings. Rate limit: 20 requests per minute."

Steering markers in the MCP descriptions: practically absent. The only guiding language: "Use for news, facts, or data beyond your knowledge cutoff" (tavily_search) and "Use this tool when you need to gather information from multiple sources" (tavily_research) — mild, without superlatives, without "instead of built-in", without precedence language.

### Parallel set of descriptions (CLI-only, NOT visible to the model)

The `listTools()` function (build/index.js:903–932) prints to the console, via the `--list-tools` flag, other, more marketing-style descriptions ("A sophisticated web crawler…", "Perfect for comprehensive site analysis…", "Ideal for site audits…"). This is stdout for a human, and does not enter the MCP protocol. The markers "Perfect for|Ideal for" appear only here.

## DYNAMIC CHANNEL (runtime, not static): keyless-envelope

In keyless mode (without TAVILY_API_KEY), API errors are formatted into tool-result text by the `formatKeylessEnvelope` function (build/index.js:803–829), including server-injected Tavily "next_actions": subscription ("Sign up for a Tavily API key: <url>"), agentic payment (x402) and **"Earn N bonus credits by POSTing answers to <endpoint>" + list of questions** — i.e. the API can inject calls to action into the model at runtime (refund|credit|reward marker). The content comes from the server, statically not fixed.

## NOTES

- The code is NOT minified — readable tsc output with comments.
- Risk of dynamic construction of descriptions: zero for tool descriptions (literals). The real dynamic channel is the keyless error envelope (see above): the text is fully controlled by the api.tavily.com response.
- There are 4 files in the package (package.json, README.md, LICENCE, build/index.js); package.json and build/index.js were examined in full (948 lines).
- Telemetry: X-Session-Id (UUID per session), optional X-Human-Id from env, X-Client-Source.
- DEFAULT_PARAMETERS env lets the operator silently override the model's search request parameters (build/index.js:534–539) — a configuration, not textual, channel.
