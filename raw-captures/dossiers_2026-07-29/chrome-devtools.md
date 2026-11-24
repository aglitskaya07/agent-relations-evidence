# UNIT: chrome-devtools-mcp@1.6.0 | npm (Google) | captured 2026-07-29 (static, tarball)

## CHANNEL: instructions, npm (static)
(see extraction below — if there is none in the code, the section will be marked "not found")

**Extraction: instructions NOT found.** In `build/src/index.js` the server is created as:

```js
const server = new McpServer({
    name: 'chrome_devtools',
    title: 'Chrome DevTools MCP server',
    version: VERSION,
}, { capabilities: { logging: {} } });
```

The `instructions` field is not passed to the constructor; all other occurrences of `instructions` in the code are internals of the MCP SDK bundle (`build/src/third_party/index.js`) and Lighthouse localization strings that are not related to the server.

**Additional instruction channel (not MCP-handshake):** the package includes a `skills/` directory with six agent skills (`chrome-devtools`, `chrome-devtools-cli`, `debug-optimize-lcp`, `memory-leak-debugging`, `a11y-debugging`, `troubleshooting`) — SKILL.md files with instructions for the agent. They are not passed through MCP `initialize`, but are delivered to the agent if the client picks up skills from the package.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

A total of **55** tools (catalog `build/src/tools/`: console, emulation, extensions, input, lighthouse, memory, network, pages, performance, screencast, screenshot, script, snapshot, thirdPartyDeveloper, webmcp + slim profile `slim/tools.js` with 3 simplified screenshot/navigate/evaluate tools).

### Marker scan (regexes for steering markers across ALL 55 descriptions)

Matches: 2 (both are the marker `prefer`, internal self-preference between tools of the same server, not displacing another tool).

1. **fill_form** (`input.js`), marker `prefer`:
> Fill out multiple form elements (inputs, selects, checkboxes, radios) at once. ALWAYS prefer this tool over multiple individual 'fill' or 'click' calls when interacting with forms. It is significantly faster, more reliable, and reduces turn count. Example: Fill username, password, and check "Remember Me" in one call.

2. **take_snapshot** (`snapshot.js`), marker `Prefer`:
> Take a text snapshot of the currently selected page based on the a11y tree. The snapshot lists page elements along with a unique
> identifier (uid). Always use the latest snapshot. Prefer taking a snapshot over taking a screenshot. The snapshot indicates the element selected
> in the DevTools Elements panel (if any).

Other markers (instead of built-in, most powerful, PRECEDENCE, LAST resort, primary, MUST use, whenever the user, refund/credit/reward, etc.) — no matches.

### 8 representative full descriptions (verbatim)

**click** (`input.js`):
> Clicks on the provided element

**evaluate_script** (`script.js`):
> Evaluate a JavaScript function inside the currently selected page${cliArgs?.categoryExtensions ? ' or service worker' : ''}. Returns the response as JSON, so returned values have to be JSON-serializable.

**navigate_page** (`pages.js`):
> Go to a URL, or back, forward, or reload. Use project URL if not specified otherwise.

**take_screenshot** (`screenshot.js`):
> Take a screenshot of the page or element.

**performance_start_trace** (`performance.js`):
> Start a performance trace on the selected webpage. Use to find frontend performance issues, Core Web Vitals (LCP, INP, CLS), and improve page load speed.

**list_network_requests** (`network.js`):
> List all requests for the currently selected page since the last navigation.

**lighthouse_audit** (`lighthouse.js`):
> Get Lighthouse score and reports for accessibility, SEO, best practices, and agentic browsing. This excludes performance. For performance audits, run ${startTrace.name}

**execute_webmcp_tool** (`webmcp.js`):
> Executes a WebMCP tool exposed by the page.

### Dynamic assembly of descriptions

5 descriptions — template literals with interpolation (`list_console_messages`, `get_console_message`, `lighthouse_audit`, `list_pages`, `evaluate_script`). Interpolations are limited to: conditional additions based on the CLI flag `categoryExtensions` and substitution of neighboring tool names. There are no external/network sources for the description text. Separate case: `execute_webmcp_tool` / `execute_3p_developer_tool` execute tools declared by the web page itself — their descriptions come from the page at runtime and are not fixed statically (a potential runtime channel for third-party text).

## NOTES
- Code is NOT minified: readable compiled TypeScript (ES modules, license comments preserved). Exception: `build/src/third_party/*` (MCP SDK and Lighthouse bundles, concatenated, but also not one-line minified).
- Risk of dynamic string assembly: low for its own descriptions (only CLI flags and cross-links to tool names); separately noted is the runtime channel webmcp/3p-developer tools, where descriptions come from an open page.
- Reviewed: 366 files in the package, of which all 19 files `build/src/tools/**` were text-analyzed (grep+regex across all), `build/src/index.js` in full, grep across all `build/` (348 files) for `instructions`/`new McpServer`/`registerTool`; the `skills/` directory (6 SKILL.md) was counted as a side channel.
