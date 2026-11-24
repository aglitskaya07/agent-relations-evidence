# UNIT: @n8n/mcp-browser | npm v0.15.0 (published 2026-07-21T07:28:25.906Z) | scopes: npm-top | captured 2026-07-29 (static, tarball)

Type: a real MCP server (dist/server.js: `new McpServer({ name: 'n8n-browser', version: '1.0.0' })`, stdio + StreamableHTTP transports; also exported as the `createBrowserTools` library). n8n browser automation on top of Playwright/agent-browser, connects to the user's real Chrome through the "n8n AI Browser Bridge" extension.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name` and `version` are passed to the `McpServer` constructor — there is no `instructions` field in `server.js` or anywhere else in dist (grep for "instructions" finds only text about installing Brave in browser-discovery.js).

## CHANNEL: tool descriptions, npm (static, coverage=full)

31 tools (session 2, tabs 4, navigation 4, interaction 9, inspection 7, wait 1, state 2, credential 2). All descriptions verbatim:

1. **browser_connect** — `Connect to the user's browser for web automation. Optionally specify a Chromium-based browser (chrome, brave, edge, chromium). Requires the n8n AI Browser Bridge extension to be installed. Must be called before using any other browser tools.`
2. **browser_disconnect** — `Disconnect from the browser and release all resources.`
3. **browser_tab_open** — `Open a new tab. Optionally navigate to a URL.`
4. **browser_tab_list** — `List all browser tabs currently controlled.`
5. **browser_tab_focus** — `Switch the active tab. Note: focusing is not required to interact with a tab — you can interact with any tab regardless of focus.`
6. **browser_tab_close** — `Close a tab.`
7. **browser_navigate** — `Navigate to a URL and wait for the page to load.`
8. **browser_back** — `Navigate back in browser history.`
9. **browser_forward** — `Navigate forward in browser history.`
10. **browser_reload** — `Reload the current page.`
11. **browser_click** — `Click an element. Use ref from browser_snapshot (preferred) or a selector as fallback.`
12. **browser_type** — `Type text into an element. Use ref from browser_snapshot (preferred) or a selector as fallback.`
13. **browser_select** — `Select option(s) in a <select> element. Use ref from browser_snapshot (preferred) or a selector as fallback. Always use this for native select elements instead of clicks`
14. **browser_drag** — `Drag from one element to another. Use refs from browser_snapshot (preferred) or selectors as fallback.`
15. **browser_hover** — `Hover over an element. Use ref from browser_snapshot (preferred) or a selector as fallback.`
16. **browser_press** — `Press keyboard key(s). Examples: "Enter", "Control+A", "Escape".`
17. **browser_scroll** — `Scroll an element into view (mode: "element"), or scroll the page by direction/amount (mode: "direction").`
18. **browser_upload** — `Set files on a file input element, or fulfill a pending file chooser dialog. If a file chooser is pending, no element target is needed.`
19. **browser_dialog** — `Handle a JavaScript dialog (alert, confirm, prompt, beforeunload). Call before the action that triggers the dialog, or when a dialog is already pending.`
20. **browser_snapshot** — `Use this tool as your primary way to observe the page. Returns a ref-annotated accessibility tree — a compact text representation of all visible elements. Each interactive element gets a numeric ref for use in subsequent tool calls (browser_click, browser_type, etc.). Snapshots are small and fast. Prefer this over browser_screenshot unless you specifically need visual/layout information.`
21. **browser_screenshot** — `Take a screenshot of the page or a specific element. Returns a base64-encoded PNG image. Note: Prefer browser_snapshot for most tasks — it is smaller, faster, and returns refs for element targeting. Use screenshots only when you need visual information (layout, images, charts).`
22. **browser_content** — `Extract page content as structured markdown with headings, links, lists, and tables preserved. Uses readability extraction to strip navigation, ads, and boilerplate. Prefer browser_snapshot for element discovery and interaction; use this when you need to read and understand page text content.`
23. **browser_evaluate** — `Execute JavaScript in the page context and return the result. The script must be an expression or IIFE. The result is JSON-serialized.`
24. **browser_console** — `Get console messages and page errors (uncaught exceptions). Page errors appear as entries with level "error". Use level filter to narrow results.`
25. **browser_pdf** — `Generate a PDF of the current page.`
26. **browser_network** — `Get recent network requests and responses.`
27. **browser_wait** — `Wait for one or more conditions. Conditions can be combined — all must be satisfied.`
28. **browser_cookies** — `Get, set, or clear cookies.`
29. **browser_storage** — `Get, set, or clear localStorage or sessionStorage.`
30. **browser_capture_secret** — `Read a secret value from a DOM element (identified by a snapshot ref) and store it in the session buffer. The value is never returned to the LLM. Use browser_create_credential to assemble buffered secrets into a credential.`
31. **browser_create_credential** — `Assemble secrets captured with browser_capture_secret into a new n8n credential. Literal fields go in ` `` `data` `` `; fields that must come from the buffer go in ` `` `resolveData` `` ` (leaf values are buffer field names). The buffer is cleared after success unless clear=false.`
### Steering markers in descriptions (soft, within-package)
- `primary` — browser_snapshot: "Use this tool as your primary way to observe the page" (directs between ITS OWN tools, not against external ones).
- `Prefer this over` / `Prefer` — browser_snapshot («Prefer this over browser_screenshot»), browser_screenshot («Prefer browser_snapshot for most tasks — it is smaller, faster»), browser_content («Prefer browser_snapshot for element discovery»), click/type/select/drag/hover («ref … (preferred)»).
- `Always` — browser_select: «Always use this for native select elements instead of clicks».
- `Must be called before` — browser_connect: "Must be called before using any other browser tools" (technical session requirement).
- There are no externally aggressive markers (instead of built-in, takes precedence, LAST resort, Do NOT answer from memory, ignore previous, etc.) — NO.

## NOTES
- Code is NOT minified: plain tsc output with source maps and .d.ts, reads freely.
- Risk of dynamic string assembly: low. Descriptions are static literals (in session.js — concatenation of adjacent literals, reconstructed verbatim). There is no dynamic behavior in descriptions.
- Reviewed ~18 files: package.json, README.md, dist/server.js, dist/tools/{index, tabs, navigation, interaction, inspection, wait, state, session, credential, helpers}.js + grep across all dist.
- Security feature: browser_capture_secret / browser_create_credential pair — the server declares that secrets from the page are buffered outside the LLM context and assembled into n8n-credential; plus the redaction/ and sensitivity/ modules (redaction of sensitive data in snapshots).
- HTTP transport by default bearer-token + loopback-only + Origin rejection — noticeably more careful than average in the sample.
