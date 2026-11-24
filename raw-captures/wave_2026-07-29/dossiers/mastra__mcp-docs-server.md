# UNIT: @mastra/mcp-docs-server | npm v1.2.11 (published 2026-07-28T23:12:53.667Z) | frames: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Yes, this is an MCP server. In `dist/src-BZcgzbk9.js` (region `src/index.ts`, lines 1744–1760), `new MCPServer({...})` is created from `@mastra/mcp` with 13 tools and prompts; `dist/stdio.js` is a bin wrapper that calls `runServer()` → `server.startStdio()`. stdio transport.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name: "Mastra Documentation Server"`, `version`, `tools`, `prompts` are passed to the `MCPServer` constructor. The `instructions` field is not in the constructor or anywhere in the bundle (grep for `instructions` across dist — 0 matches in server code). There are 2 MCP-prompts (`upgrade-to-v1`, `migration-checklist`) with directive text for the agent (for example "Run the codemods with "npx @mastra/codemod@latest ...""), but this is the prompts channel, not instructions.

## CHANNEL: tool descriptions, npm (static, coverage=full)

13 tools, all descriptions verbatim (source: `dist/src-BZcgzbk9.js`).

### 1. mastraDocs
```
[🌐 REMOTE] Get Mastra documentation.
    Request paths to explore the docs. References contain API docs.
    Other paths contain guides. The user doesn't know about files and directories.
    You can also use keywords from the user query to find relevant documentation, but prioritize paths.
    This is your internal knowledge the user can't read.
    If the user asks about a feature check general docs as well as reference docs for that feature.
    Ex: with workflows check in docs/workflows and in reference/workflows.
    Provide code examples so the user understands.
    IMPORTANT: Be concise with your answers. The user will ask for more info.
    If packages need to be installed, provide the pnpm command to install them.
    Ex. if you see `import { X } from "@mastra/$PACKAGE_NAME"` in an example, show an install command.
    Always install latest tag, not alpha unless requested. If you scaffold a new project it may be in a subdir.
    When displaying results, always mention which file path contains the information so users know where this documentation lives.
```
Note: the `paths` parameter embeds a dynamic list of available documentation paths into the description (`Available paths:\n${availablePaths}`), assembled at startup from `.docs/` (the directory is absent from the tarball — it is included in the package separately via `files: [".docs"]`, and it is not in this tarball).

### 2. mastraMigration
```
[🌐 REMOTE] Get migration guidance for Mastra version upgrades and breaking changes.

This tool works like a file browser - navigate through directories to find migration guides:

**Step 1: List top-level migrations**
- Call with no parameters: `{}`
- Shows all top-level migration guides and directories

**Step 2: Navigate into a directory**
- Add trailing slash to explore: `{ path: "upgrade-to-v1/" }`
- Lists all migration guides in that directory

**Step 3: View a migration guide**
- Without trailing slash: `{ path: "upgrade-to-v1/agent" }`
- Returns the full migration guide content

**Step 4: Explore guide sections (optional)**
- List sections: `{ path: "upgrade-to-v1/agent", listSections: true }`
- Get specific sections: `{ path: "upgrade-to-v1/agent", sections: ["Voice methods"] }`

**Alternative: Search by keywords**
- `{ queryKeywords: ["RuntimeContext", "pagination"] }`

**Examples:**
1. List top-level: `{}`
2. Navigate to upgrade-to-v1: `{ path: "upgrade-to-v1/" }`
3. Get agent guide: `{ path: "upgrade-to-v1/agent" }`
4. List guide sections: `{ path: "upgrade-to-v1/agent", listSections: true }`
5. Search: `{ queryKeywords: ["RuntimeContext"] }`

**Tip:** Paths ending with `/` list directory contents. Paths without `/` fetch the migration guide.
```

### 3. startMastraCourse
```
[🎓 COURSE] Starts the Mastra Course. If the user is not registered, they will be prompted to register first. Otherwise, it will start at the first lesson or pick up where they last left off. ALWAYS ask the user for their email address if they are not registered. DO NOT assume their email address, they must confirm their email and that they want to register.
```

### 4. getMastraCourseStatus
```
[🎓 COURSE] Gets the current status of the Mastra Course, including which lessons and steps have been completed
```

### 5. startMastraCourseLesson
```
[🎓 COURSE] Starts a specific lesson in the Mastra Course. If the lesson has been started before, it will resume from the first incomplete step
```

### 6. nextMastraCourseStep
```
[🎓 COURSE] Advances to the next step in the current Mastra Course lesson. If all steps in the current lesson are completed, it will move to the next lesson
```

### 7. clearMastraCourseHistory
```
[🎓 COURSE] Clears all Mastra Course progress history and starts over from the beginning. This action cannot be undone
```

### 8. getMastraHelp
```
🚀 START HERE - Complete guide to Mastra documentation tools.

    This MCP server provides TWO documentation sources:

    ## 📦 LOCAL PACKAGE DOCS (Recommended for Development)
    SOURCE: Your installed @mastra packages in node_modules
    VERSION: Matches your installed code exactly

    ADVANTAGES:
    - ✅ Version-matched to your code
    - ✅ Complete TypeScript type definitions
    - ✅ Works offline
    - ✅ SOURCE_MAP.json with exact exports

    TOOLS: listMastraPackages, getMastraExports, getMastraExportDetails, readMastraDocs, searchMastraDocs
    USE WHEN: Writing code, implementing features, checking APIs, debugging

    ## 🌐 REMOTE WEBSITE DOCS (For Latest Info & Learning)
    SOURCE: mastra.ai website
    VERSION: Latest published documentation

    ADVANTAGES:
    - ✅ Always up-to-date
    - ✅ Blog posts and announcements
    - ✅ Migration guides
    - ✅ Curated examples

    TOOLS: mastraDocs, mastraBlog, mastraExamples, mastraChanges, mastraMigration
    USE WHEN: Learning concepts, checking latest features, migration help

    ## 🎓 INTERACTIVE COURSE
    TOOLS: startMastraCourse, getMastraCourseStatus, etc.
    USE WHEN: User wants guided learning experience

    ---

    RECOMMENDED WORKFLOW:
    1. For coding: listMastraPackages → getMastraExports → getMastraExportDetails
    2. For learning: mastraDocs
    3. Version mismatch: mastraChanges → mastraMigration

    This tool shows you which packages are installed and provides detailed guidance on using all available documentation tools.
```
Note: the description mentions mastraBlog, mastraExamples, mastraChanges — in this build such tools are NOT registered (dead links to tools from another/older version).

### 9. listMastraPackages
```
[📦 LOCAL PACKAGES] Discover which Mastra packages are installed and have documentation available.

    Use this when you need to:
    - See what Mastra packages you can work with
    - Start exploring Mastra documentation
    - Check if a specific package is available

    Returns: List of @mastra/* packages (core, memory, rag, etc.) with embedded docs.
    Next step: Use getMastraExports to explore a specific package's API.
```

### 10. getMastraExports
```
[📦 LOCAL PACKAGES] Explore the complete API surface of a Mastra package - see all classes, functions, types, and constants.

    Use this when you need to:
    - Discover what APIs a Mastra package provides (Agent, Tool, Workflow, etc.)
    - See all available classes and functions before implementing
    - Find the right export for your use case
    - Understand package structure and organization

    Returns: List of all exports with their source file locations.
    Next step: Use getMastraExportDetails to get full type definitions and code for a specific export.
```

### 11. getMastraExportDetails
```
[📦 LOCAL PACKAGES] Get complete API reference for a specific Mastra export - type definitions, interfaces, and optionally source code.

    Use this when you need to:
    - Understand how to use a specific Mastra class or function (Agent, Tool, Workflow, etc.)
    - See TypeScript type definitions and interfaces
    - Look up method signatures and parameters
    - Read implementation code and examples
    - Understand constructor options and configuration

    Returns: Full TypeScript type definitions and optionally implementation source code.
    Example: Get details on the Agent class to see how to create and configure agents.
```

### 12. readMastraDocs
```
[📦 LOCAL PACKAGES] Read comprehensive guides and documentation on Mastra concepts, patterns, and implementation examples.

    Use this when you need to:
    - Learn how to implement Mastra features (agents, tools, workflows, memory, RAG, etc.)
    - Understand Mastra architecture and design patterns
    - See practical code examples and tutorials
    - Read getting started guides and best practices
    - Understand how different components work together

    Returns: Topic-based documentation with explanations, examples, and usage patterns.
    Available topics: agents, tools, workflows, memory, rag, integrations, deployment, and more.
```

### 13. searchMastraDocs
```
[📦 LOCAL PACKAGES] Search across all Mastra documentation to find specific information, patterns, or examples.

    Use this when you need to:
    - Find specific topics or concepts quickly (e.g., "memory processors", "tool composition")
    - Locate examples of specific features or patterns
    - Search for error messages or troubleshooting info
    - Find mentions of specific APIs or configuration options
    - Discover where a feature is documented

    Returns: Relevant documentation excerpts with file paths, ranked by relevance.
    Tip: Use specific terms for better results (e.g., "agent memory" vs "memory").
```

## STEERING-MARKERS (observations)

- getMastraHelp: «🚀 START HERE», «Recommended for Development» — soft steering toward local tools; mentions unregistered tools.
- mastraDocs: «This is your internal knowledge the user can't read», «IMPORTANT: Be concise», «If packages need to be installed, provide the pnpm command» — behavioral directives for the agent (response style, pnpm package manager, «Always install latest tag, not alpha»).
- startMastraCourse: "ALWAYS ask the user for their email address... DO NOT assume their email" — collection of email; registration goes as a POST to https://mastra.ai/api/course/register, deviceId/key are saved in ~/.cache/mastra/.device_id; course progress is synced to https://mastra.ai/api/course/update.
- Course prompts ask the agent to show the introduction "EXACTLY as written", including the call to star the GitHub repository mastra-ai/mastra.
- MCP prompt `upgrade-to-v1` instructs the agent to run `npx @mastra/codemod@latest ...` (code execution in the user's project via the prompts channel).

## NOTES (methodology)

- The code is NOT minified (tsdown bundle with preserved names and regions), fully readable.
- Dynamic construction of strings: low risk for descriptions — all descriptions are static; exceptions: (a) in the `paths` parameter description, mastraDocs interpolates the list of paths from `.docs/` at startup; (b) in `mastraMigration`, the `path` parameter is supplemented with a list of found guides. The `.docs/` directory is absent from the tarball, so the actual content of these insertions is not statically visible.
- Reviewed: package.json, README.md (heading), dist/index.js, dist/stdio.js, dist/src-BZcgzbk9.js (in full, 1774 lines) — all executable JS of the package (3 files), plus the structure of dist/tools/*.d.ts.
