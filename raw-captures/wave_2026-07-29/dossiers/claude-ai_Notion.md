# UNIT: claude-ai:Notion | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (20 tools, via ToolSearch)

Примечание экстрактора: описания приведены дословно в том виде, в каком их получает агент; у 10 инструментов описание обрезано самим харнессом на маркере «… [truncated]» — обрезка отмечена в тексте.

### tool: notion-create-attachment
Create an attachment and upload it to Notion.

Provide exactly one source:
- content for small UTF-8 text artifacts such as HTML, Markdown, plain text, CSV, JSON, XML, CSS, YAML, TSV, calendar, GPX, or SVG files.
- source_url for a file available at a direct, publicly reachable HTTPS URL. This supports binary files and temporary signed download URLs. Notion performs a metadata-only HEAD request when supported, followed by the GET request that downloads the file. The URL must not redirect, require cookies or request headers, or resolve to a private network address.


The filename must use a supported extension. The optional content_type is a MIME type and must agree with the filename; omit it to infer the type from the extension. Inline content is limited to 200 KiB after UTF-8 encoding. URL downloads must complete within one minute and are limited to 5 MiB for free workspaces and 50 MiB for paid workspaces. For local files, larger files, URLs that redirect, or authenticated downloads requiring headers, use ntn files create or the Notion File Upload API instead.

The response includes a markdown_source value. To place the uploaded file on a page, pass that source to create-pages or update-page. Attach it within one hour: unattached uploads remain temporary and are deleted after they expire. "HTML", "HTML block", "HTML artifact", and "HTML embed" all mean an HTML file placed with <embed src="file-upload://..."> so Notion renders the sandboxed preview. Never place HTML in a code block or file block. Use <file src="file-upload://..."> for other files.

<examples>
1. Create an HTML artifact: {"filename":"report.html","content":"<!doctype html><html><body><h1>Report</h1></body></html>"}
2. Create Markdown with an explicit MIME type: {"filename":"notes.md","content_type":"text/markdown","content":"# Notes\n\nHello"}
3. Import a PDF from a signed URL: {"filename":"report.pdf","source_url":"https://storage.example.com/report.pdf?signature=..."}
</examples>

### tool: notion-create-comment
Add a comment to a page or specific content.

Creates a new comment. Provide `page_id` to identify the page, then choose ONE targeting mode:
- `page_id` alone: Page-level comment on the entire page
- `page_id` + `selection_with_ellipsis`: Comment on specific block content
- `discussion_id`: Reply to an existing discussion thread (page_id is still required)


Provide exactly one content format:
- `markdown`: Preferred. Inline Notion-flavored Markdown for comment text. For exact syntax, read the MCP resource `notion://docs/enhanced-markdown-spec` through your MCP client's resource-reading interface, or call the Notion "fetch" tool with this URI if your client does not support reading MCP resources. Do NOT pass this URI to any other URL-fetching tool. Use only the Rich text types and Mentions syntax that comments support. Comments support inline formatting (bold, italic, strikethrough, underline, code, links), inline math using `$`Equation`$`, and user/page/database/date mention tags such as `<mention-date start="YYYY-MM-DD"/>`. Do not use UI shortcuts like `@today`, `@name`, `[[page]]`, or autocomplete-style emoji syntax; those are editor affordances, not markdown syntax. Mention tags must include a real `url` where required by the spec. Block-level Markdown such as headings, lists, tables, blockquotes, and fenced code blocks is stored as plain comment text rather than rendered as blocks.
- `rich_text`: Array of rich text objects.


For content targeting, use `selection_with_ellipsis` with ~10 chars from start and end: "# Section Ti...tle content"

<example description="Page-level comment">
{"page_id": "uuid", "markdown": "Comment with **important** context."}
</example>
<example description="Comment on specific content">
{"page_id": "uuid", "selection_with_ellipsis": "# Meeting No...es heading",
 "markdown": "Comment on this section."}
</example>
<example description="Reply to discussion">
{"page_id": "uuid", "discussion_id": "discussion://pageId/blockId/discussionId",
 "markdown": "Reply with [context](https://ex… [ОБРЕЗАНО харнессом]

### tool: notion-create-database
Creates a new Notion database using SQL DDL syntax, or a typed database using Notion's canonical schema for tasks, projects, or skills.

Provide exactly one of:
- schema: a CREATE TABLE statement. If no title property is provided, "Name" is auto-added.
- database_type: one of tasks, projects, or skills. The database is created with the canonical required properties and typed metadata used by Notion.


Returns Markdown with schema, SQLite definition, and data source ID in <data-source> tag for use with update_data_source and query_data_sources tools.

Type syntax:
- Simple: TITLE, RICH_TEXT, DATE, PEOPLE, CHECKBOX, URL, EMAIL, PHONE_NUMBER, STATUS, FILES
- SELECT('opt':color, ...) / MULTI_SELECT('opt':color, ...)
- NUMBER [FORMAT 'dollar'] / FORMULA('expression')
- RELATION('data_source_id') — one-way relation
- RELATION('data_source_id', DUAL) — two-way relation
- RELATION('data_source_id', DUAL 'synced_name') — two-way with synced property name
- RELATION('data_source_id', DUAL 'synced_name' 'synced_id') — two-way with synced name and ID (for self-relations)
- ROLLUP('rel_prop', 'target_prop', 'function')
- UNIQUE_ID [PREFIX 'X'] / CREATED_TIME / LAST_EDITED_TIME
- Any column: COMMENT 'description text' Colors: default, gray, brown, orange, yellow, green, blue, purple, pink, red


<example description="Minimal">{"schema": "CREATE TABLE (\"Name\" TITLE)"}</example>
<example description="Tasks">{"database_type": "tasks", "title": "Tasks"}</example>
<example description="With parent and options">{"parent": {"page_id": "f336d0bc-b841-465b-8045-024475c079dd"}, "title": "Projects", "schema": "CREATE TABLE (\"Name\" TITLE, \"Budget\" NUMBER FORMAT 'dollar', \"Tags\" MULTI_SELECT('eng':blue, 'design':pink), \"Task ID\" UNIQUE_ID PREFIX 'PRJ')"}</example>
<example description="Self-relation (two-step: create database first, then use its data source ID with update_data_source to add self-relations)">{"title": "Tasks", "schema": "CREATE TABLE (\"Name\" TITLE, \"Parent\" RELATION('ds_id', DUAL 'Children' 'children'), \"Children\" RELATION(… [ОБРЕЗАНО харнессом]

### tool: notion-create-pages
## Overview

Creates one or more Notion pages, with the specified properties and content.

## Parent

All pages created with a single call to this tool will have the same parent. The parent can be a Notion page ("page_id") or data source ("data_source_id"). If the parent is omitted, the pages are created as standalone, workspace-level private pages, and the person that created them can organize them later as they see fit.

If you have a database URL, ALWAYS pass it to the "fetch" tool first to get the schema and URLs of each data source under the database. You can't use the "database_id" parent type if the database has more than one data source, so you'll need to identify which "data_source_id" to use based on the situation and the results from the fetch tool (data source URLs look like collection://<data_source_id>).

If you know the pages should be created under a data source, do NOT use the database ID or URL under the "page_id" parameter; "page_id" is only for regular, non-database pages.

## Content

Notion page content is a string in Notion-flavored Markdown format.

Don't include the page title at the top of the page's content. Only include it under "properties".

**IMPORTANT**: For the complete Markdown specification, always first read the MCP resource `notion://docs/enhanced-markdown-spec` through your MCP client's resource-reading interface, or call the Notion "fetch" tool with this URI if your client does not support reading MCP resources. Do NOT pass this URI to any other URL-fetching tool. Do NOT guess or hallucinate Markdown syntax. This spec is also applicable to other tools like update-page and fetch.

## Properties

Notion page properties are a JSON map of property names to SQLite values.

When creating pages in a database:
- Use the correct property names from the data source schema shown in the fetch tool results.
- Always include a title property. Data sources always have exactly one title property, but it may not be named "title", so, again, rely on the fetched data source schema.


For pages… [ОБРЕЗАНО харнессом]

### tool: notion-create-view
Create a new view on a Notion database.

Exactly one of "database_id" or "parent_page_id" must be provided:
- "database_id": add a new view tab to an existing database.
- "parent_page_id": create an inline linked database view on a page that references the existing "data_source_id" (like the UI "/linked" command). The linked view block is appended to the end of the parent page.


Use "fetch" first to get the database_id, parent_page_id, and data_source_id (from <data-source> tags in the response). The caller must have edit access to the database (or parent page) and access to the data source.

Supported types: table, board, list, calendar, timeline, gallery, form, chart, map, dashboard.

The optional "configure" param accepts a DSL for filters, sorts, grouping,
and display options. See the notion://docs/view-dsl-spec resource for full
syntax (readable via your MCP client's resource-reading interface, or by
passing the URI to the Notion "fetch" tool). Key directives:
- FILTER "Property" = "value" — filter rows
- SORT BY "Property" ASC — sort rows
- GROUP BY "Property" — group by property (required for board views)
- CALENDAR BY "Property" — date property (required for calendar views)
- TIMELINE BY "Start" TO "End" — date range (required for timeline views)
- MAP BY "Property" — location property (required for map views)
- CHART column|bar|line|donut|number — chart type with optional AGGREGATE, COLOR, HEIGHT, SORT, STACK BY, CAPTION
- FORM CLOSE|OPEN — close/open form submissions
- FORM ANONYMOUS true|false — toggle anonymous submissions
- FORM PERMISSIONS none|reader|editor — set submission permissions
- SHOW "Prop1", "Prop2" — set visible properties
- COVER "Property" — cover image property


<example description="Table view on existing database">{"database_id": "abc123", "data_source_id": "def456", "name": "All Tasks", "type": "table"}</example>
<example description="Board grouped by Status">{"database_id": "abc123", "data_source_id": "def456", "name": "Task Board", "type": "board", "configure": "GROUP BY \"Statu… [ОБРЕЗАНО харнессом]

### tool: notion-download-attachment
Download the contents of a small UTF-8 text attachment created by the Notion MCP `create-attachment` tool.

Pass the `file_upload_id` returned by `create-attachment`. The attachment must belong to the requesting integration, have completed uploading, and use a supported text format such as HTML, Markdown, plain text, CSV, JSON, XML, CSS, YAML, TSV, calendar, GPX, or SVG.

The response contains the complete text in `content` so you can save it locally, edit it, and call `create-attachment` again to upload a new version. Downloads are limited to 200 KiB. This tool does not fetch arbitrary URLs or return binary files. For larger or binary attachments, use the signed file URL returned when reading the containing Notion page.

<examples>
1. Download a text attachment: {"file_upload_id":"12345678-90ab-cdef-1234-567890abcdef"}
</examples>

### tool: notion-duplicate-page
Duplicate a Notion page. The page must be within the current workspace, and you must have permission to access it. The duplication completes asynchronously, so do not rely on the new page identified by the returned ID or URL to be populated immediately. Let the user know that the duplication is in progress and that they can check back later using the 'fetch' tool or by clicking the returned URL and viewing it in the Notion app.

### tool: notion-fetch
Retrieves details about a Notion entity (page, database, or data source) by URL or ID.

Provide URL or ID in `id` parameter. Make multiple calls to fetch multiple entities.

Pages use enhanced Markdown format. For the complete specification, read the MCP resource `notion://docs/enhanced-markdown-spec` through your MCP client's resource-reading interface, or call the Notion "fetch" tool with this URI if your client does not support reading MCP resources. Do NOT pass this URI to any other URL-fetching tool.

Pass a `notion://docs/*` URI (e.g. `notion://docs/enhanced-markdown-spec` or `notion://docs/view-dsl-spec`) as the `id` to read that documentation resource through this tool. The content is identical to the MCP resource of the same URI.

Databases return all data sources (collections). Each data source has a unique ID shown in `<data-source url="collection://...">` tags. You can pass a data source ID directly to this tool to fetch details about that specific data source, including its schema and properties. Use data source IDs with update_data_source and query_data_sources tools. Multi-source databases (e.g., with linked sources) will show multiple data sources.

Set `include_discussions` to true to see discussion counts and inline discussion markers that correlate with the `get_comments` tool. The page output will include a `<page-discussions>` summary tag with discussion count, preview snippets, and `discussion://` URLs that match the discussion IDs returned by `get_comments`.

Pass the special id `"self"` to get the connected workspace and user identity instead of an entity. The result includes a `self` object with the workspace id + name and the authenticated user's id, name, and email. Use this to label the connection (e.g. by workspace name) or obtain a stable id for the connected workspace and user.

On MCP and RunTool surfaces, `self` also includes `current_tool_access`: a map from tool names to `available`, `available_with_limit` (calls can be made up to the limit included with the workspace's plan), `… [ОБРЕЗАНО харнессом]

### tool: notion-get-comments
Get comments and discussions from a Notion page.

Returns discussions with full comment content in XML format. By default, returns page-level discussions only.

Tip: Use the `fetch` tool with `include_discussions: true` first to see where discussions are anchored in the page content, then use this tool to retrieve full discussion threads. The `discussion://` URLs in the fetch output match the discussion IDs returned here.

Parameters:
- `include_all_blocks`: Include discussions on child blocks (default: false)
- `include_resolved`: Include resolved discussions (default: false)
- `discussion_id`: Fetch a specific discussion by ID or URL


<example>{"page_id": "page-uuid"}</example>
<example>{"page_id": "page-uuid", "include_all_blocks": true}</example>
<example>{"page_id": "page-uuid", "discussion_id": "discussion://pageId/blockId/discussionId"}</example>

### tool: notion-move-pages
Move one or more Notion pages or databases to a new parent.

### tool: notion-query-data-sources
Query data from Notion databases using SQL or by specifying a view.

By default, uses SQL mode to execute SQLite queries against one or more data sources. Alternatively, use view mode to execute a database view's existing filters and sorts. Archive selection is supported in view mode only. SQL mode does not accept "is_archived"; SQL archive support is a separate infrastructure follow-up.

Limits: Single-data-source SQL queries have a usage limit on select plans. Queries across multiple data sources require the latest Enterprise plan.

Prerequisites:
1. Use the "fetch" tool first to get database schema and data source URLs
2. Data source URLs are found in <data-source url="..."> tags in fetch results


SQL mode (default):
Execute custom SQLite queries against one or more data sources.
- Use data source URLs as table names in your query
- Supports parameterized queries for security
- Checkbox values: use "__YES__" for checked, "__NO__" for unchecked


Examples:
1. Simple query without explicit mode (defaults to SQL): { "data": { "data_source_urls": ["collection://f336d0bc-b841-465b-8045-024475c079dd"], "query": "SELECT * FROM \"collection://f336d0bc-b841-465b-8045-024475c079dd\" LIMIT 10" } }


2. Query with parameters: { "data": { "mode": "sql", "data_source_urls": ["collection://abc123"], "query": "SELECT * FROM \"collection://abc123\" WHERE Status = ? AND Priority = ?", "params": ["In Progress", "High"] } }


3. Query checkboxes: { "data": { "data_source_urls": ["collection://def456"], "query": "SELECT * FROM \"collection://def456\" WHERE Completed = ?", "params": ["__YES__"] } }


View mode: Execute a specific database view's query with its filters and sorts. Omit "is_archived" or set it to false for non-archived rows. Set "is_archived": true to apply the view inside the archived partition. When the response has "has_more": true, pass its "next_cursor" as "start_cursor" in a follow-up view-mode request with the same "is_archived" value.

Example: { "data": { "mode": "view", "view_url": "https://www.notion.so/workspac… [ОБРЕЗАНО харнессом]

### tool: notion-query-database-view
Query data from a Notion database view.

Executes a database view's existing filters, sorts, and column selections to return matching pages. Use this to query a view exactly as configured. For custom SQL queries, aggregation, or querying across multiple data sources, use query_data_sources instead. By default, it returns non-archived rows only. Set "is_archived": true to query archived rows only.

Prerequisites:
1. Use the "fetch" tool first to get the database and its view URLs
2. View URLs are found in database responses, typically in the format: https://www.notion.so/workspace/db-id?v=view-id


Example: { "view_url": "https://www.notion.so/workspace/Tasks-DB-abc123?v=def456", "is_archived": false }

When the response has "has_more": true, pass its "next_cursor" as "start_cursor" in a follow-up request with the same "is_archived" value.

Common use cases:
- Query databases using pre-defined views (filters/sorts already configured), e.g. look for all tickets marked "In Progress" in a Tasks DB
- Export filtered data for analysis
- Generate reports from database content

### tool: notion-query-meeting-notes
Query the current user's meeting notes data source.

Applies a filter over meeting note properties. Title keyword searching is done via filter on property "title" (e.g. string_contains). Title keyword matching is case-insensitive; capitalization does not matter. Returns up to 50 rows of matching meeting notes.

Prerequisites:
1. Use the "search" tool to find people IDs if you need to filter by attendees


Query building:
- Ignore terms semantically related to meeting outputs (e.g. "summaries", "notes", "todos", "action items", "deliverables"). These signal the user wants outcomes from their meetings, not a title filter.
- For example, "what are my meeting todos?" means filter meetings and find action items — do NOT add a title filter for "todos".
- Only add a title filter when confident the user is targeting a specific meeting title (e.g. "standup", "sprint planning", "1:1 with Alice").
- Generic date phrases like "recent meetings", "latest meetings", "meetings this week", or "yesterday's meetings" should be interpreted as date range filters — never as title filters.
- If a filter returns no results, simplify to a single term. The system is lexical, so multi-word title filters may not match.
- Unless a user explicitly asks about a meeting titled with another user's name, assume they're referring to attendees or creators. Only add a title filter with a person's name as a fallback if attendee filtering returns no results.


Default behavior:
- This tool by default returns meeting notes where the current user is an attendee or creator. There is no need to add a filter for the current user.


Filterable properties:
- "title" (text) — meeting title
- "notion://meeting_notes/attendees" (person) — meeting attendees
- "created_time" (date) — when the meeting note was created
- "created_by" (person) — who created the meeting note
- "last_edited_time" (date) — when the meeting note was last edited
- "last_edited_by" (person) — who last edited the meeting note


Combinator filters use "filters" (not "operands"): { "operator… [ОБРЕЗАНО харнессом]

### tool: notion-search
Search the user's Notion workspace and connected sources (Slack, Google Drive,
GitHub, Jira, Teams, SharePoint, OneDrive, Linear) and return a ranked list
of results to read. Two query types:
- "internal" (default): content across Notion and connected sources.
- "user": find people by name or email.


When to use this vs. get-answer:
- Use search when you want results to read, filter, cite, or fetch in full, or when you'll synthesize across sources yourself.
- Use get-answer when you just want one synthesized answer and don't need the underlying pages. If its answer isn't good enough, come back to search for the full results.


How to search well:
- One question or topic per call. Make separate calls for separate needs.
- If the question names a person, timeframe, teamspace, or database, pass the matching filter. Otherwise omit filters for the broadest recall.
- Keep responses small: set page_size (default 10, max 25) and max_highlight_length (default 200; 0 to omit) as low as you can.
- After finding a Notion result, call fetch with its "id" for full contents.


The backend is auto-selected: AI search when the user has Notion AI and connectors, otherwise faster workspace-only search. Use content_search_mode only when you specifically need one or the other.

To search within a database: fetch the database first to get its data source URL (collection://...) from <data-source url="..."> tags, then pass that as data_source_url. For multi-source databases, match by view ID (?v=...) or search each source. Don't combine a database URL or ID with the collection:// prefix, and don't use a database URL as page_url.

		<example description="Search with date range filter (only documents created in 2024)">
		{
			"query": "quarterly revenue report",
			"query_type": "internal",
			"filters": {
				"created_date_range": {
					"start_date": "2024-01-01",
					"end_date": "2025-01-01"
				}
			}
		}
		</example>

		<example description="Teamspace + creator filter">
		{"query": "project updates", "query_type": "internal", "team… [ОБРЕЗАНО харнессом]

### tool: notion-update-data-source
Update a Notion data source's schema, title, or attributes using SQL DDL statements. Returns Markdown showing updated structure and schema.

Accepts a data source ID (collection ID from fetch response's <data-source> tag) or a single-source database ID. Multi-source databases require the specific data source ID.

The statements param accepts semicolon-separated DDL statements:
- ADD COLUMN "Name" <type> - add a new property
- DROP COLUMN "Name" - remove a property
- RENAME COLUMN "Old" TO "New" - rename a property
- ALTER COLUMN "Name" SET <type> - change type/options


Same type syntax as create_database. Key types:
- SELECT('opt':color, ...) / MULTI_SELECT('opt':color, ...)
- NUMBER [FORMAT 'dollar'] / FORMULA('expression')
- RELATION('ds_id') / RELATION('ds_id', DUAL) / RELATION('ds_id', DUAL 'synced_name' 'synced_id')
- ROLLUP('rel_prop', 'target_prop', 'function') / UNIQUE_ID [PREFIX 'X']
- Simple: TITLE, RICH_TEXT, DATE, PEOPLE, CHECKBOX, URL, EMAIL, PHONE_NUMBER, STATUS, FILES


<example description="Add properties">{"data_source_id": "f336d0bc-b841-465b-8045-024475c079dd", "statements": "ADD COLUMN \"Priority\" SELECT('High':red, 'Medium':yellow, 'Low':green); ADD COLUMN \"Due Date\" DATE"}</example>
<example description="Rename property">{"data_source_id": "f336d0bc-b841-465b-8045-024475c079dd", "statements": "RENAME COLUMN \"Status\" TO \"Project Status\""}</example>
<example description="Remove property">{"data_source_id": "f336d0bc-b841-465b-8045-024475c079dd", "statements": "DROP COLUMN \"Old Property\""}</example>
<example description="Add self-relation">{"data_source_id": "f336d0bc-b841-465b-8045-024475c079dd", "statements": "ADD COLUMN \"Parent\" RELATION('f336d0bc-b841-465b-8045-024475c079dd', DUAL 'Children' 'children'); ADD COLUMN \"Children\" RELATION('f336d0bc-b841-465b-8045-024475c079dd', DUAL 'Parent' 'parent')"}</example>
<example description="Update title">{"data_source_id": "f336d0bc-b841-465b-8045-024475c079dd", "title": "Project Tracker 2024"}</example>
<example description="Trash data source">{"dat… [ОБРЕЗАНО харнессом]

### tool: notion-update-page
## Overview

Update a Notion page's properties or content.

## Properties

Notion page properties are a JSON map of property names to SQLite values.

For pages in a database:
- ALWAYS use the "fetch" tool first to get the data source schema and the	exact property names.
- Provide a non-null value to update a property's value.
- Omitted properties are left unchanged.


**IMPORTANT**: Some property types require specific formats:
- Date properties: Split into "date:{property}:start", "date:{property}:end" (optional), and "date:{property}:is_datetime" (0 or 1)
- Place properties: Split into "place:{property}:name", "place:{property}:address", "place:{property}:latitude", "place:{property}:longitude", and "place:{property}:google_place_id" (optional)
- Number properties: Use JavaScript numbers (not strings)
- Checkbox properties: Use "__YES__" for checked, "__NO__" for unchecked
- Relation properties: Use an array of related page URLs or page IDs, e.g. ["https://www.notion.so/26ab1f9f4c5f80b18d3bd10a6b1d2f4e", "26ab1f9f-4c5f-80b1-8d3b-d10a6b1d2f4e"]


**Special property naming**: Properties named "id" or "url" (case insensitive) must be prefixed with "userDefined:" (e.g., "userDefined:URL", "userDefined:id")

For pages outside of a database:
- The only allowed property is "title",	which is the title of the page in inline markdown format.


## Content

Notion page content is a string in Notion-flavored Markdown format.

**IMPORTANT**: For the complete Markdown specification, first read the MCP resource `notion://docs/enhanced-markdown-spec` through your MCP client's resource-reading interface, or call the Notion "fetch" tool with this URI if your client does not support reading MCP resources. Do NOT pass this URI to any other URL-fetching tool. Do NOT guess or hallucinate Markdown syntax.

For small edits, send the smallest edit region that captures the intended change. Prefer "update_content" for targeted search-and-replace edits, or "insert_content" when you only need to prepend or append content. Avoid full-page "r… [ОБРЕЗАНО харнессом]

### tool: notion-update-view
Update a view's name, filters, sorts, or display configuration.

Use "fetch" to get view IDs from database responses. Only include fields
you want to change. The "configure" param uses the same DSL as create_view.
Use CLEAR to remove settings:
- CLEAR FILTER — remove all filters
- CLEAR SORT — remove all sorts
- CLEAR GROUP BY — remove grouping


See notion://docs/view-dsl-spec resource for full syntax (readable via your MCP client's resource-reading interface, or by passing the URI to the Notion "fetch" tool).

<example description="Rename">{"view_id": "abc123", "name": "Sprint Board"}</example>
<example description="Update filter">{"view_id": "abc123", "configure": "FILTER \"Status\" = \"Done\""}</example>
<example description="Clear filter, add sort">{"view_id": "abc123", "configure": "CLEAR FILTER; SORT BY \"Created\" DESC"}</example>
<example description="Update grouping">{"view_id": "abc123", "configure": "GROUP BY \"Priority\"; SHOW \"Name\", \"Status\""}</example>

### tool: notion-get-async-task
Retrieves the current status of an async task that was started by another tool (for example, "create_pages" called with "allow_async": true).

The status is one of "queued", "running", "retrying", "succeeded", or "failed". When the task has succeeded, the operation's result is included; when it has failed, an error is included instead.

Poll this tool with the "task_id" from the original tool's "async_task" response. Wait briefly between polls — the original response includes a suggested backoff.

<examples>
1. Check a task's status: {"task_id": "task_abc123"}
</examples>

### tool: notion-get-teams
Retrieves a list of teams (teamspaces) in the current workspace. Shows which teams exist, user membership status, IDs, names, and roles.

Teams are returned split by membership status and limited to a maximum of 10 results.

<examples>
1. List all teams (up to the limit of each type): {}

2. Search for teams by name: {"query": "engineering"}

3. Find a specific team: {"query": "Product Design"}
</examples>

### tool: notion-get-users
Retrieves a list of users in the current workspace. Shows workspace members and guests with their IDs, names, emails (if available), and types (person or bot).

Supports cursor-based pagination to iterate through all users in the workspace.

<examples>
1. List all users (first page): {}

2. Search for users by name or email: {"query": "john"}

3. Get next page of results: {"start_cursor": "abc123"}

4. Set custom page size: {"page_size": 20}

5. Fetch a specific user by ID: {"user_id": "00000000-0000-4000-8000-000000000000"}

6. Fetch the current user: {"user_id": "self"}
</examples>
