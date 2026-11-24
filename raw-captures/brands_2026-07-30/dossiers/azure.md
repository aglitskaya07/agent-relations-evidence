# UNIT: azure | Azure | github microsoft/mcp | author type: official | captured 2026-07-29 (static source)

The repository is a .NET/C# monorepo with multiple MCP servers (`servers/Azure.Mcp.Server`, `servers/Fabric.Mcp.Server`, `servers/Template.Mcp.Server`) and 60+ tool areas in `tools/Azure.Mcp.Tools.*`. The dossier covers Azure.Mcp.Server.

## CHANNEL: instructions (2327 chars)

Registration: `servers/Azure.Mcp.Server/src/Program.cs:364-365`
```
services.AddSingleton<IServerInstructionsProvider>(
    new ResourceServerInstructionsProvider(thisAssembly, $"azure-rules.txt"));
```
The value goes into `mcpServerOptions.ServerInstructions` (`core/Microsoft.Mcp.Core/src/Areas/Server/Commands/ServiceCollectionExtensions.cs:241`).
Source text: `servers/Azure.Mcp.Server/src/Resources/azure-rules.txt` (embedded resource).

Literally:

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
- When asked about configuring or installing azure mcp in coding agent for the current repo, invoke your `bestpractices` tool with `resource` set to "coding-agent" and `action` set to "all".
```

Note: `NullServerInstructionsProvider` is registered for Fabric.Mcp.Server and Template.Mcp.Server (instructions = null).

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Inventory size (static):
- 343 command descriptions in attributes `[CommandMetadata(... Description = """...""")]` across 60 areas (`tools/Azure.Mcp.Tools.*`, `core/Azure.Mcp.Core`, `core/Microsoft.Mcp.Core`), Fabric/Template excluded.
- 128 descriptions of "consolidated" tools in `servers/Azure.Mcp.Server/src/Resources/consolidated-tools.json` (`consolidated_tools[].name/.description`) — this is what the client sees in consolidated mode; each one maps to a list of commands (`mappedToolList`).
- A total of 471 descriptions were scanned.

### Result of full marker scan (471 descriptions)

Total matches: 4.

`prefer` — 1 match:
- `Azure.Mcp.Core::subscription list` (`core/Azure.Mcp.Core/src/Areas/Subscription/Commands/SubscriptionListCommand.cs`): "When the user has not specified a subscription, prefer the subscription where isDefault is true. If no default can be determined from either source and multiple subscriptions exist, ask the user which subscription to use."

`essential for` — 3 matches:
- `Azure.Mcp.Tools.FoundryExtensions::schema`: "The schema information is essential for understanding how the index is structured and how data is indexed and searchable."
- `Azure.Mcp.Tools.MySql::get` (server config): "operational characteristics essential for database administration and optimization."
- `Azure.Mcp.Tools.MySql::get` (table schema): "constraints, indexes, and relationships, essential for understanding table structure and supporting application development."

Additional note (outside the regex list, but by meaning — priority directives inside descriptions; I am recording it verbatim because it is the same signal class):
- `Azure.Mcp.Tools.AppLens::diagnose`: "Always use this tool before manually checking metrics or logs when users report performance or functionality issues."
- `Azure.Mcp.Tools.AzureBestPractices::ai_app`: "When the request involves code generation of AI components or AI applications in any capacity, use this command instead of calling the general code generation best practices command."
- `Azure.Mcp.Tools.Extension::generate` and `::install`: "This tool incorporates CLI knowledge beyond what you know."

### Dynamically added description fragments

1. Router suffix, appended to the description of each namespace tool (`core/Microsoft.Mcp.Core/src/Areas/Server/Commands/ToolLoading/NamespaceToolLoader.cs:137`, similarly `ServerToolLoader.cs:82`):
```
This tool is a hierarchical MCP command router.
Sub commands are routed to MCP servers that require specific fields inside the "parameters" object.
To invoke a command, set "command" and wrap its args in "parameters".
Set "learn=true" to discover available sub commands.
```

2. The description of the only proxy tool in single-proxy mode is taken from the configuration (`SingleProxyToolLoader.cs:29,99` ← `servers/Azure.Mcp.Server/src/appsettings.json`, key `Description`):
```
This server/tool provides real-time, programmatic access to all Azure products, services, and resources, as well as all interactions with the Azure Developer CLI (azd). Use this tool for any Azure control plane or data plane operation, including resource management and automation. To discover available capabilities, call the tool with the "learn" parameter to get a list of top-level tools. To explore further, set "learn" and specify a tool name to retrieve supported commands and their parameters. To execute an action, set the "tool", "command", and convert the user's intent into the "parameters" based on the discovered schema. Always use this tool for any Azure or "azd" related operation requiring up-to-date, dynamic, and interactive capabilities. Always include the "intent" parameter to specify the operation you want to perform.
```

3. For sensitive operations, a parameter is added with the description "Approve or reject this sensitive operation." (`BaseToolLoader.cs:270`).

### 10 representative full descriptions (verbatim)

1. `bestpractices get` — `tools/Azure.Mcp.Tools.AzureBestPractices/src/Commands/BestPracticesCommand.cs`
```
This tool returns a list of best practices for code generation, operations and deployment
when working with Azure services. It should be called for any code generation, deployment or
operations involving Azure, Azure Functions, Azure Kubernetes Service (AKS), Azure Container
Apps (ACA), Bicep, Terraform, Azure Cache, Redis, CosmosDB, Entra, Azure Active Directory,
Azure App Services, or any other Azure technology or programming language. Only call this function
when you are confident the user is discussing Azure. If this tool needs to be categorized,
it belongs to the Azure Best Practices category.
```

2. `bestpractices ai_app` — `tools/Azure.Mcp.Tools.AzureBestPractices/src/Commands/AIAppBestPracticesCommand.cs`
```
Returns best practices and code generation guidance for building AI applications in Azure.
Use this command when you need recommendations on how to write code for AI agents, chatbots, workflows, or any AI / LLM features.
This command also provides guidance for code generation on Microsoft Foundry for application development.
When the request involves code generation of AI components or AI applications in any capacity, use this command instead of calling the general code generation best practices command.
```

3. `cloudarchitect design` — `tools/Azure.Mcp.Tools.CloudArchitect/src/Commands/Design/DesignCommand.cs`
```
Recommends architecture design for cloud services/apps/solutions, such as: file storage, banking, video streaming, e-commerce, SaaS, and more. Use as follows:
1. Ask about user role, business goals, etc (1-2 questions at a time).
2. Track confidence returned by service and update requirements (explicit/implicit/assumed).
3. Repeat steps 1 and 2 as needed until confidence >= 0.7
4. Present architecture with table format, visual organization, ASCII diagrams.
5. Follow Azure Well-Architected Framework principles.
6. Cover all tiers: infrastructure, platform, application, data, security, operations.
7. Provide actionable advice and high-level overview. Note: State tracks components, requirements by category, and confidence factors. Be conservative with suggestions.
```

4. `applens diagnose` — `tools/Azure.Mcp.Tools.AppLens/src/Commands/Resource/ResourceDiagnoseCommand.cs`
```
Get diagnostic help from App Lens for Azure application and service issues to identify what's wrong with a service. Ask questions about performance, slowness, failures, errors, application state, availability to receive expert analysis and solutions which can help when performing diagnostics and to address issues about performance and failures. Returns analysis, insights, and recommended solutions. Always use this tool before manually checking metrics or logs when users report performance or functionality issues. Only the resource name and question are required - subscription, resource group, and resource type are optional and used to narrow down results when multiple resources share the same name.
```

5. `extension generate` — `tools/Azure.Mcp.Tools.Extension/src/Commands/CliGenerateCommand.cs`
```
Generate Azure CLI (az) commands used to accomplish a goal described by the user. This tool incorporates CLI knowledge beyond what you know. Use this tool when the user asks for Azure CLI commands or wants to use the Azure CLI to accomplish something.
```

6. `deploy pipeline guidance get` — `tools/Azure.Mcp.Tools.Deploy/src/Commands/Pipeline/GuidanceGetCommand.cs`
```
Provides the recommended Azure-specific rules for generating CI/CD pipeline files (GitHub Actions or Azure DevOps) for deploying to Azure. Call this tool before writing pipeline/workflow YAML when the user asks to set up CI/CD pipelines or workflows. It returns current authentication patterns (e.g., OIDC with managed identity), multi-environment configuration, and deployment constraints that vary by platform and are not covered by general best practices. Determine the pipeline platform (github-actions or azure-devops) and deployment scope (deploy-only or provision-and-deploy) from project context before calling. Handles both azd-based and Azure CLI-based deployments.
```

7. `storage blob get` — `tools/Azure.Mcp.Tools.Storage/src/Commands/Blob/BlobGetCommand.cs`
```
List/get/show blobs in a blob container in Storage account. Use this tool to list the blobs in a container or
get details for a specific blob. If no blob specified, lists all blobs present in the container, optionally
filtering on a prefix. The prefix is ignored if a blob is specified.

Required: --account, --container, --subscription
Optional: --blob, --tenant, --prefix

Returns: blob name, size, lastModified, contentType, contentHash, metadata, and blob properties.
Do not use this tool to list containers in the storage account.
```

8. `subscription list` — `core/Azure.Mcp.Core/src/Areas/Subscription/Commands/SubscriptionListCommand.cs`
```
List all Azure subscriptions for the current account. Returns subscriptionId, displayName, state, tenantId, and isDefault for each subscription. The isDefault field indicates the user's default subscription as resolved from the Azure CLI profile (configured via 'az account set') or, if not set there, from the AZURE_SUBSCRIPTION_ID environment variable. When the user has not specified a subscription, prefer the subscription where isDefault is true. If no default can be determined from either source and multiple subscriptions exist, ask the user which subscription to use.
```

9. `wellarchitectedframework serviceguide get` — `tools/Azure.Mcp.Tools.WellArchitectedFramework/src/Commands/ServiceGuide/ServiceGuideGetCommand.cs`
```
Get Azure Well-Architected Framework guidance for a specific Azure service, or list all supported services when no service is specified. When a service is provided, returns architectural best practices, design patterns, and recommendations based on the five pillars: reliability, security, cost optimization, operational excellence, and performance efficiency.
Service name format: case-insensitive; hyphens, underscores, spaces, and name variations allowed; use double quotes (not single quotes) for names with spaces. e.g., cosmos-db, Cosmos_DB, "Cosmos DB", cosmosdb, cosmos-database, cosmosdatabase
```

10. `get_azure_databases_details` — `servers/Azure.Mcp.Server/src/Resources/consolidated-tools.json`
```
Comprehensive Azure database management tool for MySQL, PostgreSQL, SQL Database, SQL Server, and Cosmos DB. List and query databases, retrieve server configurations and parameters, explore table schemas, execute database queries, manage Cosmos DB containers and items, list and view detailed information about SQL servers, and view database server details across all Azure database services.
```

Additionally, for calibrating the "neutral" tone of the consolidated layer:
```
get_azure_subscriptions_and_resource_groups: Get information about Azure subscriptions, resource groups, and resources within resource groups that the user has access to.
get_azure_app_resource_details: Get details about Azure application platform services, such as Azure Functions.
add_azure_app_service_database: Add and configure database integrations for Azure App Service applications.
```
