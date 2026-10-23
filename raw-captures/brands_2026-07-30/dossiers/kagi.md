# UNIT: kagi | Kagi Search | github kagisearch/kagimcp | тип автора: официальный | captured 2026-07-29 (static source)

Подтверждено: это MCP-сервер. `src/kagimcp/server.py` создаёт `mcp = FastMCP("kagimcp", auth=_KagiKeyPassthroughVerifier())`, регистрирует инструменты через `@mcp.tool()`, запускается в stdio или streamable-http (`mcp.run(...)`).

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `FastMCP("kagimcp", auth=...)` вызывается без параметра `instructions`; в репозитории нет ни одного упоминания `instructions` в коде (единственное совпадение — слово в прозе README про установку).

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 2.

### 1. `kagi_search_fetch`

Описание (docstring):

> Fetch web results for a query using the Kagi Search API. Use for general search and when the user explicitly tells you to 'fetch' results/information. Results are numbered so that a user may refer to a result by a specific number.

Описания параметров (дословно):

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

Описание (docstring):

> Extract the content of a web page as markdown using the Kagi Extract API. Use this to read the full content of a page when needed.

Описания параметров (дословно):

- `url`: "The HTTPS URL of the page to extract content from."

## Прочие статические наблюдения

- Оператор развёртывания может скрыть часть параметров `kagi_search_fetch` от модели через env `KAGI_HIDDEN_PARAMS` (`ToolTransform` / `ArgTransformConfig(hide=True)`) — это меняет видимую модели схему, но не текст описаний инструментов.
- Имена и описания инструментов заданы литералами в исходнике; динамической сборки строк описаний нет.
