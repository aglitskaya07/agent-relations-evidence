# UNIT: exa | Exa | github exa-labs/exa-mcp-server | author type: official | captured 2026-07-29 (static source)

This is an MCP server. `@modelcontextprotocol/sdk` + `McpServer` in `src/stdio.ts` (stdio transport), plus HTTP/Vercel entry `api/mcp.ts` via `createMcpHandler` from `mcp-handler`. Tool registration — `src/mcp-handler.ts` → `initializeMcpServer()`, implementation of each tool — `src/tools/*.ts` via `server.tool(name, description, schema, hints, handler)`.

## CHANNEL: instructions
(not found statically)

The constructor `new McpServer({...})` in `src/stdio.ts:47-55` passes only `name: "exa-search-server"`, `title: "Exa"`, `version: "3.2.1"`, `websiteUrl`, `icons`. `createMcpHandler` in `api/mcp.ts:527-543` passes only `serverInfo` (the same fields). The `instructions` field is not in the server declaration in either of the two entry points; occurrences of the word `instructions` in the repository relate to the `deep_researcher_start` tool parameter and types in `src/types.ts`.

## CHANNEL: tool descriptions (coverage=full)

There are 12 tool identifiers in the `src/toolRegistry.ts` registry in total. By default, only `web_search_exa` and `web_fetch_exa` have `enabled: true`; the others are enabled through `ENABLED_TOOLS`/`TOOLS`. `crawling_exa` is the same `registerWebFetchTool` with a rename, and its description is identical to `web_fetch_exa`.

### 1. web_search_exa
(src/tools/webSearch.ts:20-31)
```
Search the web for any topic and get clean, ready-to-use content.

      Best for: Finding current information, news, facts, people, companies, or answering questions about any topic.
      Returns: Clean text content from top search results.

      Query tips:
      describe the ideal page, not keywords. "blog post comparing React and Vue performance" not "React vs Vue".
      Use category:people / category:company to search through Linkedin profiles / companies respectively.
      If highlights are insufficient, follow up with web_fetch_exa on the best URLs.
```

### 2. web_search_advanced_exa
(src/tools/webSearchAdvanced.ts:12-18)
```
Advanced web search with full control over filters, domains, dates, and content options.

Best for: When you need specific filters like date ranges, domain restrictions, or category filters.
Not recommended for: Simple searches - use web_search_exa instead.
Returns: Search results with optional highlights, summaries, and subpage content.
```

### 3. web_fetch_exa
(src/tools/webFetch.ts:35-40; default name, `toolName` is overridable)
```
Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL.

Best for: Extracting full content from known URLs. Batch multiple URLs in one call.
Returns: Clean text content and metadata from the page(s).
```

### 4. crawling_exa
(src/mcp-handler.ts:101-104 — `registerWebFetchTool(server, config, 'crawling_exa')`, the description is the same as `web_fetch_exa`)
```
Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL.

Best for: Extracting full content from known URLs. Batch multiple URLs in one call.
Returns: Clean text content and metadata from the page(s).
```

### 5. get_code_context_exa
(src/tools/exaCode.ts:12-20)
```
Find code examples, documentation, and programming solutions. 

Best for: Any programming question - API usage, library examples, code snippets, debugging help.
Returns: Relevant code and documentation.

Query tips: describe what you're looking for specifically. "Python requests library POST with JSON body" not "python http".
If highlights are insufficient, follow up with web_fetch_exa on the best URLs.
```

### 6. company_research_exa
(src/tools/companyResearch.ts:12-17)
```
[Deprecated: Use web_search_advanced_exa instead] Research any company to get business information, news, and insights.

Best for: Learning about a company's products, services, recent news, or industry position.
Returns: Company information from trusted business sources.
```

### 7. people_search_exa
(src/tools/peopleSearch.ts:12-17)
```
[Deprecated: Use web_search_advanced_exa instead] Find people and their professional profiles.

Best for: Finding professionals, executives, or anyone with a public profile.
Returns: Profile information and links.
```

### 8. linkedin_search_exa
(src/tools/linkedInSearch.ts:12-14)
```
⚠️ DEPRECATED: This tool is deprecated. Please use 'people_search_exa' instead. This tool will be removed in a future version. For now, it searches for people on LinkedIn using Exa AI - finds professional profiles and people.
```

### 9. deep_search_exa
(src/tools/deepSearch.ts:12-18)
```
[Deprecated: Use web_search_advanced_exa instead] Deep search with automatic query expansion for thorough research. Generates multiple search variations to find results from multiple angles, then synthesizes a short answer with citations.

Best for: Complex questions needing information from multiple angles.
Returns: A synthesized answer with citations, plus individual search results with highlights. When structuredOutput is enabled, returns structured JSON instead of markdown.
Note: Requires an Exa API key. 'deep' mode takes 4-12s, 'deep-reasoning' takes 12-50s.
```

### 10. deep_researcher_start
(src/tools/deepResearchStart.ts:11-17)
```
[Deprecated] Start an AI research agent that searches, reads, and writes a detailed report. Takes 15 seconds to 2 minutes.

Best for: Complex research questions needing deep analysis and synthesis.
Returns: Research ID - use deep_researcher_check to get results.
Important: Call deep_researcher_check with the returned research ID to get the report.
```

### 11. deep_researcher_check
(src/tools/deepResearchCheck.ts:16-22)
```
[Deprecated] Check status and get results from a deep research task.

Best for: Getting the research report after calling deep_researcher_start.
Returns: Research report when complete, or status update if still running.
Important: Keep calling with the same research ID until status is 'completed'.
```

### 12. agent_run
(src/tools/agentRun.ts:539-541)
```
Run an Exa Agent with live progress. New runs always stream. If a run outlives one call window, the tool returns its ID; call agent_run again with runId to keep waiting. Effort defaults to low.
```

## ADDITIONAL CHANNEL: prompts + skills

`src/mcp-handler.ts:152-169` registers the prompt `web_search_help` ("Get help with web search using Exa"), and when agent tools are enabled — the prompt `agent_research_help` ("Get help structuring a multi-step Exa Agent research run."), whose body is loaded from the skill file (`src/utils/agentSkill.ts`, `skills/agent/SKILL.md`). The repository also contains `skills/search/SKILL.md` with a set of reference files and `.claude-plugin/plugin.json` — that is, part of the control text is delivered not through the MCP `instructions` channel, but as a Claude plugin/skills and as prompt content.

## Registry metadata (not MCP descriptions, but visible in `listToolMetadata`)

`src/toolRegistry.ts` stores for each tool a separate human-readable name/description pair (for example `web_search_exa` → "Real-time web search using Exa AI"), which is returned by the service tool listing, not in `tools/list`.
