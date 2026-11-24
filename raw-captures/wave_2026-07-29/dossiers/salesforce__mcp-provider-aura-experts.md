# UNIT: @salesforce/mcp-provider-aura-experts | npm v0.3.7 (published 2026-03-26T19:54:06.868Z) | scopes: npm-top | captured 2026-07-29 (static, tarball)

## Package type
This is NOT a standalone MCP server, but also not a client/SDK: it is a provider plugin for Salesforce DX MCP Server (`@salesforce/mcp`). Exports `AuraExpertsMcpProvider extends McpProvider` (from `@salesforce/mcp-provider-api`), which provides 4 MCP tools to the host server via `getTools()`. MCP server code (Server/McpServer) is not constructed in the bundle -- SDK schemas are bundled into the code (`z.object({... instructions: t.optional(t.string())})`), but there are no calls to `new Server(...)`. I classify it as a server-side tool provider -- the dossier by channels is applicable.

## CHANNEL: instructions, npm (static)
(not found statically) — the package does not create a server and does not pass `instructions`; this is done by the host `@salesforce/mcp`.

## CHANNEL: tool descriptions, npm (static, coverage=full)
4 tools (names — from minified constants qO/zO/VO + literal):

1. **create_aura_blueprint_draft** — title: "Aura Create Blueprint Draft"
   > Use this tool to generate a Product Requirements Document (PRD) from a Salesforce Aura component. The PRD outlines the component's structure, functionality, and requirements for migrating or converting it into a Lightning Web Component (LWC), as part of the Aura to LWC migration workflow orchestrator.

2. **enhance_aura_blueprint_draft** — title: "Aura Enhance Blueprint Draft"
   > Use this tool to enhance a draft Product Requirements Document (PRD) as part of the Aura to LWC migration workflow orchestrator.

3. **transition_prd_to_lwc** — title: "Aura Transition from PRD to LWC Component Creation"
   > Use this tool to provide next-step migration instructions from a Product Requirements Document (PRD) to a Lightning Web Component (LWC), as part of the Aura to LWC migration workflow orchestrator. The PRD is generated from a Salesforce Aura component.

4. **orchestrate_aura_migration** — title: "Aura Orchestrate Migration"
   > Use this tool to orchestrate a workflow to convert or migrate a Salesforce Aura component into its Lightning Web Component (LWC) equivalent. The input can be either an Aura component bundle file (e.g., .cmp, .controller.js, .helper.js, etc.) or a directory containing Aura component bundle files.

Marker scan for steering regexes: no matches in the descriptions (no "instead of built-in", "takes precedence", "MUST use", superlatives, etc.). The descriptions are neutral, with a "Use this tool to ..." style.

## Steering through tool OUTPUT (observation outside mandatory channels)
A substantial part of the package's steering surface is not the descriptions, but the texts that the tools RETURN to the agent at runtime: expanded imperative instructions ("# Component Analysis Instructions...", "**Your Task**: Follow the instructions...", "**Run each tool in order, using the output of one to inform the next step.**", "**⚡ Expert-Powered**: These instructions are automatically synchronized with our experts. When the experts get smarter, so do these instructions!"). The orchestrator builds a chain from all 4 tools and instructs a transition to another provider's `create_lwc_component_from_prd` tool (LWC).

## Notes
- Code: a single rollup bundle `index.bundle.js` (~1.04 MB, 64 lines, minified, constant names mangled). I looked at 4 files: package.json, index.bundle.d.ts, index.bundle.js, README.md (per the list).
- Dynamic construction of strings: tool descriptions are static literals (low risk); runtime instructions in outputs are assembled from template strings from "expert grounding" — the content is partially dynamic.
- package.json: "(For Interal Use Only)"; dependencies include express/cors/eventsource (bundled SDK transport code), but the server is not instantiated.
