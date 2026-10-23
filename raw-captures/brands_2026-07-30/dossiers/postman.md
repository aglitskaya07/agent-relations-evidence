# UNIT: postman | Postman | github postmanlabs/postman-mcp-server | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CHECK

MCP-сервер подтверждён: `src/index.ts` создаёт `new McpServer({ name: SERVER_NAME, version: APP_VERSION }, ...)` из `@modelcontextprotocol/sdk`, регистрирует 134 инструмента и MCP-ресурсы; TypeScript, stdio + HTTP.

## CHANNEL: instructions (195 chars)

Строка передана вторым аргументом конструктора `new McpServer(...)` в `src/index.ts:264-265` (только если файл `src/resources/Instructions.md` успешно прочитан):

```
Before answering any API-related questions, fetch the MCP resource at URI `postman://instructions` using FetchMcpResource from this MCP server, and follow the usage instructions contained within.
```

### Referenced resource: `postman://instructions` (src/resources/Instructions.md, 8370 chars)

Регистрируется как MCP-ресурс в `src/index.ts:494-503`. instructions-строка выше явно предписывает клиенту загрузить и следовать этому файлу, поэтому текст приведён дословно и целиком:

```markdown
# Postman MCP Server — Instructions

## What is Postman?

Postman is a comprehensive API platform used by developers and teams to design, build, test, document, and share APIs. It provides tools for making HTTP requests, organizing API endpoints into collections, managing environments and variables, creating mock servers, setting up monitors, and publishing API documentation.

## What is this MCP server?

This is a Model Context Protocol (MCP) server that exposes Postman's API as a set of tools you can invoke. It lets you interact with your Postman workspace programmatically — managing collections, environments, APIs, mocks, monitors, and more — all through structured tool calls.

## Postman elements

Postman organises API work around a set of core elements. Understanding these is key to using the MCP server effectively.

- **Workspace** — A shared space that groups related collections, environments, APIs, mocks, and monitors. Every element belongs to a workspace. Workspaces can be personal, team, partner, or public.
- **Collection** — An ordered set of API requests grouped into folders. Collections are the primary unit for organising, documenting, testing, and running API calls. Each collection can contain folders, requests, responses (saved examples), pre-request scripts, and tests.
- **Folder** — A logical grouping of requests inside a collection. Folders can be nested to create a hierarchy (e.g. by resource or feature).
- **Request** — A single API call definition inside a collection. It includes the HTTP method, URL, headers, query parameters, body, authorization settings, and optional pre-request/test scripts.
- **Response (saved example)** — A snapshot of a request/response pair saved inside a request. Saved examples are used by mock servers to return realistic responses and serve as inline documentation.
- **Environment** — A set of key-value variables scoped to a particular context (e.g. development, staging, production). Variables can be of type `default` or `secret`. Environments are applied to requests at runtime so you can switch contexts without editing URLs or headers.
- **API (Spec)** — A versioned API definition (OpenAPI, GraphQL SDL, etc.) managed inside Postman. An API can be linked to collections, environments, mocks, monitors, and documentation.
- **Mock server** — A simulated endpoint that returns responses based on the saved examples in a collection. Useful for front-end development and testing before the real API is ready.
- **Monitor** — A scheduled runner that executes a collection on a set interval and reports results. Monitors are used for uptime checks, integration tests, and alerting.
- **Tags** — Labels attached to collections or workspaces for categorisation and search. Tags make it easier to find related elements across the organisation.

## Private API Network
The Private API Network is an organisation-wide catalogue of approved APIs, collections, and workspaces. Teams publish elements to the Private API Network so others can discover and reuse them.

## Public API Network (Postman API Network)
The Public API Network is a collection of APIs and collections published by Postman and third-party developers. It's a public repository of APIs and collections that anyone can use.

## Finding APIs

These instructions apply any time the user wants to find, discover, or locate an API — whether internal or public.

**Do NOT rely on your own knowledge of available tools or APIs to answer questions like "is there an API for X?" or "find me an API that does Y."**
 Always search first using this workflow

**Follow the search workflow whenever the user:**
 - Asks to **find**, **discover**, **locate**, or **look up** an API
 - Asks **"is there an API for..."** or **"can I do X via an API?"**
 - Asks about capabilities that may or may not exist
 - Is unsure what API to use for a task

> **Anti-pattern to avoid:**
> User asks "Is there a bulk API for workspaces?" → You scan the tool list, don't see one, and say "No such API exists."
> Correct behavior: Follow the search workflow below, search the network, and only then draw conclusions.

---

### Decision Framework: Which Ownership to Use

Use the `searchPostmanElements` tool with the appropriate `ownership` and optional `filters` parameters.

**Default to `ownership: "organization"`** for all requests. Use filters to narrow the results.

#### Use `ownership: "organization"` (Default) When:

- The user asks to "find an API", "search for a service", or "look up an endpoint"
- The user mentions internal services (e.g., "find the notification service", "search for our payment API")
- The user wants to integrate with a team or company API
- The user says "find a trusted API for X" or "what APIs do we have for Y"
- The user references internal infrastructure, microservices, or team-shared resources
- The request is ambiguous — **always prefer organization scope**

**Narrow with filters as needed:**

| Goal                                                            | Filter to add                                           |
|-----------------------------------------------------------------|---------------------------------------------------------|
| Trusted internal APIs in the organization (Private API Network) | `filters: {"$and":[{"privateNetwork":{"$eq":true}}]}`   |
| All internal APIs in the organization                           | `filters: {"$and":[{"visibility":{"$eq":"internal"}}]}` |
| Publicly visible APIs (e.g. Stripe, GitHub)                     | `filters: {"$and":[{"visibility":{"$eq":"public"}}]}`   |
| Specific workspace                                              | `filters: {"$and":[{"workspaceId":{"$eq":"<id>"}}]}`    |
#### Use `ownership: "external"` When:

- The user explicitly wants to search beyond the organization (Third party APIs)
- The user asks for a well-known public API (e.g., "find the Stripe API", "search for the GitHub API")

**When in doubt, use `ownership: "organization"` first.** If no relevant results are found, broaden to `ownership: "all"` and try different visibility filters while letting the user know.

---

### Search Workflow

#### Step 1: Determine Search Ownership

Based on the user's request, decide which ownership to use using the decision framework above.

#### Step 2: Execute the Search

`searchPostmanElements(entityType, q, ownership: organization, filters?)`
- Use `entityType: "collections"` to find API collections (recommended starting point)
- Use `entityType: "requests"` to find specific API requests
- Use `entityType: "workspaces"`, `"apis"`, `"specs"`, `"flows"`, `"environments"`, or `"mocks"` for other entity types
- Craft a concise, relevant search query from the user's intent (e.g., "notification", "payment", "authentication")
- For Private API Network results: add `filters: {"$and":[{"privateNetwork":{"$eq":true}}]}`
- For internally visible APIs (e.g. API of another team in the organization): add `filters: {"$and":[{"visibility":{"$eq":"internal"}}]}`
- For publicly visible APIs (e.g. Stripe, GitHub): add `filters: {"$and":[{"visibility":{"$eq":"public"}}]}`
- To filter by workspace: add `filters: {"$and":[{"workspaceId":{"$eq":"<id>"}}]}`

#### Step 3: Present Results

- Summarize the search results clearly to the user
- Highlight the most relevant matches based on the user's intent
- If multiple results are found, briefly describe each and ask the user which one to explore
- If no results are found, broaden to `ownership: "all"` with different visibility filters and let the user know

#### Step 4: Explore the Selected API

Once the user selects a collection:

1. `getCollection(collectionId)` — Fetch collection details with the recursive itemRefs index
2. `getCollectionRequest(requestId, collectionId, uid: true, populate: false)` — Explore individual requests
3. `getCollectionFolder(folderId, collectionId, uid: true, populate: false)` — Explore folders

**IMPORTANT:** After establishing a collection, do NOT call `searchPostmanElements` again to find requests within it. Use `getCollectionRequest` and `getCollectionFolder` to navigate the collection's contents.

- **Never conclude that an API doesn't exist based solely on the MCP tool list.** The tool list covers tools for *using* Postman, not the full universe of APIs your organization may have published. Always search before concluding.
```

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов: 134 (> 40), суммарно ~41266 символов описаний. Полный маркер-скан по всем 134 описаниям выполнен; ниже все совпадения и 10 репрезентативных полных описаний.

### Полный список имён инструментов

```
addWorkspaceToPrivateNetwork, createCollection, createCollectionComment, createCollectionFolder, createCollectionFork, createCollectionRequest, createCollectionResponse, createEnvironment, createFolderComment, createMock, createMockServerResponse, createMonitor, createRequestComment, createResponseComment, createSpec, createSpecFile, createWorkspace, deleteApiCollectionComment, deleteCollection, deleteCollectionComment, deleteCollectionFolder, deleteCollectionRequest, deleteCollectionResponse, deleteEnvironment, deleteFolderComment, deleteMock, deleteMockServerResponse, deleteMonitor, deleteRequestComment, deleteResponseComment, deleteSpec, deleteSpecFile, deleteWorkspace, duplicateCollection, generateCollection, generateSpecFromCollection, getAllSpecs, getAnalyticsData, getAnalyticsMetadata, getApiDiscoveryInstructions, getAsyncSpecTaskStatus, getAuthenticatedUser, getCodeGenerationInstructions, getCollection, getCollectionComments, getCollectionContext, getCollectionFolder, getCollectionForks, getCollectionRequest, getCollectionResponse, getCollectionTags, getCollectionUpdatesTasks, getCollections, getCollectionsForkedByUser, getDuplicateCollectionTaskStatus, getEnabledTools, getEnvironment, getEnvironmentContext, getEnvironments, getFolderComments, getFolderContext, getGeneratedCollectionSpecs, getInstalledApiMaintenanceInstructions, getMock, getMockServerResponse, getMockServerResponses, getMocks, getMonitor, getMonitorRunResults, getMonitors, getPostmanContextOverview, getRequestCodeContext, getRequestComments, getRequestContext, getResponseComments, getResponseContext, getSourceCollectionStatus, getSpec, getSpecCollections, getSpecDefinition, getSpecFile, getSpecFiles, getStatusOfAnAsyncApiTask, getTaggedEntities, getWorkspace, getWorkspaceContext, getWorkspaceEnvironmentsContext, getWorkspaceGlobalVariables, getWorkspaceTags, getWorkspaces, getWorkspacesContext, listMonitorExecutions, listPrivateNetworkAddRequests, listPrivateNetworkWorkspaces, listRunsForExecution, mergeCollectionFork, patchCollection, patchEnvironment, publishDocumentation, publishMock, pullCollectionChanges, putCollection, putEnvironment, removeWorkspaceFromPrivateNetwork, resolveCommentThread, respondPrivateNetworkAddRequest, runCollection, runMonitor, searchLearningCenter, searchPostmanElements, syncCollectionWithSpec, syncSpecWithCollection, transferCollectionFolders, transferCollectionRequests, transferCollectionResponses, unpublishDocumentation, unpublishMock, updateApiCollectionComment, updateCollectionComment, updateCollectionFolder, updateCollectionRequest, updateCollectionResponse, updateCollectionTags, updateFolderComment, updateMock, updateMockServerResponse, updateMonitor, updateRequestComment, updateResponseComment, updateSpecFile, updateSpecProperties, updateWorkspace, updateWorkspaceGlobalVariables, updateWorkspaceTags
```

### Marker scan: совпадений 6

- **createMock** — дословно: «…he bare collection ID. - If you only have a \`collectionId\`, resolve the UID first:   1) Prefer GET \`/collections/{collectionId}\` and read \`uid\`, or   2) Construct \`{ownerId}-{coll…»
- **createMock** — дословно: «…d = me.user.id\` - Use the \`workspace\` query to place the mock in a specific workspace. Prefer explicit workspace scoping.…»
- **getAnalyticsData** — дословно: «…models_by_usage\`, \`activity_distribution\`, \`peak_activity\`, \`usage_leaderboard\`, \`credit_usage_by_model\`, \`messages_sent\`, \`credit_usage\`, \`agent_mode_sessions\`, \`new_vs_…»
- **getAnalyticsData** — дословно: «…\`peak_activity\`, \`usage_leaderboard\`, \`credit_usage_by_model\`, \`messages_sent\`, \`credit_usage\`, \`agent_mode_sessions\`, \`new_vs_returning_users\`, \`agent_mode_users\`  The \…»
- **getMocks** — дословно: «…workspaces.  - Always pass either the \`workspace\` or \`teamId\` query to scope results. Prefer \`workspace\` when known. - If you need team-scoped results, set \`teamId\` from the curr…»
- **putCollection** — дословно: «…e existing items and creates new items.  - To perform an update asynchronously, use the \`Prefer\` header with the \`respond-async\` value. When performing an async update, this endpoint…»

Все совпадения носят технический характер (HTTP-заголовок `Prefer`, рекомендация скоупить запрос по workspace, названия метрик биллинга Postman) и не являются директивами перенаправления агента.

### 10 репрезентативных полных описаний

#### searchPostmanElements

```
Search for Postman entities (requests, collections, workspaces, specs, flows, environments, and mocks).

**Ownership:**
- `organization` — Search within all resources owned by your organization (default).
- `external` — Search within the public Postman network (third-party and community APIs).
- `all` — Search across all scopes.

**When to use each ownership value and filters:**

| Goal | Recommended approach |
|------|----------------------|
| Find an internal API (e.g. "our notification service") | `ownership: organization` |
| Find a trusted API published to the Private Network | `ownership: organization` + `privateNetwork: true` filter |
| Find an internal API in all resources of organization and are visible to the organization only | `ownership: organization` + `visibility: internal` filter |
| Find an API by your organization that is made publicly visible | `ownership: organization` + `visibility: public` filter |
| Find a third party publicly visible API (e.g. "Stripe API", "Twilio API") | `ownership: external` + `visibility: public` filter |
| User says "our APIs", "internal", "team" | `ownership: organization` |
| Search across all scopes | `ownership: all` |

**Element Types:**
- `requests`: Search for individual API requests.
- `collections`: Search for API collections.
- `workspaces`: Search for Postman workspaces.
- `specs`: Search for API specifications.
- `flows`: Search for Postman Flows.
- `environments`: Search for Postman Environments.
- `mocks`: Search for Postman Mock Servers.

**Filters:**

Use the `filters` parameter to narrow results. The top-level key must be `$and` with an array of condition objects. Each condition object must contain exactly one field key.

Supported filter fields:
| Field | Operators | Notes |
|-------|-----------|-------|
| `workspaceId` | `$eq`, `$ne`, `$in`, `$nin` | All element types. `$in`/`$nin` accept arrays. |
| `collectionId` | `$eq`, `$ne`, `$in`, `$nin` | Requests and collections only. |
| `visibility` | `$eq`, `$ne` | Values: `public`, `partner`, `internal`. All element types. |
| `privateNetwork` | `$eq`, `$ne` | Boolean. All element types. |
| `publisherIsVerified` | `$eq`, `$ne` | Boolean. All element types. |
| `method` | `$eq`, `$ne`, `$in`, `$nin` | HTTP methods (GET, POST, etc.). Requests only. |
| `tags` | `$eq`, `$ne`, `$in`, `$nin` | Workspaces and collections only. |
| `requestId` | `$eq`, `$ne`, `$in`, `$nin` | Requests only. |
| `specificationId` | `$eq`, `$ne`, `$in`, `$nin` | Specs only. |
| `flowId` | `$eq`, `$ne`, `$in`, `$nin` | Flows only. |
| `createdBy` | `$eq`, `$ne`, `$in`, `$nin` | All element types. |
| `organizationId` | `$eq`, `$ne`, `$in`, `$nin` | All element types. |
| `teamId` | `$eq`, `$ne`, `$in`, `$nin` | All element types. |
| `isGitConnected` | `$eq`, `$ne` | Boolean. Workspaces, collections, requests, specs, flows, environments, mocks. |
| `type` | `$eq`, `$ne`, `$in`, `$nin` | Requests only. |

**Filter examples:**
- Private API Network only: `{"$and":[{"privateNetwork":{"$eq":true}}]}`
- Single workspace: `{"$and":[{"workspaceId":{"$eq":"ws-abc123"}}]}`
- Multiple workspaces: `{"$and":[{"workspaceId":{"$in":["ws-1","ws-2"]}}]}`
- Public visibility: `{"$and":[{"visibility":{"$eq":"public"}}]}`
- GET requests only: `{"$and":[{"method":{"$eq":"GET"}}]}`
- Combine conditions: `{"$and":[{"visibility":{"$eq":"public"}},{"workspaceId":{"$eq":"ws-abc123"}}]}`
- Environments in a workspace: `{"$and":[{"workspaceId":{"$eq":"ws-abc123"}}]}`
```

#### getPostmanContextOverview

```
Returns the Postman Context overview (markdown). Explains the core concepts (workspaces, collections, requests, installed code) and the end-to-end workflow for finding APIs, generating client code, and maintaining installed requests over time.

Call this FIRST — and only — when the user wants to explore APIs in Postman's network, answer questions about how an API works, plan an integration, or generate client code grounded in real Postman API definitions, AND you have not already loaded the overview in this session. Do NOT call this for routine Postman operations like listing or editing workspaces, collections, environments, mocks, monitors, or specs — go straight to the relevant resource tool. After reading the overview, route to the appropriate topic-specific instructions tool: getApiDiscoveryInstructions (find/search/compare APIs), getCodeGenerationInstructions (generate client code from a request), or getInstalledApiMaintenanceInstructions (list, update, or remove installed requests).
```

#### getCollection

```
Get information about a collection. By default this tool returns the lightweight collection map (metadata + recursive itemRefs).
Use the model parameter to opt in to Postman's full API responses:
- model=minimal — root-level folder/request IDs only
- model=full — full Postman collection payload.
```

#### getCollections

```
The workspace ID query is required for this endpoint. If not provided, the LLM should ask the user to provide it.
```

#### getApiDiscoveryInstructions

```
Returns instructions (markdown) for finding APIs in Postman — searching the public network, browsing private/internal/team collections, filtering by ownership and visibility, and comparing candidate APIs. Includes the rules for presenting results with Postman links and the patterns for evaluating tradeoffs between APIs.

Call this when the user wants to find, search for, or compare APIs (e.g., "find me an email API", "search for the Payvance API", "compare Payvance and Cashloom"). Prerequisite: call getPostmanContextOverview first if you have not already loaded the Postman Context overview in this session.
```

#### getCodeGenerationInstructions

```
Returns the full workflow instructions for discovering APIs, exploring collections, and generating client code from Postman. Includes step-by-step guidance, tool usage patterns, and code generation rules.

MANDATORY: You MUST call this tool when the user says to "use postman", or when the user wants to do something that requires locating a specific API for the purpose of answering questions, planning a build, and in most cases proceeding to generate code that calls the API. ALWAYS call getCodeGenerationInstructions BEFORE calling other tools in this workflow. This tool returns comprehensive step-by-step instructions on how to search for APIs, gather API-specific context from other tools, and then generate client code based on the context retrieved.
```

#### getInstalledApiMaintenanceInstructions

```
Returns instructions (markdown) for maintaining the API requests already installed in the user's project — listing installed requests, checking installed requests against their Postman sources for upstream changes, finding unused requests, and safely removing installed requests. Installed requests are identifiable by a "Generated by Postman Code" comment in the file header.

Call this when the user wants to manage existing integrations (e.g., "what requests do we have installed?", "are my API integrations up to date?", "find unused Postman requests", "remove the Payvance requests"). Prerequisite: call getPostmanContextOverview first if you have not already loaded the Postman Context overview in this session.
```

#### searchLearningCenter

```
Search the official Postman documentation and learning resources at https://learning.postman.com.

Use this tool when you need authoritative, up-to-date guidance on how to use Postman features — for example creating mock servers, writing tests, using environments, configuring monitors, or any "how do I…" question about the Postman product. Returns relevant documentation passages with their source URLs.

Do not use this tool to search a user's own Postman resources (collections, workspaces, specs) — use `searchPostmanElements` for that.
```

#### getAnalyticsData

```
Gets analytics data based on the specified resource, metrics, and given filters for team, internal, and public workspaces, as well as Partner Workspaces.

**Note:**

This endpoint only accepts the following resource:metric query parameter combinations:
- \`user\` — \`workspace_active_users\`, \`active_users\`
- \`workspace\` — \`elements_in_workspace\`, \`active_workspaces\`, \`api_calls\`, \`active_collections\`, \`response_status\`, \`pending_invites\`, \`needs_attention\`, \`success_rate\`, \`user_requests\`, \`collection_error_aggregate\`
- \`team\` — \`user_api_journey\`, \`workspace_distribution\`, \`internal_workspace_distribution\`, \`license_consumption\`, \`members\`, \`last_autoflex_cycle\`, \`partner_engagement_funnel\`
- \`ai\` — \`top_agent_models_by_usage\`, \`activity_distribution\`, \`peak_activity\`, \`usage_leaderboard\`, \`credit_usage_by_model\`, \`messages_sent\`, \`credit_usage\`, \`agent_mode_sessions\`, \`new_vs_returning_users\`, \`agent_mode_users\`

The \`view\` query parameter only accepts the following values when called with the following resource:metric pairs:
- \`detailed\` or \`summary\` — \`user:active_users\`, \`workspace:active_workspaces\`, \`workspace:pending_invites\`, \`workspace:needs_attention\`, \`workspace:success_rate\`, \`team:partner_engagement_funnel\`
\`summary\` only — \`workspace:elements_in_workspace\`, \`workspace:workspace_active_users\`, \`workspace:api_calls\`, \`workspace:response_status\`, \`team:user_api_journey\`, \`team:workspace_distribution\`, \`team:internal_workspace_distribution\`, \`team:license_consumption\`
- \`detailed\` only — \`workspace:active_collections\`, \`workspace:user_requests\`
```

#### createMock

```
Creates a mock server in a collection.

- Pass the collection UID (ownerId-collectionId), not the bare collection ID.
- If you only have a \`collectionId\`, resolve the UID first:
  1) Prefer GET \`/collections/{collectionId}\` and read \`uid\`, or
  2) Construct \`{ownerId}-{collectionId}\` using ownerId from GET \`/me\`:
    - For team-owned collections: \`ownerId = me.teamId\`
    - For personal collections: \`ownerId = me.user.id\`
- Use the \`workspace\` query to place the mock in a specific workspace. Prefer explicit workspace scoping.
```
