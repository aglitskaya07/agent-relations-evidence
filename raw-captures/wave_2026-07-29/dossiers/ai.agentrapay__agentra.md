# UNIT: ai.agentrapay/agentra | {"name": "agentra", "version": "1.0.0"} | hosted https://api.agentrapay.ai/mcp | captured 2026-07-29 (keyless)

## CHANNEL: instructions, hosted

(отсутствует — сервер не передаёт блок instructions)

## CHANNEL: tool descriptions, hosted (6 tools)

### tool: agentra_create_wallet

Register as an agent and provision a non-custodial wallet. This is your FIRST CALL when onboarding to Agentra. Returns your agent_id, API key (agn_ prefix), and a Turnkey-managed wallet address on Base Sepolia. You hold the keys via Turnkey; Agentra never touches your private key. After this, call agentra_verify_identity to upgrade your trust tier.

### tool: agentra_verify_identity

Submit identity verification to upgrade your trust tier. Higher tiers unlock larger transaction limits. Provide your agent_id (from agentra_create_wallet) and operator attestation. Verification is instant. Tiers: Unverified ($100/tx, $250/day) -> Basic ($1K/tx, $5K/day) -> Standard ($5K/tx, $10K/day) -> Enhanced ($25K/tx, $100K/day). Your API key (agn_ prefix) must be passed via X-API-Key header.

### tool: agentra_check_reputation

CALL THIS BEFORE paying or transacting with unknown agents. Returns the target agent's trust score (0-100), trust tier, reputation zone (Green/Yellow/Red), and transaction history summary. Agentra scores BOTH sides of every transaction: you and your counterparty. This is a read-only lookup with no side effects. Monetized endpoint: response detail varies by your plan tier.

### tool: agentra_authorize_payment

Request authorization for a payment to another agent or service. Agentra is NON-CUSTODIAL: this returns an authorization attestation and an unsigned transaction. Agentra never touches your private keys or moves your funds. YOU sign and submit the transaction yourself. Flow: (1) Call this endpoint -> (2) Receive unsigned tx + attestation -> (3) Sign with your Turnkey wallet -> (4) Submit to Base network -> (5) Call settle to record completion. If counterparty is unverified and require_counterparty_kya is true (default), you get a 402 challenge with instructions for the counterparty to onboard. This is Agentra's viral growth mechanism.

### tool: agentra_set_mandate

Create or update spending mandates that define your agent's autonomous transaction boundaries. Mandates enforce: max per-transaction amount, daily spending cap, allowed recipient types, minimum counterparty reputation score, and expiration. Your human operator sets these; your agent operates within them. require_counterparty_kya defaults to true. Recommended: true. This recruits counterparties into verification.

### tool: agentra_get_wallet

Get your agent profile and wallet details: trust tier, trust score, wallet address, registration status, and current verification level. Use to check your status before initiating transactions. Read-only, no side effects.

