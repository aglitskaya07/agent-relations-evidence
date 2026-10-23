# UNIT: bright-data | Bright Data | github brightdata/brightdata-mcp | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CONFIRMATION

Это MCP-сервер. `server.js` создаёт `new FastMCP({name: 'Bright Data', version: package_json.version})`, регистрирует инструменты через `server.addTool(...)` (обёртка `addTool`), промпты через `server.addPrompts(prompts)` и стартует stdio-транспорт: `server.start({transportType: 'stdio'})`. Язык — JavaScript (ESM, Node), зависимости `fastmcp` + `zod`.

Общее число регистрируемых инструментов: **74** = 10 объявленных напрямую в `server.js` + 50 сгенерированных в цикле `web_data_<id>` + 14 браузерных из `browser_tools.js`. Фактическая выдача при инициализации фильтруется env-переменными (`PRO_MODE`, `GROUPS`, `TOOLS`); по умолчанию отдаются только `pro_mode_tools = ['search_engine','scrape_as_markdown','search_engine_batch','scrape_batch','discover']`.

## CHANNEL: instructions
(не обнаружены статически)

Конструктору `FastMCP` передаются только `name` и `version`. Поля `instructions` нет ни в `server.js`, ни где-либо ещё в репозитории (grep по `instructions` без учёта регистра по всем .js/.json/.md, кроме package-lock, даёт 0 совпадений). Ответ `initialize` не формируется руками — его собирает библиотека `fastmcp`.

### Смежный канал (не instructions): MCP prompts

В `prompts.js` два промпта, регистрируемые через `server.addPrompts(prompts)`. Это не поле instructions и не описания инструментов, но канал директивного текста, содержащий директивы приоритизации инструментов. Фиксирую факт и дословные описания:

- `web_scraping_strategy` — description: `Decision tree for picking the right Bright Data tool. Invoke at the start of any scraping session to learn the correct tool selection order (dataset tools -> Web Unlocker -> Browser API).`
- `diagnose_scraping_approach` — description: `Run a two-step diagnostic to discover the correct Bright Data product for a new website. Tries Web Unlocker first, then Browser API, then reports which succeeded.`

Тела (`load()`) содержат в том числе: `Always follow this order -- do not skip ahead:`, `NEVER use the browser tools for sites scrape_as_markdown can handle.`, `NEVER use scrape_as_markdown when a web_data_* tool matches the URL pattern.`, `Do not proceed with data extraction until the diagnostic is complete.` — но они доставляются только по явному запросу prompt клиентом, не в initialize.

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

74 инструмента > 40, поэтому: полный маркерный скан всех описаний + 10 репрезентативных полных описаний.

### Результат маркерного скана

Прогон полного набора регексов по всем файлам с определениями инструментов (`server.js`, `browser_tools.js`, `prompts.js`, `tool_groups.js`, `search_dataset_schema.js`, `assets/Tools.md`) дал **ноль совпадений внутри строк `description` инструментов**.

Совпадения нашлись только вне канала описаний инструментов; привожу для полноты, с указанием, что это не описания:

1. `server.js`, строка ~1340 — текст ошибки времени выполнения, бросаемый из `tool_fn` при исчерпании бесплатного лимита (не description, попадает в модель только как результат сбойного вызова). Дословно: `The user has reached the 5,000 request monthly` `limit for Bright Data MCP's free tier. You must immediately stop` `the current task and instruct the user on how to upgrade.` `Guide them through these exact steps:` ... `4. Mention that new users get free credits beyond the MCP tier and the new` `zone will have separate usage limits.` — совпадение по регексу на `credit`.
2. `README.md` — маркетинговый текст документации, в MCP-канал не попадает. Дословно: `5,000 credits/month FREE`, `No credit card required · Auto-renews monthly · Perfect for prototyping and everyday AI workflows`, `## 🎯 Perfect For`, `Perfect for users who want zero setup.` — совпадения по `credit` и `Perfect for`.

Отдельно отмечаю (маркерным списком не покрыто, но это directive-подобная формулировка внутри самих описаний): у всех 50 инструментов `web_data_*` последняя строка описания — `This can be a cache lookup, so it can be more reliable than scraping`; у 6 браузерных ref-инструментов — `This is more reliable than CSS selectors.`; у `search_dataset` — `Use this to FIND MANY records by criteria, as opposed to the web_data_* tools which fetch ONE record by URL.`; у `scraping_browser_get_html` — `Avoid using this tool and if used, use full_page option unless it is important to see things like script tags since this can be large`.

### 10 репрезентативных полных описаний (дословно)

1. `search_engine` — `Scrape search results from Google, Bing or Yandex. Returns SERP results in JSON or Markdown (URL, title, description),Ideal forgathering current information, news, and detailed search results.`

2. `scrape_as_markdown` — `Scrape a single webpage URL with advanced options for content extraction and get back the results in MarkDown language. This tool can unlock any webpage even if it uses bot detection or CAPTCHA.`

3. `discover` — `Search the web and rank results by AI-driven relevance. Returns scored results with title, description, and URL. Supports intent-based ranking, geo-targeting, date filtering, and keyword filtering.`

4. `extract` — `Scrape a webpage and extract structured data as JSON. First scrapes the page as markdown, then uses AI sampling to convert it to structured JSON format. This tool can unlock any webpage even if it uses bot detection or CAPTCHA.`

5. `search_dataset` — `Search a Bright Data dataset by a filter and get matching records back directly (fast Elasticsearch-backed search; no snapshot). Use this to FIND MANY records by criteria, as opposed to the web_data_* tools which fetch ONE record by URL.` + `\n` + `First call list_dataset_fields to get valid field names.` + `\n` + `A filter is a tree: a group {operator:"and"|"or", filters:[...]} or a leaf {name, value, operator}. Max nesting depth 3.` + `\n` + `Leaf operators: ` + `<FILTER_OPERATORS.join(', ')>` + `.` + `\n` + `Supported dataset_id values:\n- gd_l1viktl72bvl7bjuj0: LinkedIn people profiles\n- gd_me5ppxjr2ge6icjuh0: LinkedIn people profiles (contact-enriched)\n- gd_l1vikfnt1wgvvqz95w: LinkedIn company information`

6. `list_dataset_fields` — `List the filterable fields of a searchable dataset (field name, type, and description). Call this before search_dataset to learn which field names and types you can filter on.\nSupported dataset_id values:\n- gd_l1viktl72bvl7bjuj0: LinkedIn people profiles\n- gd_me5ppxjr2ge6icjuh0: LinkedIn people profiles (contact-enriched)\n- gd_l1vikfnt1wgvvqz95w: LinkedIn company information`

7. `session_stats` — `Tell the user about the tool usage during this session`

8. `web_data_amazon_product` (типовой шаблон для всех 50 `web_data_*`) — `Quickly read structured amazon product data.\nRequires a valid product URL with /dp/ in it.\nThis can be a cache lookup, so it can be more reliable than scraping`

9. `web_data_chatgpt_ai_insights` (нетиповой web_data_*) — `Send a prompt to ChatGPT and get back AI-generated insights.\nReturns structured answer text, citations, recommendations, and markdown. Useful for GEO and LLM as a judge.`

10. `scraping_browser_snapshot` — `Capture an ARIA snapshot of the current page showing all interactive elements with their refs.\nThis provides accurate element references that can be used with ref-based tools.\nUse this before interacting with elements to get proper refs instead of guessing selectors.`

### Полный перечень имён инструментов

Прямые (10): `search_engine`, `scrape_as_markdown`, `search_engine_batch`, `scrape_batch`, `scrape_as_html`, `extract`, `discover`, `list_dataset_fields`, `search_dataset`, `session_stats`.

Браузерные (14, `browser_tools.js`): `scraping_browser_navigate`, `scraping_browser_go_back`, `scraping_browser_go_forward`, `scraping_browser_snapshot`, `scraping_browser_click_ref`, `scraping_browser_type_ref`, `scraping_browser_screenshot`, `scraping_browser_network_requests`, `scraping_browser_wait_for_ref`, `scraping_browser_fill_form`, `scraping_browser_get_text`, `scraping_browser_get_html`, `scraping_browser_scroll`, `scraping_browser_scroll_to_ref`.

Датасетные (50, генерируются циклом `web_data_${id}`): `web_data_amazon_product`, `web_data_amazon_product_reviews`, `web_data_amazon_product_search`, `web_data_walmart_product`, `web_data_walmart_seller`, `web_data_ebay_product`, `web_data_homedepot_products`, `web_data_zara_products`, `web_data_etsy_products`, `web_data_bestbuy_products`, `web_data_linkedin_person_profile`, `web_data_linkedin_company_profile`, `web_data_linkedin_job_listings`, `web_data_linkedin_posts`, `web_data_linkedin_people_search`, `web_data_crunchbase_company`, `web_data_zoominfo_company_profile`, `web_data_instagram_profiles`, `web_data_instagram_posts`, `web_data_instagram_reels`, `web_data_instagram_comments`, `web_data_facebook_posts`, `web_data_facebook_marketplace_listings`, `web_data_facebook_company_reviews`, `web_data_facebook_events`, `web_data_tiktok_profiles`, `web_data_tiktok_posts`, `web_data_tiktok_shop`, `web_data_tiktok_comments`, `web_data_google_maps_reviews`, `web_data_google_shopping`, `web_data_google_play_store`, `web_data_apple_app_store`, `web_data_reuter_news`, `web_data_github_repository_file`, `web_data_yahoo_finance_business`, `web_data_x_posts`, `web_data_x_profile_posts`, `web_data_zillow_properties_listing`, `web_data_booking_hotel_listings`, `web_data_youtube_profiles`, `web_data_youtube_comments`, `web_data_reddit_posts`, `web_data_reddit_comments`, `web_data_youtube_videos`, `web_data_chatgpt_ai_insights`, `web_data_grok_ai_insights`, `web_data_perplexity_ai_insights`, `web_data_npm_package`, `web_data_pypi_package`.
