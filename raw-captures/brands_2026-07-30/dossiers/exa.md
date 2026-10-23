# UNIT: exa | Exa | github exa-labs/exa-mcp-server | тип автора: официальный | captured 2026-07-29 (static source)

Это MCP-сервер. `@modelcontextprotocol/sdk` + `McpServer` в `src/stdio.ts` (stdio-транспорт), плюс HTTP/Vercel-вход `api/mcp.ts` через `createMcpHandler` из `mcp-handler`. Регистрация инструментов — `src/mcp-handler.ts` → `initializeMcpServer()`, реализация каждого инструмента — `src/tools/*.ts` через `server.tool(name, description, schema, hints, handler)`.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `new McpServer({...})` в `src/stdio.ts:47-55` передаёт только `name: "exa-search-server"`, `title: "Exa"`, `version: "3.2.1"`, `websiteUrl`, `icons`. `createMcpHandler` в `api/mcp.ts:527-543` передаёт только `serverInfo` (те же поля). Поля `instructions` в объявлении сервера нет ни в одном из двух входов; вхождения слова `instructions` в репозитории относятся к параметру инструмента `deep_researcher_start` и типам в `src/types.ts`.

## CHANNEL: tool descriptions (coverage=full)

Всего в реестре `src/toolRegistry.ts` 12 идентификаторов инструментов. По умолчанию `enabled: true` только у `web_search_exa` и `web_fetch_exa`; остальные включаются через `ENABLED_TOOLS`/`TOOLS`. `crawling_exa` — это тот же `registerWebFetchTool` с переименованием, описание идентично `web_fetch_exa`.

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
(src/tools/webFetch.ts:35-40; имя по умолчанию, `toolName` перезаписываемо)
```
Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL.

Best for: Extracting full content from known URLs. Batch multiple URLs in one call.
Returns: Clean text content and metadata from the page(s).
```

### 4. crawling_exa
(src/mcp-handler.ts:101-104 — `registerWebFetchTool(server, config, 'crawling_exa')`, описание то же, что у `web_fetch_exa`)
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

## ДОПОЛНИТЕЛЬНЫЙ КАНАЛ: prompts + skills

`src/mcp-handler.ts:152-169` регистрирует prompt `web_search_help` («Get help with web search using Exa»), а при включённых agent-инструментах — prompt `agent_research_help` («Get help structuring a multi-step Exa Agent research run.»), тело которого подгружается из файла скилла (`src/utils/agentSkill.ts`, `skills/agent/SKILL.md`). Репозиторий также содержит `skills/search/SKILL.md` с набором reference-файлов и `.claude-plugin/plugin.json` — то есть часть управляющего текста доставляется не через MCP-канал instructions, а как Claude-плагин/скиллы и как prompt-контент.

## Метаданные реестра (не MCP-описания, но видимы в `listToolMetadata`)

`src/toolRegistry.ts` хранит для каждого инструмента отдельную человекочитаемую пару name/description (например `web_search_exa` → "Real-time web search using Exa AI"), которая отдаётся служебным листингом инструментов, а не в `tools/list`.
