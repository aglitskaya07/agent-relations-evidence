# UNIT: playwright | Playwright | github microsoft/playwright-mcp | тип автора: официальный | captured 2026-07-29 (static source)

## IS-A-SERVER: да

`package.json`: `"name": "@playwright/mcp"`, `"mcpName": "io.github.microsoft/playwright-mcp"`, `"bin": {"playwright-mcp": "cli.js"}`, `"description": "Playwright Tools for MCP"`, автор Microsoft Corporation, версия 0.0.78. Есть `server.json`, Dockerfile, `index.d.ts` с экспортом `createConnection`.

ВАЖНАЯ ОСОБЕННОСТЬ СНИМКА: этот репозиторий — тонкая обёртка. Реализация сервера в нём отсутствует.
`src/README.md` (весь каталог `src/` состоит из одного этого файла):
> # Where is the source?
>
> Playwright MCP source code is located in the [Playwright monorepo](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/mcp). Please refer to the contributor's guide in [CONTRIBUTING.md](../CONTRIBUTING.md) for more details.

`index.js` целиком (после лицензионной шапки):
```js
const { tools } = require('playwright-core/lib/coreBundle');
module.exports = { createConnection: tools.createConnection };
```

Поэтому конструктор сервера и объявления инструментов физически лежат в зависимости `playwright-core@1.62.0-alpha-...`, которой в снимке нет. Единственный доступный статически носитель дословных описаний — `README.md`, генерируемый скриптом `update-readme.js` напрямую из `tool.schema.description` (см. `formatToolForReadme`, строки 69–96: `lines.push(\`  - Description: ${tool.description}\`)`). То есть тексты в README — машинная копия реальных описаний инструментов, а не пересказ.

## CHANNEL: instructions
(не обнаружены статически)

Grep по всему репозиторию на `instructions|serverInfo|initialize(` даёт только три совпадения, все нерелевантные: CONTRIBUTING.md (про CLA), README.md строка 506 (про установку Chrome-расширения), SECURITY.md (про шаги воспроизведения бага). Ни `new Server(...)`, ни `McpServer`, ни поля `instructions` в снимке нет — они находятся в `playwright-core/lib/coreBundle`, недоступном для статического чтения.

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов, объявленных в сгенерированной секции README: **69** (все с префиксом `browser_`). Категории по `--caps`: Core automation, Tab management, Configuration, Network, Storage, DevTools, Coordinate-based, PDF generation, Test assertions.

### Результат маркер-скана (по всем 69 описаниям + заголовкам)

Единственное совпадение:

- `browser_verify_text_visible` — «Prefer» в: `Verify text is visible on the page. Prefer browser_verify_element_visible if possible.`
  (маршрутизация внутри самого сервера, не против внешних инструментов)

Дополнительно отмечу как содержательно смежное, хотя формальным маркером не поймано (сравнение своего инструмента с чужим/другим способом):
- `browser_snapshot`: «... this is better than screenshot»
- `browser_take_screenshot`: «You can't perform actions based on the screenshot, use browser_snapshot for actions.»
- `browser_network_request` / `browser_network_requests` — взаимные отсылки друг на друга.
- `browser_find`: «... which is cheaper than capturing the whole snapshot when you only need to locate an element and its ref.»

### 10 репрезентативных полных описаний (дословно)

- **browser_navigate** — Title: Navigate to a URL — Description: `Navigate to a URL`
- **browser_snapshot** — Title: Page snapshot — Description: `Capture accessibility snapshot of the current page, this is better than screenshot`
- **browser_take_screenshot** — Title: Take a screenshot — Description: `Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.`
- **browser_find** — Title: Find in page snapshot — Description: `Search the accessibility snapshot of the current page for text or a regular expression. Returns matching snapshot nodes with a few lines of surrounding context (like search snippets), each shown under its path from the root of the tree, which is cheaper than capturing the whole snapshot when you only need to locate an element and its ref.`
- **browser_run_code_unsafe** — Title: Run Playwright code (unsafe) — Description: `Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.`
- **browser_network_requests** — Title: List network requests — Description: `Returns a numbered list of network requests since loading the page. Use browser_network_request with the number to get full details.`
- **browser_route** — Title: Mock network requests — Description: `Set up a route to mock network requests matching a URL pattern`
- **browser_set_storage_state** — Title: Restore storage state — Description: `Restore storage state (cookies, local storage) from a file. This clears existing cookies and local storage before restoring.`
- **browser_annotate** — Title: Annotate the current page — Description: `Open the Playwright Dashboard in annotation mode for the current page and wait for the user to draw annotations. Returns the annotated screenshot, ARIA snapshot, and the list of annotations.`
- **browser_verify_text_visible** — Title: Verify text visible — Description: `Verify text is visible on the page. Prefer browser_verify_element_visible if possible.`

### Полный перечень (name — title — description, дословно)

1. browser_click — Click — `Perform click on a web page`
2. browser_close — Close browser — `Close the page`
3. browser_console_messages — Get console messages — `Returns all console messages`
4. browser_drag — Drag mouse — `Perform drag and drop between two elements`
5. browser_drop — Drop files or data onto an element — `Drop files or MIME-typed data onto an element, as if dragged from outside the page. At least one of "paths" or "data" must be provided.`
6. browser_evaluate — Evaluate JavaScript — `Evaluate JavaScript expression on page or element`
7. browser_file_upload — Upload files — `Upload one or multiple files`
8. browser_fill_form — Fill form — `Fill multiple form fields`
9. browser_find — Find in page snapshot — `Search the accessibility snapshot of the current page for text or a regular expression. Returns matching snapshot nodes with a few lines of surrounding context (like search snippets), each shown under its path from the root of the tree, which is cheaper than capturing the whole snapshot when you only need to locate an element and its ref.`
10. browser_handle_dialog — Handle a dialog — `Handle a dialog`
11. browser_hover — Hover mouse — `Hover over element on page`
12. browser_navigate — Navigate to a URL — `Navigate to a URL`
13. browser_navigate_back — Go back — `Go back to the previous page in the history`
14. browser_network_request — Show network request details — `Returns full details (headers and body) of a single network request, or a single part if \`part\` is set. Use the number from browser_network_requests.`
15. browser_network_requests — List network requests — `Returns a numbered list of network requests since loading the page. Use browser_network_request with the number to get full details.`
16. browser_press_key — Press a key — `Press a key on the keyboard`
17. browser_resize — Resize browser window — `Resize the browser window`
18. browser_run_code_unsafe — Run Playwright code (unsafe) — `Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.`
19. browser_select_option — Select option — `Select an option in a dropdown`
20. browser_snapshot — Page snapshot — `Capture accessibility snapshot of the current page, this is better than screenshot`
21. browser_take_screenshot — Take a screenshot — `Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.`
22. browser_type — Type text — `Type text into editable element`
23. browser_wait_for — Wait for — `Wait for text to appear or disappear or a specified time to pass`
24. browser_tabs — Manage tabs — `List, create, close, or select a browser tab.`
25. browser_get_config — Get config — `Get the final resolved config after merging CLI options, environment variables and config file.`
26. browser_network_state_set — Set network state — `Sets the browser network state to online or offline. When offline, all network requests will fail.`
27. browser_route — Mock network requests — `Set up a route to mock network requests matching a URL pattern`
28. browser_route_list — List network routes — `List all active network routes`
29. browser_unroute — Remove network routes — `Remove network routes matching a pattern (or all routes if no pattern specified)`
30. browser_cookie_clear — Clear cookies — `Clear all cookies`
31. browser_cookie_delete — Delete cookie — `Delete a specific cookie`
32. browser_cookie_get — Get cookie — `Get a specific cookie by name`
33. browser_cookie_list — List cookies — `List all cookies (optionally filtered by domain/path)`
34. browser_cookie_set — Set cookie — `Set a cookie with optional flags (domain, path, expires, httpOnly, secure, sameSite)`
35. browser_localstorage_clear — Clear localStorage — `Clear all localStorage`
36. browser_localstorage_delete — Delete localStorage item — `Delete a localStorage item`
37. browser_localstorage_get — Get localStorage item — `Get a localStorage item by key`
38. browser_localstorage_list — List localStorage — `List all localStorage key-value pairs`
39. browser_localstorage_set — Set localStorage item — `Set a localStorage item`
40. browser_sessionstorage_clear — Clear sessionStorage — `Clear all sessionStorage`
41. browser_sessionstorage_delete — Delete sessionStorage item — `Delete a sessionStorage item`
42. browser_sessionstorage_get — Get sessionStorage item — `Get a sessionStorage item by key`
43. browser_sessionstorage_list — List sessionStorage — `List all sessionStorage key-value pairs`
44. browser_sessionstorage_set — Set sessionStorage item — `Set a sessionStorage item`
45. browser_set_storage_state — Restore storage state — `Restore storage state (cookies, local storage) from a file. This clears existing cookies and local storage before restoring.`
46. browser_storage_state — Save storage state — `Save storage state (cookies, local storage) to a file for later reuse`
47. browser_annotate — Annotate the current page — `Open the Playwright Dashboard in annotation mode for the current page and wait for the user to draw annotations. Returns the annotated screenshot, ARIA snapshot, and the list of annotations.`
48. browser_hide_highlight — Hide element highlight — `Remove a highlight overlay previously added for the element.`
49. browser_highlight — Highlight element — `Show a persistent highlight overlay around the element on the page.`
50. browser_resume — Resume paused script execution — `Resume script execution after it was paused. When called with step set to true, execution will pause again before the next action.`
51. browser_start_tracing — Start tracing — `Start trace recording`
52. browser_start_video — Start video — `Start video recording`
53. browser_stop_tracing — Stop tracing — `Stop trace recording`
54. browser_stop_video — Stop video — `Stop video recording`
55. browser_video_chapter — Video chapter — `Add a chapter marker to the video recording. Shows a full-screen chapter card with blurred backdrop.`
56. browser_video_hide_actions — Hide action overlays — `Stop annotating actions performed on the page.`
57. browser_video_show_actions — Show action overlays — `Annotate subsequent actions performed on the page with a callout that names the action and highlights the target element. Useful while video recording or screencasting.`
58. browser_mouse_click_xy — Click — `Click mouse button at a given position`
59. browser_mouse_down — Press mouse down — `Press mouse down`
60. browser_mouse_drag_xy — Drag mouse — `Drag left mouse button to a given position`
61. browser_mouse_move_xy — Move mouse — `Move mouse to a given position`
62. browser_mouse_up — Press mouse up — `Press mouse up`
63. browser_mouse_wheel — Scroll mouse wheel — `Scroll mouse wheel`
64. browser_pdf_save — Save as PDF — `Save page as PDF`
65. browser_generate_locator — Create locator for element — `Generate locator for the given element to use in tests`
66. browser_verify_element_visible — Verify element visible — `Verify element is visible on the page`
67. browser_verify_list_visible — Verify list visible — `Verify list is visible on the page`
68. browser_verify_text_visible — Verify text visible — `Verify text is visible on the page. Prefer browser_verify_element_visible if possible.`
69. browser_verify_value — Verify value — `Verify element value`

Примечание: `update-readme.js` фильтрует `tool.skillOnly` инструменты (строка 49), поэтому skill-only инструменты, если такие есть в upstream, в этот перечень не попали.
