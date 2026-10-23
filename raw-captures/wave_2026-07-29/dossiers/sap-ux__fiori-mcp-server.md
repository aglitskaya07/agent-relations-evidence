# UNIT: @sap-ux/fiori-mcp-server | npm v1.11.2 (published 2026-07-28T07:55:19.281Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (подтверждено)

Настоящий stdio MCP-сервер: `bin: fiori-mcp → dist/index.js`, бандл esbuild с вшитым `@modelcontextprotocol/sdk` 1.29.0, собственный обработчик initialize возвращает `serverInfo:{name:"fiori-mcp"}` + строку instructions; статический массив из 10 инструментов, отдаётся через tools/list (grep: `tools/list` ×9, `tools/call` ×7, `registerTool`/`server.tool(` — 0, регистрация через сырые request handlers). Издатель — SAP (monorepo open-ux-tools). Также содержит embeddings-базу документации (`dist/data/embeddings/`) и ONNX/WASM-рантайм для локального семантического поиска (`search_docs`), keyring-прибилды и телеметрию (`jZ.sendTelemetry` на initialize).

## CHANNEL: instructions, npm (static, 2767 chars)

Передаётся в ответе initialize (поле `instructions`), дословно:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨🚨🚨 STOP - READ THIS BEFORE CALLING ANY TOOLS 🚨🚨🚨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOU ARE CONNECTED TO: SAP Fiori MCP Server

MANDATORY PROTOCOL - NO EXCEPTIONS:
1. Call tools/list FIRST in every session
2. Read the inputSchema for EVERY tool before calling it
3. Use ONLY the properties defined in inputSchema
4. DO NOT add extra properties, notes, or wrapper objects

IF YOU SKIP THESE STEPS:
❌ Your tool call will FAIL
❌ User's task will FAIL
❌ You will waste tokens and time
❌ You are violating the MCP protocol

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CORRECT Tool Call Workflow

✅ Step 1: Call tools/list
✅ Step 2: Examine inputSchema of the tool you need
✅ Step 3: Construct parameters using ONLY properties from inputSchema
✅ Step 4: Call the tool

## INCORRECT Workflow (DO NOT DO THIS)

❌ Assume you know the schema from training data
❌ Skip reading inputSchema
❌ Add properties not in inputSchema
❌ Wrap parameters in extra objects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Modifying an existing SAP Fiori application (3-step workflow)

When the user wants to modify an existing Fiori app, you MUST follow these steps in order:

1. **list_functionality** (Step 1) — Call with the absolute path to the Fiori app. Returns all supported modification operations and their functionalityIds.
2. **get_functionality_details** (Step 2) — Call with a functionalityId from Step 1. Returns the exact parameters required for the modification.
3. **execute_functionality** (Step 3) — Call with the parameters from Step 2 to apply the modification.

Never skip steps or guess functionalityIds. Never use a functionalityId as a tool name.

## Generating a new SAP Fiori application

- For OData/non-CAP projects: use `generate_fiori_app_odata`
  - BEFORE CALLING: Read its inputSchema from tools/list
  - REQUIRED top-level properties: floorplan, project
  - OPTIONAL top-level properties: service, entityConfig
  - DO NOT add: config, metadata, NOTE, or any other properties

- For CAP projects: use `generate_fiori_app_cap`
  - BEFORE CALLING: Read its inputSchema from tools/list

- If a SAP system or service URL is involved, call `download_odata_service_metadata` first and pass ALL fields it returns into the generator config.

## Other available tools

- `list_sap_systems` — list available SAP backends/destinations
- `list_fiori_apps` — discover existing Fiori apps in a directory
- `search_docs` — search Fiori Elements, SAPUI5, and annotation documentation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Наблюдения по стирингу в instructions: агрессивный императивный тон («STOP», «NO EXCEPTIONS», угрозы провала), но весь стиринг направлен внутрь собственного сервера (дисциплина схем и порядок шагов). Примечательно: instructions дважды отсылают агента к ЧУЖИМ MCP-серверам («Service Center MCP», «CDS MCP») — редкий паттерн кооперативного, а не захватнического стиринга.

## CHANNEL: tool descriptions, npm (static, coverage=full)

10 инструментов (все, дословно). Найденные вхождения `{name:"winston"...}` и `{name:"ejs"...}` — это package.json забандленных зависимостей, не инструменты.

### 1. search_docs
```
Searches code snippets of Fiori Elements, Annotations, SAPUI5, Fiori tools documentation for the given query. You MUST use this tool if you're unsure about Fiori APIs. Optionally returns only code blocks.
```

### 2. list_fiori_apps
```
Scans a specified directory to find existing SAP Fiori applications that can be modified.
                    This is an optional, preliminary tool.
                    **Use this first ONLY if the target application's name or path is not already known.**
                    The output can be used to ask the user for clarification before starting the main 3-step workflow.
```

### 3. list_sap_systems
```
Lists all SAP systems from the user's environment. This tool should only be used if the Service Center MCP tool list systems is unavailable. 
                    **ALWAYS** use the Service Center MCP tool 'list_systems' first if it is available. This tool is a fallback for environments where the Service Center MCP tool is not available.
                    Also use this tool when the user asks to 'list systems', 'list backends', or any equivalent phrasing.
                    Use this tool when the user references a SAP system by name or when you need to discover available systems
                    before calling 'download_odata_service_metadata' or generating a Fiori application.
```

### 4. download_odata_service_metadata
```
Downloads the metadata (EDMX) of a specific OData service URL from a SAP system and saves it as metadata.xml.
                    Note: this tool replaces the old 'fetch-service-metadata' functionality that was previously available via the 'execute_functionality' workflow — use this tool directly instead.

                    Usage guidelines:
                    - Use this before calling 'generate_fiori_app_odata' when the user provides a SAP system reference and a service path. 
                    - If a service name or technical id is provided instead of a service path DO NOT USE THIS TOOL. Instead use the Service Center MCP server tool to retrieve the service metadata and then pass it to 'generate_fiori_app_odata'.
                    - If a service path is provided by the user, use it directly via servicePath parameter.
                    - If the user provides a system name or host, use 'list_sap_systems' first to resolve it.
                    - Pass the full URL as sapSystemQuery.
                    - Returns host, servicePath, client, and metadataFilePath inside the result's parameters object.
                    - Pass ALL returned fields directly into the service config of 'generate_fiori_app_odata'. Map the returned properties to the app config service property input to 'generate_fiori_app_odata'.
                    - **Note:** This tool is only supported in VSCode. For SAP Business Application Studio, use the Service Center MCP server tool to retrieve the service metadata instead.
                    **IMPORTANT**: On VSCode, if the service requires authentication and the system is not already stored, ask the user to store it first. Do not ask for credentials directly.
```

### 5. generate_fiori_app_odata
```
Creates (generates) a new SAP Fiori UI application either within an existing CAP project or standalone. ALWAYS read ALL of the following instructions carefully before calling this tool.

        🚨 CRITICAL - READ SCHEMA FIRST 🚨
        Before calling this tool, you MUST:
        1. Examine the inputSchema below to understand the EXACT structure required
        2. The input MUST match the schema type 'GeneratorConfigOData' with these TOP-LEVEL properties:
           - floorplan (must be: 'FE_LROP', 'FE_OVP', 'FE_ALP', 'FE_WORKLIST', 'FE_FEOP', 'FE_FPM', 'FF_SIMPLE', required)
           - project (object, required)
           - service (object, optional)
           - entityConfig (object, optional)
        3. DO NOT create properties like "config", or any other structure - use ONLY the properties defined in inputSchema

        Steps:
        1. Construct the tool arguments.
           - **IMPORTANT** ALWAYS use the app config schema defined by the type 'GeneratorConfigOData' to create the input structure. NEVER create an input in any other format.
           - The input MUST use the exact property names defined in the inputSchema: floorplan, project, service, entityConfig.
           - **ONLY** if the Service Center MCP is NOT available and the user provided a SAP system reference or URL with a **service path**, you **MUST** first call 'download_odata_service_metadata'.
           - If the Service Center MCP is available and the user provided a **service name or technical service id**, you **MUST** call the Service Center MCP server tool to retrieve the metadata and properties required for the service property of the input. 
           - Use the data returned to provide the required values (host, servicePath, client, destination, metadataFilePath) directly in the service property of the input.
           - If the Service Center MCP was used both host and destination **MUST** be passed in the service property of the input.
           - If Fiori MCP 'download_odata_service_metadata' was used and returns a host URL — pass it as service.host. If the host is not provided, you **MUST** ask for it.
           - **IMPORTANT**: On VSCode, if the service requires authentication and is not already stored, ask the user to store it first. Never ask for credentials directly.

        2. Parse the metadata.xml to understand the data model (entities, associations).

        3. Generate the application once the config is complete and valid.

        Example of CORRECT input structure:
        {
          "floorplan": "FE_LROP",
          "project": {
            "name": "my-travel-app",
            "title": "My Travel App",
            "description": "Travel management application",
            "targetFolder": "/home/user/projects",
            "ui5Version": "1.136.7"
          },
          "service": {
            "host": "https://my-system.example.com",
            "servicePath": "<full-odata-service-path>",
            "client": "000",
            "metadataFilePath": "/home/user/projects/metadata.xml",
            "destination": "MY_DESTINATION"
          },
          "entityConfig": {
            "mainEntity": { "entityName": "Travel" },
            "generateFormAnnotations": true,
            "generateLROPAnnotations": true
          }
        }
```

### 6. generate_fiori_app_cap
```
Creates (generates) a new SAP Fiori UI application within an existing CAP project.
                    To populate parameters, you **MUST** use the ***CDS MCP*** to search the model for service definitions, entities, associations, and UI annotations.
                    As a fallback, only if no such tool is available, manually read and parse all .cds files in the projectPath.
                    The configuration **MUST** be a valid JSON object matching the tool's inputSchema and based on the project files.
```

### 7. list_functionality
```
**(Step 1 of 3) — Use this to modify an existing SAP Fiori application.**
                    Returns the complete list of supported modification operations for a given application, including:
                    adding or deleting pages, creating controller extensions, and changing any Fiori Elements manifest property.
                    This is the **first mandatory step** for modifying an existing app and requires a valid absolute path to a SAP Fiori application.
                    You MUST use a functionalityId from this tool's output in 'get_functionality_details' (Step 2).
                    You MUST NOT use a functionalityId as a tool name.
                    Do not guess or assume functionalityIds — only use what this tool returns.
                    **Note: If the target application is not known, use 'list_fiori_apps' first.**
                    **Note: To generate a new app, use 'generate_fiori_app_odata' or 'generate_fiori_app_cap' instead.**
                    If the functionality list does not cover your goal, use 'search_docs' as a fallback.
```

### 8. get_functionality_details
```
**(Step 2 of 3)**
                    Gets the required parameters and detailed information for a specific functionality to modify an existing SAP Fiori application.
                    You MUST provide a functionalityId obtained from 'list_functionality' (Step 1).
                    The output of this tool is required for the final step 'execute_functionality' (Step 3).
```

### 9. execute_functionality
```
**(Step 3 of 3)**
                    Executes a specific functionality to modify an existing SAP Fiori application with provided parameters.
                    This is the **final step** of the workflow and performs the actual modification.
                    You MUST provide the exact parameter information obtained from get_functionality_details (Step 2).
```

### 10. (маркер-заметки по стирингу в описаниях)
- Плотность MUST/ALWAYS/NEVER очень высокая (десятки вхождений), но все директивы — про дисциплину внутри собственного воркфлоу, не про вытеснение встроенных инструментов агента.
- `search_docs`: «You MUST use this tool if you're unsure about Fiori APIs» — единственная директива, претендующая на замещение знаний модели (мягкая, доменно-ограниченная).
- Анти-захват: list_sap_systems и download_odata_service_metadata явно уступают приоритет стороннему «Service Center MCP» («ALWAYS use the Service Center MCP tool ... first», «This tool is a fallback»), generate_fiori_app_cap требует чужой «CDS MCP». Сервер сам понижает себя в иерархии — противоположность паттернам «PRECEDENCE/primary interface».
- Безопасность: дважды «Do not ask for credentials directly / Never ask for credentials directly».

## NOTES
- Код: единый esbuild-бандл dist/index.js, 9.45 MB, 4715 строк, минифицирован (переменные вида `Bio`, `Iyt`), но все строки инструментов и instructions лежат литералами (template literals) — статическая экстракция полная.
- Риск динамической сборки строк: низкий для tools/instructions (статический массив у позиции ~9.40M, instructions — литерал в initialize-хендлере). Однако `list_functionality` возвращает ДИНАМИЧЕСКИЙ список «functionalities» (генерируется из @sap/ux-specification по конкретному проекту) — это второй, не пойманный статикой канал текста, который агент читает как инструкции (functionality-описания). Также в бандле — локальная embeddings-база доков (records.jsonl/embeddings.bin): контент search_docs-выдачи статикой не оценивался.
- Телеметрия: на initialize отправляется telemetry (mcpClientName/Version) через @sap-ux/telemetry (Application Insights код в бандле).
- Файлов просмотрено: package.json, README.md (бегло), dist/index.js (regex-скан целиком), листинг дерева (~23 файла в пакете). Код пакета НЕ исполнялся.
