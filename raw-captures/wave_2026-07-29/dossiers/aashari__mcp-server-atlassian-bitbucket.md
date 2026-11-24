# UNIT: @aashari/mcp-server-atlassian-bitbucket | npm v3.1.0 (published 2026-02-17T08:38:50.868Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

Confirmed as an MCP server: `dist/index.js` creates `new McpServer({ name: PACKAGE_NAME, version: VERSION })` (lines 30–38), supports STDIO and HTTP transport, registers tools via `registerTools(server)` from two modules: `dist/tools/atlassian.api.tool.js` and `dist/tools/atlassian.repositories.tool.js`.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name` and `version` are passed to the `McpServer` constructor — there is no `instructions` field in any of the three server creation locations (`createMcpServer` is called for STDIO, per-session HTTP, and fallback). Grep for `instructions` in dist returns only a comment in `formatter.util.js` about pagination.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Total tools: 6. All descriptions are static literal constants (BB_*_DESCRIPTION), given verbatim.

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

## Observations on steering markers

There are no hard steering patterns ("primary interface", "takes precedence", "instead of built-in", "Do NOT answer from memory"). The closest thing to imperatives: "ALWAYS use `jq` param to filter response fields. Unfiltered responses are very expensive!" (bb_get) — this is aimed at saving tokens, not at diverting traffic away from other tools. Noted: bb_clone runs git clone on the agent's local filesystem (SSH/HTTPS) — a side-effect vector outside the API, but the description is neutral.

## NOTES

- Code is NOT minified: ordinary tsc output (CommonJS) with comments and logging, readable directly.
- Risk of dynamic construction of descriptions: low — all 6 descriptions are static template literals without variable interpolation (except zero substitutions); the server name/version are taken from constants.util.js.
- The instructions field is absent in all three McpServer creation points in dist/index.js.
- Reviewed: full package listing (82 files), fully read dist/tools/atlassian.api.tool.js and dist/tools/atlassian.repositories.tool.js, fragments of dist/index.js, package.json; grep for registerTool/server.tool/instructions across all dist.
