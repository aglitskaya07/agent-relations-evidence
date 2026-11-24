# UNIT: actual-mcp | npm v1.12.0 (published 2026-07-27T11:23:59.338Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

A full-featured MCP server for Actual Budget (personal finance). `build/server.js` creates `new Server({ name: 'Actual Budget', version: '1.0.0' }, { capabilities: { resources, tools, prompts, logging } })` from `@modelcontextprotocol/sdk`, and registers resources/tools/prompts. Write tools are enabled by the `enableWrite` flag (otherwise only 8 read tools).

## CHANNEL: instructions, npm (static)

(not found statically)

Only `name`/`version` and capabilities are passed to the `Server` constructor — there is no `instructions` field. Grep for `instructions` throughout `build/` (without .map) — 0 matches.

Note: the server has a prompts channel (`build/prompts.js`) with three prompts (`financial-insights`, `budget-review`, `actual-cleanup`) — these are user-invoked prompts, not auto-injected instructions. They contain directive phrasing for the model, for example from `financial-insights`: «IMPORTANT: Any transactions in the "Investment & Savings" category group should be treated as POSITIVE savings, not as spending. […] Do NOT recommend reducing these amounts unless they're clearly unsustainable». The tone is domain task labeling, not steering between tools/providers.

## CHANNEL: tool descriptions, npm (static, coverage=full)

There are 25 tools in total (8 read + 17 write, write behind the `enableWrite` flag). All descriptions verbatim:

### Read tools
| name | description |
|---|---|
| get-transactions | Get transactions for an account with optional filtering |
| spending-by-category | Get spending breakdown by category for a specified date range |
| monthly-summary | Get monthly income, expenses, and savings |
| balance-history | Get account balance history over time |
| get-accounts | Retrieve a list of all accounts with their current balance and ID. |
| get-grouped-categories | Retrieve a list of all category groups with their id, name, type and category list. |
| get-payees | Retrieve a list of all payees with their id, name, categoryId and transferAccountId. |
| get-rules | Retrieve a list of all rules. PS amount comes in cents: positive for deposit, negative for payment |

### Write tools
| name | description |
|---|---|
| create-category | Create a new category |
| update-category | Update a category |
| delete-category | Delete a category |
| create-category-group | Create a new category group |
| update-category-group | Update a category group |
| delete-category-group | Delete a category group |
| create-payee | Create a new payee |
| update-payee | Update a payee |
| delete-payee | Delete a payee |
| create-rule | Create a new rule |
| update-rule | Update a rule |
| delete-rule | Delete a rule |
| update-transaction | Update an existing transaction. Can modify date, amount, payee, category, notes, cleared status, and subtransactions. |
| delete-transaction | Delete a transaction by its ID. This action is permanent and cannot be undone. |
| create-transaction | Create a new transaction. Use this to add transactions to accounts. Supports transfers between accounts by specifying transfer_account_id. |
| import-transactions | Import a list of transactions into an account using reconciliation logic. Deduplicates via imported_id to prevent duplicates on repeated imports. Supports dry-run mode to preview changes without persisting them. |
| run-bank-sync | Run bank synchronization (GoCardless/SimpleFIN) to download latest transactions. Provide accountId for a specific account, use "onbudget"/"offbudget" for groups, or omit to sync all linked accounts. |

Marker scan of steering regexes across all 25 descriptions: 0 matches. The descriptions are purely functional, with no prioritization over other tools, superlatives, "primary/precedence/last resort", etc.

## NOTES

- The code is NOT minified — readable tsc output with sourcemaps and .d.ts, static analysis is reliable.
- Risk of dynamic string assembly: low. Descriptions are literals (for import-transactions and run-bank-sync — concatenation of literals `'…' + '…'`, assembled manually verbatim). The only dynamics are date interpolation in prompt texts (`${start}`, `${end}`, `${months}`), does not affect steering.
- Reviewed: 75 JS files in the package; manually read server.js, tools/index.js, prompts.js, package.json; python regex across all 25 tools/*/index.js; grep `instructions` across all build/.
- The tools/prompts lists are static (arrays `readTools`/`writeTools`/`promptsSchema`); no runtime mutations of the lists were found.
