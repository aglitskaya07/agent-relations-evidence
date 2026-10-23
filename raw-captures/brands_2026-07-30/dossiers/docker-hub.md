# UNIT: docker-hub | Docker Hub | github docker/hub-mcp | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript. `src/server.ts:41` — `new Server({name:'dockerhub-mcp-server', version:'1.0.0'}, {capabilities:{tools:{}}})`, где `Server` = `McpServer` из `@modelcontextprotocol/sdk/server/mcp.js`. Транспорты: `StdioServerTransport` и `StreamableHTTPServerTransport` (`POST /mcp` через express). Инструменты регистрируются через `asset.RegisterTools()` в четырёх модулях: `src/repos.ts`, `src/accounts.ts`, `src/search.ts`, `src/scout.ts`.

## CHANNEL: instructions
(не обнаружены статически)

Второй аргумент конструктора `McpServer` содержит только `capabilities`; поля `instructions` нет. Грепы по `instructions` в `src/` и `package.json` — 0 совпадений. Обработчика `initialize` вручную нет (используется дефолт SDK).

## CHANNEL: tool descriptions (coverage=full)

13 инструментов (совпадает с `tools.txt`). Описания приведены дословно из вызовов `this.server.registerTool(...)` — это то, что реально уходит в `tools/list`.

Важное замечание об источнике: в корне репозитория есть сгенерированный `tools.json`, но он НЕ отражает боевые описания — генератор `src/scripts/toolsList.ts` подставляет `description: tool.title, // Use title instead of description to have less noise in the tools list`. Поэтому в `tools.json` вместо описаний лежат короткие тайтлы. Ниже — описания из исходников; для сравнения дан и тайтл из `tools.json`.

### 1. listRepositoriesByNamespace
`src/repos.ts:237`
> List paginated repositories by namespace

(в tools.json как description подставлен title: `List Repositories by Organisation (namespace)`; annotations.title: `List Repositories by Namespace`)

### 2. createRepository
`src/repos.ts:291`
> Create a new repository in the given namespace. You MUST ask the user for the repository name and if the repository has to be public or private. Can optionally pass a description.\nIMPORTANT: Before calling this tool, you must ensure you have:\n The repository name (name).

(в исходнике `\n` — экранированные переводы строки внутри одиночной кавычки; tools.json title: `Create a repository in organisation (namespace) or personal namespace`; annotations.title: `Create Repository in namespace`)

### 3. getRepositoryInfo
`src/repos.ts:309`
> Get the details of a repository in the given namespace.

(tools.json title: `Get Repository Details`; annotations.title: `Get Repository Info`)

### 4. updateRepositoryInfo
`src/repos.ts:334`
> Update the details of a repository in the given namespace. Description, overview and status are the only fields that can be updated. While description and overview changes are fine, a status change is a dangerous operation so the user must explicitly ask for it.

(tools.json title: `Update Repository Details`; annotations.title: `Get Repository Info`)

### 5. checkRepository
`src/repos.ts:378`
> Check if a repository exists in the given namespace.

(tools.json title: `Check Repository Exists`; annotations.title: `Check Repository Exists`)

### 6. listRepositoryTags
`src/repos.ts:395`
> List paginated tags by repository

(tools.json title: `List tags by repository`; annotations.title: `List Repository Tags`)

### 7. getRepositoryTag
`src/repos.ts:438`
> Get the details of a tag in a repository. It can be use to show the latest tag details for example.

(tools.json title: `Get Repository Tag Details`; annotations.title: `Get Repository Tag`)

### 8. checkRepositoryTag
`src/repos.ts:460`
> Check if a tag exists in a repository

(tools.json title: `Check Repository Tag Exists`; annotations.title: `Check Repository Tag`)

### 9. listNamespaces
`src/accounts.ts:61`
> List paginated namespaces

(tools.json title: `List organisations (namespaces) the user has access to`; annotations.title: `List Namespaces`)

### 10. getPersonalNamespace
`src/accounts.ts:86`
> Get the personal namespace name

(tools.json title: `Get user personal namespace`; annotations.title: `Get Personal Namespace`)

### 11. listAllNamespacesMemberOf
`src/accounts.ts:100`
> List all namespaces the user is a member of

(tools.json title: `List all organisations (namespaces) the user is a member of including personal namespace`; annotations.title: `List All Namespaces user is a member of`)

### 12. search
`src/search.ts:94`
> Search for repositories in Docker Hub. It sorts results by best match if no sort criteria is provided. If user asks for secure, production-ready images the "dockerHardenedImages" tool should be called first to get the list of DHI images available in the user organisations (if any) and fallback to search tool if no DHI images are available or user is not authenticated.

(tools.json title: `Search Repositories`; annotations.title: `Search Repositories`)

### 13. dockerHardenedImages
`src/scout.ts:61`
> This API is used to list Docker Hardened Images (DHIs) available in the user organisations. The tool takes the organisation name as input and returns the list of DHI images available in the organisation. It depends on the "listNamespaces" tool to be called first to get the list of organisations the user has access to.

(tools.json title: `List available Docker Hardened Images in user organisations`; annotations.title: `List available Docker Hardened Images`)
