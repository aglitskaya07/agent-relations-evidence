# UNIT: tavily | Tavily | github tavily-ai/tavily-mcp | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CHECK
Это MCP-сервер. `src/index.ts:85-95`: `new Server({ name: "tavily-mcp", version: "0.2.21" }, { capabilities: { tools: {} } })` из `@modelcontextprotocol/sdk` 1.26.0, обработчики `ListToolsRequestSchema` (строка 165) и `CallToolRequestSchema` (строка 445), транспорт stdio. Код целиком в одном файле `src/index.ts` (1070 строк), других исходников в репозитории нет.

## CHANNEL: instructions
(не обнаружены статически)

Второй аргумент конструктора `Server` содержит только `capabilities: { tools: {} }` — поля `instructions` нет. Кастомного обработчика `initialize` в репозитории нет. Токен `instructions` в файле встречается только как имя параметра инструментов `tavily_crawl` / `tavily_map` (natural language instructions для краулера) и при пробросе `args.instructions` в API-запрос.

## CHANNEL: tool descriptions (coverage=full)

Источник: `src/index.ts`, массив `const tools: Tool[]` внутри `setupToolHandlers()` (строки ~166–443). 5 инструментов.

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

## SECONDARY: CLI `--list-tools` descriptions (не отдаются по MCP)

Функция `listTools()` (строки ~1014–1044) печатает в stdout другой, более развёрнутый набор описаний. Он НЕ участвует в ответе `tools/list` и до модели по протоколу не доходит; приведён для полноты.

- **tavily_search** — A real-time web search tool powered by Tavily's AI engine. Features include customizable search depth (basic/advanced/fast/ultra-fast), domain filtering, time-based filtering, and support for both general and news-specific searches. Returns comprehensive results with titles, URLs, content snippets, and optional image results.
- **tavily_extract** — Extracts and processes content from specified URLs with advanced parsing capabilities. Supports both basic and advanced extraction modes, with the latter providing enhanced data retrieval including tables and embedded content. Ideal for data collection, content analysis, and research tasks.
- **tavily_crawl** — A sophisticated web crawler that systematically explores websites starting from a base URL. Features include configurable depth and breadth limits, domain filtering, path pattern matching, and category-based filtering. Perfect for comprehensive site analysis, content discovery, and structured data collection.
- **tavily_map** — Creates detailed site maps by analyzing website structure and navigation paths. Offers configurable exploration depth, domain restrictions, and category filtering. Ideal for site audits, content organization analysis, and understanding website architecture and navigation patterns.
- **tavily_research** — Performs comprehensive research on any topic or question by gathering information from multiple sources. Supports different research depths ('mini' for narrow tasks, 'pro' for broad research, 'auto' for automatic selection). Ideal for in-depth analysis, report generation, and answering complex questions requiring synthesis of multiple sources.

## PARAMETER-LEVEL NOTE
Описания параметров также статические строковые литералы. Отдельно отмечу `tavily_search.include_domains`: «A list of domains to specifically include in the search results, if the user asks to search on specific sites set this to the domain of the site» — поведенческая инструкция внутри описания параметра, а не только описание типа.

## DYNAMIC-ASSEMBLY RISK
Низкий. Все `name`/`description` — литералы в одном массиве, без шаблонных подстановок, конкатенации и условных ветвлений. Единственная динамика — keyless-режим: при отсутствии `TAVILY_API_KEY` часть инструментов возвращает в рантайме сообщение о необходимости ключа, но список инструментов и их описания при этом не меняются.
