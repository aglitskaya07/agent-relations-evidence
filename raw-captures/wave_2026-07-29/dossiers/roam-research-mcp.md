# UNIT: roam-research-mcp | npm v2.22.0 (published 2026-06-13T14:21:43.490Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Полноценный MCP-сервер (Roam Research): `new Server(...)` из `@modelcontextprotocol/sdk` в `build/server/roam-server.js`, транспорты stdio + Streamable HTTP, обработчики ListTools/CallTool. Не SDK и не клиент.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `new Server({name, version}, {capabilities})` поле `instructions` не передаётся. Примечание: существует боковой канал — тул `roam_markdown_cheatsheet` возвращает файл `Roam_Markdown_Cheatsheet.md` и ДОКЛЕИВАЕТ к нему содержимое произвольного файла из env `CUSTOM_INSTRUCTIONS_PATH` (tool-handlers.js:120-134). Это инструкции, доставляемые через tool result, а не через initialize.

## CHANNEL: tool descriptions, npm (static, coverage=full)

24 инструмента, все описания дословно (из build/tools/schemas.js):

### roam_add_todo

Add a list of todo items as individual blocks to today's daily page in Roam. Each item becomes its own actionable block with todo status.
NOTE on Roam-flavored markdown: For direct linking: use [[link]] syntax. For aliased linking, use [alias]([[link]]) syntax. Do not concatenate words in links/hashtags - correct: #[[multiple words]] #self-esteem (for typically hyphenated words).
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_fetch_page_by_title

Fetch page by title. Returns content in the specified format.

### roam_create_page

Create a new standalone page in Roam with optional content, including structured outlines and tables, using explicit nesting levels and headings (H1-H3). This is the preferred method for creating a new page with an outline in a single step. Best for:
- Creating foundational concept pages that other pages will link to/from
- Establishing new topic areas that need their own namespace
- Setting up reference materials or documentation
- Making permanent collections of information
- Creating pages with mixed text and table content in one call.
**Efficiency Tip:** This tool batches page and content creation efficiently. For adding content to existing pages, use `roam_process_batch_actions` instead.
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_create_outline

Add a structured outline to an existing page or block (by title text or uid), with customizable nesting levels. To create a new page with an outline, use the `roam_create_page` tool instead. The `outline` parameter defines *new* blocks to be created. To nest content under an *existing* block, provide its UID or exact text in `block_text_uid`, and ensure the `outline` array contains only the child blocks with levels relative to that parent. Including the parent block's text in the `outline` array will create a duplicate block. Best for:
- Adding supplementary structured content to existing pages
- Creating temporary or working outlines (meeting notes, brainstorms)
- Organizing thoughts or research under a specific topic
- Breaking down subtopics or components of a larger concept
Best for simpler, contiguous hierarchical content. For complex nesting (e.g., tables) or granular control over block placement, consider `roam_process_batch_actions` instead.
**API Usage Note:** This tool performs verification queries after creation. For large outlines (10+ items) or when rate limits are a concern, consider using `roam_process_batch_actions` instead to minimize API calls.
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_import_markdown

Import nested markdown content into Roam under a specific block. Can locate the parent block by UID (preferred) or by exact string match within a specific page. If a `parent_string` is provided and the block does not exist, it will be created. Returns a nested structure of the created blocks.
**API Usage Note:** This tool fetches the full nested structure after import for verification. For large imports or when rate limits are a concern, consider using `roam_process_batch_actions` with pre-structured actions instead.
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_search_for_tag

Search for blocks containing a specific tag. Use `primary_tag` for the tag to find, and optionally `page_title_uid` to limit search to a specific page. Supports pagination via `limit` and `offset`. Use this tool to search for memories tagged with the ROAM_MEMORIES_TAG.

### roam_search_by_status

Search for blocks with a specific status (TODO/DONE) across all pages or within a specific page.

### roam_search_block_refs

Search for block references within a page or across the entire graph. Can search for references to a specific block, a page title, or find all block references.

### roam_search_hierarchy

Search for parent or child blocks in the block hierarchy. Can search up or down the hierarchy from a given block.

### roam_find_pages_modified_today

Find pages that have been modified today (since midnight), with pagination and sorting options.

### roam_search_by_text

Search for blocks containing specific text across all pages or within a specific page. Use `scope: "page_titles"` to search for pages by namespace prefix (e.g., "Convention/" finds all pages starting with that prefix). This tool supports pagination via the `limit` and `offset` parameters.

### roam_search_by_date

Search for blocks or pages based on creation or modification dates. Not for daily pages with ordinal date titles.

### roam_markdown_cheatsheet

Provides the comprehensive Roam syntax reference. Covers: formatting, links & references (page refs, block refs, embeds including embed-children and embed-path), tags, dates, tasks, attributes, queries (native and :q Datalog tables with built-in rules), tables, kanban, mermaid diagrams (with theme support), advanced components (dropdowns, tooltips, templates, document mode, word-count), CSS tags (#.rm-E, #.rm-hide, etc.), anti-patterns, tool selection guide, and API efficiency tips.

**IMPORTANT:** Always load this cheatsheet before creating or updating Roam content. It prevents common syntax errors and guides tool selection.

### roam_remember

Add a memory or piece of information to remember, stored on the daily page with ROAM_MEMORIES_TAG tag and optional categories (unless include_memories_tag is false). 
NOTE on Roam-flavored markdown: For direct linking: use [[link]] syntax. For aliased linking, use [alias]([[link]]) syntax. Do not concatenate words in links/hashtags - correct: #[[multiple words]] #self-esteem (for typically hyphenated words).
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_recall

Retrieve all stored memories on page titled ROAM_MEMORIES_TAG, or tagged block content with the same name. Returns a combined, deduplicated list of memories. Optionally filter blocks with a specific tag and sort by creation date.

### roam_datomic_query

Execute a custom Datomic query on the Roam graph for advanced data retrieval beyond the available search tools. This provides direct access to Roam's query engine. Note: Roam graph is case-sensitive.

__Optimal Use Cases for `roam_datomic_query`:__
- __Advanced Filtering (including Regex):__ Use for scenarios requiring complex filtering, including regex matching on results post-query, which Datalog does not natively support for all data types. It can fetch broader results for client-side post-processing.
- __Highly Complex Boolean Logic:__ Ideal for intricate combinations of "AND", "OR", and "NOT" conditions across multiple terms or attributes.
- __Arbitrary Sorting Criteria:__ The go-to for highly customized sorting needs beyond default options.
- __Proximity Search:__ For advanced search capabilities involving proximity, which are difficult to implement efficiently with simpler tools.

List of some of Roam's data model Namespaces and Attributes: ancestor (descendants), attrs (lookup), block (children, heading, open, order, page, parents, props, refs, string, text-align, uid), children (view-type), create (email, time), descendant (ancestors), edit (email, seen-by, time), entity (attrs), log (id), node (title), page (uid, title), refs (text).
Predicates (clojure.string/includes?, clojure.string/starts-with?, clojure.string/ends-with?, <, >, <=, >=, =, not=, !=).
Aggregates (distinct, count, sum, max, min, avg, limit).
Tips: Use :block/parents for all ancestor levels, :block/children for direct descendants only; combine clojure.string for complex matching, use distinct to deduplicate, leverage Pull patterns for hierarchies, handle case-sensitivity carefully, and chain ancestry rules for multi-level queries.

### roam_process_batch_actions

**RATE LIMIT EFFICIENT:** This is the most API-efficient tool for multiple block operations. Combine all create/update/delete operations into a single call whenever possible. For intensive page updates or revisions, prefer this tool over multiple sequential calls.

Executes a sequence of low-level block actions (create, update, move, delete) in a single, non-transactional batch. Actions are executed in the provided order.

**UID Placeholders for Nested Blocks:** Use `{{uid:name}}` syntax for parent-child references within the same batch. The server generates proper random UIDs and returns a `uid_map` showing placeholder→UID mappings. Example: `{ uid: "{{uid:parent1}}", string: "Parent" }` then `{ location: { "parent-uid": "{{uid:parent1}}" }, string: "Child" }`. Response includes `{ success: true, uid_map: { "parent1": "Xk7mN2pQ9" } }`.

For actions on existing blocks, a valid block UID is required. Note: Roam-flavored markdown, including block embedding with `((UID))` syntax, is supported within the `string` property for `create-block` and `update-block` actions. For actions on existing blocks or within a specific page context, it is often necessary to first obtain valid page or block UIDs. Tools like `roam_fetch_page_by_title` or other search tools can be used to retrieve these UIDs before executing batch actions. For simpler, sequential outlines, `roam_create_outline` is often more suitable.
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_fetch_block

Fetch a block by its UID with optional children (down to a specified depth) and/or ancestors (up to page root). Returns the block's UID, text, order, children array, and optionally an ancestors array with the chain to the page root.

### roam_create_table

Create a table in Roam with specified headers and rows. This tool abstracts the complex nested structure that Roam tables require, making it much easier to create properly formatted tables.

**Why use this tool:**
- Roam tables require precise nested block structures that are error-prone to create manually
- Automatically handles the {{[[table]]}} container and nested column structure
- Validates row/column consistency before execution
- Converts empty cells to spaces (required by Roam)

**Example:** A table with headers ["", "Column A", "Column B"] and rows [{label: "Row 1", cells: ["A1", "B1"]}] creates a 2x3 table.
IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_move_block

Move a block to a new location (different parent or position). This is a convenience wrapper around `roam_process_batch_actions` for single block moves.

### roam_update_page_markdown

Update an existing page with new markdown content using smart diff. Preserves block UIDs where possible and generates minimal changes. This is ideal for:
- Syncing external markdown files to Roam
- AI-assisted content updates that preserve references
- Batch content modifications without losing block references

**How it works:**
1. Fetches existing page blocks
2. Matches new content to existing blocks by text similarity
3. Generates minimal create/update/move/delete operations
4. Preserves UIDs for matched blocks (keeping references intact)

IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource.

### roam_fetch_page_full_view

Fetch a complete page view that mirrors what Roam Research shows in its UI: the page's own content, plus all linked references (backlinks) grouped by source page, each with their ancestor breadcrumb context and children expanded to the specified depth. Use this when you need the full picture of a page — both what is written on it and everything else in the graph that references it.

### roam_get_subpages

Fetch all sub-pages (namespace children) of a given page prefix. Matches by page title prefix — pages titled "Prefix/Something" are sub-pages of "Prefix" and appear in the Hierarchy section of that page. This is namespace/title-prefix matching, distinct from roam_search_hierarchy which traverses block parent/child relationships. Optionally filter to only sub-pages containing a specific tag (e.g. filter active projects with filter_tag="active"), and optionally include each sub-page's full block content.

### roam_rename_page

Rename a page by changing its title. Identifies the page by current title or UID.

## MARKER NOTES

Стеринг-паттерны в описаниях (дословно):
- roam_create_page: "This is the preferred method for creating a new page with an outline in a single step. Best for: ..."
- roam_process_batch_actions: "**RATE LIMIT EFFICIENT:** This is the most API-efficient tool for multiple block operations. ... prefer this tool over multiple sequential calls."
- Повторяющийся императив в 7 описаниях: "IMPORTANT: Before using this tool, ensure that you have loaded into context the 'Roam Markdown Cheatsheet' resource."
- roam_markdown_cheatsheet: "**IMPORTANT:** Always load this cheatsheet before creating or updating Roam content."
- roam_remember (параметр parent_uid): "Takes precedence over heading parameter." — техническое, про параметры, не про конкуренцию с другими серверами.
Все паттерны направлены внутрь собственного набора тулов (self-routing); внешнего стеринга (принижения built-in инструментов клиента, "instead of web search" и т.п.) не найдено.
