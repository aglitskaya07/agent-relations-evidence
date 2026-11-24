# UNIT: chrome-mcp | Chrome MCP | github hangwin/mcp-chrome | author type: community | captured 2026-07-29 (static source)

Confirmation of the MCP server: `app/native-server/src/mcp/mcp-server.ts` — `new Server({name:'ChromeMcpServer',version:'1.0.0'},{capabilities:{tools:{}}})` from `@modelcontextprotocol/sdk/server/index.js`; stdio variant in `app/native-server/src/mcp/mcp-server-stdio.ts` (`StdioChromeMcpServer`). Handlers `ListToolsRequestSchema` / `CallToolRequestSchema` in `app/native-server/src/mcp/register-tools.ts`, tool catalog — `packages/shared/src/tools.ts` (`TOOL_SCHEMAS`).

## CHANNEL: instructions
(not found statically)

Neither of the two constructors `new Server(...)` passes the `instructions` field; the options contain only `capabilities`. The `initialize` response is not overridden manually (the SDK default is used).

## CHANNEL: tool descriptions (coverage=full)

The total number of tools in the static catalog `TOOL_SCHEMAS`: 27. Plus dynamic tools `flow.<slug>`, whose name/description arrive at runtime from the extension (`rr_list_published_flows`), are not statically available.

### get_windows_and_tabs

Get all currently open browser windows and tabs

### performance_start_trace

Starts a performance trace recording on the selected page. Optionally reloads the page and/or auto-stops after a short duration.

### performance_stop_trace

Stops the active performance trace recording on the selected page.

### performance_analyze_insight

Provides a lightweight summary of the last recorded trace. For deep insights (CWV, breakdowns), integrate native-side DevTools trace engine.

### chrome_read_page

Get an accessibility tree representation of visible elements on the page. Only returns elements that are visible in the viewport. Optionally filter for only interactive elements.\nTip: If the returned elements do not include the specific element you need, use the computer tool\'s screenshot (action="screenshot") to capture the element\'s on-screen coordinates, then operate by coordinates.

### chrome_computer

Use a mouse and keyboard to interact with a web browser, and take screenshots.\n* Whenever you intend to click on an element like an icon, you should consult a read_page to determine the ref of the element before moving the cursor.\n* If you tried clicking on a program or link but it failed to load, even after waiting, try screenshot and then adjusting your click location so that the tip of the cursor visually falls on the element that you want to click.\n* Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the element. Don't click boxes on their edges unless asked.

### chrome_navigate

Navigate to a URL, refresh the current tab, or navigate browser history (back/forward)

### chrome_screenshot

[Prefer read_page over taking a screenshot and Prefer chrome_computer] Take a screenshot of the current page or a specific element. For new usage, use chrome_computer with action="screenshot". Use this tool if you need advanced options.

### chrome_close_tabs

Close one or more browser tabs

### chrome_switch_tab

Switch to a specific browser tab

### chrome_get_web_content

Fetch content from a web page

### chrome_network_request

Send a network request from the browser with cookies and other browser context

### chrome_network_capture

Unified network capture tool. Use action="start" to begin capturing, action="stop" to end and retrieve results. Set needResponseBody=true to capture response bodies (uses Debugger API, may conflict with DevTools). Default mode uses webRequest API (lightweight, no debugger conflict, but no response body).

### chrome_handle_download

Wait for a browser download and return details (id, filename, url, state, size)

### chrome_history

Retrieve and search browsing history from Chrome

### chrome_bookmark_search

Search Chrome bookmarks by title and URL

### chrome_bookmark_add

Add a new bookmark to Chrome

### chrome_bookmark_delete

Delete a bookmark from Chrome

### chrome_javascript

Execute JavaScript code in a browser tab and return the result. Uses CDP Runtime.evaluate with awaitPromise and returnByValue; automatically falls back to chrome.scripting.executeScript if the debugger is busy. Output is sanitized (sensitive data redacted) and truncated by default.

### chrome_click_element

Click on an element in a web page. Supports multiple targeting methods: CSS selector, XPath, element ref (from chrome_read_page), or viewport coordinates. More focused than chrome_computer for simple click operations.

### chrome_fill_or_select

Fill or select a form element on a web page. Supports input, textarea, select, checkbox, and radio elements. Use CSS selector, XPath, or element ref to target the element.

### chrome_request_element_selection

Request the user to manually select one or more elements on the current page. Use this as a human-in-the-loop fallback when you cannot reliably locate the target element after approximately 3 attempts using chrome_read_page combined with chrome_click_element/chrome_fill_or_select/chrome_computer. The user will see a panel with instructions and can click on the requested elements. Returns element refs compatible with chrome_click_element/chrome_fill_or_select (including iframe frameId for cross-frame support).

### chrome_keyboard

Simulate keyboard input on a web page. Supports single keys (Enter, Tab, Escape), key combinations (Ctrl+C, Ctrl+V), and text input. Can target a specific element or send to the focused element.

### chrome_console

Capture console output from a browser tab. Supports snapshot mode (default; one-time capture with ~2s wait) and buffer mode (persistent per-tab buffer you can read/clear instantly without waiting).

### chrome_upload_file

Upload files to web forms with file input elements using Chrome DevTools Protocol

### chrome_handle_dialog

Handle JavaScript dialogs (alert/confirm/prompt) via CDP

### chrome_gif_recorder

Record browser tab activity as an animated GIF.\n\nModes:\n- Fixed FPS mode (action="start"): Captures frames at regular intervals. Good for animations/videos.\n- Auto-capture mode (action="auto_start"): Captures frames automatically when chrome_computer or chrome_navigate actions succeed. Better for interaction recordings with natural pacing.\n\nUse "stop" to end recording and save the GIF.

Note on quoting: the descriptions are given verbatim as string literals in the source; the `\n` sequences in the text are TypeScript string escape sequences, and at runtime they become line breaks.