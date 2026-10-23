# UNIT: playwright-mcp@0.0.78 | npm @playwright/mcp (Microsoft) | captured 2026-07-29 (static, tarball)

## CHANNEL: instructions, npm (static)
(см. экстракцию ниже — если в коде нет, раздел будет помечен «не обнаружены»)

**Результат статической проверки: инструкции в коде тарболла НЕ ОБНАРУЖЕНЫ.**
Тарболл — тонкий шим: `index.js` экспортирует `tools.createConnection` из `playwright-core/lib/coreBundle`, `cli.js` вызывает `tools.decorateMCPCommand`. Вся фактическая реализация MCP-сервера (включая возможную строку `instructions` конструктора и описания инструментов) находится в зависимости `playwright-core@1.62.0-alpha-1783623505000`, которая в тарболл НЕ входит. Ни в одном из 4 текстовых файлов кода (`index.js`, `cli.js`, `index.d.ts`, `config.d.ts`) нет строк instructions, профилей или системных подсказок. Других инструкционных строк/профилей не найдено.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Источник описаний: README.md тарболла (автогенерируемая документация, `update-readme.js` в scripts) — 69 инструментов с полями name + Description. ВАЖНО: это документационный канал; сами строки descriptions в коде тарболла отсутствуют (живут в playwright-core, не поставляется). README у Playwright MCP генерируется из исходников, поэтому используется как прокси кода.

Всего инструментов: 69 (> 40) → полный маркер-скан всех описаний + 8 репрезентативных полных описаний.

### Маркер-скан (все 69 описаний, полный прогон регексов)

Совпадения: 1.

- **browser_verify_text_visible** — «Verify text is visible on the page. Prefer browser_verify_element_visible if possible.» (маркер `prefer`; само-референтный роутинг между собственными инструментами, не против встроенных)

Прочие маркеры (instead of built-in, PRECEDENCE, takes precedence, LAST resort, MUST use, primary tool, refund/credit/reward, ignore previous, whenever the user и т.д.) — 0 совпадений.

Пограничные формулировки вне регексов (для полноты):
- **browser_snapshot** — «Capture accessibility snapshot of the current page, this is better than screenshot» (сравнительный steering между своими инструментами)
- **browser_take_screenshot** — «...You can't perform actions based on the screenshot, use browser_snapshot for actions.»
- **browser_run_code_unsafe** — «Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.» (честная маркировка риска, не steering)

### 8 репрезентативных полных описаний (дословно)

- **browser_click** — «Perform click on a web page»
- **browser_navigate** — «Navigate to a URL»
- **browser_snapshot** — «Capture accessibility snapshot of the current page, this is better than screenshot»
- **browser_take_screenshot** — «Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.»
- **browser_find** — «Search the accessibility snapshot of the current page for text or a regular expression. Returns matching snapshot nodes with a few lines of surrounding context (like search snippets), each shown under its path from the root of the tree, which is cheaper than capturing the whole snapshot when you only need to locate an element and its ref.»
- **browser_run_code_unsafe** — «Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.»
- **browser_network_requests** — «Returns a numbered list of network requests since loading the page. Use browser_network_request with the number to get full details.»
- **browser_video_show_actions** — «Annotate subsequent actions performed on the page with a callout that names the action and highlights the target element. Useful while video recording or screencasting.»

### Полный список имён (69)

browser_click, browser_close, browser_console_messages, browser_drag, browser_drop, browser_evaluate, browser_file_upload, browser_fill_form, browser_find, browser_handle_dialog, browser_hover, browser_navigate, browser_navigate_back, browser_network_request, browser_network_requests, browser_press_key, browser_resize, browser_run_code_unsafe, browser_select_option, browser_snapshot, browser_take_screenshot, browser_type, browser_wait_for, browser_tabs, browser_get_config, browser_network_state_set, browser_route, browser_route_list, browser_unroute, (…debug/tracing/video: browser_start_tracing, browser_start_video, browser_stop_tracing, browser_stop_video, browser_video_chapter, browser_video_hide_actions, browser_video_show_actions…), browser_mouse_click_xy, browser_mouse_down, browser_mouse_drag_xy, browser_mouse_move_xy, browser_mouse_up, browser_mouse_wheel, browser_pdf_save, browser_generate_locator, browser_verify_element_visible, browser_verify_list_visible, browser_verify_text_visible, browser_verify_value и др. — полный перечень в README.md строки 857–1581.

## NOTES (static analysis)

- Код НЕ минифицирован, но тарболл содержит только шим (2 файла JS по ~20-30 строк). Реализация сервера — в неопубликованной в этом тарболле зависимости playwright-core; для полной проверки инструкций initialize нужен отдельный статический разбор playwright-core.
- Риск динамической сборки строк: в самом тарболле нулевой (нет строк вообще); в playwright-core — не оценивался (вне охвата).
- Просмотрено файлов: 7 (все файлы тарболла: index.js, cli.js, index.d.ts, config.d.ts, package.json, README.md, LICENSE).
