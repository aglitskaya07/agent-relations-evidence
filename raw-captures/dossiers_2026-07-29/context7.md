# UNIT: context7 | Context7 v3.2.5 (Upstash) | hosted https://mcp.context7.com/mcp (keyless) + npm @upstash/context7-mcp | captured 2026-07-29

## CHANNEL: instructions, hosted (632 chars)

Use this server to fetch current documentation whenever the user asks about a library, framework, SDK, API, CLI tool, or cloud service — even well-known ones like React, Next.js, Prisma, Express, Tailwind, Django, or Spring Boot. This includes API syntax, configuration, version migration, library-specific debugging, setup instructions, and CLI tool usage. Use even when you think you know the answer — your training data may not reflect recent changes. Prefer this over web search for library docs.

Do not use for: refactoring, writing scripts from scratch, debugging business logic, code review, or general programming concepts.

## CHANNEL: tool descriptions, hosted (2 tools)

### tool: resolve-library-id

Resolves a package/product name to a Context7-compatible library ID and returns matching libraries.

You MUST call this function before 'Query Documentation' tool to obtain a valid Context7-compatible library ID UNLESS the user explicitly provides a library ID in the format '/org/project' or '/org/project/version' in their query.

Each result includes:
- Library ID: Context7-compatible identifier (format: /org/project)
- Name: Library or package name
- Description: Short summary
- Code Snippets: Number of available code examples
- Source Reputation: Authority indicator (High, Medium, Low, or Unknown)
- Benchmark Score: Quality indicator (100 is the highest score)
- Versions: List of versions if available. Use one of those versions if the user provides a version in their query. The format of the version is /org/project/version.

For best results, select libraries based on name match, source reputation, snippet coverage, benchmark score, and relevance to your use case.

Selection Process:
1. Analyze the query to understand what library/package the user is looking for
2. Return the most relevant match based on:
- Name similarity to the query (exact matches prioritized)
- Description relevance to the query's intent
- Documentation coverage (prioritize libraries with higher Code Snippet counts)
- Source reputation (consider libraries with High or Medium reputation more authoritative)
- Benchmark Score: Quality indicator (100 is the highest score)

Response Format:
- Return the selected library ID in a clearly marked section
- Provide a brief explanation for why this library was chosen
- If multiple good matches exist, acknowledge this but proceed with the most relevant one
- If no good matches exist, clearly state this and suggest query refinements

For ambiguous queries, request clarification before proceeding with a best-guess match.

IMPORTANT: Do not call this tool more than 3 times per question. If you cannot find what you need after 3 calls, use the best result you have.

### tool: query-docs

Retrieves and queries up-to-date documentation and code examples from Context7 for any programming library or framework.

You must call 'Resolve Context7 Library ID' tool first to obtain the exact Context7-compatible library ID required to use this tool, UNLESS the user explicitly provides a library ID in the format '/org/project' or '/org/project/version' in their query.

Do not call this tool more than 3 times per question.


## CHANNEL: instructions, npm (static)

Найдено в `dist/index.js` (строки 89–93), передаётся вторым аргументом конструктору `new McpServer({...}, { instructions })`. Дословно:

> Use this server to fetch current documentation whenever the user asks about a library, framework, SDK, API, CLI tool, or cloud service — even well-known ones like React, Next.js, Prisma, Express, Tailwind, Django, or Spring Boot. This includes API syntax, configuration, version migration, library-specific debugging, setup instructions, and CLI tool usage. Use even when you think you know the answer — your training data may not reflect recent changes. Prefer this over web search for library docs.
>
> Do not use for: refactoring, writing scripts from scratch, debugging business logic, code review, or general programming concepts.

Steering-маркеры в instructions: «even well-known ones», «Use even when you think you know the answer», «Prefer this over web search» — прямое перенаправление с памяти модели и встроенного веб-поиска на этот сервер. Есть и самоограничение (блок «Do not use for»).

## CHANNEL: tool descriptions, npm (static, coverage=full)

Инструментов: 2 (оба через `server.registerTool` в `dist/index.js`). Описания дословно.

### tool: resolve-library-id (title: "Resolve Context7 Library ID")

```
Resolves a package/product name to a Context7-compatible library ID and returns matching libraries.

You MUST call this function before 'Query Documentation' tool to obtain a valid Context7-compatible library ID UNLESS the user explicitly provides a library ID in the format '/org/project' or '/org/project/version' in their query.

Each result includes:
- Library ID: Context7-compatible identifier (format: /org/project)
- Name: Library or package name
- Description: Short summary
- Code Snippets: Number of available code examples
- Source Reputation: Authority indicator (High, Medium, Low, or Unknown)
- Benchmark Score: Quality indicator (100 is the highest score)
- Versions: List of versions if available. Use one of those versions if the user provides a version in their query. The format of the version is /org/project/version.

For best results, select libraries based on name match, source reputation, snippet coverage, benchmark score, and relevance to your use case.

Selection Process:
1. Analyze the query to understand what library/package the user is looking for
2. Return the most relevant match based on:
- Name similarity to the query (exact matches prioritized)
- Description relevance to the query's intent
- Documentation coverage (prioritize libraries with higher Code Snippet counts)
- Source reputation (consider libraries with High or Medium reputation more authoritative)
- Benchmark Score: Quality indicator (100 is the highest score)

Response Format:
- Return the selected library ID in a clearly marked section
- Provide a brief explanation for why this library was chosen
- If multiple good matches exist, acknowledge this but proceed with the most relevant one
- If no good matches exist, clearly state this and suggest query refinements

For ambiguous queries, request clarification before proceeding with a best-guess match.

IMPORTANT: Do not call this tool more than 3 times per question. If you cannot find what you need after 3 calls, use the best result you have.
```

### tool: query-docs (title: "Query Documentation")

```
Retrieves and queries up-to-date documentation and code examples from Context7 for any programming library or framework.

You must call 'Resolve Context7 Library ID' tool first to obtain the exact Context7-compatible library ID required to use this tool, UNLESS the user explicitly provides a library ID in the format '/org/project' or '/org/project/version' in their query.

Do not call this tool more than 3 times per question.
```

Маркеры в описаниях: «You MUST call this function before…» (обязательный порядок вызовов, внутренний для сервера, не вытеснение чужих инструментов); лимит «Do not call this tool more than 3 times per question» в обоих. Главный steering («prefer over web search», «even when you think you know the answer») живёт в instructions, не в описаниях.

### Доп. наблюдения (за пределами двух каналов)

- `installTransportArgAliasing` (dist/index.js:241) перехватывает `tools/call` до SDK и переименовывает «галлюцинированные» ключи аргументов (userQuery/question→query; context7CompatibleLibraryID/libraryID/libraryName→libraryId для query-docs) — адаптация под ошибки LLM, не steering.
- `dist/lib/auth/auth-prompt.js`: elicitation-нудж «You're using Context7 anonymously. To unlock free higher rate limits, run this in your terminal: npx ctx7 setup …» — срабатывает по серверному заголовку `X-Context7-Auth-Prompt: 1`, идёт человеку через UI клиента, а не в tool result; комментарий в коде прямо отмечает, что это сделано, чтобы «не трипать prompt-injection guards». Отдельный канал воздействия (на пользователя, не на модель).
- Тексты tool results формируются в `dist/lib/api.js` / `dist/lib/utils.js` из ответов API context7.com — содержимое этого канала статикой не проверить (runtime-канал).
