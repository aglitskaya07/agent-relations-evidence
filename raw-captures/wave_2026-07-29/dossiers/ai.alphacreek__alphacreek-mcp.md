# UNIT: ai.alphacreek/alphacreek-mcp | {"name": "alphacreek-mcp", "version": "1.0.1"} | hosted https://mcp.alphacreek.ai/mcp | captured 2026-07-29 (keyless)

## CHANNEL: instructions, hosted (2356 chars)

AlphaCreek MCP provides SEC and UK FCA filing navigation and source text.
Use filing_registry=sec_edgar (default) for US SEC filings. Use filing_registry=fca_nsm for UK FCA NSM annual reports.
1. Choose the filing period first. Multiple fiscal periods may be available per ticker (several 10-K/20-F and 10-Q/6-K filings). Call list_filings when you need a specific reporting period, then use the returned artifact_document_id for get_filing_toc and other navigation tools. If artifact_document_id is omitted, get_filing_toc and similar locators resolve the latest filing only.
2. Read filings navigation-first. Start with get_filing_toc using the chosen artifact_document_id, then read targeted nodes via read_node_content. Use the node id from each TOC line; these are the same values shown as NODE_ID lines in read_node_content output. Pass one node via node_id or several via node_ids.
3. Prefer source tables for exact financial values. Narrative nodes often explain year-over-year changes, while absolute reported values are usually in nearby sibling or child tables under headings like 'Revenues', 'By type', 'By geography', or 'Segment results'. When text says 'The following table presents...', inspect the adjacent TableElement before answering.
4. Batch reads from the same filing. When reading several nodes from one filing, pass them in one read_node_content call via node_ids to save round-trips. read_node_content returns full node text as plain MCP text only.
For FCA filings (filing_registry=fca_nsm), TOC node ids are HTML page element ids (for example pf2a, page12, or pageView1). Use those ids with read_node_content. CITATION_URL links open the FCA reader scrolled to that page id.
<important>5. Cite every material claim. read_node_content output pairs NODE_ID lines with CITATION_URL lines. For every material claim or logical paragraph in your answer, place one or more relevant CITATION_URL links immediately next to the claim, using the URL paired with each supporting NODE_ID. A TOC node may expand into more granular child NODE_ID blocks; cite those child NODE_ID/CITATION_URL pairs when they are the closest supporting source.</important>
6. If an AlphaCreek MCP tool fails with a quota or 403 limit message, tell the user their monthly limit is reached and share https://www.alphacreek.ai/dashboard#usage for usage and upgrade.

## CHANNEL: tool descriptions, hosted (4 tools)

### tool: get_latest_filing

Return latest filing metadata for a company or ticker.

### tool: list_filings

List available filings for a ticker (newest first) with artifact_document_id and dates. Use filing_registry=fca_nsm for UK FCA annual reports. Use this first when you need a specific reporting period.

### tool: get_filing_toc

Return the full filing table of contents for one filing. If artifact_document_id is omitted, resolves the single latest filing for ticker/company (and optional document_type) only. Use list_filings first to discover a specific reporting period. For FCA filings, pass filing_registry=fca_nsm; TOC node ids are HTML page element ids (e.g. pf2a, page12, pageView1).

### tool: read_node_content

Return content for one or more navigation nodes in a filing. Pass one node via node_id or several via node_ids, using the node ids from TOC lines. These are the same values shown as NODE_ID lines in read_node_content output. The authoritative node content is returned as plain MCP text only: an ARTIFACT_DOCUMENT_ID header, then per-node blocks with NODE_ID, TITLE, CITATION_URL, CONTENT_START … CONTENT_END. A TOC node may expand into more granular child NODE_ID blocks; cite those granular NODE_ID/CITATION_URL pairs when they support the claim. For every material claim or logical paragraph in your answer, place one or more relevant CITATION_URL links immediately next to the claim, using the URL paired with each supporting NODE_ID.

