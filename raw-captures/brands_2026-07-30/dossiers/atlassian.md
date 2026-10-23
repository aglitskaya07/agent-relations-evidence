# UNIT: atlassian | Atlassian (Jira/Confluence) | github sooperset/mcp-atlassian | тип автора: комьюнити | captured 2026-07-29 (static source)

Это MCP-сервер: Python, FastMCP. Композитный сервер `AtlassianMCP` (src/mcp_atlassian/servers/main.py:885) монтирует два под-сервера: `jira_mcp` (namespace="jira") и `confluence_mcp` (namespace="confluence"). Имена инструментов клиенту отдаются с префиксом неймспейса (jira_*, confluence_*).

## CHANNEL: instructions (52 chars + 58 chars)

Корневой сервер `main_mcp = AtlassianMCP(name="Atlassian MCP", lifespan=..., auth=...)` — параметр instructions НЕ задан.

Под-сервер Jira (src/mcp_atlassian/servers/jira.py:50-53), instructions (52 chars):

```
Provides tools for interacting with Atlassian Jira.
```

Под-сервер Confluence (src/mcp_atlassian/servers/confluence.py:182-185), instructions (58 chars):

```
Provides tools for interacting with Atlassian Confluence.
```

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов найдено статически: 98 (63 jira + 35 confluence). Определения — декораторы `@jira_mcp.tool(...)` / `@confluence_mcp.tool(...)`; description берётся из docstring функции (параметр description= в декораторах не используется, задаются только tags и annotations{title, readOnlyHint, destructiveHint}).

### Полный маркер-скан всех 98 описаний

Прогон всех регексов задания (case-insensitive) по полным текстам всех 98 описаний: **0 совпадений**. Дополнительная контрольная grep-проверка по подстрокам prefer / best for / great for / perfect for / essential / precedence / must use / immediately / memory по обоим файлам целиком дала только нейтральные технические вхождения, не относящиеся к описаниям инструментов как рулевые формулировки:

- jira.py:586 (описание параметра fields): "Use '*all' for all fields (including custom fields), or omit for essential fields only."
- jira.py:1728 (описание параметра): "Never assume what it might be, always ask the user."
- jira.py:2091 (описание параметра): "thousands of tokens. The issue 'key' is always returned regardless. "
- jira.py:3339 / jira.py:3427: "Project keys are always returned in uppercase."
- jira.py:3789: "If true, fail immediately when raiseOnBehalfOf cannot be applied. "

### Полный список имён инструментов

**jira** (63): jira_get_user_profile, jira_search_assignable_users, jira_get_issue_watchers, jira_add_watcher, jira_remove_watcher, jira_get_issue, jira_search, jira_search_fields, jira_get_field_options, jira_get_project_issues, jira_get_transitions, jira_get_worklog, jira_download_attachments, jira_get_issue_images, jira_get_agile_boards, jira_get_board_issues, jira_get_sprints_from_board, jira_get_sprint_issues, jira_get_link_types, jira_create_issue, jira_batch_create_issues, jira_batch_get_changelogs, jira_update_issue, jira_assign_issue, jira_delete_issue, jira_move_issue, jira_add_comment, jira_edit_comment, jira_add_worklog, jira_link_to_epic, jira_create_issue_link, jira_create_remote_issue_link, jira_remove_issue_link, jira_transition_issue, jira_create_sprint, jira_update_sprint, jira_add_issues_to_sprint, jira_move_issues_to_backlog, jira_get_project_issue_types, jira_get_create_fields, jira_get_project_versions, jira_get_project_components, jira_get_all_projects, jira_search_projects, jira_get_project_fields, jira_get_service_desk_for_project, jira_get_service_desk_queues, jira_get_queue_issues, jira_get_request_types, jira_get_request_type_fields, jira_create_customer_request, jira_create_version, jira_batch_create_versions, jira_update_version, jira_get_issue_proforma_forms, jira_get_proforma_form_details, jira_update_proforma_form_answers, jira_get_issue_dates, jira_get_issue_sla, jira_get_issue_development_info, jira_get_issues_development_info, jira_get_project_epic_hierarchy, jira_get_cross_project_dependencies

**confluence** (35): confluence_search, confluence_get_page, confluence_get_page_children, confluence_get_space_page_tree, confluence_get_comments, confluence_get_labels, confluence_add_label, confluence_create_page, confluence_update_page, confluence_update_page_section, confluence_delete_page, confluence_move_page, confluence_add_comment, confluence_reply_to_comment, confluence_get_inline_comments, confluence_add_inline_comment, confluence_search_user, confluence_get_page_history, confluence_get_page_diff, confluence_get_page_views, confluence_upload_attachment, confluence_upload_attachments, confluence_get_attachments, confluence_download_attachment, confluence_download_content_attachments, confluence_delete_attachment, confluence_get_page_images, confluence_list_page_templates, confluence_get_page_template, confluence_create_page_from_template, confluence_get_page_restrictions, confluence_set_page_restrictions, confluence_copy_page, confluence_check_content_permissions, confluence_get_space_permissions

### 10 репрезентативных полных описаний (дословно)

#### jira_search

```
Search Jira issues using JQL (Jira Query Language).

Args:
    ctx: The FastMCP context.
    jql: JQL query string.
    fields: Comma-separated fields to return.
    limit: Maximum number of results.
    start_at: Starting index for pagination.
    projects_filter: Comma-separated list of project keys to filter by.
    expand: Optional fields to expand.
    page_token: Pagination token from a previous search result (Cloud only).
    use_display_names: Opt into human-readable custom field keys.

Returns:
    JSON string representing the search results including pagination info.
```

#### jira_get_issue

```
Get details of a specific Jira issue.

Includes Epic links and relationship information. Use the
``include`` parameter to inline enrichments (remote_links,
transitions, watchers, changelog, comments, worklogs) so that
separate tool calls are not needed.

Args:
    ctx: The FastMCP context.
    issue_key: Jira issue key.
    fields: Comma-separated fields to return.
    expand: Optional fields to expand.
    comment_limit: Maximum number of comments.
    properties: Issue properties to return.
    update_history: Whether to update issue view history.
    include: Comma-separated enrichment sections to inline.
    use_display_names: Opt into human-readable custom field keys.

Returns:
    JSON string representing the Jira issue object.

Raises:
    ValueError: If the Jira client is not configured.
```

#### jira_create_issue

```
Create a new Jira issue with optional Epic link or parent for subtasks.

Args:
    ctx: The FastMCP context.
    project_key: The JIRA project key.
    summary: Summary/title of the issue.
    issue_type: Issue type (e.g., 'Task', 'Bug', 'Story', 'Epic', 'Subtask').
    assignee: Assignee's user identifier (string): Email, display name, or account ID (e.g., 'user@example.com', 'John Doe', 'accountid:...').
    description: Issue description in Markdown format.
    components: Comma-separated list of component names.
    additional_fields: JSON string of additional fields.

Returns:
    JSON string representing the created issue object.

Raises:
    ValueError: If in read-only mode or Jira client is unavailable.
```

#### jira_update_issue

```
Update an issue and optionally transition, comment, and log work.

Args:
    ctx: The FastMCP context.
    issue_key: Jira issue key.
    fields: Optional JSON string of fields to update. Text fields like
        'description' should use Markdown format.
    additional_fields: Optional JSON string of additional fields.
    components: Comma-separated list of component names.
    attachments: Optional JSON array string or comma-separated list of file paths.
    transition: Optional transition name or ID.
    comment: Optional issue comment in Markdown format.
    comment_visibility: Optional JSON string restricting comment visibility.
    worklog: Optional time spent to log.
    worklog_started: Optional ISO datetime when the worklog started.
    return_fields: Fields to include in the returned issue. Comma-separated list to trim the response and save tokens, or '*all' (default) for the full issue.

Returns:
    JSON string representing the updated issue object and attachment results.

Raises:
    ValueError: If in read-only mode or Jira client unavailable, or invalid input.
```

#### jira_get_issue_sla

```
Calculate SLA metrics for a Jira issue.

Computes various time-based metrics including cycle time, lead time,
time spent in each status, due date compliance, and more.

Working hours can be configured via environment variables:
- JIRA_SLA_WORKING_HOURS_ONLY: Enable working hours filtering (true/false)
- JIRA_SLA_WORKING_HOURS_START: Start time (e.g., "09:00")
- JIRA_SLA_WORKING_HOURS_END: End time (e.g., "17:00")
- JIRA_SLA_WORKING_DAYS: Working days (e.g., "1,2,3,4,5" for Mon-Fri)
- JIRA_SLA_TIMEZONE: Timezone for calculations (e.g., "America/New_York")

Args:
    ctx: The FastMCP context.
    issue_key: The Jira issue key.
    metrics: Comma-separated list of metrics to calculate.
    working_hours_only: Use working hours only for calculations.
    include_raw_dates: Include raw date values in response.

Returns:
    JSON string with calculated SLA metrics.
```

#### jira_update_proforma_form_answers

```
Update form field answers using the Jira Forms REST API.

This is the primary method for updating form data. Each answer object
must specify the question ID, answer type, and value.

**⚠️ KNOWN LIMITATION - DATETIME fields:**
The Jira Forms API does NOT properly preserve time components in DATETIME fields.
Only the date portion is stored; times are reset to midnight (00:00:00).

**Workaround for DATETIME fields:**
Use jira_update_issue to directly update the underlying custom fields instead:
1. Get the custom field ID from the form details (question's "jiraField" property)
2. Use jira_update_issue with fields like: {"customfield_XXXXX": "2026-01-09T11:50:00-08:00"}

Example:
```python
# Instead of updating via form (loses time):
# jira_update_proforma_form_answers(issue_key, form_id, [{"questionId": "91", "type": "DATETIME", "value": "..."}])

# Use direct field update (preserves time):
jira_update_issue(issue_key, {"customfield_10542": "2026-01-09T11:50:00-08:00"})
```

**Automatic DateTime Conversion:**
For DATE and DATETIME fields, you can provide values as:
- ISO 8601 strings (e.g., "2024-12-17T19:00:00Z", "2024-12-17")
- Unix timestamps in milliseconds (e.g., 1734465600000)

The tool automatically converts ISO 8601 strings to Unix timestamps.

Example answers:
[
    {"questionId": "q1", "type": "TEXT", "value": "Updated description"},
    {"questionId": "q2", "type": "SELECT", "value": "Product A"},
    {"questionId": "q3", "type": "NUMBER", "value": 42},
    {"questionId": "q4", "type": "DATE", "value": "2024-12-17"}
]

Common answer types:
- TEXT: String values
- NUMBER: Numeric values
- DATE: Date values (ISO 8601 string or Unix timestamp in ms)
- DATETIME: DateTime values - ⚠️ USE WORKAROUND ABOVE
- SELECT: Single selection from options
- MULTI_SELECT: Multiple selections (value as list)
- CHECKBOX: Boolean values

Args:
    ctx: The FastMCP context.
    issue_key: The issue key containing the form.
    form_id: The form UUID (get from get_issue_proforma_forms).
    answers: List of answer objects with questionId, type, and value.

Returns:
    JSON string with operation result.
```

#### confluence_search

```
Search Confluence content using simple terms or CQL.

Args:
    ctx: The FastMCP context.
    query: Search query - can be simple text or a CQL query string.
    limit: Maximum number of results (1-50).
    spaces_filter: Comma-separated list of space keys to filter by.

Returns:
    JSON string representing a list of simplified Confluence page objects.
```

#### confluence_create_page

```
Create a new Confluence page.

Args:
    ctx: The FastMCP context.
    space_key: The key of the space.
    title: The title of the page.
    content: The content of the page (format depends on content_format).
        Mutually exclusive with content_file; exactly one must be
        supplied.
    content_file: Filesystem path to read the page body from (UTF-8).
        Useful for bodies too large to pass as an inline tool argument.
    parent_id: Optional parent page ID.
    content_format: The format of the content ('markdown', 'wiki',
        'storage', or 'xhtml').
    enable_heading_anchors: Whether to enable heading anchors (markdown only).
    include_content: Whether to include page content in the response.
    emoji: Optional page title emoji (icon shown in navigation).
    page_width: Optional page layout width ('full-width' or 'default').
    table_layout: Optional table width preset ('full-width', 'wide', 'default').
    subtype: Optional page subtype. Use "live" to create a Confluence Live Doc.

Returns:
    JSON string representing the created page object.

Raises:
    ValueError: If in read-only mode, Confluence client is unavailable, or invalid content_format.
```

#### confluence_update_page

```
Update an existing Confluence page.

Args:
    ctx: The FastMCP context.
    page_id: The ID of the page to update.
    title: The new title of the page.
    content: The new content of the page (format depends on
        content_format). Mutually exclusive with content_file; exactly
        one must be supplied.
    content_file: Filesystem path to read the new page body from
        (UTF-8). Useful for bodies too large to pass as an inline tool
        argument.
    is_minor_edit: Whether this is a minor edit.
    version_comment: Optional comment for this version.
    parent_id: Optional new parent page ID.
    content_format: The format of the content ('markdown', 'wiki',
        'storage', or 'xhtml').
    enable_heading_anchors: Whether to enable heading anchors (markdown only).
    include_content: Whether to include page content in the response.
    emoji: Optional page title emoji (icon shown in navigation).
    page_width: Optional page layout width ('full-width' or 'default').
    table_layout: Optional table width preset ('full-width', 'wide', 'default').

Returns:
    JSON string representing the updated page object.

Raises:
    ValueError: If Confluence client is not configured, available, or invalid content_format.
```

#### confluence_get_attachments

```
List all attachments for a Confluence content item (page or blog post).

Returns metadata about attachments including:
- Attachment ID, title, and file type
- File size and download URL
- Creation/modification dates
- Version information

**Important**: Confluence API returns 'application/octet-stream' as the media type
for most binary files (PNG, JPG, PDF) instead of specific types like 'image/png'.
For filtering by file type, using the 'filename' parameter is more reliable
(e.g., filename='*.png' pattern matching if supported, or exact filename).

Useful for:
- Discovering what files are attached to a page
- Getting attachment IDs for download operations
- Checking if a specific file exists
- Listing images/documents for processing

Args:
    ctx: The FastMCP context.
    content_id: The ID of the content.
    start: Starting index for pagination.
    limit: Maximum number of results (1-100).
    filename: Optional exact filename filter.
    media_type: Optional MIME type filter (note: most binaries return 'application/octet-stream').

Returns:
    JSON string with list of attachments and metadata.
```
