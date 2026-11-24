# UNIT: @adeu/mcp-server | npm v1.30.0 (published 2026-07-24T10:17:31.505Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

Verification: a real MCP server. `new McpServer({ name: "adeu-redlining-service", version: packageVersion })` + `StdioServerTransport` in `src/index.ts` (and identically in the built `dist/index.js`). Purpose: redlining DOCX (tracked changes, comments, diff, finalization) on the `@adeu/core` engine. 5 tools (1 via `registerAppTool` with a UI resource, 4 via `server.registerTool`) + 1 UI resource `ui://adeu/markdown-ui`.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name` and `version` are passed to the `McpServer` constructor — there is no `instructions` field in `src/index.ts` or in `dist/index.js`. The only occurrences of the word "instructions" in the code are developer comments.

## CHANNEL: tool descriptions, npm (static, coverage=full)

A build tag is dynamically added to ALL descriptions at registration: `` [Adeu v${packageVersion}+${gitSha}]`` (wrappers around `registerTool`/`registerAppTool`, src/index.ts:201–227). Values are taken from env `PACKAGE_VERSION`/`GIT_SHA`, otherwise "unknown".

End-to-end pattern: for each of the 5 tools, the first parameter is a required `reasoning` with a description like "Why do I need to … ? State this reason before any other parameter." (the value is ignored in handlers: `void reasoning`). This nudges the model toward proto-CoT, not inter-server steering.

### 1. read_docx (registerAppTool, UI: ui://adeu/markdown-ui)
Description (verbatim, READ_DOCX_COMMON_DESC + READ_DOCX_TAIL):

> Reads a DOCX file. Returns text with inline CriticMarkup for Tracked Changes and Comments: {++inserted++}, {--deleted--}, {==highlighted==}{>>comment<<}. Set clean_view=True for the finalized 'Accepted' text without markup.
>
> Modes:
> - 'full' (default): paginated body content. Use page=N to navigate.
> - 'outline': heading map only — start here for large docs to plan targeted reads. Defaults to L1-L2 headings; pass outline_max_level=3-6 to see deeper structure.
> - 'appendix': defined terms, anchors, and cross-reference targets. Consult before editing legal/technical docs to avoid breaking references.
>
> `page`: a positive integer (1-indexed, default 1) or 'all'. Pages are synthetic length-based chunks sized for LLM consumption, NOT printed Word pages. In mode='full', page='all' returns the whole body with no page chrome. With `search_query`, `page` instead restricts matches to that page (default: search all pages).

### 2. process_document_batch
Description (verbatim, PROCESS_BATCH_COMMON_DESC + PROCESS_BATCH_OPERATIONS_DESC):

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

## STEERING-ASSESSMENT
- There is no inter-server/inter-tool steering language: neither "instead of built-in", nor "primary", nor "precedence", nor "prefer over", nor "LAST resort", etc. All imperatives ("always call `read_docx` immediately before…", "Never write CriticMarkup … manually", "start here for large docs") are within-cycle coordination of the server's own tools, not displacing another tool.
- The only non-functional element is the build tag at the end of each description and the mandatory `reasoning` parameter ("State this reason before any other parameter") on all 5 tools.
- The code explicitly encodes knowledge of a budget of about 2048 characters for a tool description in real clients (comment in src/index.ts:176–182) — descriptions are deliberately packed to fit the limit.

## NOTES
- The code is not minified: both src/*.ts and dist/index.js (esbuild/tsup bundle) are readable, with comments; dist was compared with src — server/descriptions match.
- Dynamic construction of strings: minimal and observable — concatenation of constant descriptions + runtime build tag from env (GIT_SHA/PACKAGE_VERSION). Risk of hidden injections into descriptions is low.
- Reviewed: src/index.ts (in full, 1143 lines), src/shared.ts, package.json, structure of dist/ and greps over dist/index.js; tests/fixtures/assets were reviewed by list. In total there are ~40 files in the package, 5 were substantively analyzed.
