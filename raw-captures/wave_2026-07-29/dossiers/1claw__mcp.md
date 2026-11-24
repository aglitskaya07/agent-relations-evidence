# UNIT: @1claw/mcp | npm v0.41.4 (published 2026-07-17T20:50:03.534Z) | frames: pulsemcp,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (yes)

A full-fledged MCP server on FastMCP (`fastmcp` ^3.33.0): `dist/index.js` creates `new FastMCP(serverOpts)`, registers tools via `server.addTool(...)`, resource `vault://secrets` via `server.addResource(...)`, starts stdio or httpStream (`server.start(...)`). `bin: 1claw-mcp -> dist/index.js`. Domain: 1claw secret storage + blockchain transaction signing + payment cards for agents.

## CHANNEL: instructions, npm (static)
(not found statically)

`serverOpts` contains only `name: "1claw"`, `version`, `health`, and (for httpStream) `authenticate`. The `instructions` field is not passed to the FastMCP constructor; grep for `instructions` throughout `dist/` — 0 matches.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

A total of 52 name+description pairs were extracted: 51 tool definitions + 1 resource ("Vault secrets"). There are 50 unique tool names (`list_secrets` is defined twice — cloud variant and local daemon variant; they are registered mutually exclusively). At the same time, 49 tools are registered in the default cloud mode (44 from tools/ + inspect_content + 4 "stretch": rotate_and_store, rotate_generate, list_versions, get_env_bundle); in ONECLAW_LOCAL_VAULT mode — proxy_request + local list_secrets + inspect_content; in ONECLAW_LOCAL_ONLY — only inspect_content.

### Marker scan (full, across all 52 descriptions)

Exactly 1 match, and it is harmless (about the key TTL, not about displacing other tools):

- **lease_bankr_key** — match `Prefer`:
  > "Provision a short-lived Bankr wallet API key for an agent (privileged; requires explicit policy on agents/{id}/bankr/*). Partner key stays server-side; leased key is stored for Shroud — never returned in tool output. Prefer ttl_seconds 300–900 for autonomous agents; revoke when done via list + revoke."

Zero matches for all steering markers: instead of built-in, PRECEDENCE / takes precedence, LAST resort, Do NOT answer from memory, primary tool/interface, always default, MUST use, whenever the user, ignore previous, etc. The descriptions are concrete, with no attempt to displace built-in tools or other servers.

The only behavioral imperative addressed to the agent (not steering between tools, but secret hygiene) is in **get_secret**:
> "Fetch the decrypted value of a secret from the 1claw vault by its path (e.g. 'api-keys/stripe'). Use this immediately before making an API call that requires the credential. Do not store the value or include it in summaries."

### 8 representative full descriptions (verbatim)

1. **list_secrets** (tools/list_secrets.js): "List all secrets stored in the 1claw vault. Returns paths, types, versions, and metadata — never secret values. Use this to discover what credentials are available before fetching one."
2. **put_secret**: "Store a new secret or update an existing one in the 1claw vault. Provide the path, value, and type. Each call creates a new version. Supports optional expiry and max access count."
3. **execute_http**: "Execute an HTTP request through a pre-configured binding. The binding's credential is injected server-side — the agent never sees it. Requires execution_intents_enabled on the agent."
4. **sign_digest**: "Sign a client-computed 32-byte digest directly (raw/blind signing). Returns a 65-byte r‖s‖v ECDSA signature (v=27/28) that recovers to the signer EOA. Use this for ERC-1271 / ERC-7739 nested EIP-712 flows (e.g. Polymarket CLOB orders) where the canonical hash is computed client-side and must match the verifier exactly. WARNING: this is blind signing — no domain/transaction inspection is performed and guardrails are bypassed. The agent must have `raw_signing_enabled` set by a human, or the request returns 403. Every use is audit-logged."
5. **submit_transaction**: "Submit a transaction to be signed by 1claw's Intents API and optionally broadcast. Supports EVM (legacy + EIP-1559) and non-EVM chains (Bitcoin, Solana, XRP, Cardano, Tron). value is the major-unit decimal string (ETH/BTC/SOL/XRP/ADA/TRX). token_mint supports ERC-20 transfers on EVM chains (contract address) as well as SPL/TRC-20 on non-EVM. Set simulate_first=true for Tenderly pre-flight (EVM-only; no-op on non-EVM)."
6. **order_card**: "Order a US prepaid payment card for an agent, paying via x402 from the agent's Base USDC balance. Requires cards_enabled on the agent and a Pro+ plan. Never returns PAN/CVV — poll get_card_status, then a human reveals card details in the dashboard."
7. **inspect_content**: "Inspect text content for security threats including command injection, encoding obfuscation, social engineering, and PII. Returns a JSON threat report (safe, verdict, threat_count, threats). Use before processing untrusted input."
8. **proxy_request**: "Make an HTTP request with a secret injected by the local daemon. The secret value is NEVER exposed — the daemon injects it per policy. Requires a policy to be configured: `1claw daemon policy add <secret> --hosts <allowed_host>`."

Other tools (names): get_secret, delete_secret, describe_secret, create_vault, list_vaults, grant_access, share_secret, simulate_transaction, simulate_bundle, sign_transaction, sign_message, sign_typed_data, list_transactions, get_transaction, provision_signing_key, list_signing_keys, get_signing_key_balance, lease_bankr_key, order_gift_card, search_gift_cards, list_cards, get_card_status, platform_list_apps, platform_create_app, platform_bootstrap_user, platform_reissue_claim, platform_rotate_key, list_approvals, get_approval, request_approval, treasury_propose, treasury_sign_proposal, treasury_list_proposals, execute_intent, list_bindings, create_binding, test_binding, list_executions, rotate_and_store, rotate_generate, list_versions, get_env_bundle.

## NOTES (methodology)

- The code is NOT minified: tsc compiler output with sourcemaps, readable names, comments preserved (SEC-004/SEC-005/H-9/L2, etc.).
- Risk of dynamic assembly of description strings: low. All description fields are static string literals (in places, concatenation of literals `"..." + "..."`); grep for `description:` without a string literal yields only pass-throughs of `proto.description` and zod-`describe`. There are no template literals/variables in descriptions.
- Reviewed: package.json, README.md (heading), dist/index.js in full, all 43 dist/tools/*.js files (regex extraction), dist/security/index.js and dist/client.js (by size/grep). In total, ~48 files of text analysis; the package code was not executed.
- The `vault://secrets` resource is the only addResource; prompts are not registered.
