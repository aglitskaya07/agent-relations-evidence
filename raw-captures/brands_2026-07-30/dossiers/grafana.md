# UNIT: grafana | Grafana | github grafana/mcp-grafana | тип автора: официальный | captured 2026-07-29 (static source)

Язык: Go (mark3labs/mcp-go). Сервер подтверждён: `server.NewMCPServer("mcp-grafana", ...)` в `cmd/mcp-grafana/main.go:334`, транспорты stdio/sse/http.

## CHANNEL: instructions (3095 chars)

Строка передаётся как `server.WithInstructions(instructions)` (`cmd/mcp-grafana/main.go:332-337`); собирается функцией `buildInstructions()` (там же, строки 226-263) из шаблона и карты `categoryDescription` (строки 46-80). Ниже — дословная реконструкция при дефолтных флагах (все категории включены, proxied включён):

```
This server provides access to your Grafana instance and the surrounding ecosystem.

Available Capabilities:
- Search: Find dashboards, folders, and other Grafana resources.
- Datasources: List and fetch details for datasources.
- Incidents: Search, create, update, and resolve incidents in Grafana Incident.
- Prometheus: Run PromQL queries, retrieve metric metadata, and explore label names/values.
- Loki: Run LogQL queries, retrieve log metadata, and explore label names/values.
- Elasticsearch and OpenSearch: Query Elasticsearch and OpenSearch datasources using Lucene syntax or Query DSL for logs and metrics.
- Quickwit: Query Quickwit datasources using Lucene syntax or Query DSL for logs and documents.
- InfluxDB: Query InfluxDB datasources.
- Alerting: List and fetch alert rules and notification contact points.
- Dashboards: Search, retrieve, update, and create dashboards. Extract panel queries and datasource information.
- Folders: Manage dashboard folders.
- OnCall: View and manage on-call schedules, shifts, teams, and users.
- Asserts: Query and analyze assertion data.
- Sift Investigations: Start and manage Sift investigations, analyze logs/traces, find error patterns, and detect slow requests.
- Admin: List teams and perform administrative tasks.
- Pyroscope: Profile applications and fetch profiling data.
- Navigation: Generate deeplink URLs for Grafana resources like dashboards, panels, and Explore queries, with optional built-in shortening.
- Annotations: Create and manage dashboard annotations.
- Rendering: Export dashboard panels or full dashboards as PNG images (requires Grafana Image Renderer plugin).
- Snapshots: List, get, create, and delete dashboard snapshots.
- CloudWatch: Query AWS CloudWatch datasources for metrics and logs.
- Examples: Query example tools.
- ClickHouse: Query ClickHouse datasources via Grafana with macro and variable substitution support.
- Snowflake: Query Snowflake datasources via Grafana (including the SNOWFLAKE.TELEMETRY.EVENTS event table) with macro and variable substitution support.
- Run Panel Query: Execute panel queries directly.
- Graphite: Query Graphite datasources for metrics.
- Athena: Query Amazon Athena datasources via Grafana with SQL, macro substitution, and schema discovery.
- Plugins: Check whether Grafana plugins are installed and fetch plugin details.
- API: Make authenticated HTTP requests to any Grafana API endpoint with optional jq-style response filtering.
- Config: Generate operator-facing configuration snippets (e.g. Alloy label-enforcement pipelines).
- Provisioning: List provisioning repositories (e.g. git-sync sources) to discover repository slugs for use with rendering tools.
- Agent Observability: Search and inspect LLM conversations, generations, and evaluation scores from Grafana Agent Observability.
- Proxied Tools: Access tools from external MCP servers (like Tempo) through dynamic discovery.

Timestamp parameters without a timezone offset are interpreted as UTC. Include an offset like '-05:00' or use relative syntax like 'now-1h' to query in a different timezone.
```

Дословный шаблон сборки (из кода):

```go
b.WriteString("This server provides access to your Grafana instance and the surrounding ecosystem.\n\n")
// if len(capabilities) > 0:
//   "Available Capabilities:\n" + для каждой: "- " + desc + "\n"
// else:
//   "No tool categories are currently enabled.\n"
b.WriteString("\nTimestamp parameters without a timezone offset are interpreted as UTC. Include an offset like '-05:00' or use relative syntax like 'now-1h' to query in a different timezone.\n")
```

Дословная строка для proxied-категории (добавляется вне `toolEntries`, строка 244): `"Proxied Tools: Access tools from external MCP servers (like Tempo) through dynamic discovery."`

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего статических регистраций через `mcpgrafana.MustTool(name, description, handler, ...)`: **103** (уникальных имён 100 — `alerting_manage_rules`, `grafana_api_request`, `generate_deeplink` имеют по два варианта: read-only и read-write). Регистрация категорий — `tools/*.go`, функции `Add<Category>Tools`. Проксируемые инструменты (`proxied_tools.go`) приходят с внешних MCP-серверов в рантайме и статически не содержат описаний.

### Полный список инструментов (имя — файл — длина описания)

- `list_teams` — tools/admin.go — 113 chars
- `list_users_by_org` — tools/admin.go — 119 chars
- `list_all_roles` — tools/admin.go — 175 chars
- `get_role_details` — tools/admin.go — 118 chars
- `get_role_assignments` — tools/admin.go — 120 chars
- `list_user_roles` — tools/admin.go — 147 chars
- `list_team_roles` — tools/admin.go — 96 chars
- `get_resource_permissions` — tools/admin.go — 113 chars
- `get_resource_description` — tools/admin.go — 83 chars
- `agento11y_manage_conversations` — tools/agento11y.go — 1629 chars
- `agento11y_manage_generations` — tools/agento11y.go — 594 chars
- `alerting_manage_rules` — tools/alerting.go — 464 chars
- `alerting_manage_rules` — tools/alerting.go — 461 chars
- `alerting_manage_routing` — tools/alerting_routing.go — 561 chars
- `get_annotations` — tools/annotations.go — 83 chars
- `create_annotation` — tools/annotations.go — 125 chars
- `update_annotation` — tools/annotations.go — 140 chars
- `get_annotation_tags` — tools/annotations.go — 99 chars
- `grafana_api_request` — tools/api.go — 224 chars
- `grafana_api_request` — tools/api.go — 255 chars
- `get_assertions` — tools/asserts.go — 100 chars
- `list_athena_catalogs` — tools/athena.go — 142 chars
- `list_athena_databases` — tools/athena.go — 114 chars
- `list_athena_tables` — tools/athena.go — 138 chars
- `describe_athena_table` — tools/athena.go — 120 chars
- `query_athena` — tools/athena.go — 640 chars
- `query_clickhouse` — tools/clickhouse.go — 389 chars
- `list_clickhouse_tables` — tools/clickhouse.go — 150 chars
- `describe_clickhouse_table` — tools/clickhouse.go — 153 chars
- `query_cloudwatch` — tools/cloudwatch.go — 627 chars
- `list_cloudwatch_namespaces` — tools/cloudwatch.go — 224 chars
- `list_cloudwatch_metrics` — tools/cloudwatch.go — 225 chars
- `list_cloudwatch_dimensions` — tools/cloudwatch.go — 219 chars
- `suggest_loki_alloy_label_config` — tools/config.go — 166 chars
- `get_dashboard_by_uid` — tools/dashboard.go — 560 chars
- `update_dashboard` — tools/dashboard.go — 2177 chars
- `get_dashboard_panel_queries` — tools/dashboard.go — 507 chars
- `get_dashboard_property` — tools/dashboard.go — 680 chars
- `get_dashboard_summary` — tools/dashboard.go — 236 chars
- `list_datasources` — tools/datasources.go — 145 chars
- `create_datasource` — tools/datasources.go — 652 chars
- `update_datasource` — tools/datasources.go — 540 chars
- `get_datasource` — tools/datasources.go — 260 chars
- `check_datasources_health` — tools/datasources.go — 72 chars
- `query_elasticsearch` — tools/elasticsearch.go — 574 chars
- `get_query_examples` — tools/examples.go — 414 chars
- `create_folder` — tools/folder.go — 86 chars
- `query_graphite` — tools/graphite.go — 539 chars
- `list_graphite_metrics` — tools/graphite.go — 456 chars
- `list_graphite_tags` — tools/graphite.go — 360 chars
- `query_graphite_density` — tools/graphite.go — 594 chars
- `list_incidents` — tools/incident.go — 158 chars
- `create_incident` — tools/incident.go — 244 chars
- `add_activity_to_incident` — tools/incident.go — 185 chars
- `get_incident` — tools/incident.go — 137 chars
- `query_influxdb` — tools/influxdb.go — 476 chars
- `list_loki_label_names` — tools/loki.go — 262 chars
- `list_loki_label_values` — tools/loki.go — 324 chars
- `query_loki_logs` — tools/loki.go — 791 chars
- `query_loki_stats` — tools/loki.go — 837 chars
- `query_loki_patterns` — tools/loki.go — 514 chars
- `analyze_loki_labels` — tools/loki_label_analyzer.go — 258 chars
- `generate_deeplink` — tools/navigation.go — 600 chars
- `generate_deeplink` — tools/navigation.go — 488 chars
- `list_oncall_schedules` — tools/oncall.go — 256 chars
- `get_oncall_shift` — tools/oncall.go — 201 chars
- `get_current_oncall_users` — tools/oncall.go — 178 chars
- `list_oncall_teams` — tools/oncall.go — 112 chars
- `list_oncall_users` — tools/oncall.go — 251 chars
- `list_alert_groups` — tools/oncall.go — 503 chars
- `get_alert_group` — tools/oncall.go — 95 chars
- `get_plugin` — tools/plugins.go — 273 chars
- `install_plugin` — tools/plugins.go — 198 chars
- `search_plugin_information` — tools/plugins.go — 531 chars
- `list_prometheus_metric_metadata` — tools/prometheus.go — 132 chars
- `query_prometheus` — tools/prometheus.go — 340 chars
- `list_prometheus_metric_names` — tools/prometheus.go — 350 chars
- `list_prometheus_label_names` — tools/prometheus.go — 156 chars
- `list_prometheus_label_values` — tools/prometheus.go — 264 chars
- `query_prometheus_histogram` — tools/prometheus.go — 312 chars
- `list_provisioning_repositories` — tools/provisioning.go — 339 chars
- `validate_provisioning_file` — tools/provisioning.go — 441 chars
- `list_pyroscope_label_names` — tools/pyroscope.go — 452 chars
- `list_pyroscope_label_values` — tools/pyroscope.go — 407 chars
- `list_pyroscope_profile_types` — tools/pyroscope.go — 442 chars
- `query_pyroscope` — tools/pyroscope.go — 451 chars
- `query_quickwit` — tools/quickwit.go — 556 chars
- `get_panel_image` — tools/rendering.go — 428 chars
- `run_panel_query` — tools/run_panel_query.go — 710 chars
- `search_dashboards` — tools/search.go — 139 chars
- `search_folders` — tools/search.go — 109 chars
- `get_sift_investigation` — tools/sift.go — 153 chars
- `get_sift_analysis` — tools/sift.go — 147 chars
- `list_sift_investigations` — tools/sift.go — 120 chars
- `find_error_pattern_logs` — tools/sift.go — 172 chars
- `find_slow_requests` — tools/sift.go — 115 chars
- `list_snapshots` — tools/snapshot.go — 78 chars
- `get_snapshot` — tools/snapshot.go — 81 chars
- `create_snapshot` — tools/snapshot.go — 115 chars
- `delete_snapshot` — tools/snapshot.go — 42 chars
- `query_snowflake` — tools/snowflake.go — 728 chars
- `list_snowflake_tables` — tools/snowflake.go — 177 chars
- `describe_snowflake_table` — tools/snowflake.go — 157 chars

### Маркер-скан всех 103 описаний

Совпадений: **1**.

- инструмент `query_loki_logs` (tools/loki.go), совпадение `Prefer`, дословный контекст:

  > ...ing log lines precisely, use a `count_over_time()` metric query with queryType='instant'. Prefer using `query_loki_stats` first to cheaply check whether a stream contains data (avoiding ...

Остальные шаблоны из скан-набора совпадений не дали ни в одном описании.

### 10 репрезентативных полных описаний (дословно)

#### `search_dashboards` (tools/search.go, 139 chars)

```
Search for Grafana dashboards by a query string. Returns a list of matching dashboards with details like title, UID, folder, tags, and URL.
```

#### `query_prometheus` (tools/prometheus.go, 340 chars)

```
WORKFLOW: list_prometheus_metric_names -> list_prometheus_label_values -> query_prometheus. Query a PromQL-compatible datasource (Prometheus, Thanos, Mimir, Cloud Monitoring, etc.) using a PromQL expression. Supports instant queries (single point) and range queries (time range). Time: RFC3339 or relative expressions like 'now'\, 'now-1h'.
```

#### `query_loki_logs` (tools/loki.go, 791 chars)

```
Executes a log query against a Loki or VictoriaLogs datasource and returns matching log entries (or metric samples on Loki). Defaults to the last hour, a limit of 10 entries, and 'backward' direction (newest first). The `logql` parameter takes LogQL on Loki and LogsQL on VictoriaLogs (e.g., Loki: `{app="foo"} |= "error"`; VictoriaLogs: `{app="foo"} "error"`). To count matching log lines precisely, use a `count_over_time()` metric query with queryType='instant'. Prefer using `query_loki_stats` first to cheaply check whether a stream contains data (avoiding expensive queries against empty streams) and `list_loki_label_names` / `list_loki_label_values` to verify labels exist before querying. Note: `query_loki_stats` returns approximate storage-level counts, not exact log line counts.
```

#### `grafana_api_request` (tools/api.go, 224 chars)

```
Make an authenticated HTTP request to the Grafana API. Similar to 'gh api' for GitHub. Supports any Grafana API endpoint with optional jq-style response filtering. Use this for API endpoints that don't have a dedicated tool.
```

#### `generate_deeplink` (tools/navigation.go, 600 chars)

```
Generate deeplink URLs for Grafana resources. Supports dashboards (requires dashboardUid or provisioningPreview), panels (requires dashboardUid or provisioningPreview, plus panelId), and Explore queries (requires datasourceUid and optionally queries). For dashboard and panel links, provisioningPreview points at a dashboard staged on a provisioning repository branch (e.g. a git-sync PR preview). For explore links, the time range and queries are embedded inside the Grafana explore state. Set shorten=true to also attempt a /goto/<uid> short URL; if shortening fails, the full deeplink is returned.
```

#### `update_dashboard` (tools/dashboard.go, 2177 chars)

```
Create or update a dashboard. Two modes: (1) Full JSON — provide 'dashboard' for new dashboards or complete replacements. (2) Patch — provide 'uid' + 'operations' to make targeted changes to an existing dashboard. One of these two modes is required; 'folderUid'\, 'message'\, and 'overwrite' are supplementary and do nothing on their own. Dashboard authoring guidance: if a saved query must support one\, many\, or All values from a multi-select variable inside a regex expression or matcher\, save '${var:regex}' rather than plain '$var'. Saved dashboard annotation queries/definitions must be written into dashboard JSON under 'annotations.list'; the create_annotation tool creates annotation events and does not add a reusable dashboard annotation query/definition to the saved dashboard. For stat panels over the current dashboard range\, make the query return the range-level result the stat should display; panel-side reduction only reduces returned series and does not compute peak-over-range or ratio-of-peaks semantics for you. Patch operations support JSONPaths like '$.panels[0].targets[0].expr'\, '$.panels[1].title'\, '$.panels[2].targets[0].datasource'\, '$.templating.list/-'\, and '$.annotations.list/-'. Append to arrays with '/- ' syntax: '$.panels/- '. Remove by index: {"op": "remove"\, "path": "$.panels[2]"}. Multiple removes on the same array are automatically reordered to avoid index-shifting issues. Note: only numeric array indices are supported in patch paths; filter expressions like [?(@.id==2)] and wildcards like [*] are not supported. v2 dashboards (check 'isV2' from get_dashboard_by_uid) use a different shape: patch '$.elements.<name>.spec.title' or '$.elements.<name>.spec.data.spec.queries[0].spec' and edit '$.variables'/'$.layout' rather than '$.panels'/'$.templating.list'. Full-JSON saves containing top-level 'elements'/'layout' are written as v2 and require a Kubernetes-capable Grafana. After creating or updating a dashboard\, verify that panel queries return data by using `run_panel_query` or the appropriate query tool (`query_prometheus`\, `query_loki_logs`\, etc.) to validate expressions before considering the task complete.
```

#### `alerting_manage_rules` (tools/alerting.go, 464 chars)

```
List and inspect Grafana alert rules with filtering capabilities.

When to use:
- Understanding why an alert is or isn't firing
- Auditing alert rule configuration (queries, conditions, labels, notification settings)
- Finding alert rules by state, folder, group, or name
- Comparing rule versions to see what changed

When NOT to use:
- Checking how alerts are routed to receivers (use alerting_manage_routing)
- Modifying or creating alert rules (read-only tool)
```

#### `query_pyroscope` (tools/pyroscope.go, 451 chars)

```
Unified Pyroscope query tool for fetching profiles or metrics from Pyroscope. Profile data shows WHICH functions consume resources; metrics data
shows WHEN consumption spiked. Use query_type="both" for complete analysis in one call.

query_type options (extends Grafana's PyroscopeQueryType):
- "profile": returns DOT-format call graph
- "metrics": returns time-series data points
- "both" (default): returns both profile and metrics in one response
```

#### `agento11y_manage_conversations` (tools/agento11y.go, 1629 chars)

```
List, search, and fetch LLM conversations from Grafana Agent Observability (the grafana-agento11y-app plugin).

Operations:
- 'list': recent conversations (lightweight; id, title, generation count, timestamps), paginated via limit and cursor
- 'search': search conversations by filter expression and time range; results include models, agents, error counts, rating and eval summaries, and trace IDs
- 'get': one conversation by ID with all its generations, including full prompts and outputs (can be large)

Filter syntax for 'search': key operator value, with the value in double quotes; multiple filters are separated by spaces and combined with AND.
Filter keys (trace): model, provider, agent, agent.version, status, error.type, error.category, duration, tool.name, operation, namespace, cluster, service
Filter keys (metadata): generation_count, eval.passed, eval.evaluator_id, eval.score_key, eval.score
Operators: =, !=, >, <, >=, <=, =~ (regex)
Example: status = "error" agent = "claude-code"

Pagination: when a response has next_cursor, fetch the next page by calling the same operation again with cursor set to next_cursor. For 'search', also repeat the same filters, start_time, and end_time as the first call, using absolute RFC3339 times; relative ranges like now-24h shift between calls and the cursor will be rejected.

When to use:
- Debugging an AI application: find failing or low-rated conversations, then inspect their generations
- Reviewing evaluation results and user ratings across conversations

When NOT to use:
- Fetching a single generation or its evaluation scores (use agento11y_manage_generations)
```

#### `install_plugin` (tools/plugins.go, 198 chars)

```
Install a Grafana plugin by its plugin ID. If the version is not already confirmed with the user, omit it — the tool will look up the latest version and return it for confirmation before installing.
```

### Примечание по вариантам одного имени

- `alerting_manage_rules` вариант 1 (tools/alerting.go, 464 chars):

```
List and inspect Grafana alert rules with filtering capabilities.

When to use:
- Understanding why an alert is or isn't firing
- Auditing alert rule configuration (queries, conditions, labels, notification settings)
- Finding alert rules by state, folder, group, or name
- Comparing rule versions to see what changed

When NOT to use:
- Checking how alerts are routed to receivers (use alerting_manage_routing)
- Modifying or creating alert rules (read-only tool)
```

- `alerting_manage_rules` вариант 2 (tools/alerting.go, 461 chars):

```
Manage Grafana alert rules with full CRUD capabilities and filtering.

When to use:
- Understanding why an alert is or isn't firing
- Auditing alert rule configuration (queries, conditions, labels, notification settings)
- Finding alert rules by state, folder, group, or name
- Creating, updating, or deleting alert rules
- Comparing rule versions to see what changed

When NOT to use:
- Checking how alerts are routed to receivers (use alerting_manage_routing)
```

- `grafana_api_request` вариант 1 (tools/api.go, 224 chars):

```
Make an authenticated HTTP request to the Grafana API. Similar to 'gh api' for GitHub. Supports any Grafana API endpoint with optional jq-style response filtering. Use this for API endpoints that don't have a dedicated tool.
```

- `grafana_api_request` вариант 2 (tools/api.go, 255 chars):

```
Make an authenticated HTTP request to the Grafana API. Similar to 'gh api' for GitHub. Supports any Grafana API endpoint with optional jq-style response filtering. Use this for API endpoints that don't have a dedicated tool. Only GET requests are allowed.
```

- `generate_deeplink` вариант 1 (tools/navigation.go, 600 chars):

```
Generate deeplink URLs for Grafana resources. Supports dashboards (requires dashboardUid or provisioningPreview), panels (requires dashboardUid or provisioningPreview, plus panelId), and Explore queries (requires datasourceUid and optionally queries). For dashboard and panel links, provisioningPreview points at a dashboard staged on a provisioning repository branch (e.g. a git-sync PR preview). For explore links, the time range and queries are embedded inside the Grafana explore state. Set shorten=true to also attempt a /goto/<uid> short URL; if shortening fails, the full deeplink is returned.
```

- `generate_deeplink` вариант 2 (tools/navigation.go, 488 chars):

```
Generate deeplink URLs for Grafana resources. Supports dashboards (requires dashboardUid or provisioningPreview), panels (requires dashboardUid or provisioningPreview, plus panelId), and Explore queries (requires datasourceUid and optionally queries). For dashboard and panel links, provisioningPreview points at a dashboard staged on a provisioning repository branch (e.g. a git-sync PR preview). In read-only mode, shorten=true is accepted but ignored and the full deeplink is returned.
```
