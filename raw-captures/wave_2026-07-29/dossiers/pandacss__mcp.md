# UNIT: @pandacss/mcp | npm v1.12.0 (published 2026-07-29T04:27:43.890Z) | scopes: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server
Yes, a full stdio MCP server: `new McpServer({ name: "@pandacss/mcp", version: "1.0.0" })` from `@modelcontextprotocol/sdk/server/mcp.js` + `StdioServerTransport` (dist/index.js:55-58, 184). CLI (`panda-mcp`, bin.js → dist/cli.js) — server startup + `init` command, writing config into .mcp.json/.cursor/.vscode/.windsurf/.codex. Official Panda CSS package (repo chakra-ui/panda, packages/mcp).

## CHANNEL: instructions, npm (static)
(not found statically)

The McpServer constructor receives only `{ name, version }` — there is no `instructions` field in any bundle; grep for the word `instructions` in the entire package — 0 matches.

## CHANNEL: tool descriptions, npm (static, coverage=full)
12 tools (registerTool), descriptions verbatim; identical in all three bundles (dist/index.js, dist/cli.js, dist/chunk-IBM3OGUU.mjs):

1. `get_tokens` — "Get all design tokens with their values, CSS variables, and usage examples"
2. `get_semantic_tokens` — "Get semantic tokens with their conditional values (responsive, color modes)"
3. `get_recipes` — "Get component recipes with their variants, default values, and usage examples"
4. `get_patterns` — "Get layout patterns with their properties and usage examples"
5. `get_conditions` — "Get all conditions (breakpoints, pseudo-classes, color modes) and their CSS values"
6. `get_keyframes` — "Get keyframe animations defined in the theme"
7. `get_text_styles` — "Get text style compositions for typography"
8. `get_layer_styles` — "Get layer style compositions for visual styling"
9. `get_animation_styles` — "Get animation style compositions"
10. `get_color_palette` — "Get the color palette with all color values"
11. `get_config` — "Get the resolved Panda CSS configuration including paths, JSX settings, and output options"
12. `get_usage_report` — "Get a usage report of design tokens and recipes across the codebase. Shows which tokens/recipes are used, unused, or missing. Useful for auditing, cleanup, and identifying dead code."

Parameter descriptions (schema .describe): "Filter by token category", "Filter by recipe name", "Filter by pattern name", "Analysis scope: token, recipe, or all (default)".

## STEERING-MARKERS
None found. No matches on the marker regexes (primary/precedence/MUST use/prefer/instead of built-in, etc.). The descriptions are dry, factual, without pressure toward choosing a tool. The only mildly promotional phrase is "Useful for auditing, cleanup, and identifying dead code" in get_usage_report; in the init-command outro: "MCP setup complete! Your AI assistants can now use Panda CSS tools." (this is output to the user in the terminal, not a channel to the model).

## NOTES
- The code is not minified — readable tsup bundle, names and strings preserved.
- Risk of dynamic construction of descriptions: low. All descriptions are static literals. The only dynamic part is the enum schemas recipeNameSchema/patternNameSchema are built from the project panda.config (ctx.recipes.keys / ctx.patterns.keys), but the describe texts are fixed.
- There are 9 files in the package; examined: package.json, bin.js, README.md (heading), dist/index.js (fully), grep check of dist/cli.js, dist/chunk-IBM3OGUU.mjs, dist/index.mjs, dist/cli.mjs. index.mjs/cli.mjs are thin re-exports of the chunk file.
- The package code was not executed (text analysis only).
