# UNIT: ai.agenticterminal/directory | {"name": "at-directory", "version": "0.0.1"} | hosted https://mcp.agenticterminal.ai/mcp | captured 2026-07-29 (keyless)

## CHANNEL: instructions, hosted

(отсутствует — сервер не передаёт блок instructions)

## CHANNEL: tool descriptions, hosted (6 tools)

### tool: search_merchants

Search OP-verified merchants by rail, chain, category, agent-callable tier, trust tier, and free text. Ranked by trust tier then verification recency.

### tool: get_merchant

Get the full record for one merchant including all rails, payment endpoints, and OP attestation. Tier 2+ requires an AT credential.

### tool: verify_payment_endpoint

Run a live check against a merchant's declared payment endpoint for a rail. Returns health, detail, and rail-specific evidence.

### tool: list_categories

List the category taxonomy with merchant counts.

### tool: list_rails

List supported payment rails and their current merchant counts.

### tool: whoami

Report the resolved credential state and rate limits for the calling agent.

