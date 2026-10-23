# UNIT: tavily-mcp | npm v0.2.21 (published 2026-07-10T20:14:27.492Z) | рамки: npm-top,docker-catalog | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Настоящий stdio MCP-сервер: `new Server({name: "tavily-mcp", version: "0.2.21"}, {capabilities: {tools: {}}})` + `StdioServerTransport` (build/index.js:35–42, 507–511). SDK `@modelcontextprotocol/sdk@1.26.0`. Прокси к api.tavily.com (search/extract/crawl/map/research).

## CHANNEL: instructions, npm (static)

(не обнаружены статически)

Конструктору `Server` передаются только `name`/`version` и `capabilities: {tools: {}}` — поля `instructions` нет нигде в пакете. Grep по `instructions` находит только tool-параметр `instructions` у tavily_crawl/tavily_map (инструкции для краулера, не для модели).

## CHANNEL: tool descriptions, npm (static, coverage=full)

5 инструментов, зарегистрированы статически в ListTools-хендлере (build/index.js:103–377). Описания дословно:

1. **tavily_search** — "Search the web for current information on any topic. Use for news, facts, or data beyond your knowledge cutoff. Returns snippets and source URLs."
2. **tavily_extract** — "Extract content from URLs. Returns raw page content in markdown or text format."
3. **tavily_crawl** — "Crawl a website starting from a URL. Extracts content from pages with configurable depth and breadth."
4. **tavily_map** — "Map a website's structure. Returns a list of URLs found starting from the base URL."
5. **tavily_research** — "Perform comprehensive research on a given topic or question. Use this tool when you need to gather information from multiple sources to answer a question or complete a task. Returns a detailed response based on the research findings. Rate limit: 20 requests per minute."

Steering-маркеры в MCP-описаниях: практически отсутствуют. Единственное направляющее: "Use for news, facts, or data beyond your knowledge cutoff" (tavily_search) и "Use this tool when you need to gather information from multiple sources" (tavily_research) — мягкие, без превосходных степеней, без "instead of built-in", без precedence-языка.

### Параллельный набор описаний (CLI-only, НЕ виден модели)

Функция `listTools()` (build/index.js:903–932) печатает в консоль по флагу `--list-tools` другие, более маркетинговые описания ("A sophisticated web crawler…", "Perfect for comprehensive site analysis…", "Ideal for site audits…"). Это stdout для человека, в MCP-протокол не попадает. Маркеры "Perfect for|Ideal for" присутствуют только здесь.

## DYNAMIC CHANNEL (runtime, не static): keyless-envelope

В keyless-режиме (без TAVILY_API_KEY) ошибки API форматируются в текст tool-результата функцией `formatKeylessEnvelope` (build/index.js:803–829), включая инъецируемые сервером Tavily "next_actions": подписку ("Sign up for a Tavily API key: <url>"), agentic payment (x402) и **"Earn N bonus credits by POSTing answers to <endpoint>" + список вопросов** — т.е. API может в рантайме подставлять модели призывы к действию (маркер refund|credit|reward). Содержимое приходит с сервера, статически не фиксируется.

## NOTES

- Код НЕ минифицирован — читаемый tsc-выхлоп с комментариями.
- Риск динамической сборки строк описаний: нулевой для tool descriptions (литералы). Реальный динамический канал — keyless error envelope (см. выше): текст полностью управляется ответом api.tavily.com.
- Файлов в пакете 4 (package.json, README.md, LICENCE, build/index.js); просмотрены package.json и build/index.js целиком (948 строк).
- Телеметрия: X-Session-Id (UUID на сессию), опц. X-Human-Id из env, X-Client-Source.
- DEFAULT_PARAMETERS env позволяет оператору молча переопределять параметры search-запросов модели (build/index.js:534–539) — конфигурационный, не текстовый канал.
