# UNIT: meta-ads | Meta Ads (FB/Instagram) | github pipeboard-co/meta-ads-mcp | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CHECK

Это MCP-сервер. Python-пакет `meta_ads_mcp`, `meta_ads_mcp/core/server.py:3` — `from mcp.server.fastmcp import FastMCP`, `server.py:17` — `mcp_server = FastMCP("meta-ads")`. Регистрируются MCP-ресурсы (`mcp_server.resource(uri="meta-ads://resources")`) и 43 инструмента через декоратор `@mcp_server.tool()` в модулях `meta_ads_mcp/core/*.py`. Транспорты: stdio и Streamable HTTP.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор вызывается только с именем: `FastMCP("meta-ads")` (meta_ads_mcp/core/server.py:17). Ни `instructions=`, ни ручного ответа на `initialize` в репозитории нет. Слово "instructions" встречается только как ключ в JSON-ответах инструментов (например, в `get_login_link`: `"instructions": "Click the link above to authenticate with Meta Ads."`), это payload результата, а не канал server instructions.

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов: 43 (42 через декоратор `@mcp_server.tool()` + `get_login_link`, регистрируемый условно строкой `get_login_link = mcp_server.tool()(get_login_link)` при `ENABLE_LOGIN_LINK`). Описание = docstring функции (FastMCP берёт description из docstring). Так как > 40, применён полный маркер-скан всех 43 описаний + 12 репрезентативных полных описаний.

### Полный список инструментов (файл:строка, размер описания)

- `get_ad_accounts` — core/accounts.py:44, description 341 chars
- `get_account_info` — core/accounts.py:78, description 983 chars
- `get_ads` — core/ads.py:446, description 367 chars
- `get_ad_details` — core/ads.py:491, description 169 chars
- `get_creative_details` — core/ads.py:514, description 171 chars
- `create_ad` — core/ads.py:566, description 776 chars
- `get_ad_creatives` — core/ads.py:638, description 244 chars
- `get_ad_image` — core/ads.py:718, description 399 chars
- `get_image_by_hash` — core/ads.py:871, description 625 chars
- `get_ad_video` — core/ads.py:954, description 1216 chars
- `update_ad` — core/ads.py:1229, description 469 chars
- `upload_ad_image` — core/ads.py:1318, description 775 chars
- `compute_image_crops` — core/ads.py:1540, description 1203 chars
- `create_ad_creative` — core/ads.py:1712, description 18026 chars
- `update_ad_creative` — core/ads.py:2914, description 2015 chars
- `search_pages_by_name` — core/ads.py:3301, description 347 chars
- `get_account_pages` — core/ads.py:3324, description 270 chars
- `save_ad_image_locally` — core/ads.py:1103, description 345 chars
- `search_ads_archive` — core/ads_library.py:16, description 764 chars
- `get_adsets` — core/adsets.py:12, description 341 chars
- `get_adset_details` — core/adsets.py:52, description 314 chars
- `create_adset` — core/adsets.py:88, description 9959 chars
- `update_adset` — core/adsets.py:498, description 4342 chars
- `create_budget_schedule` — core/budget_schedules.py:13, description 725 chars
- `get_campaigns` — core/campaigns.py:12, description 1355 chars
- `get_campaign_details` — core/campaigns.py:90, description 454 chars
- `create_campaign` — core/campaigns.py:117, description 2582 chars
- `update_campaign` — core/campaigns.py:265, description 2035 chars
- `duplicate_campaign` — core/duplication.py:32, description 809 chars
- `duplicate_adset` — core/duplication.py:83, description 808 chars
- `duplicate_ad` — core/duplication.py:137, description 431 chars
- `duplicate_creative` — core/duplication.py:179, description 1218 chars
- `get_insights` — core/insights.py:58, description 6218 chars
- `search` — core/openai_deep_research.py:310, description 622 chars
- `fetch` — core/openai_deep_research.py:365, description 944 chars
- `generate_report` — core/reports.py:15, description 859 chars
- `search_interests` — core/targeting.py:12, description 382 chars
- `get_interest_suggestions` — core/targeting.py:41, description 424 chars
- `estimate_audience_size` — core/targeting.py:70, description 1464 chars
- `search_behaviors` — core/targeting.py:463, description 327 chars
- `search_demographics` — core/targeting.py:488, description 533 chars
- `search_geo_locations` — core/targeting.py:515, description 581 chars
- `get_login_link` — core/authentication.py:42, description 446 chars

### Результат маркер-скана по всем 43 описаниям

Совпадений: 2. Оба технические, без директивности в отношении выбора инструментов вне сервера.

1. `get_image_by_hash` (core/ads.py:871) — дословно:

```
...image_hash from an existing creative (object_story_spec.link_data.image_hash, asset_feed_spec images[].hash, etc.). To view the image of an existing ad, prefer get_ad_image(ad_id).
```

2. `create_ad_creative` (core/ads.py:1712) — дословно:

```
The ad set must use optimization_goal=REMINDERS_SET and the placement
                  must be restricted to Instagram feeds/stories.
```

Прочих совпадений по скану нет: описания состоят из перечислений аргументов Graph API, ограничений Meta API и примеров вызовов. Единственная маркетинговая формулировка, найденная вручную вне регекс-набора — в `generate_report` (core/reports.py:15): `**This is a premium feature available with Pipeboard Pro.**`; в `get_login_link`: `If using Pipeboard authentication (recommended), set the PIPEBOARD_API_TOKEN environment variable instead (token obtainable via https://pipeboard.co).`; в `duplicate_campaign`/`duplicate_adset`: `Recommended: Use this to run robust experiments.`

### 12 репрезентативных полных описаний (дословно)

### get_ad_accounts  (core/accounts.py:44, 341 chars)
```
Get ad accounts accessible by a user.

amount_spent and balance are returned in currency units (e.g. USD dollars),
not cents.

Args:
    access_token: Meta API access token (optional - will use cached token if not provided)
    user_id: Meta user ID or "me" for the current user
    limit: Maximum number of accounts to return (default: 200)
```

### get_account_info  (core/accounts.py:78, 983 chars)
```
Get detailed information about a specific ad account.

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    access_token: Meta API access token (optional - will use cached token if not provided)
    fields: Optional comma-separated Graph API fields to return. When provided,
            replaces the default field set. Useful for fetching extras like
            funding_source_details, spend_cap, is_prepay_account, min_daily_budget,
            disable_reason, capabilities. Default fields:
            id, name, account_id, account_status, amount_spent, balance, currency,
            age, business_city, business_country_code, timezone_name.
            For prepaid accounts (is_prepay_account=true, common in Brazil), the
            Business Manager "available balance" is the sum of funding_source_details
            STORED_BALANCE entries plus coupons — the `balance` field alone is the
            amount due to be billed, not the available pre-paid funds.
```

### get_ads  (core/ads.py:446, 367 chars)
```
Get ads for a Meta Ads account with optional filtering.

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    access_token: Meta API access token (optional - will use cached token if not provided)
    limit: Maximum number of ads to return (default: 10)
    campaign_id: Optional campaign ID to filter by
    adset_id: Optional ad set ID to filter by
```

### search  (core/openai_deep_research.py:310, 622 chars)
```
Search through Meta Ads data and return matching record IDs.
It searches across ad accounts, campaigns, ads, pages, and businesses to find relevant records
based on the provided query.

Args:
    query: Search query string to find relevant Meta Ads records
    access_token: Meta API access token (optional - will use cached token if not provided)
    
Returns:
    JSON response with list of matching record IDs
    
Example Usage:
    search(query="active campaigns")
    search(query="account spending")
    search(query="facebook ads performance")
    search(query="facebook pages")
    search(query="user businesses")
```

### fetch  (core/openai_deep_research.py:365, 944 chars)
```
Fetch a record previously returned by the 'search' tool in the same session.

IMPORTANT LIMITATIONS:
- This tool ONLY returns records that were cached by a prior 'search' call.
  It does NOT make direct API calls to Meta. If the record was not found by
  'search' first, this tool will return "Record not found".
- Do NOT use this tool to look up campaigns, adsets, or ads by ID directly.

For direct lookups by ID, use these tools instead:
- get_campaign_details(campaign_id=...) - for campaigns
- get_adset_details(adset_id=...) - for ad sets
- get_ads(account_id=..., campaign_id=...) - for ads
- get_adsets(account_id=..., campaign_id=...) - for ad sets in a campaign

Args:
    id: The record ID to fetch (format: "type:id", e.g., "account:act_123456").
        Must have been returned by a previous 'search' call.

Returns:
    JSON response with record data, or "Record not found" if the record
    was not previously cached by 'search'.
```

### generate_report  (core/reports.py:15, 859 chars)
```
Generate comprehensive Meta Ads performance reports.

**This is a premium feature available with Pipeboard Pro.**

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    access_token: Meta API access token (optional - will use cached token if not provided)
    report_type: Type of report to generate (account, campaign, comparison)
    time_range: Time period for the report (e.g., 'last_30d', 'last_7d', 'this_month')
    campaign_ids: Specific campaign IDs (required for campaign/comparison reports)
    export_format: Output format for the report (pdf, json, html)
    report_name: Custom name for the report (auto-generated if not provided)
    include_sections: Specific sections to include in the report
    breakdowns: Audience breakdown dimensions (age, gender, country, etc.)
    comparison_period: Time period for comparison analysis
```

### get_login_link  (core/authentication.py:42, 446 chars)
```
Get a clickable login link for Meta Ads authentication.

NOTE: This method should only be used if you're using your own Facebook app.
If using Pipeboard authentication (recommended), set the PIPEBOARD_API_TOKEN
environment variable instead (token obtainable via https://pipeboard.co).

Args:
    access_token: Meta API access token (optional - will use cached token if not provided)

Returns:
    A clickable resource link for Meta authentication
```

### duplicate_campaign  (core/duplication.py:32, 809 chars)
```
Duplicate a Meta Ads campaign with all its ad sets and ads.

Recommended: Use this to run robust experiments.

Args:
    campaign_id: Meta Ads campaign ID to duplicate
    name_suffix: Suffix to add to the duplicated campaign name
    include_ad_sets: Whether to duplicate ad sets within the campaign
    include_ads: Whether to duplicate ads within ad sets
    include_creatives: Whether to duplicate ad creatives
    copy_schedule: Whether to copy the campaign schedule
    new_daily_budget: Override the daily budget for the new campaign
    new_start_time: Override start time for duplicated ad sets (ISO 8601, e.g. 2026-03-10T00:00:00-0500)
    new_end_time: Override end time for duplicated ad sets (ISO 8601, e.g. 2026-03-20T23:59:59-0500)
    new_status: Status for the new campaign (ACTIVE or PAUSED)
```

### estimate_audience_size  (core/targeting.py:70, 1464 chars)
```
Estimate audience size for targeting specifications using Meta's delivery_estimate API.

This function provides comprehensive audience estimation for complex targeting combinations
including demographics, geography, interests, and behaviors. It also maintains backwards
compatibility for simple interest validation.

Args:
    access_token: Meta API access token (optional - will use cached token if not provided)
    account_id: Meta Ads account ID (format: act_XXXXXXXXX) - required for comprehensive estimation
    targeting: Complete targeting specification including demographics, geography, interests, etc.
              Example: {
                  "age_min": 25,
                  "age_max": 65,
                  "geo_locations": {"countries": ["PL"]},
                  "flexible_spec": [
                      {"interests": [{"id": "6003371567474"}]},
                      {"interests": [{"id": "6003462346642"}]}
                  ]
              }
    optimization_goal: Optimization goal for estimation (default: "REACH"). 
                      Options: "REACH", "LINK_CLICKS", "IMPRESSIONS", "CONVERSIONS", etc.
    interest_list: [DEPRECATED - for backwards compatibility] List of interest names to validate
    interest_fbid_list: [DEPRECATED - for backwards compatibility] List of interest IDs to validate

Returns:
    JSON string with audience estimation results including estimated_audience_size,
    reach_estimate, and targeting validation
```

### search_ads_archive  (core/ads_library.py:16, 764 chars)
```
Search the Facebook Ads Library archive.

Args:
    search_terms: The search query for ads.
    ad_reached_countries: List of country codes (e.g., ["US", "GB"]).
    access_token: Meta API access token (optional - will use cached token if not provided).
    ad_type: Type of ads to search for (e.g., POLITICAL_AND_ISSUE_ADS, HOUSING_ADS, ALL).
    limit: Maximum number of ads to return.
    fields: Comma-separated string of fields to retrieve for each ad.

Example Usage via curl equivalent:
    curl -G \
    -d "search_terms='california'" \
    -d "ad_type=POLITICAL_AND_ISSUE_ADS" \
    -d "ad_reached_countries=['US']" \
    -d "fields=ad_snapshot_url,spend" \
    -d "access_token=<ACCESS_TOKEN>" \
    "https://graph.facebook.com/<API_VERSION>/ads_archive"
```

### get_campaigns  (core/campaigns.py:12, 1355 chars)
```
Get campaigns for a Meta Ads account with optional filtering.

Note: By default, the Meta API returns a subset of available fields. 
Other fields like 'effective_status', 'spend_cap', 'budget_remaining',
'promoted_object', 'source_campaign_id', etc., might be available but
require specifying them in the API call (currently not exposed by this
tool's parameters).

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    access_token: Meta API access token (optional - will use cached token if not provided)
    limit: Maximum number of campaigns to return (default: 10)
    status_filter: Filter by effective status (e.g., 'ACTIVE', 'PAUSED', 'ARCHIVED').
                   Maps to the 'effective_status' API parameter, which expects an array
                   (this function handles the required JSON formatting). Leave empty for all statuses.
    objective_filter: Filter by campaign objective(s). Can be a single objective string or a list of objectives.
                     Valid objectives: 'OUTCOME_AWARENESS', 'OUTCOME_TRAFFIC', 'OUTCOME_ENGAGEMENT',
                     'OUTCOME_LEADS', 'OUTCOME_SALES', 'OUTCOME_APP_PROMOTION'.
                     Examples: 'OUTCOME_LEADS' or ['OUTCOME_LEADS', 'OUTCOME_SALES'].
                     Leave empty for all objectives.
    after: Pagination cursor to get the next set of results
```

### get_insights  (core/insights.py:58, 6218 chars)
```
Get performance insights for a campaign, ad set, ad or account.

Args:
    object_id: ID of the campaign, ad set, ad or account. You can also use the alias parameters below.
    account_id: Alias for object_id when querying account-level insights
    campaign_id: Alias for object_id when querying campaign-level insights
    adset_id: Alias for object_id when querying ad-set-level insights
    ad_id: Alias for object_id when querying ad-level insights
    access_token: Meta API access token (optional - will use cached token if not provided)
    time_range: Either a preset time range string or a dictionary with "since" and "until" dates in YYYY-MM-DD format
               Preset options: today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, 
               last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, 
               last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year
               Dictionary example: {"since":"2023-01-01","until":"2023-01-31"}
    breakdown: Optional breakdown dimension. Valid values include:
               Demographic: age, gender, country, region, dma
               Platform/Device: device_platform, platform_position, publisher_platform, impression_device
               NOTE: platform_position is a Meta-restricted breakdown — Meta requires it to be paired
               with publisher_platform (otherwise "(#100) ... (action_type, platform_position) is invalid").
               When you pass platform_position, this tool auto-adds publisher_platform, and the
               action-typed fields (actions, action_values, conversions, cost_per_action_type) are
               returned per placement, so you get leads/CPL/conversions broken down by placement.
               Creative Assets: ad_format_asset, body_asset, call_to_action_asset, description_asset,
                              image_asset, link_url_asset, title_asset, video_asset, media_type,
                              creative_relaxation_asset_type, flexible_format_asset_type,
                              gen_ai_asset_type
               NOTE: Asset breakdowns (image_asset, video_asset, etc.) only return data for ads
               running with Dynamic Creative; for non-DCO ads, expect empty rows.
               NOTE: media_type collides with the default action_breakdowns=[action_type], so
               this tool auto-overrides action_breakdowns to [] when you pass media_type.
               Action-typed metrics (actions, action_values, conversions) are still returned
               but are no longer sliced by action_type alongside media_type.
               media_asset_url, media_creator, media_destination_url, media_format,
               media_origin_url, and media_text_content are NOT supported by Meta's Insights API
               (Meta returns "(#100) Tried accessing nonexisting field"). Use the asset breakdowns
               above instead.
               Campaign/Ad Attributes: breakdown_ad_objective, breakdown_reporting_ad_id, app_id, product_id
               Conversion Tracking: coarse_conversion_value, conversion_destination, standard_event_content_type,
                                   signal_source_bucket, is_conversion_id_modeled, fidelity_type, redownload
               Time-based: hourly_stats_aggregated_by_advertiser_time_zone, 
                          hourly_stats_aggregated_by_audience_time_zone, frequency_value
               Extensions/Landing: ad_extension_domain, ad_extension_url, landing_destination, 
                                  mdsa_landing_destination
               Attribution: sot_attribution_model_type, sot_attribution_window, sot_channel, 
                           sot_event_type, sot_source
               Mobile/SKAN: skan_campaign_id, skan_conversion_id, skan_version, postback_sequence_index
               CRM/Business: crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id,
                            crm_advertiser_vertical_id, crm_ult_advertiser_id, user_persona_id, user_persona_name
               Advanced: hsid, is_auto_advance, is_rendered_as_delayed_skip_ad, mmm, place_page_id,
                        marketing_messages_btn_name, impression_view_time_advertiser_hour_v2, comscore_market,
                        comscore_market_code
    level: Level of aggregation (ad, adset, campaign, account)
    limit: Maximum number of results to return per page (default: 25, Meta API allows much higher values)
    after: Pagination cursor to get the next set of results. Use the 'after' cursor from previous response's paging.next field.
    action_attribution_windows: Optional list of attribution windows (e.g., ["1d_click", "7d_click", "1d_view"]).
               When specified, actions include additional fields for each window. The 'value' field always shows 7d_click.
    action_breakdowns: Optional list of action_breakdowns to apply to action-typed metrics. Pass [] to disable
               the default action_type slicing (required when combining action data with breakdowns that collide
               with action_type, e.g. media_type — auto-applied for media_type when not set).
               Meta supports values like action_type, action_target_id, action_destination, etc.
    compact: When True, strips redundant action-type duplicates from the response
             (omni_*, onsite_web_*, offsite_conversion.fb_pixel_*, etc.) to reduce
             payload size by ~60%. The canonical action types (purchase, add_to_cart,
             view_content, etc.) are always preserved. Default: False.

Note on response size: This tool always returns a fixed set of fields (impressions, clicks,
spend, cpc, cpm, ctr, reach, actions, action_values, etc.) and cannot filter to a subset.
For large result sets (50+ rows), the actions/action_values arrays can make responses very
large (1–2MB+). If you only need specific metrics like spend or impressions, consider using
bulk_get_insights with compact=true and the fields parameter:
    bulk_get_insights(level="ad", account_ids=[...], compact=true, fields=["spend", "impressions"])
bulk_get_insights supports level="ad", "adset", "campaign", and "account".
```
