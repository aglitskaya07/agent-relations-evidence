# UNIT: @storybook/mcp | npm v0.8.0 (published 2026-07-08T13:29:46.422Z) | scopes: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Yes, this is an MCP server (HTTP handler factory). `dist/index.js` creates `new McpServer({name, version, description}, { adapter, instructions, capabilities })` from the `tmcp` package + `HttpTransport` (`@tmcp/transport-http`), registers 3 tools via `server.tool(...)`, and exports `createStorybookMcpHandler`. Official package by Storybook Core Team; serves component documentation from Storybook manifests (`/manifests/components.json`, `/manifests/docs.json`).

## CHANNEL: instructions, npm (static, 1020 chars)

Passed into the `McpServer` constructor as `instructions: instructions_default` (src: `dist/instructions-CiOmp0JI.js`, also exported as `STORYBOOK_MCP_INSTRUCTIONS`). Verbatim:

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

3 tools (all ≤ 40, included in full, verbatim).

### 1. `list-all-documentation` (title: "List All Documentation")

> List all available UI components and documentation entries from the Storybook, returning the IDs the other documentation tools take as input. Call this first for any UI task — before writing a new component, check what the design system already provides and build on it instead of hand-rolling a duplicate; before answering any question about props, API, or usage, discover the relevant IDs here rather than reading component source. Then fetch the entries with get-documentation, referencing only IDs returned here — never guess IDs. When multiple Storybook sources are configured, entries from every source are included; scope follow-up calls to one source via their `storybookId` input. Pass `withStoryIds: true` when you need story IDs for other tools.

Parameter `withStoryIds` (description): "When true, includes story sub-bullets under each component with story name and story ID. Use this to discover IDs for downstream story-focused workflows without filesystem lookup."

### 2. `get-documentation-for-story` (title: "Get Documentation for Story")

> Get detailed documentation for a specific story variant of a UI component. Use this when you need to see more usage examples of a component, via the stories written for it.

### 3. `get-documentation` (title: "Get Documentation")

> Get documentation for a UI component or docs entry.
>
> Returns the first 3 stories (including story IDs) with code snippets showing how props are used, plus TypeScript prop definitions. Call this before using a component to avoid hallucinating prop names, types, or valid combinations, and to answer any question about a component's props, API, or usage — reading or grepping the component source is not a substitute. Stories reveal real prop usage patterns, interactions, and edge cases that type definitions alone don't show. If the example stories don't show the prop you need, use the get-documentation-for-story tool to fetch the story documentation for the specific story variant you need.
>
> Example: id="button" returns Primary, Secondary, Large stories with code like <Button variant="primary" size="large"> showing actual prop combinations.

Note: in the source, the description for `get-documentation` is assembled from a template literal with substitutions `${MAX_STORIES_TO_SHOW}` (= 3) and `${GET_STORY_TOOL_NAME}` (= "get-documentation-for-story") — both constants are static, values are substituted above.

Shared parameter `storybookId` (multi-source mode, description): "The Storybook source ID (e.g., \"local\", \"tetra\"). Required when multiple Storybooks are composed. See list-all-documentation for available sources."

Parameter `id` for get-documentation (description): "The component or docs entry ID (e.g., \"button\")".

### Steering markers (observations)

- instructions: "**CRITICAL: Never hallucinate...** you MUST verify it is documented via these tools", "Call **list-all-documentation** once at the start of the task" — an imperative workflow, but the scope is limited to working with components.
- list-all-documentation: "Call this first for any UI task", "...discover the relevant IDs here rather than reading component source" — displacing local code reading in favor of the tool for any UI tasks.
- get-documentation: "reading or grepping the component source is not a substitute" — the same displacing of grep/read.
- There are no class markers "instead of built-in web search", "primary interface", "PRECEDENCE", "LAST resort", promotional "Perfect for/Great for", awards/credits, "ignore previous". The pressure is moderate and domain-relevant (anti-hallucination props).

## NOTES

- Code is NOT minified: readable tsdown bundle with preserved JSDoc comments and semantic names.
- Risk of dynamic string assembly: low. The only template literal in description (`get-documentation`) uses only local static constants; instructions are a static literal in a separate chunk.
- Reviewed files: 5 of 6 in the package in full (package.json, dist/index.js, dist/instructions-CiOmp0JI.js, README.md — heading via ls, LICENSE not read; index.d.ts — types, not read in full, all server logic is in index.js).
- The package is a library/factory (exports a handler), with no own bin/stdio entry point in the published build (stdio transport only in devDependencies); intended for embedding in the Storybook dev-server/addon. Nevertheless, this is server-side MCP code with instructions and tools — classified as a server.
