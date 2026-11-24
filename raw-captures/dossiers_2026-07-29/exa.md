# UNIT: exa | exa-search-server v3.2.1 | hosted https://mcp.exa.ai/mcp (keyless) + npm exa-mcp-server | captured 2026-07-29

## CHANNEL: instructions, hosted

(absent — the server does not pass an instructions block)

## CHANNEL: tool descriptions, hosted (2 tools)

### tool: web_search_exa

Search the web for any topic and get clean, ready-to-use content.

      Best for: Finding current information, news, facts, people, companies, or answering questions about any topic.
      Returns: Clean text content from top search results.

      Query tips:
      describe the ideal page, not keywords. "blog post comparing React and Vue performance" not "React vs Vue".
      Use category:people / category:company to search through Linkedin profiles / companies respectively.
      If highlights are insufficient, follow up with web_fetch_exa on the best URLs.

### tool: web_fetch_exa

Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL.

Best for: Extracting full content from known URLs. Batch multiple URLs in one call.
Returns: Clean text content and metadata from the page(s).


## CHANNEL: instructions, npm (static)
(not found statically)

The server is created as `new McpServer({name:"exa-search-server",title:"Exa",version:"3.2.1"})` — without an `instructions` field in both bundles (`smithery/stdio/index.cjs`, `smithery/shttp/index.cjs`). All occurrences of `instructions` in the code are either internal MCP SDK contents (`this._instructions`), or the `instructions` parameter of the `deep_researcher_start` tool, or the MIME table.

## CHANNEL: tool descriptions, npm (static, coverage=full)

10 tools in both bundles (stdio and shttp are identical in composition). Descriptions verbatim:

### web_search_exa
```
Search the web for any topic and get clean, ready-to-use content.

      Best for: Finding current information, news, facts, people, companies, or answering questions about any topic.
      Returns: Clean text content from top search results.

      Query tips: 
      describe the ideal page, not keywords. "blog post comparing React and Vue performance" not "React vs Vue".
      Use category:people / category:company to search through Linkedin profiles / companies respectively.
      If highlights are insufficient, follow up with web_fetch_exa on the best URLs.
```

### web_fetch_exa
```
Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL.

Best for: Extracting full content from known URLs. Batch multiple URLs in one call.
Returns: Clean text content and metadata from the page(s).
```

### web_search_advanced_exa
```
Advanced web search with full control over filters, domains, dates, and content options.

Best for: When you need specific filters like date ranges, domain restrictions, or category filters.
Not recommended for: Simple searches - use web_search_exa instead.
Returns: Search results with optional highlights, summaries, and subpage content.
```

### get_code_context_exa
```
Find code examples, documentation, and programming solutions. 

Best for: Any programming question - API usage, library examples, code snippets, debugging help.
Returns: Relevant code and documentation.

Query tips: describe what you're looking for specifically. "Python requests library POST with JSON body" not "python http".
If highlights are insufficient, follow up with web_fetch_exa on the best URLs.
```

### company_research_exa
```
[Deprecated: Use web_search_advanced_exa instead] Research any company to get business information, news, and insights.

Best for: Learning about a company's products, services, recent news, or industry position.
Returns: Company information from trusted business sources.
```

### people_search_exa
```
[Deprecated: Use web_search_advanced_exa instead] Find people and their professional profiles.

Best for: Finding professionals, executives, or anyone with a public profile.
Returns: Profile information and links.
```

### linkedin_search_exa
```
⚠️ DEPRECATED: This tool is deprecated. Please use 'people_search_exa' instead. This tool will be removed in a future version. For now, it searches for people on LinkedIn using Exa AI - finds professional profiles and people.
```

### deep_researcher_start
```
[Deprecated] Start an AI research agent that searches, reads, and writes a detailed report. Takes 15 seconds to 2 minutes.

Best for: Complex research questions needing deep analysis and synthesis.
Returns: Research ID - use deep_researcher_check to get results.
Important: Call deep_researcher_check with the returned research ID to get the report.
```

### deep_researcher_check
```
[Deprecated] Check status and get results from a deep research task.

Best for: Getting the research report after calling deep_researcher_start.
Returns: Research report when complete, or status update if still running.
Important: Keep calling with the same research ID until status is 'completed'.
```

### deep_search_exa
```
[Deprecated: Use web_search_advanced_exa instead] Deep search with automatic query expansion for thorough research. Generates multiple search variations to find results from multiple angles, then synthesizes a short answer with citations.

Best for: Complex questions needing information from multiple angles.
Returns: A synthesized answer with citations, plus individual search results with highlights. When structuredOutput is enabled, returns structured JSON instead of markdown.
Note: Requires an Exa API key. 'deep' mode takes 4-12s, 'deep-reasoning' takes 12-50s.
```

### Extraction notes (static, npm 3.2.1)
- Code is minified (esbuild bundles ~1.0 MB stdio / ~2.4 MB shttp), there are no TS sources in the package — only `smithery/stdio/index.cjs` and `smithery/shttp/index.cjs`.
- Descriptions are static literals (template literals without interpolation), so the risk of dynamic construction of description strings is low.
- The names of two tools are overridable via config: registration of the form `.tool(r||"web_search_exa", ...)` and `.tool(r||"web_fetch_exa", ...)` — the name can be substituted at the configuration stage, while the description remains the same.
- Steering markers in descriptions: guiding chains between own tools ("use web_search_exa instead", "follow up with web_fetch_exa", "Use after web_search_exa") and deprecation redirects; no markers of displacing another tool ("instead of built-in", "takes precedence", "always default" etc.) were found.
