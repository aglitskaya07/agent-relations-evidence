# UNIT: opendia | npm v1.1.1 (published 2026-07-03T00:48:00.032Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT
This is a real MCP server. `server.js` implements a manual JSON-RPC router (`handleMCPRequest`) that handles the methods `initialize`, `tools/list`, `tools/call`, `resources/list`, `prompts/list`, `prompts/get`. The SDK `@modelcontextprotocol/*` is not used — the protocol is implemented manually on top of Express + `ws`. The server acts as a bridge between MCP and a browser extension (Chrome/Firefox) via WebSocket. The actual tool set comes dynamically from the extension (`availableTools`); if the extension is absent, a static fallback set is returned (`getFallbackTools`).

## CHANNEL: instructions, npm (static, 143 chars)
The `instructions` string returned in the `initialize` response (server.js:192–193):

"🎯 Enhanced browser automation with anti-detection bypass for Twitter/X, LinkedIn, Facebook. Extension may take a moment to connect."

serverInfo.name = "browser-mcp-server", version "2.0.0" (despite the npm package version 1.1.1).

Additionally: when calling `tools/call` without a connected extension, an error text with setup instructions is returned (server.js:241) — this is response content, not the instructions channel.

## CHANNEL: tool descriptions, npm (static, coverage=full)

IMPORTANT: the real list of tools is formed by the extension at runtime (`availableTools.map(...)`, server.js:216) and is NOT included in the tarball — the extension is supplied separately. Below are 18 static fallback tools from `getFallbackTools()` (server.js), which the server returns until the extension connects. They are <= 40 → included ALL, verbatim.

1. **page_analyze** — "🔍 BACKGROUND TAB READY: Analyze any tab without switching! Two-phase intelligent page analysis with token efficiency optimization. Use tab_id parameter to analyze background tabs while staying on current page. (Extension required)"

2. **page_extract_content** — "📄 BACKGROUND TAB READY: Extract content from any tab without switching! Perfect for analyzing multiple research tabs, articles, or pages simultaneously. Use tab_id to target specific background tabs. (Extension required)"

3. **element_click** — "🖱️ BACKGROUND TAB READY: Click elements in any tab without switching! Perform actions on background tabs while staying on current page. Use tab_id to target specific tabs. (Extension required)"

4. **element_fill** — "✏️ BACKGROUND TAB READY: Fill forms in any tab without switching! Enhanced focus and event simulation for modern web apps with anti-detection bypass for Twitter/X, LinkedIn, Facebook. Use tab_id to fill forms in background tabs. (Extension required)"

5. **page_navigate** — "🧭 Navigate to URLs with wait conditions (Extension required)"

6. **page_wait_for** — "⏳ Wait for elements or conditions (Extension required)"

7. **tab_create** — "Creates tabs. CRITICAL: For multiple identical tabs, ALWAYS use 'count' parameter! Examples: {url: 'https://x.com', count: 5} creates 5 Twitter tabs. {url: 'https://github.com', count: 10} creates 10 GitHub tabs. Single tab: {url: 'https://example.com'}. Multiple different URLs: {urls: ['url1', 'url2']}."

8. **tab_close** — "❌ Close specific tab(s) by ID or close current tab (Extension required)"

9. **tab_list** — "📋 TAB DISCOVERY: Get list of all open tabs with IDs for background tab targeting! Shows content script readiness status and tab details. Essential for multi-tab workflows - use tab IDs with other tools to work on background tabs. (Extension required)"

10. **tab_switch** — "🔄 Switch to a specific tab by ID (Extension required)"

11. **element_get_state** — "🔍 Get detailed state information for a specific element (disabled, clickable, etc.) (Extension required)"

12. **get_bookmarks** — "Get all bookmarks or search for specific bookmarks (Extension required)"

13. **add_bookmark** — "Add a new bookmark (Extension required)"

14. **get_history** — "🕒 Search browser history with comprehensive filters for finding previous work (Extension required)"

15. **get_selected_text** — "📝 BACKGROUND TAB READY: Get selected text from any tab without switching! Perfect for collecting quotes, citations, or highlighted content from multiple research tabs simultaneously. (Extension required)"

16. **page_scroll** — "📜 BACKGROUND TAB READY: Scroll any tab without switching! Critical for long pages. Navigate through content in background tabs while staying on current page. Use tab_id to target specific tabs. (Extension required)"

17. **get_page_links** — "🔗 Get all hyperlinks on the current page with smart filtering (Extension required)"

18. **page_style** — "🎨 Transform page appearance with themes, colors, fonts, and fun effects! Apply preset themes like 'dark_hacker', 'retro_80s', or create custom styles. Perfect for making boring pages fun or improving readability."

## MARKER-ANALYSIS (for reference)
Run of steering markers. No explicit precedence/override/"instead of built-in"/refund patterns were found. Soft imperative markers:
- **tab_create**: "CRITICAL: ... ALWAYS use 'count' parameter!", "DO NOT make 5 separate calls!" (in inputSchema field descriptions) — a forceful instruction for the agent to generate batch opening of many tabs (a potential vector for mass auto-posting/spam together with anti-detection).
- A recurring motif in instructions and in element_fill descriptions: **"anti-detection bypass for Twitter/X, LinkedIn, Facebook"** — the server directly positions bypassing social-network anti-cheat/anti-bot detection as a feature.
- Multiple "BACKGROUND TAB READY ... without switching" — push toward hidden-from-the-user actions in background tabs.

## PROMPTS (prompts/list, static)
The server also returns 6 workflow prompts (not tools): post_to_social ("Post content to social media platforms with anti-detection bypass"), post_selected_quote, research_workflow, analyze_browsing_session, organize_tabs, fill_form_assistant.

## NOTES
- The code is NOT minified (2555 lines, readable), only text analysis was performed, the package code was not run.
- Risk of dynamic construction of tool strings: HIGH by composition, but not by text in the tarball — the actual tool name/description values come from the browser extension at runtime (`availableTools`), which is not in the npm package. Only the 143-character `instructions` and 18 fallback descriptions are statically fixed.
- Reviewed files: 3 (package.json, server.js, README.md — the last one briefly). Fallback descriptions were extracted with a regex over the server.js text.
