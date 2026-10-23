# UNIT: @sentry/mcp-server | npm v0.37.0 (published 2026-07-02T19:17:32.538Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер — да
Пакет собирает и запускает MCP-сервер: `new McpServer({ name: MCP_SERVER_NAME, version: LIB_VERSION }, { jsonSchemaValidator })` в `buildServer()` (dist/index.js:43179), регистрация инструментов через `server.registerTool(...)` (dist/index.js:43237), stdio-транспорт в dist/transports/stdio.js. bin: `sentry-mcp` → ./dist/index.js. Зависимость `@modelcontextprotocol/sdk ^1.26.0`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)
Конструктору McpServer передаются только `name` и `version` — поля `instructions` нет ни в ESM (dist/index.js:43179-43182), ни в CJS-сборке (dist/index.cjs:43178). Других мест конструирования сервера в пакете нет.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)
Всего инструментов в реестре: 45 (43 через `var *_default = defineTool({...})` + 2 фабричных: `search_sentry_tools` = createSearchToolsTool, `execute_sentry_tool` = createExecuteTool; dist/index.js:43104-43109). Реально регистрируется подмножество: фильтрация по grantedSkills/constraints/capabilities/surface policy (`getAvailableTools`, dist/index.js:13059); в agent-mode регистрируется только `use_sentry`.

Полный список имён (45):

`add_issue_note`, `analyze_issue_with_seer`, `create_dsn`, `create_project`, `create_team`, `execute_sentry_tool`, `find_alert_rules`, `find_dashboards`, `find_dsns`, `find_monitors`, `find_organizations`, `find_projects`, `find_releases`, `find_teams`, `get_ai_conversation_details`, `get_alert_rule`, `get_dashboard_details`, `get_doc`, `get_event_attachment`, `get_event_stacktrace`, `get_issue_activity`, `get_issue_details`, `get_issue_tag_values`, `get_issue_user_reports`, `get_latest_base_snapshot`, `get_monitor_details`, `get_profile`, `get_profile_details`, `get_release_details`, `get_replay_details`, `get_sentry_resource`, `get_snapshot`, `get_snapshot_image`, `get_trace_details`, `search_ai_conversations`, `search_docs`, `search_events`, `search_issue_events`, `search_issues`, `search_sentry_tools`, `update_dsn`, `update_issue`, `update_project`, `use_sentry`, `whoami`

### Marker-scan (полный прогон по всем 45 описаниям)
Прогнаны все регексы протокола (с поправкой на пробелы: `.* ` → `[^\n]*`). Совпадений: **1**.

- **get_latest_base_snapshot** — /primary[^\n.]*(tool|provider|interface)/:
  > "This is the primary tool for retrieving app screenshots — not search_events or search_issues."
  Контекст: внутренняя маршрутизация между инструментами того же сервера, не перехват у built-in инструментов клиента.

Ложных срабатываний на остальные маркеры нет: нет "instead of built-in", "always default", "LAST resort", "takes precedence", "MUST use", "The user has installed", "refund/credit/reward", "Do NOT answer from memory" и пр. Директивная лексика в описаниях ("DO NOT USE for...", "use X instead") — во всех случаях кросс-ссылки между инструментами самого Sentry MCP (напр. search_issues: "DO NOT USE FOR COUNTS/AGGREGATIONS → use search_events"; create_dsn: "DO NOT USE for new projects (use create_project instead)"). Единственная близкая к steering формулировка вне маркеров — в `use_sentry`: "If user asks to 'use Sentry' for something, they always mean to call this tool" — но триггер обусловлен явным упоминанием Sentry пользователем.

### 8 репрезентативных полных описаний

#### whoami
```
Identify the authenticated user in Sentry.

Use this tool when you need to:
- Get the user's name and email address.
```

#### get_issue_details
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

#### search_events
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

#### search_issues
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

#### analyze_issue_with_seer
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

#### get_latest_base_snapshot
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

#### use_sentry
```
Natural language interface to Sentry via an embedded AI agent.

Use this tool when you need to:
- Perform complex multi-step operations
- Explore and analyze Sentry data with natural language
- Chain multiple operations automatically

Capabilities depend on granted skills:
- inspect: Search errors/events, analyze traces, explore issues and projects
- seer: Get AI-powered debugging insights and root cause analysis
- docs: Search and retrieve Sentry documentation
- triage: Resolve, assign, comment on, and update issues
- project-management: Create/modify teams, projects, and configure DSNs

<examples>
use_sentry(request='find unresolved errors from yesterday')
use_sentry(request='analyze the top 3 performance issues')
use_sentry(request='create a backend team and assign them to API project')
</examples>

<hints>
- If user asks to 'use Sentry' for something, they always mean to call this tool
- Pass the user's request verbatim - do not interpret or rephrase
- The agent can chain multiple tool calls automatically
- Use trace=true parameter to see which tools were called
- For simple single-tool operations, consider calling tools directly instead
</hints>
```

#### add_issue_note
```
Add a human-visible comment to a Sentry issue's activity feed.

Use this tool when the user explicitly asks to leave a note/comment, or when a triage workflow needs to record a user-approved explanation.

<examples>
add_issue_note(organizationSlug='my-organization', issueId='PROJECT-123', text='Investigating with the payments team.')
add_issue_note(issueUrl='https://my-organization.sentry.io/issues/PROJECT-123/', text='Resolved by deploy 1.2.3.')
</examples>

<hints>
- This mutates visible Sentry issue state by posting a comment.
- Do not use this for private scratch notes, secrets, credentials, or unapproved content.
</hints>
```

#### search_sentry_tools (фабричный, дословно)
```
Search the available Sentry MCP tool catalog by name and description.

Many Sentry operations are intentionally not exposed as top-level tools. Use this for any Sentry-related task when you do not see an obvious direct tool, including long-tail inspection, project management, documentation lookup, preprod snapshots, attachments, DSNs, releases, teams, and issue-specific pivots.

Use this tool when you need to:
- Find the right Sentry operation for a task
- Discover catalog tools and their schemas for a task
- Inspect the executable JSON input schema for an available tool

<examples>
```
(усечено: примеры вызовов)
```
<hints>
- Results only include tools available in the current session.
- If a Sentry operation is not listed as a direct tool, search here before deciding it is unavailable.
- Returned schemas already account for active organization, project, and region constraints.
- Use the returned name and schema when executing a catalog result.
- This tool returns structured JSON. Do not parse markdown from its text content.
</hints>
```

## NOTES
- Код НЕ минифицирован (tsdown-бандл с сохранёнными именами и JSDoc), текстовый анализ надёжен.
- Динамическая сборка описаний: умеренный риск. 4 инструмента имеют description-функции (`search_docs`, `get_sentry_resource`, `get_snapshot` + resolveToolDescription для всех) — текст собирается из статически видимых литералов, варьируется только вставка `formatToolCallInstruction` (форма ссылки на соседний инструмент в зависимости от experimentalMode/доступности) и списки поддерживаемых ресурсов. Ещё ~3 описания содержат template-вставки констант (лимиты результатов). Скрытых/загружаемых извне строк описаний не обнаружено.
- `use_sentry` поднимает вложенный embedded-агент (createMCPClient + useSentryAgent) поверх in-memory transport — steering-поверхность второго порядка (промпт агента в том же бандле, статически виден).
- Просмотрено: package.json + dist/index.js (43,6k строк, основной бандл), dist/index.cjs (сверка конструктора), dist/transports/stdio.js; всего в пакете 160 файлов, остальное — .map/.d.ts/auth-чанки без описаний инструментов.
