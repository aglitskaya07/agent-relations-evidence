# UNIT: ac.tandem/docs-mcp | {"name": "ac.tandem/docs-mcp", "title": "Tandem Docs MCP", "version": "0.3.2"} | hosted https://tandem.ac/mcp | captured 2026-07-29 (keyless)

## CHANNEL: instructions, hosted (72 chars)

Use tools/list and tools/call to retrieve Tandem documentation guidance.

## CHANNEL: tool descriptions, hosted (13 tools)

### tool: search_docs

Search the published Tandem docs index for relevant pages.

### tool: get_doc

Fetch and normalize a published Tandem docs page by path or URL.

### tool: get_start_path

Recommend the best Tandem docs starting path for a desktop user, server admin, or developer.

### tool: recommend_next_docs

Recommend the next Tandem docs to read after a current page, optionally biased toward a goal.

### tool: answer_how_to

Answer how to install or use Tandem, build workflows, or use the SDKs by synthesizing relevant published docs.

### tool: get_tandem_guide

Return a structured Tandem learning guide for install-engine, python-sdk, typescript-sdk, build-workflows, or headless-deploy.

### tool: warmup_docs_cache

Refresh the docs index and preload the most important Tandem docs pages into cache.

### tool: get_docs_cache_status

Inspect the current docs cache state for index sources and warmed pages.

### tool: refresh_docs_index

Force-refresh docs indexes and report whether data came from the network, cache, or stale fallback.

### tool: refresh_doc_page

Force-refresh a docs page and report whether content came from the network, cache, or stale fallback.

### tool: invalidate_docs_cache

Invalidate docs cache entries for index data, all pages, or a specific page path.

### tool: compare_docs_index_refresh

Force-refresh the docs indexes and return before/after hashes so content changes can be proven.

### tool: compare_doc_page_refresh

Force-refresh a docs page and return before/after hashes so page content changes can be proven.

