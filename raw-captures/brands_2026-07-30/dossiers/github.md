# UNIT: github | GitHub | github github/github-mcp-server | тип автора: официальный | captured 2026-07-29 (static source)

Подтверждение MCP-сервера: Go-репозиторий, `github.com/modelcontextprotocol/go-sdk/mcp`, `mcp.NewServer(...)` в `pkg/github/server.go` (передаёт `Instructions: inv.Instructions()`), stdio/http-транспорты в `internal/ghmcp/server.go` и `pkg/http/handler.go`. Это полноценный сервер, не SDK/клиент/прокси.

## CHANNEL: instructions (6479 chars)

Строка собирается в `pkg/inventory/instructions.go` (`generateInstructions`) как базовый блок + фрагменты включённых тулсетов, склеенные через " ". Ниже дословно базовый блок и все фрагменты (`pkg/github/toolset_instructions.go`).

### Base (903 chars)

```
The GitHub MCP Server provides tools to interact with GitHub platform.

Tool selection guidance:
	1. Use 'list_*' tools for broad, simple retrieval and pagination of all items of a type (e.g., all issues, all PRs, all branches) with basic filtering.
	2. Use 'search_*' tools for targeted queries with specific criteria, keywords, or complex filters (e.g., issues with certain text, PRs by author, code containing functions).

Context management:
	1. Use pagination whenever possible with batches of 5-10 items.
	2. Use minimal_output parameter set to true if the full information is not needed to accomplish a task.

Tool usage guidance:
	1. For 'search_*' tools: Use separate 'sort' and 'order' parameters if available for sorting results - do not include 'sort:' syntax in query strings. Query strings should contain only search criteria (e.g., 'org:google language:python'), not sorting instructions.
```

### Toolset: context

```
Always call 'get_me' first to understand current user permissions and context.
```

### Toolset: issues

```
## Issues

Check 'list_issue_types' first for organizations to use proper issue types. Use 'search_issues' before creating new issues to avoid duplicates. Always set 'state_reason' when closing issues.
```

### Toolset: pull_requests

```
## Pull Requests

PR review workflow: Always use 'pull_request_review_write' with method 'create' to create a pending review, then 'add_comment_to_pending_review' to add comments, and finally 'pull_request_review_write' with method 'submit_pending' to submit the review for complex reviews with line-specific comments.
```

Условный довесок (если включён тулсет `repos`):

```
Before creating a pull request, search for pull request templates in the repository. Template files are called pull_request_template.md or they're located in '.github/PULL_REQUEST_TEMPLATE' directory. Use the template content to structure the PR description and then call create_pull_request tool.
```

### Toolset: discussions

```
## Discussions

Use 'list_discussion_categories' to understand available categories before creating discussions. Filter by category for better organization.
```

### Toolset: projects

```
## Projects

Workflow: 1) list_project_fields (get field IDs), 2) list_project_items (with pagination), 3) optional updates.

Project lifecycle: Use create_project to create a new ProjectsV2 for a user or organization (requires owner_type and title). Returns the new project's id, number, title, and url; pass the returned number as project_number to subsequent project tools.

Iteration fields: Use create_iteration_field to add a new ITERATION field (e.g. "Sprint") to an existing project. Required: field_name, iteration_duration (days), start_date (YYYY-MM-DD). Only pass the iterations array when iterations need varying durations, breaks between them, or specific titles; otherwise omit it and GitHub creates three default iterations of iteration_duration days starting on start_date.

Status updates: Use list_project_status_updates to read recent project status updates (newest first). Use get_project_status_update with a node ID to get a single update. Use create_project_status_update to create a new status update for a project.

Field usage:
	- Call list_project_fields first to understand available fields and get IDs/types before filtering.
	- Use EXACT returned field names (case-insensitive match). Don't invent names or IDs.
	- Iteration synonyms (sprint/cycle) only if that field exists; map to the actual name (e.g. sprint:@current).
	- Only include filters for fields that exist and are relevant.

Pagination (mandatory):
	- Loop while pageInfo.hasNextPage=true using after=pageInfo.nextCursor.
	- Keep query, fields, per_page IDENTICAL on every page.
	- Use before=pageInfo.prevCursor only when explicitly navigating to a previous page.

Counting rules:
	- Count items array length after full pagination.
	- Never count field objects, content, or nested arrays as separate items.

Summary vs list:
	- Summaries ONLY if user uses verbs: analyze | summarize | summary | report | overview | insights.
	- Listing verbs (list/show/get/fetch/display/enumerate) → enumerate + total.

Self-check before returning:
	- Paginated fully
	- Correct IDs used
	- Field names valid
	- Summary only if requested.

Return COMPLETE data or state what's missing (e.g. pages skipped).

list_project_items query rules:
Query string - For advanced filtering of project items using GitHub's project filtering syntax:

MUST reflect user intent; strongly prefer explicit content type if narrowed:
	- "open issues" → state:open is:issue
	- "merged PRs" → state:merged is:pr
	- "items updated this week" → updated:>@today-7d (omit type only if mixed desired)
	- "list all P1 priority items" → priority:p1 (omit state if user wants all, omit type if user specifies "items")
	- "list all open P2 issues" → is:issue state:open priority:p2 (include state if user wants open or closed, include type if user specifies "issues" or "PRs")
	- "all open issues I'm working on" → is:issue state:open assignee:@me

Query Construction Heuristics:
	a. Extract type nouns: issues → is:issue | PRs, Pulls, or Pull Requests → is:pr | tasks/tickets → is:issue (ask if ambiguity)
	b. Map temporal phrases: "this week" → updated:>@today-7d
	c. Map negations: "excluding wontfix" → -label:wontfix
	d. Map priority adjectives: "high/sev1/p1" → priority:high OR priority:p1 (choose based on field presence)
	e. When filtering by label, always use wildcard matching to account for cross-repository differences or emojis: (e.g. "bug 🐛" → label:*bug*)
	f. When filtering by milestone, always use wildcard matching to account for cross-repository differences: (e.g. "v1.0" → milestone:*v1.0*)

Syntax Essentials (items):
   AND: space-separated. (label:bug priority:high).
   OR: comma inside one qualifier (label:bug,critical).
   NOT: leading '-' (-label:wontfix).
   Hyphenate multi-word field names. (team-name:"Backend Team", story-points:>5).
   Quote multi-word values. (status:"In Review" team-name:"Backend Team").
   Ranges: points:1..3, updated:<@today-30d.
   Wildcards: title:*crash*, label:bug*.
   Assigned to User: assignee:@me | assignee:username | no:assignee

Common Qualifier Glossary (items):
   is:issue | is:pr | state:open|closed|merged | assignee:@me|username | label:NAME | status:VALUE |
   priority:p1|high | sprint-name:@current | team-name:"Backend Team" | parent-issue:"org/repo#123" |
   updated:>@today-7d | title:*text* | -label:wontfix | label:bug,critical | no:assignee | has:label

Never:
   - Infer field IDs; fetch via list_project_fields.
   - Drop 'fields' param on subsequent pages if field values are needed.
```

Примечание: при `DISABLE_INSTRUCTIONS=true` инструкции пустые; сборка выполняется только если билдер вызвал `WithServerInstructions()` (вызывается в `internal/ghmcp/server.go:174` и `pkg/http/handler.go:292`).

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов: 115 (уникальные имена по снапшотам `pkg/github/__toolsnaps__/*.snap`, сверено с определениями `mcp.Tool{Name/Description}` в `pkg/github/*.go`). Больше 40 → полный маркер-скан всех описаний + репрезентативная выборка.

### Результаты полного маркер-скана (3 совпадения в 3 инструментах)

**assign_copilot_to_issue_with_intent**
> Assign Copilot to a specific issue in a GitHub repository. Prefer this tool over assign_copilot_to_issue when available.

**list_notifications**
> Use this tool whenever the user asks what to work on next, requests a summary of their GitHub activity, wants to see pending reviews, or needs to check for new updates or tasks. This tool is the primary way to discover actionable items, reminders, and outstanding work on GitHub. Always call this tool when asked what to work on next, what is pending, or what needs attention in GitHub.

**search_repositories**
> Perfect for discovering projects, finding examples, or locating specific repositories across GitHub.

Остальные 112 описаний по маркерам чисты.

### 10 репрезентативных полных описаний

**get_me**
> Get details of the authenticated GitHub user. Use this when a request is about the user's own profile for GitHub. Or when information is missing to build other tool calls.

**issue_read**
> Get information about a specific issue in a GitHub repository.

**issue_write**
> Create a new or update an existing issue in a GitHub repository.

**pull_request_read**
> Get information on a specific pull request in GitHub repository.

**search_issues**
> Search for issues in GitHub repositories using issues search syntax already scoped to is:issue

**get_file_contents**
> Get the contents of a file or directory from a GitHub repository

**actions_get**
> Get details about specific GitHub Actions resources.
> Use this tool to get details about individual workflows, workflow runs, jobs, and artifacts by their unique IDs.

**projects_write**
> Create and manage GitHub Projects: create projects, add/update/delete items, create status updates, and add iteration fields.

**get_job_logs**
> Download logs for a specific workflow job or efficiently get all failed job logs for a workflow run

**push_files**
> Push multiple files to a GitHub repository in a single commit
