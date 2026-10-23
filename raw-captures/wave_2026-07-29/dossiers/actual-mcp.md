# UNIT: actual-mcp | npm v1.12.0 (published 2026-07-27T11:23:59.338Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Полноценный MCP-сервер для Actual Budget (personal finance). `build/server.js` создаёт `new Server({ name: 'Actual Budget', version: '1.0.0' }, { capabilities: { resources, tools, prompts, logging } })` из `@modelcontextprotocol/sdk`, регистрирует resources/tools/prompts. Write-инструменты включаются флагом `enableWrite` (иначе только 8 read-инструментов).

## CHANNEL: instructions, npm (static)

(не обнаружены статически)

Конструктору `Server` передаются только `name`/`version` и capabilities — поля `instructions` нет. Grep по `instructions` во всём `build/` (без .map) — 0 совпадений.

Примечание: сервер имеет prompts-канал (`build/prompts.js`) с тремя промптами (`financial-insights`, `budget-review`, `actual-cleanup`) — это user-invoked промпты, не auto-injected instructions. Содержат директивные формулировки для модели, например из `financial-insights`: «IMPORTANT: Any transactions in the "Investment & Savings" category group should be treated as POSITIVE savings, not as spending. […] Do NOT recommend reducing these amounts unless they're clearly unsustainable». Тон — доменная разметка задачи, не steering между инструментами/провайдерами.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего 25 инструментов (8 read + 17 write, write за флагом `enableWrite`). Все описания дословно:

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

Маркер-скан steering-регексов по всем 25 описаниям: 0 совпадений. Описания чисто функциональные, без приоритезации над другими инструментами, суперлативов, «primary/precedence/last resort» и т.п.

## NOTES

- Код НЕ минифицирован — читаемый tsc-вывод с sourcemaps и .d.ts, статический анализ надёжен.
- Риск динамической сборки строк: низкий. Описания — литералы (у import-transactions и run-bank-sync — конкатенация литералов `'…' + '…'`, собрано вручную дословно). Единственная динамика — интерполяция дат в prompt-текстах (`${start}`, `${end}`, `${months}`), на steering не влияет.
- Просмотрено: 75 JS-файлов в пакете; вручную прочитаны server.js, tools/index.js, prompts.js, package.json; python-regex поверх всех 25 tools/*/index.js; grep `instructions` по всему build/.
- Списки tools/prompts статические (массивы `readTools`/`writeTools`/`promptsSchema`), рантайм-мутации списков не обнаружены.
