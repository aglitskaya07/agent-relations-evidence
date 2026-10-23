# UNIT: oxylabs | Oxylabs | github oxylabs/oxylabs-mcp | тип автора: официальный | captured 2026-07-29 (static source)

Репозиторий — Python MCP-сервер на FastMCP. Точка входа `src/oxylabs_mcp/__init__.py`:
`mcp = OxylabsMCPServer("oxylabs_mcp")` (подкласс `FastMCP`), два подсервера монтируются:
`FastMCP("scraper")` (`src/oxylabs_mcp/tools/scraper.py`) и `FastMCP("ai_studio")` (`src/oxylabs_mcp/tools/ai_studio.py`).
Инструменты фильтруются в `_list_tools_mcp` в зависимости от наличия креденшелов (scraper-набор при отсутствии username/password, AI-набор при отсутствии AI Studio API key).

## CHANNEL: instructions
(не обнаружены статически)

Конструкторам `FastMCP` передаётся только имя, параметр `instructions=` отсутствует во всём репозитории; единственные вхождения слова "instructions" — в README (про OAuth) и в e2e-тесте агента. Метаданные `server.json` содержат поле `description`: "Fetch and process content from specified URLs & sources using the Oxylabs Web Scraper API." — это описание пакета в реестре, не серверные instructions.

## CHANNEL: tool descriptions (coverage=full)

Всего 10 инструментов. Описания = docstring функций (FastMCP берёт их как description). Дословно:

### 1. universal_scraper (tools/scraper.py:25)
```
Get a content of any webpage.

    Supports browser rendering, parsing of certain webpages
    and different output formats.
```

### 2. google_search_scraper (tools/scraper.py:56)
```
Scrape Google Search results.

    Supports content parsing, different user agent types, pagination,
    domain, geolocation, locale parameters and different output formats.
```

### 3. amazon_search_scraper (tools/scraper.py:111)
```
Scrape Amazon search results.

    Supports content parsing, different user agent types, pagination,
    domain, geolocation, locale parameters and different output formats.
    Supports Amazon specific parameters such as category id, merchant id, currency.
```

### 4. amazon_product_scraper (tools/scraper.py:171)
```
Scrape Amazon products.

    Supports content parsing, different user agent types, domain,
    geolocation, locale parameters and different output formats.
    Supports Amazon specific parameters such as currency and getting
    more accurate pricing data with auto select variant.
```

### 5. ai_crawler (tools/ai_studio.py:36)
```
Tool useful for crawling a website from starting url and returning data in a specified format.

    Schema is required only if output_format is json, csv or toon.
    'render_javascript' is used to render javascript heavy websites.
    'return_sources_limit' is used to limit the number of sources to return,
    for example if you expect results from single source, you can set it to 1.
```

### 6. ai_scraper (tools/ai_studio.py:108)
```
Scrape the contents of the web page and return the data in the specified format.

    Schema is required only if output_format is json or csv.
    'render_javascript' is used to render javascript heavy websites.
```

### 7. ai_browser_agent (tools/ai_studio.py:167)
```
Run the browser agent and return the data in the specified format.

    This tool is useful if you need navigate around the website and do some actions.
    It allows navigating to any url, clicking on links, filling forms, scrolling, etc.
    Finally it returns the data in the specified format.
    Schema is required only if output_format is json, csv or toon.
    'task_prompt' describes what browser agent should achieve
```

### 8. ai_search (tools/ai_studio.py:220)
```
Search the web based on a provided query.

    'return_content' is used to return markdown content for each search result. If 'return_content'
        is set to True, you don't need to use ai_scraper to get the content of the search results urls,
        because it is already included in the search results.
    if 'return_content' is set to True, prefer lower 'limit' to reduce payload size.
```

### 9. generate_schema (tools/ai_studio.py:265)
```
Generate a json schema in openapi format.
```

### 10. ai_map (tools/ai_studio.py:286)
```
Tool useful for mapping website's URLs.
```

## Дополнительно: описания параметров (Field description), содержащие поведенческие указания

- `ai_crawler.render_javascript`: "Whether to render the HTML of the page using javascript. Much slower, therefore use it only for websites that require javascript to render the page. Unless user asks to use it, first try to crawl the page without it. If results are unsatisfactory, try to use it."
- `ai_scraper.render_javascript`: "Whether to render the HTML of the page using javascript. Much slower, therefore use it only for websites that require javascript to render the page.Unless user asks to use it, first try to scrape the page without it. If results are unsatisfactory, try to use it."
- `ai_search.render_javascript`: "Whether to render the HTML of the page using javascript. Much slower, therefore use it only if user asks to use it.First try to search with setting it to False. "
- `ai_map.render_javascript`: аналогично ai_crawler.
- `ai_crawler/ai_scraper/ai_browser_agent.output_format`: описания форматов, в т.ч. "Toon(Token-Oriented Object Notation) returns data in Toon format, which is optimized for AI agents."

Все инструменты помечены `ToolAnnotations(readOnlyHint=True)`.
