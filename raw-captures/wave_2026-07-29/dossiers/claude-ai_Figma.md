# UNIT: claude-ai:Figma | коннектор claude.ai | captured 2026-07-29 (session copy + ToolSearch)

## CHANNEL: instructions, connector (сессионная копия, обрезана харнесом ~2KB; маркер [truncated] — от харнеса)

The official Figma MCP server. Use this server whenever the user wants to create, generate, edit, implement, or sync any design, UI, screen, component, mockup, or visual — in Figma, FigJam, Figma Make, or Figma Slides — and whenever the user mentions Figma or provides a figma.com URL.

This server bridges code and design in both directions, and supports designing from scratch using existing design systems and codebases.

CAPABILITIES:
- Read designs FROM Figma into code (get_design_context, get_screenshot, get_metadata, get_figjam)
- Write designs INTO Figma from code, intent, or existing components (use_figma, generate_figma_design, create_new_file, upload_assets)
- Bridge code and design via Code Connect (get_code_connect_map, add_code_connect_map)
- Create diagrams and FigJam content (generate_diagram, get_figjam)

WHEN TO USE THESE TOOLS:
- The user wants to create, mock up, or generate any UI, screen, component, or design — even if Figma isn't named
- The user wants to implement a design as code (design-to-code)
- The user wants to push a page, view, or component into Figma (code-to-design)
- The user wants to update, sync, or edit an existing Figma file
- The user shares a figma.com URL
- The user wants to build or extend a design system, design tokens, or component library
- The user wants to create a diagram in FigJam

SKILLS (Prefer the skills shipped with the Figma plugin on the agent being used. If no Figma plugin is installed, use the skills served by the Figma MCP resource):
- /figma-use — MANDATORY before calling use_figma; fallback: skill://figma/figma-use/SKILL.md
- /figma-generate-design — for translating an app page or layout into Figma; fallback: skill://figma/figma-generate-design/SKILL.md
- /figma-generate-library — for building a design system in Figma from code; fallback: skill://figma/figma-generate-library/SKILL.md
- /figma-code-connect — for mapping Figma components to codebase components; fallback: skill://figma/figma-code-connect/SKILL.md
- /figma-use-figjam — for FigJam-specific use_f… [truncated]

## CHANNEL: tool descriptions, connector (27 tools, via ToolSearch)

### add_code_connect_map
Map a Figma node to a code component in your codebase using Code Connect. Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId.

### create_new_file
Create a new blank Figma file. IMPORTANT: You MUST load the /figma-create-new-file skill BEFORE every call to this tool, if it exists. NEVER call this tool without loading that skill first if it exists. By default the file is placed in the authenticated user's drafts folder; If specified it can be placed inside a project. Use this tool when you need a new file to work with before calling use_figma. Returns the new file key and URL. Requires a planKey. If the user already provided a planKey, use it directly. Otherwise, call the whoami tool first to get the list of plans. If the user has one plan, use its "key" field. If multiple, ask the user which team or organization to use. Optionally accepts a projectId. If the URL is of the format https://figma.com/files/project/:projectId, https://figma.com/files/:orgId/project/:projectId, or https://figma.com/files/team/:teamId/project/:projectId then use the :projectId as the projectId.

### download_assets
Download assets from a Figma file for a single node: an exported render, the original source images, and SVGs of the vector layers. The response contains: (1) `export` — an exported image of the whole node; (2) `rawImages` — original uploaded source images (JPEG, PNG, GIF, WebP) found as fills anywhere in the node subtree (capped at 20); and (3) `svgAssets` — SVGs for the vector layers in the subtree that are best represented as SVG (icons, logos, simple illustrations), the same set get_design_context surfaces (capped at 20). Each raw image carries a `format` field with its actual image format (e.g. "png", "jpeg", "gif", "webp") so you can save it with the correct file extension; if the format cannot be determined it is reported as "original". Each `svgAssets` entry has format "svg". Export precedence: when you pass defaultFormat and/or defaultScale, those override the export settings configured on the node in Figma. When you omit them, the node-configured export settings are used if present, otherwise png at scale 1. Pass defaultFormat or defaultScale only when the user explicitly asks for a specific format, size, or resolution. For cross-file image transfer, use the raw image URLs with upload_assets. URLs are temporary — download promptly. Works on Figma design files (URL path `/design/`), Figma Slides (`/slides/`), and FigJam boards (`/board/`). Does NOT work on Figma Make files (`/make/`).

### export_video
Export a Figma timeline node as an MP4 video. This tool only produces MP4 — GIF and animated SVG export are not supported yet. Renders the timeline server-side and returns a presigned download URL. The file stays available for `ttlSeconds` (defaults to 1 hour, clamped server-side to [30s, 7d]); use `availableUntil` in the response to know when it is deleted. Some renders finish in seconds, others take minutes; if the render hasn't finished within the handler budget, the response includes a `jobId` and `status: "processing"` — re-invoke `export_video` with `{ fileKey, jobId }` after 10–15s to poll. Required: `fileKey` and either `nodeId` (to start a new export) or `jobId` (to poll). The `nodeId` must be the top-level frame that owns the timeline — in a design file a frame placed directly on the page or in a section, and in Slides the slide itself (not a layer inside it) — not a nested layer or sub-clip. If you animated a descendant, pass its containing top-level frame (the slide, in Slides); if `get_motion_context` returns a `timelineCohorts` entry, its `rootNodeId` is that frame. Use the `quality` field ("low"/"medium"/"high") to control output size.

### generate_diagram
Create a flowchart, decision tree, gantt chart, sequence diagram, state diagram, or entity relationship diagram in FigJam, using Mermaid.js. Generated diagrams should be simple, unless a user asks for details. This tool also does not support generating Figma designs, class diagrams, timelines, venn diagrams, or other Mermaid.js diagram types. This tool also does not support font changes, or moving individual shapes around -- if a user asks for those changes to an existing diagram, encourage them to open the diagram in Figma. If the tool is unable to complete the user's task, reference the error that is passed back. Do not use the create_new_file tool prior to creating a diagram using this tool; generate_diagram creates its own files.

### get_code_connect_map
Get a mapping of {[nodeId]: {codeConnectSrc: e.g. location of component in codebase, codeConnectName: e.g. name of component in codebase} E.g. {'1:2': { codeConnectSrc: 'https://github.com/foo/components/Button.tsx', codeConnectName: 'Button' } }. Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId.

### get_code_connect_suggestions
Get AI-suggested strategy for linking a Figma node to code components via Code Connect. Workflow: call this tool → review suggestions with the user → call send_code_connect_mappings to save the approved mappings.

Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId.

### get_context_for_code_connect
Get structured component metadata including properties, variants, and descendant tree for a Figma component or component set. Returns property definitions with types and variant options, and a tree of descendant instances and text nodes with their property references. Designed for creating Code Connect template files. Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId.

### get_design_context
Get design context for a Figma node — the primary tool for design-to-code workflows. Returns reference code, a screenshot, and contextual metadata that must be adapted to the target project.

IMPORTANT: You MUST load figma-design-to-code guidance BEFORE calling this tool. Prefer the /figma-design-to-code skill if available; otherwise read the skill://figma/figma-design-to-code/SKILL.md MCP resource.

NEVER call this tool without loading that guidance first — skipping it produces code that ignores the target project's existing components, design tokens, and conventions.

Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. Do not pass an empty or guessed nodeId. If the URL is of the format https://figma.com/design/:fileKey/branch/:branchKey/:fileName then use the branchKey as the fileKey. If the URL is of the format https://figma.com/make/:makeFileKey/:makeFileName then use the makeFileKey to identify the Figma Make file. Only for Figma Make files (URLs containing `/make/`), and only when calling get_design_context, assume the nodeId is `0:1`. The response will contain a code string and a JSON of download URLs for the assets referenced in the code. It will also include a screenshot of the node for context by default.

### get_figjam
Generate UI code for a given FigJam node in Figma. Use the nodeId parameter to specify a node id. If no node id is provided, use `0:1` which is the root node ID. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id from the URL, for example, if given the URL https://figma.com/board/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. IMPORTANT: This tool only works for FigJam files (URL path `/board/`), not other Figma files.

### get_figma_skill
Read a single Figma skill resource (the skill index, a SKILL.md, or a skill reference file) by its skill:// URI and return its text content. You MUST ONLY use skill:// URIs. You MUST NOT use this for any other resource (docs, Make source, files, node data, etc.). Discover URIs from the server instructions or by reading the skill index at "skill://index.json". A SKILL.md links to its reference files with relative paths (e.g. references/foo.md); read those as skill://figma/<skill-name>/references/<path>. To read several resources (for example a skill plus its reference files), call this tool once per URI.

### get_libraries
Get the design libraries associated with a Figma file. Returns two lists: (1) libraries currently added to the file (subscribed), and (2) libraries available to add (community UI kits and organization libraries). Each library includes its name, library key, description, and source type. The organization libraries portion of libraries_available_to_add is paginated — when the response includes a libraries_available_to_add_next_offset value, pass it back via the offset parameter to fetch the next page. Use the library keys from the response to scope searches with search_design_system by passing them as includeLibraryKeys.

### get_metadata
IMPORTANT: Always prefer to use get_design_context tool. Get metadata for a node or page in the Figma desktop app in XML format. Useful only for getting an overview of the structure, it only includes node IDs, layer types, names, positions and sizes. You can call get_design_context on the node IDs contained in this response. Use the nodeId parameter to specify a node id, it can also be the page id (e.g. 0:1). IMPORTANT: This tool only works for Figma design files (URL path `/design/`). It is NOT supported for FigJam (`/board/`) or Slides (`/slides/`) files. This tool is not supported for Figma Make Files (URLs containing `/make/`). The nodeId parameter is optional: when omitted, the tool returns a list of the top-level pages (guid + name) in the document instead of an XML dump — use this when you don't yet know which page or node to drill into. When the user has a current selection relevant to the request, the response is prepended with a "Currently selected nodes:" block listing the selection by guid and name, so you can tell whether it matches the queried nodeId. If the URL includes `node-id`, extract it and pass it as nodeId; for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2`. If the URL does not include `node-id`, do not set nodeId; omit the field so the tool lists top-level pages. Do not pass an empty or guessed nodeId. If the URL is of the format https://figma.com/design/:fileKey/branch/:branchKey/:fileName then use the branchKey as the fileKey.

### get_motion_context
Get keyframe animation data for a Figma node. Returns animated-node inventory, keyframe tracks with easing curves, pre-computed CSS/@keyframes and motion.dev code snippets, and timeline coordination hints for recursive calls. Use after get_design_context for motion-aware code generation. Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`.

### get_screenshot
Generate a screenshot for a given node or the currently selected node in the Figma desktop app. Works on Figma design files (URL path `/design/`), FigJam boards (`/board/`), and Figma Slides (`/slides/`). The optional `maxDimension` parameter (positive integer, max 65536, default 1024) caps the longer edge of the rendered PNG in pixels — increase it when you need to inspect fine detail, decrease it for thumbnails or to save context. The JSON metadata entry in the response includes both `width`/`height` (the rendered PNG size) and `original_width`/`original_height` (the node's natural canvas size before any clamping), so callers can decide whether to re-request at a higher `maxDimension`. Use the nodeId parameter to specify a node id. nodeId parameter is REQUIRED. Use the fileKey parameter to specify the file key. fileKey parameter is REQUIRED. If a URL is provided, extract the file key and node id from the URL. For example, if given the URL https://figma.com/design/pqrs/ExampleFile?node-id=1-2 the extracted fileKey would be `pqrs` and the extracted nodeId would be `1:2`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId. This tool is not supported for Figma Make Files (URLs containing `/make/`). By default this tool returns a short-lived URL to the screenshot plus curl instructions for downloading the PNG — the URL+curl path is strongly preferred because it uses far fewer tokens than embedding the image inline. The `enableBase64Response` parameter defaults to `false`. Only set `enableBase64Response: true` when the agent cannot fetch URLs (no shell access, no HTTP client, or a sandboxed environment that blocks outbound requests); when set, an inline base64 image entry is appended to the response in addition to the URL and curl instructions. If the URL is of the format https://figma.com/design/:fileKey/branch/:branchKey/:fileName then use the branchKey as the fileKey.

### get_shader_effect
Reads a shader effect from the account library by id (from list_shader_effects), returning its name, description, version, and a manifest of its source files as { filename, bytes, uri }. Read each file's contents from its uri as an MCP resource (contents are not inlined here). Pass an optional version (commit SHA) to read a specific build; defaults to the latest.

### get_shader_fill
Reads a shader fill from the account library by id (from list_shader_fills), returning its name, description, version, and a manifest of its source files as { filename, bytes, uri }. Read each file's contents from its uri as an MCP resource (contents are not inlined here). Pass an optional version (commit SHA) to read a specific build; defaults to the latest.

### get_variable_defs
Get variable definitions for a given node id. E.g. {'icon/default/secondary': #949494}Variables are reusable values that can be applied to all kinds of design properties, such as fonts, colors, sizes and spacings. Use the nodeId parameter to specify a node id. Extract the node id from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId. This remote tool requires a concrete node target. This tool is not supported for Figma Make Files (URLs containing `/make/`). If the URL is of the format https://figma.com/design/:fileKey/branch/:branchKey/:fileName then use the branchKey as the fileKey.

### list_file_components_for_code_connect
List every component and component set PUBLISHED to a Figma file's library, with the cross-component dependency graph needed to plan Code Connect in bulk. Only published components are returned (unpublished/local-only components are omitted). Returns one entry per component with its properties (exhaustive variant options, defaults, instance-swap preferred values), page and asset/library membership, child instance tags, instance count, and direct dependencies (each flagged internal vs. external library). Unlike get_context_for_code_connect — which returns the deep descendant tree for one known component — this returns the flat whole-file graph for dependency-ordered, batched template generation. Takes only a file key (no node id). Use the fileKey parameter to specify the file key. If a URL is provided, extract the file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName, the extracted fileKey would be `:fileKey`. If the URL is of the format https://figma.com/design/:fileKey/branch/:branchKey/:fileName then use the branchKey as the fileKey.

### list_shader_effects
Lists the shader effects in the authenticated user's account library. Returns each effect's id, name, and description (plus a nextCursor when more pages exist). Use the id with get_shader_effect to read an effect's source. Shader effects are post-effects that sample an input raster, distinct from custom tools and shader fills.

### list_shader_fills
Lists the shader fills in the authenticated user's account library. Returns each fill's id, name, and description (plus a nextCursor when more pages exist). Use the id with get_shader_fill to read a fill's source. Shader fills generate pixels directly with no input raster, distinct from custom tools and shader effects.

### read_skill_uri
Deprecated alias of get_figma_skill. Call get_figma_skill instead. Read a single Figma skill resource (the skill index, a SKILL.md, or a skill reference file) by its skill:// URI and return its text content. You MUST ONLY use skill:// URIs. You MUST NOT use this for any other resource (docs, Make source, files, node data, etc.). Discover URIs from the server instructions or by reading the skill index at "skill://index.json". A SKILL.md links to its reference files with relative paths (e.g. references/foo.md); read those as skill://figma/<skill-name>/references/<path>. To read several resources (for example a skill plus its reference files), call this tool once per URI.

### search_design_system
Search for design system assets (components, variables, and styles) based on a text query. Returns matching assets from all design libraries. Use this when you need to find specific components, variables (e.g. colors, spacing tokens), or styles from design libraries.

### send_code_connect_mappings
Save multiple Code Connect mappings in bulk. Use after get_code_connect_suggestions to confirm and save approved mappings.

Use the nodeId parameter to specify a node id. Use the fileKey parameter to specify the file key. If a URL is provided, extract the node id and file key from the URL, for example, if given the URL https://figma.com/design/:fileKey/:fileName?node-id=1-2, the extracted nodeId would be `1:2` and the fileKey would be `:fileKey`. If the URL does not include `node-id`, ask the user for a node-specific URL. Do not pass an empty or guessed nodeId.

### upload_assets
Upload assets (images and SVGs) into a Figma file. Call with a "count" to get that many single-use upload URLs. POST raw asset bytes to each URL with the correct Content-Type header (e.g. image/png, image/jpeg, image/svg+xml). Each upload URL handles storage, BlobStore commit, and canvas placement automatically. For a single raster image with nodeId, sets it as a fill on that existing node. Without nodeId, creates new frames with image fills on the current page. SVGs (image/svg+xml) are imported as editable vector node trees on the current page; nodeId and scaleMode do not apply to SVGs. Supports PNG, JPG, GIF, WebP, and SVG. Max 10MB per asset. Works on Figma design files (URL path `/design/`), FigJam boards (`/board/`), and Figma Slides (`/slides/`).

### use_figma
Create, edit, generate, or sync any design in Figma — UIs, screens, mockups, components, frames, variables, styles, text, images, layouts, and design systems. This general-purpose tool writes to Figma with JavaScript via the Figma Plugin API. Works on Figma design files (URL path `/design/`), FigJam boards (`/board/`), and Figma Slides (`/slides/`).

IMPORTANT: Before calling this tool, load figma-use guidance — prefer the /figma-use skill if available, otherwise read the skill://figma/figma-use/SKILL.md MCP resource if available. Skipping this causes common, hard-to-debug failures.

Use this tool when the user wants to:
- Create or generate a Figma design, screen, UI, or mockup from scratch, intent, or code
- Update, edit, or sync an existing Figma design
- Generate or sync Figma designs from source code
- Set up or modify design tokens, variables, or styles
- Build or extend a design system or component/variant library
- Fix layout, spacing, auto-layout, or fill/hug issues
- Add component descriptions, annotations and Code Connect metadata to nodes
- Review or fix accessibility, contrast, typography, or visual polish
- Inspect or query node properties programmatically
CHOOSING BETWEEN use_figma AND generate_figma_design:
- Default to use_figma for all write operations
- Exception: generate_figma_design ONLY to capture a web app page/view for the first time. For web apps, run both in parallel — generate_figma_design captures a pixel-perfect screenshot, use_figma builds from imported design system components and refines against the screenshot
- Non-web (iOS, Android, generic UI) and from-scratch designs: use_figma only
- Updating/syncing a Figma page already captured: use_figma — even if source code changed
GOTCHAS
- For the font "Inter", the style is "Semi Bold", not "SemiBold" and "Extra Bold" not "ExtraBold"
- MUST use `await figma.setCurrentPageAsync(page)` to change pages. Setting figma.currentPage is not supported
- MUST NEVER use loadAllPagesAsync,setPluginData,createImageAsync. They are not supported API

### whoami
Returns the authenticated user's handle, email, all the plans the user belongs to (and the ID for each plan) and their seats on those plans. You MUST use this tool if you are experiencing file access/permission issues or are being rate limited by the Figma MCP to help debug the issue.
