# UNIT: vercel | Vercel Next.js DevTools | github vercel/next-devtools-mcp | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript MCP-сервер на `@modelcontextprotocol/sdk`. `src/index.ts:44` — `new Server({name: "next-devtools-mcp", version: pkg.version}, {capabilities: {tools: {}}})`, транспорт `StdioServerTransport`, обработчики `ListToolsRequestSchema` / `CallToolRequestSchema`. package.json: `next-devtools-mcp` v0.4.0.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `Server` получает только `{name, version}` и `{capabilities}` — поля `instructions` нет. Ответ `initialize` не переопределяется (кастомный хендлер отсутствует). В `server.json`, `.mcp.json`, `package.json` слова `instructions` нет.

Примечание: строка `instructions` встречается внутри JSON-ответов хендлеров (`browser-eval.ts`, `nextjs-docs.ts`) — это runtime tool-output, не канал server instructions.

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 4. Определения — через экспортируемый `metadata = { name, description }` в каждом файле `src/tools/*.ts`, агрегируются в массив `const tools = [browserEval, nextjsDocs, nextjsIndex, nextjsCall]` (`src/index.ts:25`) и отдаются в `ListTools` без модификаций.

### 1. `browser_eval`
(src/tools/browser-eval.ts:26)

```
Set up and use browser automation for this project via the agent-browser CLI.

This tool does NOT drive the browser itself. It points you at `agent-browser` — a fast, native browser-automation CLI built for agents (https://github.com/vercel-labs/agent-browser) — and tells you how to install it (if needed) and where to start. You then run its commands directly (you have shell access), which is faster and more capable than proxying automation through MCP.

Call this when you need to open pages, click, type, screenshot, or capture console errors in a real browser.
```

### 2. `nextjs_docs`
(src/tools/nextjs-docs.ts:29)

```
Find the version-accurate Next.js documentation for THIS project.

This tool does NOT fetch documentation. Next.js 16+ ships its full docs inside the installed package at `node_modules/next/dist/docs/` (markdown), kept in sync with the exact version you have installed. This tool tells you where those docs are and how to read them — so you read the docs that match this project, not a generic or outdated copy.

Call this before answering Next.js questions or writing Next.js code. Then read the relevant guide from the path it returns. If the project is on an older Next.js, it will tell you how to upgrade.
```

### 3. `nextjs_index`
(src/tools/nextjs_index.ts:19)

```
Discover all running Next.js development servers and list their available MCP tools.

WHEN TO USE THIS TOOL - Use proactively in these scenarios:

1. **Before implementing ANY changes to the app**: When asked to add, modify, or fix anything in the application:
   - "Add a loading state" → Check current component structure and routes first
   - "Fix the navigation" → Inspect existing routes and components
   - "Update the API endpoint" → Query current routes and data flows
   - "Add error handling" → Check runtime errors and component hierarchy
   - "Refactor the auth logic" → Inspect current auth implementation and routes
   - "Optimize performance" → Check runtime diagnostics and component tree
   Use this to understand where changes should be made and what currently exists.

2. **For diagnostic and investigation questions**:
   - "What's happening?" / "What's going on?" / "Why isn't this working?"
   - "Check the errors" / "See what's wrong"
   - "What routes are available?" / "Show me the routes"
   - "Clear the cache" / "Reset everything"
   - Questions about build status, compilation errors, or runtime diagnostics

3. **For agentic codebase search**: Use this as FIRST CHOICE for searching the currently running app. If not found, fallback to static codebase search tools.

KEY PRINCIPLE: If the request involves the running Next.js application (whether to investigate OR modify it), query the runtime FIRST to understand current state before proceeding.

REQUIREMENTS:
- Next.js 16 or later (MCP support was added in v16)
- If you're on Next.js 15 or earlier, upgrade first by running 'npx @next/codemod@latest upgrade latest'

Next.js 16+ exposes an MCP (Model Context Protocol) endpoint at /_next/mcp automatically when the dev server starts.
No configuration needed - MCP is enabled by default in Next.js 16 and later.

This tool discovers all running Next.js servers and returns:
- Server port, PID, and URL
- Complete list of available MCP tools for each server
- Tool descriptions and input schemas

After calling this tool, use 'nextjs_call' to execute specific tools.

[IMPORTANT] If auto-discovery returns no servers:
1. Ask the user which port their Next.js dev server is running on
2. Call this tool again with the 'port' parameter set to the user-provided port

If the MCP endpoint is not available:
1. Ensure you're running Next.js 16 or later (upgrade with 'npx @next/codemod@latest upgrade latest')
2. Verify the dev server is running (npm run dev)
3. Check that the dev server started successfully without errors
```

### 4. `nextjs_call`
(src/tools/nextjs_call.ts:24)

```
Call a specific MCP tool on a running Next.js development server.

REQUIREMENTS:
- Port number of the target Next.js dev server
- Tool name to execute
- Optional arguments object (if the tool requires parameters)

Use 'nextjs_index' first to discover available servers, tools, and their input schemas.
If 'nextjs_index' auto-discovery fails, ask the user for the port and call 'nextjs_index' again with the 'port' parameter.

IMPORTANT: When calling tools:
- The 'args' parameter MUST be an object (e.g., {key: "value"}), NOT a string
- If a tool doesn't require arguments, OMIT the 'args' parameter entirely - do NOT pass {} or "{}"
- Check the tool's inputSchema from 'nextjs_index' to see what arguments are required

Common Next.js MCP tools include:
- Error diagnostics (get compilation/runtime errors)
- Route information (list all routes)
- Build status (check compilation state)
- Cache management (clear caches)
- And more (varies by Next.js version)

Example usage:
1. Call 'nextjs_index' to see servers and tools
2. Call 'nextjs_call' with port=3000, toolName="get_errors" to get errors from server on port 3000
```

## SUPPLEMENTARY: runtime-injected guidance (не tool description, но попадает в контекст модели)

Хендлеры возвращают JSON с полями `instructions` / `ai_instruction`, формируемыми в коде:

- `nextjs-docs.ts:113` — `"Do not rely on training-data knowledge of Next.js APIs — this version may differ. Prefer the bundled docs."`
- `nextjs_index.ts:148-149` — `ai_instruction: "IMPORTANT: Server auto-discovery may not work on all operating systems or network configurations. Please ask the user: 'What port is your Next.js dev server running on?'. Once you have the port number, call this tool again with the 'port' parameter set to the user-provided port."`
- `browser-eval.ts:66-74` — набор инструкций по установке и запуску внешнего CLI `agent-browser` (`npm install -g agent-browser`).

## PARAM DESCRIPTIONS (для полноты)

- `browser_eval.task` — "Optional: what you want to do in the browser (e.g. 'open localhost:3000 and check for console errors'). Used only to tailor the guidance."
- `nextjs_docs.topic` — "Optional: what you're looking for (e.g. 'use cache', 'generateMetadata', 'middleware'). Used only to suggest where to look in the bundled docs."
- `nextjs_docs.project_path` — "Path to the Next.js project (defaults to current directory)"
- `nextjs_index.port` — "Optional port number to probe directly. Use this when auto-discovery fails - ask the user which port their Next.js dev server is running on."
- `nextjs_call.port` — "Port number of the Next.js dev server (required)."
- `nextjs_call.toolName` — "Name of the Next.js MCP tool to call (required). Use 'nextjs_index' first to discover available tool names."
- `nextjs_call.args` — "Arguments object to pass to the Next.js MCP tool. MUST be an object (e.g., {param: 'value'}), NOT a string. Only provide this parameter if the tool requires arguments - omit it entirely for tools that take no arguments. Use 'nextjs_index' to see the inputSchema for each tool."
