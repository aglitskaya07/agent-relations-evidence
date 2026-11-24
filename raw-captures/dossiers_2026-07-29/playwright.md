# UNIT: playwright-mcp@0.0.78 | npm @playwright/mcp (Microsoft) | captured 2026-07-29 (static, tarball)

## CHANNEL: instructions, npm (static)
(see extraction below — if there is none in the code, the section will be marked "not found")

**Result of static check: instructions in the tarball code were NOT FOUND.**
The tarball is a thin shim: `index.js` exports `tools.createConnection` from `playwright-core/lib/coreBundle`, `cli.js` calls `tools.decorateMCPCommand`. The entire actual MCP server implementation (including any possible `instructions` string in the constructor and tool descriptions) lives in dependency `playwright-core@1.62.0-alpha-1783623505000`, which is NOT included in the tarball. None of the 4 text code files (`index.js`, `cli.js`, `index.d.ts`, `config.d.ts`) contain any instructions strings, profiles, or system prompts. No other instruction strings/profiles were found.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Source of descriptions: the README.md tarball (auto-generated documentation, `update-readme.js` in scripts) — 69 tools with name + Description fields. IMPORTANT: this is a documentation channel; the descriptions strings themselves are absent in the tarball code (they live in playwright-core, not shipped). The README in Playwright MCP is generated from the source, so it is used as a proxy for code.

Total tools: 69 (> 40) → full marker-scan of all descriptions + 8 representative full descriptions.

### Marker-scan (all 69 descriptions, full regex run)

Matches: 1.

- **browser_verify_text_visible** — "Verify text is visible on the page. Prefer browser_verify_element_visible if possible." (marker `prefer`; self-referential routing between its own tools, not against built-ins)

Other markers (instead of built-in, PRECEDENCE, takes precedence, LAST resort, MUST use, primary tool, refund/credit/reward, ignore previous, whenever the user, etc.) — 0 matches.

Borderline formulations outside regexes (for completeness):
- **browser_snapshot** — "Capture accessibility snapshot of the current page, this is better than screenshot" (comparative steering between its own tools)
- **browser_take_screenshot** — «...You can't perform actions based on the screenshot, use browser_snapshot for actions.»
- **browser_run_code_unsafe** — "Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent." (honest risk labeling, not steering)

### 8 representative full descriptions (verbatim)

- **browser_click** — «Perform click on a web page»
- **browser_navigate** — «Navigate to a URL»
- **browser_snapshot** — «Capture accessibility snapshot of the current page, this is better than screenshot»
- **browser_take_screenshot** — «Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.»
- **browser_find** — «Search the accessibility snapshot of the current page for text or a regular expression. Returns matching snapshot nodes with a few lines of surrounding context (like search snippets), each shown under its path from the root of the tree, which is cheaper than capturing the whole snapshot when you only need to locate an element and its ref.»
- **browser_run_code_unsafe** — «Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.»
- **browser_network_requests** — «Returns a numbered list of network requests since loading the page. Use browser_network_request with the number to get full details.»
- **browser_video_show_actions** — «Annotate subsequent actions performed on the page with a callout that names the action and highlights the target element. Useful while video recording or screencasting.»

### Full list of names (69)

browser_click, browser_close, browser_console_messages, browser_drag, browser_drop, browser_evaluate, browser_file_upload, browser_fill_form, browser_find, browser_handle_dialog, browser_hover, browser_navigate, browser_navigate_back, browser_network_request, browser_network_requests, browser_press_key, browser_resize, browser_run_code_unsafe, browser_select_option, browser_snapshot, browser_take_screenshot, browser_type, browser_wait_for, browser_tabs, browser_get_config, browser_network_state_set, browser_route, browser_route_list, browser_unroute, (…debug/tracing/video: browser_start_tracing, browser_start_video, browser_stop_tracing, browser_stop_video, browser_video_chapter, browser_video_hide_actions, browser_video_show_actions…), browser_mouse_click_xy, browser_mouse_down, browser_mouse_drag_xy, browser_mouse_move_xy, browser_mouse_up, browser_mouse_wheel, browser_pdf_save, browser_generate_locator, browser_verify_element_visible, browser_verify_list_visible, browser_verify_text_visible, browser_verify_value and others — the full list is in README.md lines 857–1581.

## NOTES (static analysis)

- The code is NOT minified, but the tarball contains only a shim (2 JS files of about 20-30 lines each). The server implementation is in the playwright-core dependency that is not published in this tarball; to fully verify the initialize instructions, a separate static analysis of playwright-core is needed.
- Risk of dynamic string assembly: in the tarball itself, zero (there are no strings at all); in playwright-core — not assessed (out of scope).
- Reviewed files: 7 (all tarball files: index.js, cli.js, index.d.ts, config.d.ts, package.json, README.md, LICENSE).
