# UNIT: stripe | Stripe | github stripe/ai/tools/modelcontextprotocol | тип автора: официальный | captured 2026-07-29 (static source)

## NOT-A-SERVER

`tools/modelcontextprotocol` — не реализация MCP-сервера, а тонкий stdio↔HTTP прокси к размещённому Stripe серверу `https://mcp.stripe.com`.

Обоснование (файл `src/index.ts`, 115 строк, весь исходник пакета `@stripe/mcp`):

```ts
const MCP_SERVER_URL = 'https://mcp.stripe.com';
...
const stdioTransport = new StdioServerTransport();
...
const transport = new StreamableHTTPClientTransport(
  new URL(MCP_SERVER_URL),
  {requestInit: {headers}}
);
...
transport.onmessage = async (message) => { await stdioTransport.send(message); };
...
stdioTransport.onmessage = async (message) => { ... await httpTransport!.send(message); };
```

Ни `new Server(...)` / `new McpServer(...)`, ни `registerTool` / `server.tool(` / `setRequestHandler` в этой директории нет. Пакет только пересылает JSON-RPC сообщения между stdio-клиентом и удалённым HTTP-эндпоинтом; `initialize`-ответ, список инструментов и все их описания приходят с сервера Stripe по сети и статически в репозитории отсутствуют.

`server.json` подтверждает: сервер объявлен как remote-only.

```json
{
  "name": "com.stripe/mcp",
  "description": "MCP server integrating with Stripe - tools for customers, products, payments, and more.",
  "version": "0.2.4",
  "remotes": [ { "type": "streamable-http", "url": "https://mcp.stripe.com" } ]
}
```

Смежные директории того же репозитория (`tools/typescript/src/modelcontextprotocol/toolkit.ts`, `tools/python/stripe_agent_toolkit/*`) — тоже прокси-обёртки: они подключаются клиентом к `mcp.stripe.com`, забирают список инструментов и перерегистрируют их локально, подставляя пришедшее по сети описание:

```ts
const remoteTools = this._mcpClient.getTools();
for (const remoteTool of remoteTools) { this.registerProxyTool(remoteTool); }
...
this.tool(remoteTool.name, remoteTool.description || remoteTool.name, zodShape, async (...) => {...});
```

Python-аналог: `description=mcp_tool.get("description", mcp_tool["name"])` (langchain/crewai/openai/strands toolkits).

## CHANNEL: instructions
(не обнаружены статически)

Единственная строка, передаваемая конструктору сервера в репозитории, — `{name: 'Stripe', version: VERSION}` (`tools/typescript/src/modelcontextprotocol/toolkit.ts`, поля `instructions` нет). В `tools/modelcontextprotocol` конструктора сервера нет вовсе.

## CHANNEL: tool descriptions (coverage=none)

Описаний инструментов в исходниках нет ни одного — они формируются удалённым сервисом. Статически доступны только имена, перечисленные в `tools/modelcontextprotocol/manifest.json` (23 шт., поле `tools`, без `description`):

search_documentation, get_stripe_account_in, create_customer, list_customers, create_product, list_products, create_price, list_prices, create_payment_link, create_invoice, list_invoices, create_invoice_item, finalize_invoice, retrieve_balance, create_refund, list_payment_intents, list_subscriptions, cancel_subscription, update_subscription, list_coupons, create_coupon, update_dispute, list_disputes

Описания уровня пакета (не инструментов), для полноты:
- `manifest.json` → `"description": "Manage resources in your Stripe account and search the Stripe knowledge base."`
- `server.json` → `"description": "MCP server integrating with Stripe - tools for customers, products, payments, and more."`

README отсылает за списком инструментов наружу: «See the [Stripe MCP documentation](https://docs.stripe.com/mcp#tools) for a list of tools.»
