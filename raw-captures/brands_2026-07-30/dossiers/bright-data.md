# UNIT: bright-data | Bright Data | github brightdata/brightdata-mcp | author type: official | captured 2026-07-29 (static source)

## SERVER CONFIRMATION

This is an MCP server. `server.js` creates `new FastMCP({name: 'Bright Data', version: package_json.version})`, registers tools via `server.addTool(...)` (wrapper `addTool`), prompts via `server.addPrompts(prompts)`, and starts the stdio transport: `server.start({transportType: 'stdio'})`. Language: JavaScript (ESM, Node); dependencies `fastmcp` + `zod`.

Total number of registered tools: **74** = 10 declared directly in `server.js` + 50 generated in the `web_data_<id>` loop + 14 browser tools from `browser_tools.js`. The actual output at initialization is filtered by env variables (`PRO_MODE`, `GROUPS`, `TOOLS`); by default only `pro_mode_tools = ['search_engine','scrape_as_markdown','search_engine_batch','scrape_batch','discover']` are returned.

## CHANNEL: instructions
(not found statically)

Only `name` and `version` are passed to the `FastMCP` constructor. There is no `instructions` field in `server.js` or anywhere else in the repository (grep for `instructions` case-insensitive across all .js/.json/.md, excluding package-lock, gives 0 matches). The `initialize` response is not assembled manually — it is built by the `fastmcp` library.

### Related channel (not instructions): MCP prompts

In `prompts.js` there are two prompts registered via `server.addPrompts(prompts)`. This is not the instructions field and not tool descriptions, but a channel of directive text containing directives for tool prioritization. I record the fact and the literal descriptions:

- `web_scraping_strategy` — description: `Decision tree for picking the right Bright Data tool. Invoke at the start of any scraping session to learn the correct tool selection order (dataset tools -> Web Unlocker -> Browser API).`
- `diagnose_scraping_approach` — description: `Run a two-step diagnostic to discover the correct Bright Data product for a new website. Tries Web Unlocker first, then Browser API, then reports which succeeded.`

The bodies (`load()`) contain among other things: `Always follow this order -- do not skip ahead:`, `NEVER use the browser tools for sites scrape_as_markdown can handle.`, `NEVER use scrape_as_markdown when a web_data_* tool matches the URL pattern.`, `Do not proceed with data extraction until the diagnostic is complete.` — but they are delivered only on an explicit prompt request from the client, not in initialize.

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

74 tools > 40, therefore: full marker scan of all descriptions + 10 representative full descriptions.

### Result of marker scan

Running the full set of regexes across all files with tool definitions (`server.js`, `browser_tools.js`, `prompts.js`, `tool_groups.js`, `search_dataset_schema.js`, `assets/Tools.md`) yielded **zero matches inside tool `description` strings**.

Matches were found only outside the tool-description channel; I include them for completeness, noting that these are not descriptions:

1. `server.js`, line ~1340 — runtime error text thrown by `tool_fn` when the free limit is exhausted (not a description, reaches the model only as the result of a failed call). Verbatim: `The user has reached the 5,000 request monthly` `limit for Bright Data MCP's free tier. You must immediately stop` `the current task and instruct the user on how to upgrade.` `Guide them through these exact steps:` ... `4. Mention that new users get free credits beyond the MCP tier and the new` `zone will have separate usage limits.` — regex match on `credit`.
2. `README.md` — marketing documentation text, does not enter the MCP channel. Verbatim: `5,000 credits/month FREE`, `No credit card required · Auto-renews monthly · Perfect for prototyping and everyday AI workflows`, `## 🎯 Perfect For`, `Perfect for users who want zero setup.` — matches on `credit` and `Perfect for`.

Separately note (not covered by the marker list, but this is a directive-like formulation inside the descriptions themselves): for all 50 `web_data_*` tools, the last line of the description is `This can be a cache lookup, so it can be more reliable than scraping`; for 6 browser ref tools — `This is more reliable than CSS selectors.`; for `search_dataset` — `Use this to FIND MANY records by criteria, as opposed to the web_data_* tools which fetch ONE record by URL.`; for `scraping_browser_get_html` — `Avoid using this tool and if used, use full_page option unless it is important to see things like script tags since this can be large`.

### 10 representative full descriptions (verbatim)

1. `search_engine` — `Scrape search results from Google, Bing or Yandex. Returns SERP results in JSON or Markdown (URL, title, description),Ideal forgathering current information, news, and detailed search results.`

2. `scrape_as_markdown` — `Scrape a single webpage URL with advanced options for content extraction and get back the results in MarkDown language. This tool can unlock any webpage even if it uses bot detection or CAPTCHA.`

3. `discover` — `Search the web and rank results by AI-driven relevance. Returns scored results with title, description, and URL. Supports intent-based ranking, geo-targeting, date filtering, and keyword filtering.`

4. `extract` — `Scrape a webpage and extract structured data as JSON. First scrapes the page as markdown, then uses AI sampling to convert it to structured JSON format. This tool can unlock any webpage even if it uses bot detection or CAPTCHA.`

5. `search_dataset` — `Search a Bright Data dataset by a filter and get matching records back directly (fast Elasticsearch-backed search; no snapshot). Use this to FIND MANY records by criteria, as opposed to the web_data_* tools which fetch ONE record by URL.` + `\n` + `First call list_dataset_fields to get valid field names.` + `\n` + `A filter is a tree: a group {operator:"and"|"or", filters:[...]} or a leaf {name, value, operator}. Max nesting depth 3.` + `\n` + `Leaf operators: ` + `<FILTER_OPERATORS.join(', ')>` + `.` + `\n` + `Supported dataset_id values:\n- gd_l1viktl72bvl7bjuj0: LinkedIn people profiles\n- gd_me5ppxjr2ge6icjuh0: LinkedIn people profiles (contact-enriched)\n- gd_l1vikfnt1wgvvqz95w: LinkedIn company information`

6. `list_dataset_fields` — `List the filterable fields of a searchable dataset (field name, type, and description). Call this before search_dataset to learn which field names and types you can filter on.\nSupported dataset_id values:\n- gd_l1viktl72bvl7bjuj0: LinkedIn people profiles\n- gd_me5ppxjr2ge6icjuh0: LinkedIn people profiles (contact-enriched)\n- gd_l1vikfnt1wgvvqz95w: LinkedIn company information`

7. `session_stats` — `Tell the user about the tool usage during this session`

8. `web_data_amazon_product` (generic template for all 50 `web_data_*`) — `Quickly read structured amazon product data.\nRequires a valid product URL with /dp/ in it.\nThis can be a cache lookup, so it can be more reliable than scraping`

9. `web_data_chatgpt_ai_insights` (nonstandard web_data_*) — `Send a prompt to ChatGPT and get back AI-generated insights.\nReturns structured answer text, citations, recommendations, and markdown. Useful for GEO and LLM as a judge.`

10. `scraping_browser_snapshot` — `Capture an ARIA snapshot of the current page showing all interactive elements with their refs.\nThis provides accurate element references that can be used with ref-based tools.\nUse this before interacting with elements to get proper refs instead of guessing selectors.`

### Full list of tool names

Direct ones (10): `search_engine`, `scrape_as_markdown`, `search_engine_batch`, `scrape_batch`, `scrape_as_html`, `extract`, `discover`, `list_dataset_fields`, `search_dataset`, `session_stats`.

Browser tools (14, `browser_tools.js`): `scraping_browser_navigate`, `scraping_browser_go_back`, `scraping_browser_go_forward`, `scraping_browser_snapshot`, `scraping_browser_click_ref`, `scraping_browser_type_ref`, `scraping_browser_screenshot`, `scraping_browser_network_requests`, `scraping_browser_wait_for_ref`, `scraping_browser_fill_form`, `scraping_browser_get_text`, `scraping_browser_get_html`, `scraping_browser_scroll`, `scraping_browser_scroll_to_ref`.

Dataset-specific (50, generated by the `web_data_${id}` loop): `web_data_amazon_product`, `web_data_amazon_product_reviews`, `web_data_amazon_product_search`, `web_data_walmart_product`, `web_data_walmart_seller`, `web_data_ebay_product`, `web_data_homedepot_products`, `web_data_zara_products`, `web_data_etsy_products`, `web_data_bestbuy_products`, `web_data_linkedin_person_profile`, `web_data_linkedin_company_profile`, `web_data_linkedin_job_listings`, `web_data_linkedin_posts`, `web_data_linkedin_people_search`, `web_data_crunchbase_company`, `web_data_zoominfo_company_profile`, `web_data_instagram_profiles`, `web_data_instagram_posts`, `web_data_instagram_reels`, `web_data_instagram_comments`, `web_data_facebook_posts`, `web_data_facebook_marketplace_listings`, `web_data_facebook_company_reviews`, `web_data_facebook_events`, `web_data_tiktok_profiles`, `web_data_tiktok_posts`, `web_data_tiktok_shop`, `web_data_tiktok_comments`, `web_data_google_maps_reviews`, `web_data_google_shopping`, `web_data_google_play_store`, `web_data_apple_app_store`, `web_data_reuter_news`, `web_data_github_repository_file`, `web_data_yahoo_finance_business`, `web_data_x_posts`, `web_data_x_profile_posts`, `web_data_zillow_properties_listing`, `web_data_booking_hotel_listings`, `web_data_youtube_profiles`, `web_data_youtube_comments`, `web_data_reddit_posts`, `web_data_reddit_comments`, `web_data_youtube_videos`, `web_data_chatgpt_ai_insights`, `web_data_grok_ai_insights`, `web_data_perplexity_ai_insights`, `web_data_npm_package`, `web_data_pypi_package`.
