# UNIT: safari-mcp | npm v2.15.11 (published 2026-07-29T07:15:00.895Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Настоящий MCP-сервер: `index.js` строит `new McpServer({ name: "safari-mcp", version, description })` в фабрике `buildServer()` (строка 795), регистрирует 97 инструментов через `server.tool(...)`, транспорты stdio и HTTP (`transport.js`). Автоматизация Safari через AppleScript-хелпер (`safari-helper.swift`, бинарник `safari-helper`) + Safari-расширение (`extension/`).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор `McpServer` получает только `name`, `version`, `description` ("Safari browser automation - lightweight, keeps logins"). Поля `instructions` нет нигде в пакете (grep по всем .js/.json — единственное вхождение слова — комментарий в transport.js:33).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Всего инструментов: 97 (все имена уникальны, все описания — строковые литералы, извлечены 97/97).

### Маркер-скан: совпадения (дословно)

**safari_snapshot** — маркеры `prefer(red)`, `Prefer this over`:
> PREFERRED way to see page state. Returns accessibility tree with ref IDs for every interactive element. Use refs with click/fill/type instead of CSS selectors. Workflow: snapshot → see refs → click({ref:'0_5'}). PREFER THIS over safari_screenshot (cheaper, structured text vs heavy image) and over safari_read_page (includes interactive refs). Use safari_screenshot only when you need to see visual layout/styling.

**safari_read_page** — маркер `prefer(red)`:
> Read page text content (title, URL, body text). Use for reading article text or page content. For interacting with elements, prefer safari_snapshot (gives ref IDs). Use selector to read specific element. Use maxLength to limit output.

**safari_type_text** — маркер `Best for:`:
> Type text character-by-character with realistic key events. Best for: search boxes (triggers autocomplete), chat inputs, and fields that react to each keystroke. For rich text editors (Medium, HackerNoon, LinkedIn), use safari_fill instead — it uses framework-native APIs. For code editors (Monaco/CodeMirror), use safari_replace_editor. When using ref, always take a FRESH safari_snapshot first — refs expire after each new snapshot.

**safari_reload_extension** — маркер `prefer(red)` (ложноположительный: слово "Preferences" в UI-пути Safari):
> Hot-reload the Safari MCP Bridge extension — forces it to reload its own code from disk without requiring manual Safari Preferences → Extensions → toggle. Use after editing extension/background.js or extension/content.js in the safari-mcp repo. The extension briefly disconnects during reload and auto-reconnects within ~2 seconds. NOTE: this tool itself requires the extension version already installed to support the `reload_extension` command (added in v2.9.1+). If your extension is older, trigger a manual reload once to pick up this feature.

**safari_evaluate** — маркер `prefer(red)`:
> Execute JavaScript in the current page. Automatically falls back to AppleScript when CSP blocks execution (e.g. Google Search Console, LinkedIn). For reading data, prefer safari_read_page or safari_snapshot. For interactions, prefer safari_click/fill with refs.

**safari_wait** — маркер `prefer(red)`:
> Wait for a fixed time in milliseconds. Use only when you need a brief pause between actions. PREFER safari_wait_for (waits for element/text to appear) — it's smarter and doesn't waste time.

**safari_accessibility_snapshot** — маркер `essential for`:
> Get the accessibility tree of the page (roles, ARIA labels, focusable elements, form states). Essential for a11y auditing.

**safari_extract_tables** — маркер `Perfect for`:
> Extract HTML tables as structured JSON (headers + rows). Perfect for scraping data tables.

**safari_detect_forms** — маркер `Great for`:
> Auto-detect all forms on the page with their fields, types, selectors, and submit buttons. Great for automated form filling.

**safari_analyze_page** — маркер `Perfect for`:
> Full page analysis in ONE call: title, URL, meta tags, OG, headings, link stats, image stats, forms, and text preview. Perfect for SEO/audit.

Замечание по характеру маркеров: все совпадения — внутрисерверная маршрутизация (какой из СВОИХ инструментов дешевле/уместнее), а не вытеснение чужих инструментов или built-in возможностей хоста. Маркеры классов "instead of built-in", "takes precedence", "LAST resort", "The user has installed", "primary interface", "MUST use", "ignore previous", "refund/credit" — совпадений НЕТ.

### 8 репрезентативных полных описаний

**safari_navigate**
> Navigate to a URL in Safari. Waits for page to fully load.

**safari_snapshot**
> PREFERRED way to see page state. Returns accessibility tree with ref IDs for every interactive element. Use refs with click/fill/type instead of CSS selectors. Workflow: snapshot → see refs → click({ref:'0_5'}). PREFER THIS over safari_screenshot (cheaper, structured text vs heavy image) and over safari_read_page (includes interactive refs). Use safari_screenshot only when you need to see visual layout/styling.

**safari_navigate_and_read**
> Navigate to a URL and return the page content in one step — saves 1 full round-trip vs navigate+read_page. Use instead of safari_navigate + safari_read_page.

**safari_click**
> Click element. Use ref (from snapshot), selector, text, or x/y. Works on React/Airtable/virtual DOM apps via full PointerEvent+MouseEvent sequence + React Fiber fallback. Pure JS — never touches user's mouse. When using ref, always take a FRESH safari_snapshot first — refs expire after each new snapshot.

**safari_fill**
> Fill/replace value in an input, textarea, select, OR contenteditable (rich text). Handles React controlled inputs, ProseMirror, Draft.js, and Google Closure editors automatically. Use for SETTING a value (replaces existing). For code editors (Monaco/CodeMirror/Ace), use safari_replace_editor instead. For character-by-character typing in search boxes, use safari_type_text. IMPORTANT: When using ref, always take a FRESH safari_snapshot first — refs expire after each new snapshot (prefix changes: 5_xx → 6_xx).

**safari_screenshot**
> Take a visual screenshot (base64 JPEG). EXPENSIVE — use safari_snapshot instead for most tasks. Only use screenshot when you need to verify visual layout, styling, images, or colors that snapshot can't show.

**safari_evaluate**
> Execute JavaScript in the current page. Automatically falls back to AppleScript when CSP blocks execution (e.g. Google Search Console, LinkedIn). For reading data, prefer safari_read_page or safari_snapshot. For interactions, prefer safari_click/fill with refs.

**safari_analyze_page**
> Full page analysis in ONE call: title, URL, meta tags, OG, headings, link stats, image stats, forms, and text preview. Perfect for SEO/audit.

## NOTES (методология)

- Код НЕ минифицирован: читаемый исходник с комментариями (index.js 103 KB, safari.js 281 KB).
- Риск динамической сборки строк описаний: низкий. Все 97 вызовов `server.tool()` имеют описание строковым/шаблонным литералом; regex извлёк ровно 97/97, счёт совпадает с `grep -c "server.tool("`.
- Файлы просмотрены: index.js (детально), transport.js, package.json, mcp-helpers.js (grep), остальные .js/.json — grep-скан по слову instructions; всего в пакете ~20 файлов.
- Дамп всех 97 пар name+description: scratchpad/wave/tools_safari.json.
