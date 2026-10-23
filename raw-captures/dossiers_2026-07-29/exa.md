# UNIT: exa | exa-search-server v3.2.1 | hosted https://mcp.exa.ai/mcp (keyless) + npm exa-mcp-server | captured 2026-07-29

## CHANNEL: instructions, hosted

(отсутствует — сервер не передаёт блок instructions)

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
(не обнаружены статически)

Сервер создаётся как `new McpServer({name:"exa-search-server",title:"Exa",version:"3.2.1"})` — без поля `instructions` в обоих бандлах (`smithery/stdio/index.cjs`, `smithery/shttp/index.cjs`). Все вхождения `instructions` в коде — это либо внутренности MCP SDK (`this._instructions`), либо параметр `instructions` инструмента `deep_researcher_start`, либо MIME-таблица.

## CHANNEL: tool descriptions, npm (static, coverage=full)

10 инструментов в обоих бандлах (stdio и shttp идентичны по составу). Описания дословно:

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

### Заметки экстракции (static, npm 3.2.1)
- Код минифицирован (esbuild-бандлы ~1.0 МБ stdio / ~2.4 МБ shttp), исходников TS в пакете нет — только `smithery/stdio/index.cjs` и `smithery/shttp/index.cjs`.
- Описания — статические литералы (template literals без интерполяции), риск динамической сборки строк описаний низкий.
- Имена двух инструментов переопределяемы конфигом: регистрация вида `.tool(r||"web_search_exa", ...)` и `.tool(r||"web_fetch_exa", ...)` — имя может быть подменено на этапе конфигурации, описание при этом остаётся тем же.
- Steering-маркеры в описаниях: направляющие цепочки между собственными инструментами («use web_search_exa instead», «follow up with web_fetch_exa», «Use after web_search_exa») и deprecation-редиректы; маркеров вытеснения чужих инструментов («instead of built-in», «takes precedence», «always default» и т.п.) не обнаружено.
