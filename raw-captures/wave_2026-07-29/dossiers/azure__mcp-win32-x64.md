# UNIT: @azure/mcp-win32-x64 | npm v3.0.0-beta.30 (published 2026-07-28T18:26:14.992Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## ВЕРДИКТ ПО ТИПУ
Это MCP-сервер: Azure MCP Server, скомпилированный в нативный Windows-бинарник (`dist/azmcp.exe`, PE32+ x86-64, ~110 МБ, .NET AOT). JS-часть (`index.js`, 2.1 КБ) — только лаунчер, спавнящий exe. Внутри бинарника: `Microsoft.Mcp.Core.Areas.Server.Commands.ServerStartCommand`, `McpRuntime` (CallToolHandler/ListToolsHandler), тул-лоадеры (CommandFactoryToolLoader, NamespaceToolLoader, RegistryToolLoader, ServerToolLoader, SingleProxyToolLoader) и встроенные ресурсы `azure-rules.txt`, `consolidated-tools.json`, `registry.json`. Анализ — статическая экстракция строк (ASCII + UTF-16LE) без исполнения кода пакета.

## CHANNEL: instructions, npm (static, 2332 chars)

Источник: встроенный ресурс `Azure.Mcp.Server.Resources.azure-rules.txt`, подаётся через `ResourceServerInstructionsProvider` → `ServerInstructions` (в бинарнике: `IServerInstructionsProvider`, `ResourceServerInstructionsProvider`, `NullServerInstructionsProvider`, `set_ServerInstructions`). Дословный текст:

```
Azure MCP server usage rules:
- Use Azure Tools: When handling requests related to Azure, always use your tools.
- Troubleshoot Azure errors: When an Azure MCP tool call fails or returns an error (for example an authentication, authorization, tenant, or subscription related failure), consult the troubleshooting guide at https://aka.ms/azmcp/troubleshooting for possible causes and resolutions before giving up or asking the user. For example, if a call fails because of an incorrect subscription or tenant context, retry the tool call with the correct `tenant` and/or `subscription` parameter.
- If a user wants to use, install, or generate commands for the Azure CLI (az), Azure Developer CLI (azd), Azure Functions Core Tools CLI (func), or Azure Quick Review CLI (azqr), use your `extension` tools first.
- Use Azure Code Gen Best Practices: When generating code for Azure or any Azure services, running terminal commands for Azure, or performing operations related to Azure, invoke your `bestpractices` tool if available.
- Use Azure Deployment Best Practices: When deploying to Azure or preparing applications for deployment to Azure, invoke your `bestpractices` tool if available.
- Only call your `bestpractices` tool when you are sure the user is discussing Azure; do not call it otherwise.
- Use Azure AI App Code Generation Best Practices: When generating code for AI applications, AI agents, workflows, or chatbots, invoke your `get_azure_bestpractices_ai_app` command (under `get_azure_bestpractices` tool) if tool available. Call this tool first before creating any plans, todos or code. Only call this command when the user is discussing AI app development with Microsoft Foundry, Azure, Microsoft agent framework SDK, or without specifying any technology. Do NOT call it when the user specifies other technology or when performing Azure resource operations.
- Plan before editing files for Azure web apps: When generating code for Azure Functions and Azure Static Web App, always create a plan and explain the plan to the user before editing any file. Proceed with editing the files after getting consent from the user.
- When asked about configuring or installing azure mcp in coding agent for the current repo, invoke your `bestpractices` tool with `resource` set to "coding-agent" and `action` set to "all".BSJB
```

Оценка стеринга в instructions: умеренный, доменно-ограниченный. «When handling requests related to Azure, always use your tools»; предписания вызывать `bestpractices`/`get_azure_bestpractices_ai_app` «first before creating any plans, todos or code»; «use your `extension` tools first» для az/azd/func/azqr. Есть сдерживающие оговорки («do not call it otherwise», «Do NOT call it when the user specifies other technology»).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Поверхности экспозиции (сервер многорежимный, все видны статически):
- `consolidated-tools.json` (встроенный ресурс): **128 инструментов** с name+description+toolMetadata — консолидированный режим.
- Namespace-режим: ~30 namespace-инструментов (строки вида «X operations - …»).
- Полный режим: 180+ листовых команд (описания в UTF-16/ASCII строках бинарника).
- Single-proxy режим: один корневой инструмент "azure" (описание в appsettings.json внутри exe).
- `registry.json`: описания внешних проксируемых серверов (documentation / azd / foundry / arm).

Инструментов > 40 → полный маркер-скан по всем извлечённым строкам бинарника (~527k ASCII + ~71k UTF-16 строк) и отдельно по 128 описаниям consolidated-tools.json (по ним маркер-хитов: 0).

### Маркер-скан: совпадения в описаниях инструментов/серверов (дословно)

1. **Корневой proxy-инструмент "azure"** (appsettings.json, single-tool режим):
> "This server/tool provides real-time, programmatic access to all Azure products, services, and resources, as well as all interactions with the Azure Developer CLI (azd). Use this tool for any Azure control plane or data plane operation, including resource management and automation. To discover available capabilities, call the tool with the "learn" parameter to get a list of top-level tools. To explore further, set "learn" and specify a tool name to retrieve supported commands and their parameters. To execute an action, set the "tool", "command", and convert the user's intent into the "parameters" based on the discovered schema. Always use this tool for any Azure or "azd" related operation requiring up-to-date, dynamic, and interactive capabilities. Always include the "intent" parameter to specify the operation you want to perform."
Маркеры: `Always use this tool`, «for any … operation».

2. **registry.json → "documentation" (Microsoft Learn MCP proxy)**:
> "Search official Microsoft/Azure documentation to find the most relevant and trustworthy content for a user's query. This tool returns up to 10 high-quality content chunks (each max 500 tokens), extracted from Microsoft Learn and other official sources. Each result includes the article title, URL, and a self-contained content excerpt optimized for fast retrieval and reasoning. Always use this tool to quickly ground your answers in accurate, first-party Microsoft/Azure knowledge."
Маркеры: `Always use this tool`, `trustworthy`.

3. **applens (namespace)**:
> "AppLens diagnostic operations - Primary tool for diagnosing and troubleshooting Azure resource issues. Uses conversational AI-powered diagnostics to detect problems, identify root causes, and recommend remediation steps. This tool should be the first choice when users report errors, performance issues, availability problems, or unexpected Azure resource behavior."
Маркеры: `Primary tool`, `first choice`.

4. **applens leaf (диагностика ресурса)**:
> "Get diagnostic help from App Lens for Azure application and service issues to identify what's wrong with a service. Ask questions about performance, slowness, failures, errors, application state, availability to receive expert analysis and solutions which can help when performing diagnostics and to address issues about performance and failures. Returns analysis, insights, and recommended solutions. Always use this tool before manually checking metrics or logs when users report performance or functionality issues. Only the resource name and question are required - subscription, resource group, and resource type are optional and used to narrow down results when multiple resources share the same name."
Маркер: `Always use this tool before` (вытесняет самостоятельную проверку метрик/логов агентом).

5. **functionapp codegen**:
> "Azure Functions code generation commands. ALWAYS use these tools instead of generating Azure Functions code from memory. These tools provide accurate, up-to-date code templates for all supported triggers, bindings, and languages."
Маркеры: `ALWAYS use … instead of … from memory`.

6. **advisor aggregate (leaf)**:
> "Aggregate Azure Advisor recommendations server-side and return per-bucket counts plus a true total. This is the CORRECT tool whenever the user asks 'how many', 'top N <something>', 'which <X> has the most', 'breakdown by <field>', 'distribution of', 'count of', or any ranking/comparison question over the recommendation set. Do not try to answer such questions by calling 'list' and counting client-side"
Маркеры: `whenever the user`, «This is the CORRECT tool», запрет альтернативного пути.

7. **deploy (namespace)**:
> "Deploy operations - Generate recommended Azure deployment plans, architecture diagrams, IaC (Bicep/Terraform) rules, and CI/CD pipeline/workflow guidance. Retrieve application logs for azd-deployed apps. Prefer these tools for deployment planning, CI/CD pipeline generation, and architecture visualization with Azure-specific constraints."
Маркер: `Prefer these tools`.

8. **bestpractices (namespace)** (пробельные последовательности оригинала сжаты):
> "Azure best practices - Commands return a list of best practices for code generation, operations and deployment when working with Azure services. It should be called for any code generation, deployment or operations involving Azure, Azure Functions, Azure Kubernetes Service (AKS), Azure Container Apps (ACA), Bicep, Terraform, Azure Cache, Redis, CosmosDB, Entra, Azure Active Directory, Azure App Services, or any other Azure technology or programming language. This command set also includes the command to get AI application best practices, which provides specialized guidance for building AI applications, offering recommendations for agents, chatbots, workflows, and other AI-powered features leveraging Microsoft Foundry. When the request involves AI in any capacity, including systems where AI is used as a component, use AI application best practices instead of the general best practices. Call this tool first before creating any plans, todos or code. Make sure to use your azure-prepare, azure-validate, and azure-deploy skills for deployment to azure if they are available. Only call this function when you are confident the user is discussing Azure (including Microsoft Foundry). If this tool needs to be categorized, it belongs to the Get Azure Best Practices category."
Маркеры: «Call this tool first before creating any plans, todos or code», «for any code generation».

9. **monitor activity log (leaf)**:
> "Always use this tool if user is asking for activity logs for a resource."
Маркер: `Always use this tool`.

10. **advisor list, параметр filter**:
> "Free-text filter applied to the recommendation problem text (case-insensitive substring match). Use this whenever the user's request includes a topical phrase such as 'related to Microsoft Foundry', 'about encryption', 'mentioning right-size', or 'for Key Vault'. Extract the salient noun(s) from the phrase (e.g., 'Foundry', 'encrypt', 'right-size', 'Key Vault') and pass them here."
Маркер: `whenever the user` (на уровне параметра).

11. **subscription list (leaf)** — мягкое поведенческое указание:
> "List all Azure subscriptions for the current account. Returns subscriptionId, displayName, state, tenantId, and isDefault for each subscription. The isDefault field indicates the user's default subscription as resolved from the Azure CLI profile (configured via 'az account set') or, if not set there, from the AZURE_SUBSCRIPTION_ID environment variable. When the user has not specified a subscription, prefer the subscription where isDefault is true. If no default can be determined from either source and multiple subscriptions exist, ask the user which subscription to use."
Маркер: `prefer` (безобидное разрешение неоднозначности).

Шум, исключённый из скана описаний: десятки `prefer|must use|takes precedence` в строках сторонних SDK (Cosmos, Npgsql, MSAL, XSLT) и в payload-ресурсах (best-practices тексты, деплой-гайды, Instrumentation/Resources/*.md) — это контент, возвращаемый инструментами, а не их описания.

### 8 репрезентативных полных описаний

**1. get_azure_resilience_management_details (consolidated):**
> "Get details about Azure Resilience Management resources, including resilience goals (templates, assignments, and their resources), usage plans and enrollments, and recovery plans (plans, resources, and jobs) for Azure service groups."

**2. get_azure_best_practices (consolidated):**
> "Retrieve Azure best practices and infrastructure schema for code generation, deployment, and operations. Covers general Azure practices, Azure Functions best practices, AI app development best practices, Terraform configurations, Bicep template schemas, deployment best practices and Well-Architected Framework guidance."

**3. deploy_azure_resources_and_applications (consolidated):**
> "Deploy resources and applications to Azure. Generate architecture diagrams, deployment plans, IaC rules for Bicep and Terraform, and CI/CD pipeline guidance."

**4. get_azure_subscriptions_and_resource_groups (consolidated):**
> "Get information about Azure subscriptions, resource groups, and resources within resource groups that the user has access to."

**5. storage (namespace):**
> "Storage operations - Commands for creating, listing, getting, and managing Azure Storage accounts, blob containers, blobs, and tables. Use this tool to create storage accounts, list and get storage account details (SKU, location, HNS, HTTPS-only settings), create and list blob containers, list and get blob properties, upload files to blob storage, and list tables. Covers Azure Blob Storage, Azure Table Storage, and storage account management. Do not use for Azure Cosmos DB containers, Azure Container Registry, or Azure Managed Lustre file systems."

**6. compute (namespace):**
> "Compute operations - Commands for managing and monitoring Azure Virtual Machines (VMs), Virtual Machine Scale Sets (VMSS), and Managed Disks. This tool provides comprehensive access to VM lifecycle management, instance monitoring, size discovery, and scale set operations. Use this tool when you need to list, query, create, or monitor VMs and VMSS instances across subscriptions and resource groups. Defaults to Standard_D2s_v5 VM size for VM and VMSS creation when not specified; the --image option is required. This tool is a hierarchical MCP command router where sub-commands are routed to MCP servers that require specific fields inside the "parameters" object. To invoke a command, set "command" and wrap its arguments in "parameters". Set "learn=true" to discover available sub-commands for different Azure Compute operations."

**7. monitor (namespace):**
> "Monitor operations - Commands for managing Azure Monitor workspaces, querying and analyzing logs and metrics, listing tables and table types, working with health models and entities, web tests, and orchestrating instrumentation workflows. Use this tool to list Log Analytics workspaces, tables, and table types; run KQL queries against workspace and resource logs; retrieve health for monitor entities; query metrics and metric definitions; inspect resource activity logs; manage availability web tests; and guide instrumentation onboarding and enhancement flows. Covers Azure Monitor observability workflows. Set learn=true to discover sub-commands."

**8. advisor (namespace):**
> "Azure Advisor operations - Query Azure Advisor recommendations across subscriptions OR Apply Azure Advisor recommendations to your IaaC files (ARM, Terraform). Use when you need subscription-scoped visibility into Advisor recommendations OR want to apply Advisor recommendations to your IaaC files. Requires Azure subscription context for querying Advisor recommendations."

### Общая оценка стеринга tool descriptions
Основная масса из 128 consolidated-описаний нейтральна (маркер-скан по ним: 0 совпадений). Стеринг сосредоточен: (а) в корневом proxy-описании single-tool режима («Always use this tool for any Azure…»), (б) в registry-описании Microsoft Learn («Always use this tool to quickly ground your answers»), (в) точечно в applens/bestpractices/functionapp/advisor («Primary tool», «first choice», «ALWAYS … instead of … from memory», «Call this tool first before creating any plans»). Весь стеринг остаётся внутри Azure-домена; кросс-вендорного вытеснения built-in инструментов или чужих серверов не обнаружено.

## NOTES
- Код: нативный AOT-бинарник (PE32+, 110 МБ), JS не минифицирован (2 КБ лаунчер); строки извлечены статически (strings + UTF-16LE regex), исполнение не производилось.
- Риск динамической сборки строк: низкий для описаний (константы/JSON-ресурсы в бинарнике), но есть динамические слои: RegistryToolLoader подтягивает внешние MCP-серверы из registry.json (learn.microsoft.com/api/mcp, azd stdio, mcp.ai.azure.com, mcp.management.azure.com) — их runtime-описания статически не видны; Namespace/ServerToolLoader используют sampling-промпты для intent→command (промпты найдены в строках).
- Файлов в пакете 70; текстово смотрел package.json, index.js, Azure.Mcp.Tools.AzureMigrate.xml + полную строковую выгрузку azmcp.exe (~598k строк); 66 Instrumentation/*.md — payload-контент инструментов. Извлечены встроенные ресурсы: azure-rules.txt (2332 chars), consolidated-tools.json (128 tools, ~189 KB), registry.json, appsettings.json.
- Instructions-канал подтверждён по типам (ResourceServerInstructionsProvider → ServerInstructions); фактическую передачу в initialize статически не наблюдал, но иных кандидатов на источник instructions в бинарнике нет.
