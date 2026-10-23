# UNIT: @storybook/mcp | npm v0.8.0 (published 2026-07-08T13:29:46.422Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Да, это MCP-сервер (фабрика HTTP-хендлера). `dist/index.js` создаёт `new McpServer({name, version, description}, { adapter, instructions, capabilities })` из пакета `tmcp` + `HttpTransport` (`@tmcp/transport-http`), регистрирует 3 инструмента через `server.tool(...)` и экспортирует `createStorybookMcpHandler`. Официальный пакет Storybook Core Team; отдаёт документацию компонентов из манифестов Storybook (`/manifests/components.json`, `/manifests/docs.json`).

## CHANNEL: instructions, npm (static, 1020 chars)

Передаётся конструктору `McpServer` как `instructions: instructions_default` (src: `dist/instructions-CiOmp0JI.js`, экспортируется также как `STORYBOOK_MCP_INSTRUCTIONS`). Дословно:

> ## Documentation Workflow
>
> **CRITICAL: Never hallucinate component properties!** Before using ANY property on a component (even common-sounding ones like `shadow`), you MUST verify it is documented via these tools. If it is not documented, it does not exist — never assume props from naming conventions or other libraries; report it to the user instead.
>
> 1. Call **list-all-documentation** once at the start of the task to discover available component and docs IDs.
> 2. Call **get-documentation** with an `id` from that list to retrieve full component docs, props, usage examples, and stories.
> 3. Call **get-documentation-for-story** for extra docs on a story variant not covered by the component docs.
>
> Only use properties explicitly documented or shown in example stories. Only reference IDs returned by these tools; never guess IDs.
>
> ## Multi-Source Requests
>
> - With multiple sources configured, **list-all-documentation** returns entries from every source; pass `storybookId` to **get-documentation** to scope one.

## CHANNEL: tool descriptions, npm (static, coverage=full)

3 инструмента (все ≤ 40, включены полностью, дословно).

### 1. `list-all-documentation` (title: "List All Documentation")

> List all available UI components and documentation entries from the Storybook, returning the IDs the other documentation tools take as input. Call this first for any UI task — before writing a new component, check what the design system already provides and build on it instead of hand-rolling a duplicate; before answering any question about props, API, or usage, discover the relevant IDs here rather than reading component source. Then fetch the entries with get-documentation, referencing only IDs returned here — never guess IDs. When multiple Storybook sources are configured, entries from every source are included; scope follow-up calls to one source via their `storybookId` input. Pass `withStoryIds: true` when you need story IDs for other tools.

Параметр `withStoryIds` (description): "When true, includes story sub-bullets under each component with story name and story ID. Use this to discover IDs for downstream story-focused workflows without filesystem lookup."

### 2. `get-documentation-for-story` (title: "Get Documentation for Story")

> Get detailed documentation for a specific story variant of a UI component. Use this when you need to see more usage examples of a component, via the stories written for it.

### 3. `get-documentation` (title: "Get Documentation")

> Get documentation for a UI component or docs entry.
>
> Returns the first 3 stories (including story IDs) with code snippets showing how props are used, plus TypeScript prop definitions. Call this before using a component to avoid hallucinating prop names, types, or valid combinations, and to answer any question about a component's props, API, or usage — reading or grepping the component source is not a substitute. Stories reveal real prop usage patterns, interactions, and edge cases that type definitions alone don't show. If the example stories don't show the prop you need, use the get-documentation-for-story tool to fetch the story documentation for the specific story variant you need.
>
> Example: id="button" returns Primary, Secondary, Large stories with code like <Button variant="primary" size="large"> showing actual prop combinations.

Примечание: в исходнике description для `get-documentation` собирается из template literal с подстановками `${MAX_STORIES_TO_SHOW}` (= 3) и `${GET_STORY_TOOL_NAME}` (= "get-documentation-for-story") — обе константы статические, значения подставлены выше.

Общий shared-параметр `storybookId` (multi-source режим, description): "The Storybook source ID (e.g., \"local\", \"tetra\"). Required when multiple Storybooks are composed. See list-all-documentation for available sources."

Параметр `id` у get-documentation (description): "The component or docs entry ID (e.g., \"button\")".

### Steering-маркеры (наблюдения)

- instructions: "**CRITICAL: Never hallucinate...** you MUST verify it is documented via these tools", "Call **list-all-documentation** once at the start of the task" — императивный workflow, но скоуп ограничен работой с компонентами.
- list-all-documentation: "Call this first for any UI task", "...discover the relevant IDs here rather than reading component source" — вытеснение локального чтения кода в пользу инструмента для любых UI-задач.
- get-documentation: "reading or grepping the component source is not a substitute" — то же вытеснение grep/read.
- Нет маркеров классов "instead of built-in web search", "primary interface", "PRECEDENCE", "LAST resort", рекламных "Perfect for/Great for", наград/кредитов, "ignore previous". Давление умеренное и доменно-релевантное (анти-галлюцинация пропсов).

## NOTES

- Код НЕ минифицирован: читаемый tsdown-бандл с сохранёнными JSDoc-комментариями, семантическими именами.
- Риск динамической сборки строк: низкий. Единственный template literal в description (`get-documentation`) использует только локальные статические константы; instructions — статический литерал в отдельном чанке.
- Просмотрено файлов: 5 из 6 в пакете полностью (package.json, dist/index.js, dist/instructions-CiOmp0JI.js, README.md — заголовок через ls, LICENSE не читал; index.d.ts — типы, не читал целиком, серверная логика вся в index.js).
- Пакет — библиотека/фабрика (экспортирует handler), нет собственного bin/stdio-энтрипоинта в опубликованной сборке (stdio-транспорт только в devDependencies); предназначен для встраивания в Storybook dev-server/addon. Тем не менее это серверный MCP-код с instructions и инструментами — классифицирован как сервер.
