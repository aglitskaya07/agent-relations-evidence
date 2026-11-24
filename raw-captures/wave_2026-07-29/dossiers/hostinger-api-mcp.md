# UNIT: hostinger-api-mcp | npm v1.25.0 (published 2026-07-28T11:15:23.520Z) | scope: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

A full-featured MCP server (`@modelcontextprotocol/sdk` ^1.10.0). The `MCPServer` class in `src/core/runtime.ts` creates `new Server({name, version}, {capabilities: {tools: {}}})`, registers ListTools/CallTool handlers, and proxies calls to the Hostinger REST API (axios → `https://developers.hostinger.com`). 12 binaries: `hostinger-api-mcp` (all tools) + 11 scope servers by product (hosting, vps, dns, domains, billing, ecommerce, mail, reach, wordpress, horizons, agency-hosting). Tool lists are auto-generated from OpenAPI static JSON arrays in `src/core/tools/*.js|ts`.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name`/`version` and `capabilities: {tools: {}}` are passed to the `Server` constructor — there is no `instructions` field anywhere in `src/` (grep over all .ts/.js).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

The total number of tools in the full server `all`: **275** (a JSON array parsed from `src/core/tools/all.js`; scope servers are subsets). Average description length is 246 characters, maximum 1767. The style is neutral OpenAPI documentation: "Retrieve…", "Use this endpoint to…", without pressure to choose the tool over built-in client capabilities.

### Marker scan (full pass over all 275 descriptions by the wave regex set): 2 matches, both false positives in spirit

1. **`hosting_toggleWebsiteCacheV1`** — `prefer` pattern (internal choice between two own modes, not against someone else's tools):
> "Turns server-side caching for the website on or off, based on the enabled flag. Enable it for faster page loads, reduced server load, and improved user experience; recommended for production websites. Disabling may impact performance; to temporarily bypass caching while developing or debugging, prefer toggling cacheless mode instead.
>
> Does nothing if caching is already in the requested state."

2. `hosting_createNodeJSBuildFromArchiveV1` — the `PRECEDENCE` pattern (technical "override fields take precedence over auto-detected values", not tool hierarchy):
> "Upload a project archive, auto-detect build settings, and immediately start a Node.js build.
>
> This is the recommended single-step approach for deploying a Node.js application. The archive is uploaded to the website's file storage, build settings are auto-detected from the package.json inside the archive, and the build process starts automatically. Optional override fields take precedence over auto-detected values. Maximum archive size is 50MB. […]"

### 8 representative full descriptions (verbatim)

**agencyHosting_deployNodeStaticWebsite**
> Deploy a node-static Agency Plan (h5g) website from an archive file. WARNING: this overwrites the website's existing contents and cannot be undone — always confirm with the user before proceeding. Use this for Agency Plan websites of type node-static (a Node.js-built static site that requires a build step or a plain simple static site). The tool resolves the website from its domain, uploads the archive to the website's file browser over TUS, and triggers the build-assets process which builds the site and deploys the result to public_html. This operation is synchronous: the build and deployment complete before the tool returns, so the website is live as soon as the tool finishes successfully — there is no separate asynchronous build to wait for or poll. For plain PHP applications that should be extracted as-is, use agencyHosting_deployPhpApplication instead. The website UID is automatically resolved from the domain.

**hosting_importWordpressWebsite**
> Import a WordPress website from an archive file to a hosting server. This tool uploads a website archive (zip, tar, tar.gz, etc.) and a database dump (.sql file) to deploy a complete WordPress website. The archive will be extracted on the server automatically. Note: This process may take a while for larger sites. After upload completion, files are being extracted and the site will be available in a few minutes. The username will be automatically resolved from the domain.

**domains_purchaseNewDomainV1**
> Purchase and register a new domain name.
>
> If registration fails, login to [hPanel](https://hpanel.hostinger.com/) and check domain registration status.
>
> If no payment method is provided, your default payment method will be used automatically.
>
> If no WHOIS information is provided, default contact information for that TLD will be used. Before making request, ensure WHOIS information for desired TLD exists in your account.
>
> Some TLDs require `additional_details` to be provided and these will be validated before completing purchase.
>
> Use this endpoint to register new domains for users.

**DNS_updateDNSRecordsV1**
> Update DNS records for the selected domain.
>
> Using `overwrite = true` will replace existing records with the provided ones. Otherwise existing records will be updated and new records will be added.
>
> Use this endpoint to modify domain DNS configuration.

**reach_createANewContactV1**
> Create a new contact in the email marketing system.
>
> This endpoint allows you to create a new contact with basic information like name, email, and surname.
>
> If double opt-in is enabled, the contact will be created with a pending status and a confirmation email will be sent.

**VPS_getDataCenterListV1**
> Retrieve all available data centers.
>
> Use this endpoint to view location options before deploying VPS instances.

**billing_getCatalogItemListV1**
> Retrieve catalog items available for order.
>
> Prices in catalog items is displayed as cents (without floating point), e.g: float `17.99` is displayed as integer `1799`.
>
> Use this endpoint to view available services and pricing before placing orders.

**ecommerce_getCustomStorefrontSetupInstructionsV1**
> Retrieve step-by-step setup instructions, formatted as Markdown, for connecting a custom sales channel to your store and keeping your catalog, orders, shipping and payments in sync through the Ecommerce API.

## SIDE-CHANNEL: bundled agent skill (not an MCP channel, but a steering surface)

The package pulls in `skills/headless/SKILL.md` + `entry/skill.md` + 4 reference files — a full agent skill "hostinger-headless" (full pipeline: hosting/domain provisioning → store/WordPress → frontend build → deploy → verification). The skill explicitly instructs the agent to direct the user to purchase a paid plan ("link them to https://www.hostinger.com/web-hosting, and pause until they confirm the purchase. Do not treat this as an error"). This is commercial funnel content inside the package, but it is activated only if the host client loads skills from the package; it does not enter the MCP descriptions themselves.

## NOTES

- The code is NOT minified: readable TS sources + compiled .js alongside, tool lists are plain-JSON arrays marked "Auto-generated tool list".
- Risk of dynamic construction of descriptions: low. `runtime.ts` takes `tool.description` as-is from a static array, does not concatenate anything; instructions are not formed at all.
- Reviewed: package.json, server.json, runtime.ts (fully, key sections), src/servers/* (wrapper ~230 bytes each), full parse of src/core/tools/all.js (275 tools), skills/headless/SKILL.md; in total there are 75 files in the package.
