# UNIT: @ericthered926/duckduckgo-mcp-server | npm v0.6.0 (published 2025-12-18T06:08:25.603Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

Это подтверждённый MCP-сервер: `build/index.js` импортирует `Server` из `@modelcontextprotocol/sdk/server/index.js`, поднимает `StdioServerTransport`, регистрирует `ListToolsRequestSchema` / `CallToolRequestSchema` хендлеры. Два инструмента поиска DuckDuckGo (через библиотеку `duck-duck-scrape`).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор: `new Server(CONFIG.server, { capabilities: { tools: {} } })` — второй аргумент содержит только capabilities, поля `instructions` нет нигде в пакете (grep по `instructions` в build/ и package.json пуст, кроме README-разделов установки).

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего инструментов: 2. Описания собираются шаблонными строками из конфигурации (env-переменные с дефолтами), значения детерминированы при дефолтном окружении. Ниже — дословный шаблон + значение при дефолтах.

### 1. duckduckgo_web_search
Шаблон (index.js:131-132):
```
`Web search via DuckDuckGo. Returns max ${CONFIG.search.defaultResults} results with ${CONFIG.search.maxSnippetLength}-char snippets. ` +
`Use 'limit' param to override (1-${CONFIG.search.maxResults}). Supports region/time filters.`
```
При дефолтах (defaultResults=3, maxSnippetLength=150, maxResults=20):
> Web search via DuckDuckGo. Returns max 3 results with 150-char snippets. Use 'limit' param to override (1-20). Supports region/time filters.

Параметры (описания дословно):
- query: "Search query (max 400 chars)" (шаблон: `Search query (max ${CONFIG.search.maxQueryLength} chars)`)
- limit: "Override default result limit (1-20, default: 3)"
- count: "[DEPRECATED: use 'limit'] Number of results"
- safeSearch: "Content filtering level"
- region: "Region for localized results. Examples: 'us-en' (US), 'uk-en' (UK), 'de-de' (Germany), 'wt-wt' (worldwide, default)"
- time: "Time range filter for results"

### 2. duckduckgo_news_search
Шаблон (index.js:176-177):
```
`News search via DuckDuckGo. Returns max ${CONFIG.search.defaultResults} articles with ${CONFIG.search.maxSnippetLength}-char excerpts. ` +
`Use 'limit' param to override (1-${CONFIG.search.maxResults}).`
```
При дефолтах:
> News search via DuckDuckGo. Returns max 3 articles with 150-char excerpts. Use 'limit' param to override (1-20).

Параметры (описания дословно):
- query: "News search query (max 400 chars)"
- limit: "Override default result limit (1-20, default: 3)"
- count: "[DEPRECATED: use 'limit'] Number of results"
- safeSearch: "Content filtering level"
- time: "Time range for news articles"

## STEERING-МАРКЕРЫ
Маркер-скан по регексам исследования (instead of built-in, most powerful, always default, primary, PRECEDENCE, LAST resort, MUST use, whenever the user, Do NOT answer from memory и т.д.) по описаниям инструментов: совпадений НЕТ. Описания сухие, функциональные, без попыток перехватить приоритет у встроенного поиска.

## NOTES
- Код НЕ минифицирован — читаемый tsc-выход с комментариями, полный просмотр всех 512 строк.
- Описания инструментов собираются динамически из template literals с env-конфигом (DDG_MAX_RESULTS 1-20, DDG_MAX_SNIPPET_LENGTH 50-500), но подстановки — только числа; текстовая часть статична, риск скрытой динамической сборки steering-строк отсутствует.
- Файлов просмотрено: package.json, build/index.js (полностью), README.md (bytes), listing всех 7 файлов пакета; build/index.d.ts пустой типовой экспорт, .map — sourcemap.
- Несостыковка версий: package.json v0.6.0, но CONFIG.server.version = "0.3.0" (сервер представляется клиенту как 0.3.0).
