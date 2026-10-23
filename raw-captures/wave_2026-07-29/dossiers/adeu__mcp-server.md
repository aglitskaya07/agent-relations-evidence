# UNIT: @adeu/mcp-server | npm v1.30.0 (published 2026-07-24T10:17:31.505Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

Верификация: настоящий MCP-сервер. `new McpServer({ name: "adeu-redlining-service", version: packageVersion })` + `StdioServerTransport` в `src/index.ts` (и идентично в собранном `dist/index.js`). Назначение: редлайнинг DOCX (tracked changes, комментарии, diff, финализация) на движке `@adeu/core`. 5 инструментов (1 через `registerAppTool` c UI-ресурсом, 4 через `server.registerTool`) + 1 UI-ресурс `ui://adeu/markdown-ui`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаются только `name` и `version` — поля `instructions` нет ни в `src/index.ts`, ни в `dist/index.js`. Единственные вхождения слова "instructions" в коде — комментарии разработчика.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Ко ВСЕМ описаниям при регистрации динамически добавляется build-тег: `` [Adeu v${packageVersion}+${gitSha}]`` (обёртки над `registerTool`/`registerAppTool`, src/index.ts:201–227). Значения берутся из env `PACKAGE_VERSION`/`GIT_SHA`, иначе "unknown".

Сквозной паттерн: у каждого из 5 инструментов первый параметр — обязательный `reasoning` с description вида «Why do I need to … ? State this reason before any other parameter.» (значение в хендлерах игнорируется: `void reasoning`). Это подталкивание модели к прото-CoT, не межсерверный steering.

### 1. read_docx (registerAppTool, UI: ui://adeu/markdown-ui)
Description (дословно, READ_DOCX_COMMON_DESC + READ_DOCX_TAIL):

> Reads a DOCX file. Returns text with inline CriticMarkup for Tracked Changes and Comments: {++inserted++}, {--deleted--}, {==highlighted==}{>>comment<<}. Set clean_view=True for the finalized 'Accepted' text without markup.
>
> Modes:
> - 'full' (default): paginated body content. Use page=N to navigate.
> - 'outline': heading map only — start here for large docs to plan targeted reads. Defaults to L1-L2 headings; pass outline_max_level=3-6 to see deeper structure.
> - 'appendix': defined terms, anchors, and cross-reference targets. Consult before editing legal/technical docs to avoid breaking references.
>
> `page`: a positive integer (1-indexed, default 1) or 'all'. Pages are synthetic length-based chunks sized for LLM consumption, NOT printed Word pages. In mode='full', page='all' returns the whole body with no page chrome. With `search_query`, `page` instead restricts matches to that page (default: search all pages).

### 2. process_document_batch
Description (дословно, PROCESS_BATCH_COMMON_DESC + PROCESS_BATCH_OPERATIONS_DESC):

> Applies a batch of edits and review actions to a DOCX.
>
> Batches apply SEQUENTIALLY: each change is validated and applied against the document state produced by the changes before it, so a later change may target text an earlier one introduced. Any validation failure rejects the whole batch transactionally — nothing is applied.
>
> Each item in `changes` needs a `type`:
> 1. 'modify': search-and-replace. `target_text` must match uniquely (`match_mode`:'strict', the default) — add surrounding context, or set `match_mode`:'first'/'all'. Set `regex`:true to treat `target_text` as a regex (capture groups in `new_text` as $1, $2…). `new_text` supports Markdown: '#'–'######' headings, '**bold**', '_italic_', '\n\n' paragraph split; empty `new_text` deletes. Never write CriticMarkup ({++, {--, {>>) manually — use the `comment` field.
>    • EMPTY CELLS: a blank table cell has no text to match; `read_docx` renders every cell with a trailing `{#cell:<id>}` anchor — set `target_text` to that exact anchor and put the value in `new_text`. The pipes are display separators, not editable text.
> 2. 'accept'/'reject': finalize or revert a tracked change by `target_id` (e.g. 'Chg:12').
> 3. 'reply': reply to a comment by `target_id` (e.g. 'Com:5') with `text`.
> 4. 'insert_row': add a table row — `target_text` anchors on an existing row's text, `cells` holds the new row's cell values (strings, left to right), `position` is 'above'/'below' (default below). 'delete_row': remove the row matching `target_text`. Disk mode only.
>
> ID VOLATILITY: 'Chg:N'/'Com:N' ids shift between document states — always call `read_docx` immediately before accept/reject/reply; never reuse ids from earlier turns. `{#cell:<id>}` anchors are stable across reads and edits, but finalize_document/sanitize regenerates them — re-read after finalizing.
>
> `author_name` sets Track Changes attribution; it defaults to 'Adeu AI (TS)' when omitted.

### 3. accept_all_changes
> Accepts all tracked changes and removes all comments in a single operation.

### 4. diff_docx_files
> Compares two DOCX files and returns a compact `@@ Word Patch @@` diff — Adeu's token-level, sub-word patch format — of their text content. Useful for analyzing differences between versions before editing.

### 5. finalize_document
> Prepares a document for external distribution or e-signature. Note: in this zero-dependency environment, protection_mode='encrypt' is unsupported and falls back to a native read-only lock; export_pdf and password are ignored.

## STEERING-ОЦЕНКА
- Межсерверного/межинструментного steering-языка нет: ни "instead of built-in", ни "primary", ни "precedence", ни "prefer over", ни "LAST resort" и т.п. Все императивы ("always call `read_docx` immediately before…", "Never write CriticMarkup … manually", "start here for large docs") — внутрицикловая координация собственных инструментов сервера, не вытеснение чужих.
- Единственный не-функциональный элемент — build-тег в конце каждого description и обязательный параметр `reasoning` («State this reason before any other parameter») на всех 5 инструментах.
- В коде явно закодировано знание о бюджете ~2048 символов на tool description у реальных клиентов (комментарий src/index.ts:176–182) — описания сознательно упакованы под лимит.

## NOTES
- Код не минифицирован: и src/*.ts, и dist/index.js (esbuild/tsup-бандл) читаемы, с комментариями; dist сверен с src — сервер/описания совпадают.
- Динамическая сборка строк: минимальная и наблюдаемая — конкатенация констант описаний + runtime build-тег из env (GIT_SHA/PACKAGE_VERSION). Риск скрытых инъекций в описания низкий.
- Просмотрено: src/index.ts (полностью, 1143 строки), src/shared.ts, package.json, структура dist/ и грепы по dist/index.js; тесты/фикстуры/ассеты просмотрены по списку. Всего в пакете ~40 файлов, содержательно проанализировано 5.
