# UNIT: sentry | Sentry | github getsentry/sentry-mcp | тип автора: официальный | captured 2026-07-29 (static source)

Репозиторий: TypeScript-монорепо (pnpm workspaces). Сервер собирается в `packages/mcp-core/src/server.ts` (`buildServer` -> `new ModernMcpServer(serverInfo)` / `new LegacyMcpServer(serverInfo)`), транспорты в `packages/mcp-server/src/transports/`. Это MCP-сервер.

## CHANNEL: instructions
(не обнаружены статически)

`serverInfo` содержит только `name` (MCP_SERVER_NAME) и `version` (LIB_VERSION); поля `instructions` нет. Поиск `instructions:` по всем .ts/.tsx/.js даёт 0 совпадений; все прочие вхождения слова `instructions` — это React-компоненты страниц установки в `packages/mcp-cloudflare` и локальные переменные форматирования вывода инструментов.

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов в каноническом манифесте `packages/mcp-core/src/toolDefinitions.json`: **48** (>40, поэтому маркер-скан + выборка).

Полный список имён: `add_issue_note`, `add_team_to_project`, `analyze_issue_with_seer`, `create_dsn`, `create_project`, `create_team`, `execute_sentry_tool`, `find_alert_rules`, `find_dashboards`, `find_dsns`, `find_monitors`, `find_organizations`, `find_projects`, `find_releases`, `find_teams`, `get_ai_conversation_details`, `get_alert_rule`, `get_dashboard_details`, `get_doc`, `get_event_attachment`, `get_event_stacktrace`, `get_issue_activity`, `get_issue_breadcrumbs`, `get_issue_details`, `get_issue_tag_values`, `get_issue_user_reports`, `get_latest_base_snapshot`, `get_monitor_details`, `get_profile`, `get_profile_details`, `get_release_details`, `get_replay_details`, `get_sentry_resource`, `get_snapshot`, `get_snapshot_image`, `get_span_details`, `get_trace_details`, `remove_team_from_project`, `search_ai_conversations`, `search_docs`, `search_events`, `search_issue_events`, `search_issues`, `search_sentry_tools`, `update_dsn`, `update_issue`, `update_project`, `whoami`

### Маркер-скан (полный проход по всем 48 описаниям)
Совпадений: **1**.

**`get_latest_base_snapshot`** — дословно:

> This is the primary tool for retrieving app screenshots — not search_events or search_issues.

Все прочие регексы из скан-набора дали 0 совпадений. Контрольная проверка частот по сырому тексту всех описаний (42 089 символов): `prefer`/`Prefer` — 0, `MUST`/`always`/`Always`/`never`/`Never`/`immediately`/`Best` — 0, `must` — 2 (оба про предусловия API: «The team must already be assigned to the project», «Both `rateLimitWindow` ... must be provided together»), `primary` — 1 (цитата выше), `instead` — 3 (все — маршрутизация между собственными инструментами Sentry).

### Внутрисерверная маршрутизация (не в скан-наборе, но фиксирую дословно)
По трём вхождениям `instead` и блокам `DO NOT USE` — все указания разграничивают собственные инструменты сервера, без упоминания внешних инструментов или встроенных возможностей клиента:

- `analyze_issue_with_seer`: "- Seer Autofix does not support metric alert issues (issueCategory: metric); use get_issue_details and search_events instead"
- `create_dsn`: "DO NOT USE for new projects (use create_project instead)"
- `search_events`: "If the user says logs, log messages, error logs, or warning logs, choose logs instead of errors."
- `get_issue_details`: "DO NOT USE for:\n- General searching or listing issues (use search_issues)"
- `get_sentry_resource`: "Conversations are NOT issues — do not use search_issues for conversation queries."
- `add_issue_note`: "- Do not use this for private scratch notes, secrets, credentials, or unapproved content."

### 10 репрезентативных полных описаний (дословно)

#### `search_events` (2037 chars)

```
Search Sentry events and replays. Use for event counts/statistics.

`query` can be natural language or Sentry search syntax. With an agent configured, it fixes dataset, query, fields, and sort before running.

Supports TWO query types:
1. AGGREGATIONS (counts, sums, averages): 'how many errors', 'total tokens'
2. Individual events with timestamps: 'error logs from last hour'

Datasets:
- errors: Exception/crash events with stack traces, usually grouped into issues
- logs: Application log entries, including error-severity log messages
- spans: Raw trace/span events for performance, AI/LLM calls, requests, and operations
- metrics: Metric rows and aggregates: counters, gauges, distributions, values
- profiles: Transaction/continuous profile results, profile IDs, profiled transactions
- replays: Session replay results: rage clicks, dead clicks, visited pages, replay users
If the user says logs, log messages, error logs, or warning logs, choose logs instead of errors.

Replay searches return replay lists only; replay count()/avg()/sum() are not supported.

NOT for grouped issue lists (use search_issues) or app screenshots/images (use get_latest_base_snapshot).

<examples>
search_events(organizationSlug='my-org', query='how many errors today')
search_events(organizationSlug='my-org', dataset='errors', query='level:error')
search_events(organizationSlug='my-org', dataset='errors', fields=['issue', 'count()'], sort='-count()')
search_events(organizationSlug='my-org', dataset='spans', query='span.op:db', sort='-span.duration')
search_events(organizationSlug='my-org', dataset='replays', query='count_errors:>0', sort='-count_errors')
</examples>

<hints>
- If the user passes a parameter in the form of name/otherName, it's likely in the format of <organizationSlug>/<projectSlug>.
- Parse org/project notation directly without calling find_organizations or find_projects.
- Use fields with aggregate functions like count(), avg(), sum() for statistics
- Sort by -count() for most common, -timestamp for newest
</hints>
```

#### `search_issues` (1550 chars)

```
Search for grouped issues/problems in Sentry - returns a LIST of issues, NOT counts or aggregations.

Provide `query` as natural language or Sentry issue search syntax. When an embedded agent is configured, it fixes query and sort before running while preserving explicit Sentry search syntax.

Returns grouped issues with metadata like title, status, and user count.

Common Query Syntax:
- is:unresolved / is:resolved / is:ignored / is:for_review / is:new / is:regressed / is:escalating
- level:error / level:warning
- firstSeen:-24h / lastSeen:-7d
- assigned:me / assigned_or_suggested:me
- release:latest
- issue.category:feedback
- issue.priority:high
- environment:production
- userCount:>100

DO NOT USE FOR COUNTS/AGGREGATIONS → use search_events
DO NOT USE FOR individual events with timestamps → use search_events
DO NOT USE FOR details about a specific issue → use get_sentry_resource

<examples>
search_issues(organizationSlug='my-org', query='critical bugs from last week')
search_issues(organizationSlug='my-org', query='is:unresolved is:unassigned', sort='freq')
search_issues(organizationSlug='my-org', query='level:error firstSeen:-24h', projectSlugOrId='my-project')
</examples>

<hints>
- If the user passes a parameter in the form of name/otherName, it's likely in the format of <organizationSlug>/<projectSlugOrId>.
- Parse org/project notation directly without calling find_organizations or find_projects.
- The projectSlugOrId parameter accepts both project slugs (e.g., 'my-project') and numeric IDs (e.g., '123456').
</hints>
```

#### `get_issue_details` (1314 chars)

```
Get detailed information about a specific Sentry issue by ID.

USE THIS TOOL WHEN USERS:
- Provide a specific issue ID (e.g., 'CLOUDFLARE-MCP-41', 'PROJECT-123')
- Ask to 'explain [ISSUE-ID]', 'tell me about [ISSUE-ID]'
- Want details/stacktrace/analysis for a known issue
- Provide a Sentry issue URL

DO NOT USE for:
- General searching or listing issues (use search_issues)

TRIGGER PATTERNS:
- 'Explain ISSUE-123' → use get_issue_details
- 'Tell me about PROJECT-456' → use get_issue_details
- 'What happened in [issue URL]' → use get_issue_details

<examples>
### With Sentry URL (recommended - simplest approach)
```
get_issue_details(issueUrl='https://sentry.sentry.io/issues/6916805731/?project=4509062593708032&query=is%3Aunresolved')
```

### With issue ID and organization
```
get_issue_details(organizationSlug='my-organization', issueId='CLOUDFLARE-MCP-41')
```

### With event ID and organization
```
get_issue_details(organizationSlug='my-organization', eventId='c49541c747cb4d8aa3efb70ca5aba243')
```
</examples>

<hints>
- **IMPORTANT**: If user provides a Sentry URL, pass the ENTIRE URL to issueUrl parameter unchanged
- When using issueUrl, all other parameters are automatically extracted - don't provide them separately
- If using issueId (not URL), then organizationSlug is required
</hints>
```

#### `get_latest_base_snapshot` (1553 chars)

```
Get the latest UI screenshots/images for an app from the preprod snapshot system.

This is the primary tool for retrieving app screenshots — not search_events or search_issues.

Use this tool when you need to:
- Get screenshots, screens, golden images, or reference images for an app
- Find what the current UI looks like (latest screenshots from the main/default branch)
- List available snapshots or browse images before requesting specific ones
- Look up dark mode, light mode, or other variant screenshots
- Understand what baseline images exist when investigating snapshot test or visual regression CI failures

The appId parameter is the app identifier (e.g. 'sentry-frontend', 'com.emergetools.hackernews').
Returns compact image metadata (display_name, image_file_name, group, description) for every image.

<examples>
### Get the latest screenshots for an app

```
get_latest_base_snapshot(organizationSlug="sentry", appId="sentry-frontend", project="frontend")
```

### Get the latest screenshots for a specific branch

```
get_latest_base_snapshot(organizationSlug="sentry", appId="sentry-frontend", project="frontend", branch="main")
```
</examples>

<hints>
- The response includes compact metadata per image. Scan the list to find images matching what you need (e.g. filter by group or name containing 'button').
- To view a specific image, use get_sentry_resource(url='<snapshot_url>?selectedSnapshot=<image_file_name>').
- If you need to investigate a specific snapshot comparison, use get_sentry_resource with the snapshot URL.
</hints>
```

#### `analyze_issue_with_seer` (1533 chars)

```
Use Seer to analyze production errors and get detailed root cause analysis with specific code fixes.

Use this tool when:
- The user explicitly asks for root cause analysis, Seer analysis, or help fixing/debugging an issue
- You are unable to accurately determine the root cause from the issue details alone

Do NOT call this tool as an automatic follow-up to get_sentry_resource.

What this tool provides:
- Root cause analysis with code-level explanations
- Specific file locations and line numbers where errors occur
- Concrete code fixes you can apply
- Step-by-step implementation guidance

This tool automatically:
1. Checks if analysis already exists (instant results)
2. Starts new AI analysis if needed (~2-5 minutes)
3. Returns complete fix recommendations

<examples>
### User: "Run Seer on this issue"

```
analyze_issue_with_seer(issueUrl='https://my-org.sentry.io/issues/PROJECT-1Z43')
```

### User: "Analyze this issue and suggest a fix"

```
analyze_issue_with_seer(organizationSlug='my-organization', issueId='ERROR-456')
```
</examples>

<hints>
- Only use when the user explicitly requests analysis or you cannot determine the root cause from issue details alone
- Seer Autofix does not support metric alert issues (issueCategory: metric); use get_issue_details and search_events instead
- If the user provides an issueUrl, extract it and use that parameter alone
- The analysis includes actual code snippets and fixes, not just error descriptions
- Results are cached - subsequent calls return instantly
</hints>
```

#### `get_sentry_resource` (1551 chars)

```
Fetch a Sentry resource by URL, or by resourceType plus resourceId.
Pass a Sentry URL directly when possible; the resource type is auto-detected.

Supports issues, events, traces, spans, AI conversations, replays, monitors, preprod snapshots, and snapshot images.
Trace lookups return a condensed overview by default.

AI Conversations: A conversation is a set of spans sharing the same gen_ai.conversation.id. Use resourceType='ai_conversation' with a conversation ID, or pass a Sentry conversation URL, to fetch the transcript/details. To discover or list conversations, use search_ai_conversations. Conversations are NOT issues — do not use search_issues for conversation queries.

For preprod snapshot URLs (matching 'sentry.io/preprod/snapshots/'):
- Without ?selectedSnapshot=: returns the snapshot diff summary (changed, added, removed images)
- With ?selectedSnapshot=<image_file_name>: returns the image preview and metadata. Use the Sentry tool `get_snapshot_image` for full-resolution image bytes.

Resource IDs:
- monitor: <monitorSlug>
- snapshot: <snapshotId>

<examples>
get_sentry_resource(url='https://sentry.io/issues/PROJECT-123/')
get_sentry_resource(resourceType='issue', organizationSlug='my-org', resourceId='PROJECT-123')
get_sentry_resource(resourceType='ai_conversation', organizationSlug='my-org', resourceId='conversation-123')
get_sentry_resource(url='https://sentry.sentry.io/preprod/snapshots/123/')
get_sentry_resource(url='https://sentry.sentry.io/preprod/snapshots/123/?selectedSnapshot=login_screen.png')
</examples>
```

#### `search_sentry_tools` (1205 chars)

```
Search the available Sentry MCP tool catalog by name and description.

Many Sentry operations are intentionally not exposed as top-level tools. Use this for any Sentry-related task when you do not see an obvious direct tool, including long-tail inspection, project management, documentation lookup, preprod snapshots, attachments, DSNs, releases, teams, and issue-specific pivots.

Use this tool when you need to:
- Find the right Sentry operation for a task
- Discover catalog tools and their schemas for a task
- Inspect the executable JSON input schema for an available tool

<examples>
search_sentry_tools(query='list projects')
search_sentry_tools(query='issue details')
search_sentry_tools(query='find dsn', limit=5)
search_sentry_tools(query='snapshot image')
</examples>

<hints>
- Results only include tools available in the current session.
- If a Sentry operation is not listed as a direct tool, search here before deciding it is unavailable.
- Returned schemas already account for active organization, project, and region constraints.
- Use the returned name and schema when executing a catalog result.
- This tool returns structured JSON. Do not parse markdown from its text content.
</hints>
```

#### `execute_sentry_tool` (659 chars)

```
Execute an available Sentry MCP tool discovered through search_sentry_tools.

Use this tool when you need to:
- Call a Sentry operation returned by search_sentry_tools
- Execute a tool by name using arguments that match its returned schema

<examples>
execute_sentry_tool(name='find_projects', arguments={ organizationSlug: 'my-org' })
execute_sentry_tool(name='whoami', arguments={})
</examples>

<hints>
- Use search_sentry_tools first if you are not sure which name or arguments to pass.
- Arguments are validated against the target tool's schema before execution.
- Active organization, project, and region constraints are injected automatically.
</hints>
```

#### `update_issue` (1812 chars)

```
Update a Sentry issue's status or assignment.

Use this to resolve, reopen, assign, or ignore an issue.

<examples>
```
update_issue(organizationSlug='my-org', issueId='PROJECT-123', status='resolved')
update_issue(organizationSlug='my-org', issueId='PROJECT-123', assignedTo='user:123456')
update_issue(organizationSlug='my-org', issueId='PROJECT-123', status='ignored')
update_issue(organizationSlug='my-org', issueId='PROJECT-123', status='ignored', ignoreMode='forever')
update_issue(organizationSlug='my-org', issueId='PROJECT-123', status='ignored', ignoreMode='untilOccurrenceCount', ignoreCount=100, ignoreWindowMinutes=60)
update_issue(organizationSlug='my-org', issueId='PROJECT-123', status='ignored', reason='Ignoring because this is expected noise from the staging deploy')
```
</examples>

<hints>
- Provide `issueUrl` or `organizationSlug` + `issueId`.
- At least one of `status` or `assignedTo` is required.
- `assignedTo` format: `user:ID` or `team:ID_OR_SLUG`.
- Use `execute_sentry_tool(name='whoami', arguments={})` to find your user ID for self-assignment.
- Status values: `resolved`, `resolvedInNextRelease`, `unresolved`, `ignored`.
- `status='ignored'` defaults to `ignoreMode='untilEscalating'`.
- Ignore modes: `untilEscalating`, `forever`, `forDuration`, `untilOccurrenceCount`, `untilUserCount`.
- Matching ignore inputs are `ignoreDurationMinutes`, `ignoreCount` + optional `ignoreWindowMinutes`, or `ignoreUserCount` + optional `ignoreUserWindowMinutes`.
- To switch an already ignored issue between `untilEscalating`, `forever`, and condition-based ignore modes, first set `status='unresolved'`, then ignore it again with the new rule.
- `reason` is optional. When provided, it will be posted as a comment on the issue's activity feed explaining why the action was taken.
</hints>
```

#### `whoami` (116 chars)

```
Identify the authenticated user in Sentry.

Use this tool when you need to:
- Get the user's name and email address.
```
