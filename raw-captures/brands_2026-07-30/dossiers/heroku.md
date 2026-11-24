# UNIT: heroku | Heroku | github heroku/heroku-mcp-server | author type: official | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript repository, a real MCP server on the official SDK.
`src/index.ts`: `import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'`, `new McpServer({ name: 'Heroku MCP Server', version: VERSION }, { capabilities: { tools: { listChanged: true } } })`, transport `StdioServerTransport`, entry point `bin/heroku-mcp-server.mjs` → `dist/index.js`.
Tools are wrappers over Heroku CLI through a custom REPL (`src/repl/heroku-cli-repl.ts`).

## CHANNEL: instructions
(not found statically)

The `McpServer` constructor is called with two arguments: `{name, version}` and `{capabilities}`. There is no `instructions` field. Grep for `instructions` across all `src/`, `bin/`, `manifest.json`, `package.json` — 0 matches. The `initialize` handler is not manually overridden.

Related (not an instructions channel): one resource is registered —
`server.resource('heroku_dev_center', 'https://devcenter.heroku.com/llms.txt', { mimeType: 'text/plain', description: 'This resource provides a summary of Heroku Dev Center articles, and how to use Heroku.' }, ...)` (`src/resources/dev-center-resource.ts`). The resource body is pulled over the network at runtime (`fetch` llms.txt), not statically observable.

## CHANNEL: tool descriptions (coverage=full)

Registration pattern: `server.tool('<name>', '<description>', <zodSchema>.shape, handler)` in `src/tools/*.ts`.
There are 37 calls to `server.tool(` in total. `src/index.ts` registers 36 of them (3 AI tools — conditionally, only if the `@heroku/plugin-ai` plugin is installed). The 37th (`pipelines`, export `registerPipelinesTool` in `src/tools/pipelines.ts`) is not called in `index.ts` — marked below.

### src/tools/apps.ts
- **list_apps** — `List Heroku apps: owned, collaborator access, team/space filtering`
- **get_app_info** — `Get app details: config, dynos, addons, access, domains`
- **create_app** — `Create app: custom name, region (US/EU), team, private space`
- **rename_app** — `Rename app: validate and update app name`

### src/tools/maintenance.ts
- **maintenance_on** — `Enable maintenance mode and redirect traffic for a Heroku app`
- **maintenance_off** — `Disable maintenance mode and restore normal app operations`

### src/tools/logs.ts
- **get_app_logs** — `App logs: monitor/debug/filter by dyno/process/source`

### src/tools/spaces.ts
- **list_private_spaces** — `Lists Heroku Private Spaces with CIDR blocks, regions, compliance and capacity details. JSON output supported.`

### src/tools/teams.ts
- **list_teams** — `Lists accessible Heroku Teams. Use for: viewing teams, checking membership, getting team metadata, and verifying access. JSON output available.`

### src/tools/addons.ts
- **list_addons** — `List add-ons: all apps or specific app, detailed metadata`
- **get_addon_info** — `Get add-on details: plan, state, billing`
- **create_addon** — `Create add-on: specify service, plan, custom names`
- **list_addon_services** — `List available add-on services and features`
- **list_addon_plans** — `List service plans: features, pricing, availability`

### src/tools/data.ts
- **pg_psql** — `Execute SQL queries: analyze, debug, modify schema, manage data`
- **pg_info** — `View database status: config, metrics, resources, health`
- **pg_ps** — `Monitor active queries: progress, resources, performance`
- **pg_locks** — `Analyze locks: blocked queries, deadlocks, concurrency`
- **pg_outliers** — `Find resource-heavy queries: performance, patterns, optimization`
- **pg_credentials** — `Manage access: credentials, permissions, security, monitoring`
- **pg_kill** — `Stop processes: stuck queries, blocking transactions, runaway operations`
- **pg_maintenance** — `Track maintenance: windows, schedules, progress, planning`
- **pg_backups** — `Manage backups: schedules, status, verification, recovery`
- **pg_upgrade** — `Upgrade PostgreSQL: version migration, compatibility, safety`

### src/tools/ps.ts
- **ps_list** — `List and monitor Heroku app dynos. View running dynos, check status/health, monitor process states, verify configurations.`
- **ps_scale** — `Scale Heroku app dynos. Adjust quantities, change sizes, view formation details, manage resources.`
- **ps_restart** — `Restart Heroku app processes. Restart specific dynos, process types, or all dynos. Reset dyno states selectively.`

### src/tools/pipelines.ts
- **pipelines_create** — `Creates new Heroku deployment pipeline with configurable stages, apps, and team settings`
- **pipelines_promote** — `Promotes apps between pipeline stages with configurable target applications`
- **pipelines_list** — `Lists accessible Heroku pipelines with ownership and configuration details`
- **pipelines_info** — `Displays detailed pipeline configuration, stages, and connected applications`
- **pipelines** — `Lists and manages Heroku pipelines with configuration visibility` — NOT REGISTERED: `registerPipelinesTool` is not called in `src/index.ts`

### src/tools/deploy-to-heroku.ts
- **deploy_to_heroku** — the description is assembled by concatenating two literals directly in the `server.tool` call; the final string:
  `Use for all deployments. Deploys new/existing apps, with or without teams/spaces, and env vars to Heroku. Ask for app name if missing. Requires valid app.json via appJson param.`
- **deploy_one_off_dyno** — description is moved into the constant `execToolSchemaDescription` (`src/tools/deploy-to-heroku.ts:708`), a template string without interpolations, starts and ends with a newline. Verbatim:

~~~
Run code/commands in Heroku one-off dyno with network and filesystem access.

Requirements:
- Show command output
- Use app_info for buildpack detection
- Support shell setup commands
- Use stdout/stderr

Features:
- Network/filesystem access
- Environment variables
- File operations
- Temp directory handling

Usage:
1. Use Heroku runtime
2. Proper syntax/imports
3. Organized code structure
4. Package management:
   - Define dependencies
   - Minimize external deps
   - Prefer native modules

Example package.json:
```json
{
  "type": "module",
  "dependencies": {
    "axios": "^1.6.0"
  }
}
```
~~~

### src/tools/ai.ts (registered conditionally: only when the `@heroku/plugin-ai` plugin is installed)
- **list_ai_available_models** — `List available AI inference models`
- **provision_ai_model** — `Provision AI model access for app`
- **make_ai_inference** — `Make inference request to Heroku AI API`

## ADDITIONAL: manifest.json (DXT manifest, separate from runtime)

`manifest.json` contains its own `tools` array with a PARALLEL set of descriptions that differs from the code (e.g. `list_apps` → `List all Heroku apps. Filter by personal, collaborator, team, or space.`). This text does not enter the MCP protocol — the runtime returns strings from `src/tools/*.ts`. There are no `instructions` / `prompts` fields in the manifest.
