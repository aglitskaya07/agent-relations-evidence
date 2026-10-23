# UNIT: @aashari/mcp-server-atlassian-bitbucket | npm v3.1.0 (published 2026-02-17T08:38:50.868Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

Подтверждён как MCP-сервер: `dist/index.js` создаёт `new McpServer({ name: PACKAGE_NAME, version: VERSION })` (строки 30–38), поддерживает STDIO и HTTP-транспорт, регистрирует инструменты через `registerTools(server)` из двух модулей: `dist/tools/atlassian.api.tool.js` и `dist/tools/atlassian.repositories.tool.js`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаются только `name` и `version` — поля `instructions` нет ни в одном из трёх мест создания сервера (`createMcpServer` вызывается для STDIO, per-session HTTP и fallback). Grep по `instructions` в dist даёт только комментарий в `formatter.util.js` про пагинацию.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего инструментов: 6. Все описания — статические литералы-константы (BB_*_DESCRIPTION), приведены дословно.

### bb_get (title: "Bitbucket GET Request", readOnlyHint: true)

```
Read any Bitbucket data. Returns TOON format by default (30-60% fewer tokens than JSON).

**IMPORTANT - Cost Optimization:**
- ALWAYS use `jq` param to filter response fields. Unfiltered responses are very expensive!
- Use `pagelen` query param to restrict result count (e.g., `pagelen: "5"`)
- If unsure about available fields, first fetch ONE item with `pagelen: "1"` and NO jq filter to explore the schema, then use jq in subsequent calls

**Schema Discovery Pattern:**
1. First call: `path: "/workspaces", queryParams: {"pagelen": "1"}` (no jq) - explore available fields
2. Then use: `jq: "values[*].{slug: slug, name: name, uuid: uuid}"` - extract only what you need

**Output format:** TOON (default, token-efficient) or JSON (`outputFormat: "json"`)

**Common paths:**
- `/workspaces` - list workspaces
- `/repositories/{workspace}` - list repos in workspace
- `/repositories/{workspace}/{repo}` - get repo details
- `/repositories/{workspace}/{repo}/pullrequests` - list PRs
- `/repositories/{workspace}/{repo}/pullrequests/{id}` - get PR details
- `/repositories/{workspace}/{repo}/pullrequests/{id}/comments` - list PR comments
- `/repositories/{workspace}/{repo}/pullrequests/{id}/diff` - get PR diff
- `/repositories/{workspace}/{repo}/refs/branches` - list branches
- `/repositories/{workspace}/{repo}/commits` - list commits
- `/repositories/{workspace}/{repo}/src/{commit}/{filepath}` - get file content
- `/repositories/{workspace}/{repo}/diff/{source}..{destination}` - compare branches/commits

**Query params:** `pagelen` (page size), `page` (page number), `q` (filter), `sort` (order), `fields` (sparse response)

**Example filters (q param):** `state="OPEN"`, `source.branch.name="feature"`, `title~"bug"`

**JQ examples:** `values[*].slug`, `values[0]`, `values[*].{name: name, uuid: uuid}`

The `/2.0` prefix is added automatically. API reference: https://developer.atlassian.com/cloud/bitbucket/rest/
```

### bb_post (title: "Bitbucket POST Request")

```
Create Bitbucket resources. Returns TOON format by default (token-efficient).

**IMPORTANT - Cost Optimization:**
- Use `jq` param to extract only needed fields from response (e.g., `jq: "{id: id, title: title}"`)
- Unfiltered responses include all metadata and are expensive!

**Output format:** TOON (default) or JSON (`outputFormat: "json"`)

**Common operations:**

1. **Create PR:** `/repositories/{workspace}/{repo}/pullrequests`
   body: `{"title": "...", "source": {"branch": {"name": "feature"}}, "destination": {"branch": {"name": "main"}}}`

2. **Add PR comment:** `/repositories/{workspace}/{repo}/pullrequests/{id}/comments`
   body: `{"content": {"raw": "Comment text"}}`

3. **Approve PR:** `/repositories/{workspace}/{repo}/pullrequests/{id}/approve`
   body: `{}`

4. **Request changes:** `/repositories/{workspace}/{repo}/pullrequests/{id}/request-changes`
   body: `{}`

5. **Merge PR:** `/repositories/{workspace}/{repo}/pullrequests/{id}/merge`
   body: `{"merge_strategy": "squash"}` (strategies: merge_commit, squash, fast_forward)

The `/2.0` prefix is added automatically. API reference: https://developer.atlassian.com/cloud/bitbucket/rest/
```

### bb_put (title: "Bitbucket PUT Request")

```
Replace Bitbucket resources (full update). Returns TOON format by default.

**IMPORTANT - Cost Optimization:**
- Use `jq` param to extract only needed fields from response
- Example: `jq: "{uuid: uuid, name: name}"`

**Output format:** TOON (default) or JSON (`outputFormat: "json"`)

**Common operations:**

1. **Update repository:** `/repositories/{workspace}/{repo}`
   body: `{"description": "...", "is_private": true, "has_issues": true}`

2. **Create/update file:** `/repositories/{workspace}/{repo}/src`
   Note: Use multipart form data for file uploads (complex - prefer PATCH for metadata)

3. **Update branch restriction:** `/repositories/{workspace}/{repo}/branch-restrictions/{id}`
   body: `{"kind": "push", "pattern": "main", "users": [{"uuid": "..."}]}`

The `/2.0` prefix is added automatically. API reference: https://developer.atlassian.com/cloud/bitbucket/rest/
```

### bb_patch (title: "Bitbucket PATCH Request")

```
Partially update Bitbucket resources. Returns TOON format by default.

**IMPORTANT - Cost Optimization:** Use `jq` param to filter response fields.

**Output format:** TOON (default) or JSON (`outputFormat: "json"`)

**Common operations:**

1. **Update PR title/description:** `/repositories/{workspace}/{repo}/pullrequests/{id}`
   body: `{"title": "New title", "description": "Updated description"}`

2. **Update PR reviewers:** `/repositories/{workspace}/{repo}/pullrequests/{id}`
   body: `{"reviewers": [{"uuid": "{user-uuid}"}]}`

3. **Update repository properties:** `/repositories/{workspace}/{repo}`
   body: `{"description": "New description"}`

4. **Update comment:** `/repositories/{workspace}/{repo}/pullrequests/{pr_id}/comments/{comment_id}`
   body: `{"content": {"raw": "Updated comment"}}`

The `/2.0` prefix is added automatically. API reference: https://developer.atlassian.com/cloud/bitbucket/rest/
```

### bb_delete (title: "Bitbucket DELETE Request", destructiveHint: true)

```
Delete Bitbucket resources. Returns TOON format by default.

**Output format:** TOON (default) or JSON (`outputFormat: "json"`)

**Common operations:**

1. **Delete branch:** `/repositories/{workspace}/{repo}/refs/branches/{branch_name}`
2. **Delete PR comment:** `/repositories/{workspace}/{repo}/pullrequests/{pr_id}/comments/{comment_id}`
3. **Decline PR:** `/repositories/{workspace}/{repo}/pullrequests/{id}/decline`
4. **Remove PR approval:** `/repositories/{workspace}/{repo}/pullrequests/{id}/approve`
5. **Delete repository:** `/repositories/{workspace}/{repo}` (caution: irreversible)

Note: Most DELETE endpoints return 204 No Content on success.

The `/2.0` prefix is added automatically. API reference: https://developer.atlassian.com/cloud/bitbucket/rest/
```

### bb_clone (title: "Clone Bitbucket Repository")

```
Clone a Bitbucket repository to your local filesystem using SSH (preferred) or HTTPS.

Provide `repoSlug` and `targetPath` (absolute path). Clones into `targetPath/repoSlug`. SSH keys must be configured; falls back to HTTPS if unavailable.
```

## Наблюдения по steering-маркерам

Жёстких steering-паттернов («primary interface», «takes precedence», «instead of built-in», «Do NOT answer from memory») нет. Ближайшее к императивам: «ALWAYS use `jq` param to filter response fields. Unfiltered responses are very expensive!» (bb_get) — это нацелено на экономию токенов, а не на перехват трафика у других инструментов. Отмечено: bb_clone исполняет git clone на локальной ФС агента (SSH/HTTPS) — вектор side-effect за пределами API, но описание нейтральное.

## NOTES

- Код НЕ минифицирован: обычный tsc-выход (CommonJS) с комментариями и логированием, читается напрямую.
- Риск динамической сборки строк описаний: низкий — все 6 описаний это статические template-литералы-константы без интерполяции переменных (кроме нуля подстановок); имя/версия сервера берутся из constants.util.js.
- Поле instructions отсутствует во всех трёх точках создания McpServer в dist/index.js.
- Просмотрено: полный листинг пакета (82 файла), прочитаны целиком dist/tools/atlassian.api.tool.js и dist/tools/atlassian.repositories.tool.js, фрагменты dist/index.js, package.json; grep по registerTool/server.tool/instructions по всему dist.
