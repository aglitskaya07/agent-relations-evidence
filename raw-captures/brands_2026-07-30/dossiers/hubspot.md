# UNIT: hubspot | HubSpot | github shinzo-labs/hubspot-mcp | тип автора: комьюнити | captured 2026-07-29 (static source)

Источник: `brands/src/hubspot/hubspot-mcp-HEAD` (TypeScript, единственный файл сервера `src/index.ts`, 2531 строк).
Подтверждение сервера: `import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js"`, `const server = new McpServer(serverInfo)`, `StdioServerTransport`, плюс `createStatefulServer` от Smithery. Это полноценный MCP-сервер (обёртка HubSpot API `https://api.hubapi.com`).

## CHANNEL: instructions
(не обнаружены статически)

Конструктору передаётся только:
```
const serverInfo = {
    name: "HubSpot-MCP",
    version: "2.0.5",
    description: "An extensive MCP for the HubSpot API"
  }
  const server = new McpServer(serverInfo)
```
Поле `instructions` отсутствует; подстроки `instructions` нет ни в `src/index.ts`, ни в `index.js`, `package.json`, `smithery.yaml`, `README.md`. Обработчик `initialize` вручную не переопределяется.

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов: **112** (все через `server.tool("<name>", "<description>", { zod schema }, handler)`, 112 вхождений `server.tool(` — все 112 распознаны регексом, имена уникальны). Средняя длина описания — 45 символов.

### Полный маркер-скан (все 112 описаний)

Прогон по всем 112 описаниям дал 2 совпадения, и оба — ложные срабатывания на слове «preferences» внутри доменного термина «communication preferences»:

- `communications_get_preferences` — дословно: «Get communication preferences for a contact»
- `communications_update_preferences` — дословно: «Update communication preferences for a contact»

Иных совпадений нет: ни сравнительных/приоритетных формулировок, ни императивов к модели, ни маркетинговых квалификаторов, ни упоминаний вознаграждений/доверия к источникам. Описания — сухие CRUD-формулировки в стиле референса HubSpot API.

### 10 репрезентативных полных описаний (дословно)

1. `crm_create_company` — «Create a new company with validated properties»
2. `crm_create_object` — «Create a new CRM object»
3. `crm_create_association` — «Create an association between two objects»
4. `crm_get_contact_properties` — «Get all properties for contacts»
5. `meetings_search` — «Search meetings with specific filters»
6. `tasks_get` — «Get details of a specific task»
7. `engagement_details_create` — «Create a new engagement with details»
8. `emails_create` — «Create a new email record»
9. `communications_get_preferences` — «Get communication preferences for a contact»
10. `products_batch_update` — «Update a batch of products by internal ID, or unique values specified by the `idProperty` query param.»

### Пять самых длинных описаний (дословно; верхняя граница «плотности» текста в этом сервере)

- `products_list` — «Read a page of products. Control what is returned via the `properties` query param. `after` is the paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.»
- `products_update` — «Perform a partial update of an Object identified by ID. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.»
- `products_batch_read` — «Read a batch of products by internal ID, or unique property values. Retrieve records by the `idProperty` parameter to retrieve records by a custom unique value property.»
- `products_batch_update` — «Update a batch of products by internal ID, or unique values specified by the `idProperty` query param.»
- `products_create` — «Create a product with the given properties and return a copy of the object, including the ID.»

### Полный список всех 112 инструментов (name — description, дословно)

- `crm_create_company` — «Create a new company with validated properties»
- `crm_update_company` — «Update an existing company with validated properties»
- `crm_get_company` — «Get a single company by ID with specific properties and associations»
- `crm_search_companies` — «Search companies with company-specific filters»
- `crm_batch_create_companies` — «Create multiple companies in a single request»
- `crm_batch_update_companies` — «Update multiple companies in a single request»
- `crm_get_company_properties` — «Get all properties for companies»
- `crm_create_company_property` — «Create a new company property»
- `crm_list_objects` — «List CRM objects of a specific type with optional filtering and pagination»
- `crm_get_object` — «Get a single CRM object by ID»
- `crm_create_object` — «Create a new CRM object»
- `crm_update_object` — «Update an existing CRM object»
- `crm_archive_object` — «Archive (delete) a CRM object»
- `crm_search_objects` — «Search CRM objects using filters»
- `crm_batch_create_objects` — «Create multiple CRM objects in a single request»
- `crm_batch_read_objects` — «Create multiple CRM objects in a single request»
- `crm_batch_update_objects` — «Update multiple CRM objects in a single request»
- `crm_batch_archive_objects` — «Archive (delete) multiple CRM objects in a single request»
- `crm_list_association_types` — «List all available association types for a given object type pair»
- `crm_get_associations` — «Get all associations of a specific type between objects»
- `crm_create_association` — «Create an association between two objects»
- `crm_archive_association` — «Archive (delete) an association between two objects»
- `crm_batch_create_associations` — «Create multiple associations in a single request»
- `crm_batch_archive_associations` — «Archive (delete) multiple associations in a single request»
- `crm_create_contact` — «Create a new contact with validated properties»
- `crm_update_contact` — «Update an existing contact with validated properties»
- `crm_get_contact` — «Get a single contact by ID with specific properties and associations»
- `crm_search_contacts` — «Search contacts with contact-specific filters»
- `crm_batch_create_contacts` — «Create multiple contacts in a single request»
- `crm_batch_update_contacts` — «Update multiple contacts in a single request»
- `crm_get_contact_properties` — «Get all properties for contacts»
- `crm_create_contact_property` — «Create a new contact property»
- `crm_create_lead` — «Create a new lead with validated properties»
- `crm_update_lead` — «Update an existing lead with validated properties»
- `crm_get_lead` — «Get a single lead by ID with specific properties and associations»
- `crm_search_leads` — «Search leads with lead-specific filters»
- `crm_batch_create_leads` — «Create multiple leads in a single request»
- `crm_batch_update_leads` — «Update multiple leads in a single request»
- `crm_get_lead_properties` — «Get all properties for leads»
- `crm_create_lead_property` — «Create a new lead property»
- `meetings_list` — «List all meetings with optional filtering»
- `meetings_get` — «Get details of a specific meeting»
- `meetings_create` — «Create a new meeting»
- `meetings_update` — «Update an existing meeting»
- `meetings_archive` — «Archive (delete) a meeting»
- `meetings_search` — «Search meetings with specific filters»
- `meetings_batch_create` — «Create multiple meetings in a single request»
- `meetings_batch_update` — «Update multiple meetings in a single request»
- `meetings_batch_archive` — «Archive (delete) multiple meetings in a single request»
- `notes_create` — «Create a new note»
- `notes_get` — «Get details of a specific note»
- `notes_update` — «Update an existing note»
- `notes_archive` — «Archive (delete) a note»
- `notes_list` — «List all notes with optional filtering»
- `notes_search` — «Search notes with specific filters»
- `notes_batch_create` — «Create multiple notes in a single request»
- `notes_batch_read` — «Read multiple notes in a single request»
- `notes_batch_update` — «Update multiple notes in a single request»
- `notes_batch_archive` — «Archive (delete) multiple notes in a single request»
- `tasks_create` — «Create a new task»
- `tasks_get` — «Get details of a specific task»
- `tasks_update` — «Update an existing task»
- `tasks_archive` — «Archive (delete) a task»
- `tasks_list` — «List all tasks with optional filtering»
- `tasks_search` — «Search tasks with specific filters»
- `tasks_batch_create` — «Create multiple tasks in a single request»
- `tasks_batch_read` — «Read multiple tasks in a single request»
- `tasks_batch_update` — «Update multiple tasks in a single request»
- `tasks_batch_archive` — «Archive (delete) multiple tasks in a single request»
- `engagement_details_get` — «Get details of a specific engagement»
- `engagement_details_create` — «Create a new engagement with details»
- `engagement_details_update` — «Update an existing engagement's details»
- `engagement_details_list` — «List all engagements with optional filtering»
- `engagement_details_archive` — «Archive (delete) an engagement»
- `engagement_details_get_associated` — «Get all engagements associated with an object»
- `calls_create` — «Create a new call record»
- `calls_get` — «Get details of a specific call»
- `calls_update` — «Update an existing call record»
- `calls_archive` — «Archive (delete) a call record»
- `calls_list` — «List all calls with optional filtering»
- `calls_search` — «Search calls with specific filters»
- `calls_batch_create` — «Create multiple call records in a single request»
- `calls_batch_read` — «Read multiple call records in a single request»
- `calls_batch_update` — «Update multiple call records in a single request»
- `calls_batch_archive` — «Archive (delete) multiple call records in a single request»
- `emails_create` — «Create a new email record»
- `emails_get` — «Get details of a specific email»
- `emails_update` — «Update an existing email record»
- `emails_archive` — «Archive (delete) an email record»
- `emails_list` — «List all emails with optional filtering»
- `emails_search` — «Search emails with specific filters»
- `emails_batch_create` — «Create multiple email records in a single request»
- `emails_batch_read` — «Read multiple email records in a single request»
- `emails_batch_update` — «Update multiple email records in a single request»
- `emails_batch_archive` — «Archive (delete) multiple email records in a single request»
- `communications_get_preferences` — «Get communication preferences for a contact»
- `communications_update_preferences` — «Update communication preferences for a contact»
- `communications_unsubscribe_contact` — «Unsubscribe a contact from all email communications»
- `communications_subscribe_contact` — «Subscribe a contact to all email communications»
- `communications_get_subscription_definitions` — «Get all subscription definitions for the portal»
- `communications_get_subscription_status` — «Get subscription status for multiple contacts»
- `communications_update_subscription_status` — «Update subscription status for multiple contacts»
- `products_list` — «Read a page of products. Control what is returned via the `properties` query param. `after` is the paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.»
- `products_read` — «Read an Object identified by ID»
- `products_create` — «Create a product with the given properties and return a copy of the object, including the ID.»
- `products_update` — «Perform a partial update of an Object identified by ID. Read-only and non-existent properties will result in an error. Properties values can be cleared by passing an empty string.»
- `products_archive` — «Move an Object identified by ID to the recycling bin.»
- `products_search` — «Search products»
- `products_batch_archive` — «Archive (delete) a batch of products by ID»
- `products_batch_create` — «Create a batch of products»
- `products_batch_read` — «Read a batch of products by internal ID, or unique property values. Retrieve records by the `idProperty` parameter to retrieve records by a custom unique value property.»
- `products_batch_update` — «Update a batch of products by internal ID, or unique values specified by the `idProperty` query param.»
