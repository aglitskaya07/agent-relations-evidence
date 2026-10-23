# UNIT: @payloadcms/plugin-mcp | npm v3.86.0 (published 2026-07-10T15:42:43.512Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (плагин)

Это MCP-сервер: плагин для Payload CMS, который монтирует MCP-эндпоинт внутри Payload-приложения через `createMcpHandler` из пакета `mcp-handler` (`src/mcp/getMcpHandler.ts:109`) и регистрирует инструменты через `server.registerTool(...)`. Не standalone-бинарь, а embedded-сервер: транспорт HTTP (basePath = API-роут Payload, SSE выключен по умолчанию), авторизация по API-ключам (коллекция `payload-mcp-api-keys`).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Поле `instructions` существует, но это сквозной проброс пользовательской конфигурации, не зашитая строка: тип `MCPServerOptions.instructions?: string` (`src/types.ts:377-379`, JSDoc: «Optional instructions describing how to use the server and its features.») передаётся в `createMcpHandler(..., { instructions: serverOptions.instructions, ... })` (`src/mcp/getMcpHandler.ts:530`). Дефолтного значения в пакете нет — если интегратор ничего не задал, instructions отсутствуют.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Особенность генерации: имена инструментов динамические — для каждой включённой коллекции создаются `create{Slug}` / `update{Slug}` / `find{Slug}` / `delete{Slug}` (например `findPosts`), для глобалов — `find{GlobalSlug}` / `update{GlobalSlug}`. Описание берётся из пользовательского `collections[slug].description`, а при его отсутствии — из статического шаблона в `src/mcp/tools/schemas.ts` (для глобалов — шаблон + пользовательское описание через `\n\n`). Ниже — ВСЕ 21 статический шаблон описаний, дословно:

Базовые (CRUD, генерируются по слагам):
1. `find{Global}` (findGlobal): "Find a Payload global singleton configuration."
2. `find{Collection}` (findResources): "Find documents in a collection by ID or where clause using Find or FindByID."
3. `create{Collection}` (createResource): "Create a document in a collection."
4. `update{Collection}` (updateResource): "Update documents in a collection by ID or where clause."
5. `delete{Collection}` (deleteResource): "Delete documents in a collection by ID or where clause."
6. `update{Global}` (updateGlobal): "Update a Payload global singleton configuration."

Экспериментальные (фиксированные имена; большинство только при NODE_ENV=development + explicit opt-in):
7. `createCollection`: "Creates a new collection with specified fields and configuration."
8. `findCollections`: "Finds and lists collections with optional content and document counts."
9. `updateCollection`: "Updates an existing collection with new fields, modifications, or configuration changes."
10. `deleteCollection`: "Deletes a collection and optionally updates the configuration."
11. `findConfig`: "Reads and displays the current configuration file."
12. `updateConfig`: "Updates the configuration file with various modifications."
13. `auth`: "Checks authentication status for the current user."
14. `login`: "Authenticates a user with email and password."
15. `verify`: "Verifies a user email with a verification token."
16. `resetPassword`: "Resets a user password with a reset token."
17. `forgotPassword`: "Sends a password reset email to a user."
18. `unlock`: "Unlocks a user account that has been locked due to failed login attempts."
19. `createJob`: "Creates a new job (task or workflow) with specified configuration."
20. `updateJob`: "Updates an existing job with new configuration, schema, or handler code."
21. `runJob`: "Runs a job with specified input data and queue options."

Маркер-скан стирающих/захватывающих формулировок (PRECEDENCE, "always default", "instead of built-in", "MUST use", "primary tool", "whenever the user" и т.д.) по src/ и README: 0 совпадений. Все описания — сухие функциональные однострочники без агент-стиринга.

## NOTES
- Код НЕ минифицирован: в tarball и src/ (TypeScript), и dist/ (читаемый ESM с sourcemaps).
- Риск динамической сборки строк: умеренный и по дизайну. Имена инструментов собираются из слагов коллекций в рантайме; описания и instructions могут полностью подменяться конфигом интегратора (`collections[slug].description`, `serverOptions.instructions`, плюс произвольные custom tools/prompts/resources через `pluginOptions.mcp`). Т.е. фактический стиринг конкретной инсталляции определяется интегратором, а не пакетом — пакет сам нейтрален.
- Просмотрено: ~12 файлов вглубь (getMcpHandler.ts, registerTool.ts, schemas.ts, types.ts, index.ts, defaults.ts, tools/resource/*, tools/global/find.ts, README.md, package.json-окрестности) + grep-скан всего src/ и README (всего в пакете ~40 исходных .ts + дублирующий dist).
