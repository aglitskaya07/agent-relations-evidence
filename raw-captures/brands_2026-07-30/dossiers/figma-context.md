# UNIT: figma-context | Figma (Framelink) | github GLips/Figma-Context-MCP | author type: community | captured 2026-07-29 (static source)

## SERVER CONFIRMED

Full-fledged MCP server in TypeScript. `src/mcp/index.ts:35` — `const server = new McpServer(serverInfo)` from `@modelcontextprotocol/sdk/server/mcp.js`; tool registration via `server.registerTool(...)`; stdio/http transports (`src/server.ts`, `src/cli.ts`/`src/bin.ts`). npm package `figma-developer-mcp`, manifest `server.json` with the modelcontextprotocol schema.

## CHANNEL: instructions
(not found statically)

Only `serverInfo` is passed to the `McpServer` constructor — an object without an `instructions` field:

```ts
const serverInfo = {
  name: "Figma MCP Server",
  version: process.env.NPM_PACKAGE_VERSION ?? "unknown",
  description:
    "Gives AI coding agents access to Figma design data, providing layout, styling, and content information for implementing designs.",
};
```

The `instructions` field does not occur anywhere in the source (the only match for the word is a comment about Sharp in `src/transformers/style/image.ts:180`). There is no manual `initialize` handler in the repository — the SDK generates the response.

For reference, `server.json` (registry manifest, not the initialize channel) contains:
`"description": "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot."`

## CHANNEL: tool descriptions (coverage=full)

A total of 2 tools (the second is registered conditionally — only if `--skip-image-downloads` is not set).

### 1. `get_figma_data`
Source: `src/mcp/tools/get-figma-data-tool.ts:109-115`, registration `src/mcp/index.ts:80-98` (title "Get Figma Data", `annotations: { readOnlyHint: true }`).

Literally:

```
Get comprehensive Figma file data including layout, content, visuals, and component information
```

### 2. `download_figma_images`
Source: `src/mcp/tools/download-figma-images-tool.ts:205-208` (the `getDescription(imageDir?)` function), registration `src/mcp/index.ts:101-119` (title "Download Figma Images", `annotations: { openWorldHint: true }`).

The description is assembled dynamically — a template string with insertion of the working directory (`imageDir ?? process.cwd()`). Verbatim:

```
Download SVG and PNG images used in a Figma file based on the IDs of image or icon nodes. Images will be saved relative to the server's image directory: ${baseDir}
```

where `const baseDir = imageDir ?? process.cwd();`

## PARAM DESCRIPTIONS (for reference, not tool-level)

Argument descriptions are set via zod `.describe(...)` — purely factual ("The key of the Figma file containing the images", "The ID of the Figma image node to fetch, formatted as 1234:5678", etc.), with no directive wording.
