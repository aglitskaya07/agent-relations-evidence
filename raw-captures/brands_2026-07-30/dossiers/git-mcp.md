# UNIT: git-mcp | GitMCP | github idosal/git-mcp | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript / Cloudflare Workers. `src/index.ts` — `export class MyMCP extends McpAgent { server = new McpServer({ name: "GitMCP", version: "1.1.0" }); ... }`; инструменты регистрируются через `this.server.tool(tool.name, tool.description, tool.paramsSchema, cb, { annotations })`. Транспорт — SSE/streamable HTTP через `MyMCP.serve("/*")`. Это MCP-сервер (remote, per-repo dynamic tooling).

Набор инструментов зависит от URL, по которому подключились: `getHandlerByRepoData()` выбирает handler (`default`, `generic` для `docs/`, `threejs` для `mrdoob/three.js`, `react-router` для `remix-run/react-router`). Ниже — все статически определённые описания по всем handler'ам.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `McpServer` получает только `{ name, version }` — поля `instructions` нет; собственного обработчика `initialize` в репозитории нет.

## CHANNEL: tool descriptions (coverage=full)

Всего статически определённых инструментов: 12 (уникальных по имени/описанию).

### A. DefaultRepoHandler (`src/api/tools/repoHandlers/DefaultRepoHandler.ts`), описания собираются генераторами из `src/api/tools/commonTools.ts`

Имена динамические: `fetch_<repo>_documentation`, `search_<repo>_documentation`, `search_<repo>_code` (иначе фолбэк `fetch_documentation` / `search_documentation` / `search_code`).

1. **`fetch_<repo>_documentation`** (`generateFetchToolDescription`) — три ветки:
   - urlType == "subdomain": `Fetch entire documentation file from the ${owner}/${repo} GitHub Pages. Useful for general questions. Always call this tool first if asked about ${owner}/${repo}.`
   - urlType == "github": `Fetch entire documentation file from GitHub repository: ${owner}/${repo}. Useful for general questions. Always call this tool first if asked about ${owner}/${repo}.`
   - default: `Fetch entire documentation for the current repository.`
   - catch-фолбэк: `Fetch documentation for the current repository.`

2. **`search_<repo>_documentation`** (`generateSearchToolDescription`) — три ветки:
   - urlType == "subdomain": `Semantically search within the fetched documentation from the ${owner}/${repo} GitHub Pages. Useful for specific queries.`
   - urlType == "github": `Semantically search within the fetched documentation from GitHub repository: ${owner}/${repo}. Useful for specific queries.`
   - default: `Semantically search within the fetched documentation for the current repository.`
   - catch-фолбэк: `Search documentation for the current repository.`

3. **`search_<repo>_code`** (`generateCodeSearchToolDescription`):
   `Search for code within the GitHub repository: "${owner}/${repo}" using the GitHub Search API (exact match). Returns matching files for you to query further if relevant.`

### B. Универсальный инструмент (`src/api/tools/index.ts`), добавляется ко ЛЮБОМУ handler'у

4. **`fetch_generic_url_content`**
   `Generic tool to fetch content from any absolute URL, respecting robots.txt rules. Use this to retrieve referenced urls (absolute urls) that were mentioned in previously fetched documentation.`

### C. GenericRepoHandler (`src/api/tools/repoHandlers/GenericRepoHandler.ts`) — активен для `docs/`

5. **`match_common_libs_owner_repo_mapping`**
   `Match a library name to an owner/repo. Don't use it if you have an owner and repo already. Use this first if only a library name was provided. If found - you can use owner and repo to call other tools. If not found - try to use the library name directly in other tools.`

6. **`fetch_generic_documentation`**
   `Fetch documentation for any GitHub repository by providing owner and project name`

7. **`search_generic_documentation`**
   `Semantically search in documentation for any GitHub repository by providing owner, project name, and search query. Useful for specific queries.`

8. **`search_generic_code`**
   `Search for code in any GitHub repository by providing owner, project name, and search query. Returns matching files. Supports pagination with 30 results per page.`

### D. ThreejsRepoHandler (`src/api/tools/repoHandlers/ThreejsRepoHandler.ts`) — активен для `mrdoob/three.js`

9. **`get_threejs_reference_docs_list`**
   `Get the reference docs list. This should be the first step. It will return a list of all the reference docs and manuals and their corresponding urls.`

10. **`get_threejs_specific_docs_content`**
    `Get the content of specific docs or manuals. This should be the second step. It will return the content of the specific docs or manuals. You can pass in a list of document or manual names.`

11. **`search_threejs_documentation`**
    `Semantically search the repository documentation for the given query. Use this if you need to find information you don't have in the reference docs.`

12. **`fetch_threejs_urls_inside_docs`**
    `Fetch content from URLs that are inside the reference docs. Usually contains '#' in the url. Returns the content of the pages as markdown.`

### E. ReactRouterRepoHandler (`src/api/tools/repoHandlers/ReactRouterRepoHandler.ts`)

Берёт все инструменты DefaultRepoHandler и заменяет search-инструмент своей реализацией с ТЕМ ЖЕ именем (`generateSearchToolName`) и ТЕМ ЖЕ описанием (`generateSearchToolDescription`) — новых описаний не вносит.

### F. Прочий текст, попадающий агенту (не description, а содержимое ответа)

`ThreejsRepoHandler.noopFallbackSearch` возвращает текстом:
`Please use the ${GET_REFERENCE_DOCS_LIST_TOOL_NAME} tool first to get the list of reference docs and manuals, and then use the ${GET_SPECIFIC_DOCS_CONTENT_TOOL_NAME} tool to get the content of the specific docs or manuals.`
(подставляются `get_threejs_reference_docs_list` и `get_threejs_specific_docs_content`)

### Annotations (title / readOnlyHint)

Все 12 инструментов помечены `readOnlyHint: true`, с человекочитаемыми title: Fetch Documentation, Search Documentation, Search Code, Fetch URL Content, Match Library to Repository, Fetch Generic Documentation, Search Generic Documentation, Search Generic Code, Get Three.js Reference Docs List, Get Three.js Specific Docs Content, Search Three.js Documentation, Fetch Three.js URLs Inside Docs.

## NOTES (static-extraction caveats)

- Язык репозитория: TypeScript (Cloudflare Workers + React Router UI); MCP SDK `@modelcontextprotocol/sdk/server/mcp.js` + `agents/mcp`.
- Определения найдены в: `src/index.ts` (конструктор сервера), `src/api/tools/index.ts`, `src/api/tools/commonTools.ts` (генераторы имён и описаний, стр. ~861–999), `src/api/tools/repoHandlers/{DefaultRepoHandler,GenericRepoHandler,ThreejsRepoHandler,ReactRouterRepoHandler,handlers,RepoHandler}.ts`.
- Риск динамической сборки строк: ВЫСОКИЙ по форме, низкий по содержанию. Имена и описания трёх основных инструментов собираются в рантайме из `owner`/`repo`, вычисленных из хоста/URL запроса, плюс имя усечается `enforceToolNameLengthLimit` до 55 символов. Итоговый текст, который видит клиент, статически не зафиксирован ни в одном литерале целиком — восстановлен из шаблонных строк. Набор инструментов также рантайм-зависим: подключение к `docs/`, `mrdoob/three.js` или `remix-run/react-router` даёт другой набор.
- `dist/server.js` и `dist/tools/index.js` — устаревший скомпилированный артефакт прежней stdio-версии (там `mcp.tool(...)`, описания вида `Fetch documentation from GitHub repository: ...` без «Always call this tool first»). В досье как источник истины не брал: актуальный код — `src/`. Расхождение отмечаю как сигнал, что описания в репо со временем усиливались.
- Просмотрено файлов: ~12 (полностью прочитаны 7 TS-файлов; grep по всем 57 TS/TSX в `src/` + `app/` на `description:` / `new McpServer` / `instructions`; `src/api/tools/repoHandlers/generic/static-mapping.json` — таблица библиотек, не описания инструментов; каталог `dist/` осмотрен grep'ом).
- Код не исполнялся.
