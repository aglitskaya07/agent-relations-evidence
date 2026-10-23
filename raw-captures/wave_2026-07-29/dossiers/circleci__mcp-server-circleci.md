# UNIT: @circleci/mcp-server-circleci | npm v0.19.0 (published 2026-07-19T18:15:30.165Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## SERVER: подтверждён
MCP-сервер на `@modelcontextprotocol/sdk` — `dist/index.js` строит `new McpServer({ name: 'mcp-server-circleci', version: '1.0.0' }, { capabilities: { tools: {}, resources: {} } })`, регистрирует 13 инструментов через `server.tool(...)`, транспорты stdio и unified HTTP+SSE. Есть OpenTelemetry-обёртка над хендлерами (телеметрия по вызовам инструментов).

## CHANNEL: instructions, npm (static)
(не обнаружены статически) — конструктору McpServer передаются только name/version и capabilities; поле `instructions` нигде в dist/ не задаётся (единственное вхождение слова — фраза «Tool output instructions:» внутри описания config_helper).

## CHANNEL: tool descriptions, npm (static, coverage=full)
Всего инструментов: 13. Описания дословно из `dist/tools/*/tool.js` (шаблонная подстановка `${option1DescriptionBranchRequired}` развёрнута из `dist/tools/shared/constants.js`).

### get_build_failure_logs  (annotations: —)
```

    This tool helps debug CircleCI build failures by retrieving failure logs.

    CRITICAL REQUIREMENTS:
    1. Large Log Handling:
       - If you expect large logs or want the full output, provide outputDir. The full logs will be written to a file and the path returned.
         * Use the project/workspace root when available, otherwise use the Downloads folder (e.g., "~/Downloads").
       - If outputDir is omitted, logs are returned inline but may be truncated. When truncated, output will contain <MCPTruncationWarning> and you MUST acknowledge: "WARNING: The logs have been truncated. Only showing the most recent entries."

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL: https://app.circleci.com/pipelines/gh/organization/project
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Legacy Job URL: https://circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch
    
    Recommended Workflow:
    1. Use listFollowedProjects tool to get a list of projects
    2. Extract the projectSlug from the chosen project (format: "gh/organization/project")
    3. Use that projectSlug with a branch name for this tool

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
    
```

### find_flaky_tests  (annotations: destructiveHint: true)
```

    This tool retrieves information about flaky tests in a CircleCI project. 
    
    The agent receiving this output MUST analyze the flaky test data and implement appropriate fixes based on the specific issues identified.

    CRITICAL REQUIREMENTS:
    1. Truncation Handling (HIGHEST PRIORITY):
       - ALWAYS check for <MCPTruncationWarning> in the output
       - When present, you MUST start your response with:
         "WARNING: The logs have been truncated. Only showing the most recent entries. Earlier build failures may not be visible."
       - Only proceed with log analysis after acknowledging the truncation

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug:
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL: https://app.circleci.com/pipelines/gh/organization/project
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, BOTH parameters (workspaceRoot, gitRemoteURL) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
    
```

### get_latest_pipeline_status  (annotations: —)
```

    This tool retrieves the status of the latest pipeline for a CircleCI project. It can be used to check pipeline status, get latest build status, or view current pipeline state.

    Common use cases:
    - Check latest pipeline status
    - Get current build status
    - View pipeline state
    - Check build progress
    - Get pipeline information

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL: https://app.circleci.com/pipelines/gh/organization/project
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz
      * Legacy Job URL: https://circleci.com/gh/organization/project/123

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch
    
    Recommended Workflow:
    1. Use listFollowedProjects tool to get a list of projects
    2. Extract the projectSlug from the chosen project (format: "gh/organization/project")
    3. Use that projectSlug with a branch name for this tool

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
  
```

### get_job_test_results  (annotations: —)
```

    This tool retrieves test metadata for a CircleCI job.

    PRIORITY USE CASE:
    - When asked "are tests passing in CI?" or similar questions about test status
    - When asked to "fix failed tests in CI" or help with CI test failures
    - Use this tool to check if tests are passing in CircleCI and identify failed tests
    
    Common use cases:
    - Get test metadata for a specific job
    - Get test metadata for all jobs in a project
    - Get test metadata for a specific branch
    - Get test metadata for a specific pipeline
    - Get test metadata for a specific workflow
    - Get test metadata for a specific job

    CRITICAL REQUIREMENTS:
    1. Truncation Handling (HIGHEST PRIORITY):
       - ALWAYS check for <MCPTruncationWarning> in the output
       - When present, you MUST start your response with:
         "WARNING: The test results have been truncated. Only showing the most recent entries. Some test data may not be visible."
       - Only proceed with test result analysis after acknowledging the truncation

    2. Test Result Filtering:
       - Use filterByTestsResult parameter to filter test results:
         * filterByTestsResult: 'failure' - Show only failed tests
         * filterByTestsResult: 'success' - Show only successful tests
       - When looking for failed tests, ALWAYS set filterByTestsResult to 'failure'
       - When checking if tests are passing, set filterByTestsResult to 'success'

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI job in any of these formats:
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/789
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch
    
    For simple test status checks (e.g., "are tests passing in CI?") or fixing failed tests, prefer Option 1 with a recent pipeline URL if available.

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects and include the branch parameter
    - If using Option 2, the URL MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
    
```

### config_helper  (annotations: —)
```

  This tool helps analyze and validate and fix CircleCI configuration files.

  Parameters:
  - params: An object containing:
    - configFile: string - The full contents of the CircleCI config file as a string. This should be the raw YAML content, not a file path.

  Example usage:
  {
    "params": {
      "configFile": "version: 2.1\norbs:\n  node: circleci/node@7\n..."
    }
  }

  Note: The configFile content should be provided as a properly escaped string with newlines represented as \n.

  Tool output instructions:
    - If the config is invalid, the tool will return the errors and the original config. Use the errors to fix the config.
    - If the config is valid, do nothing.
  
```

### run_pipeline  (annotations: destructiveHint: true)
```

    This tool triggers a new CircleCI pipeline and returns the URL to monitor its progress.

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI project in any of these formats:
      * Project URL with branch: https://app.circleci.com/pipelines/gh/organization/project?branch=feature-branch
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/xyz

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch

    Configuration:
    - an optional configContent parameter can be provided to override the default pipeline configuration

    Pipeline Selection:
    - If the project has multiple pipeline definitions, the tool will return a list of available pipelines
    - You must then make another call with the chosen pipeline name using the pipelineChoiceName parameter
    - The pipelineChoiceName must exactly match one of the pipeline names returned by the tool
    - If the project has only one pipeline definition, pipelineChoiceName is not needed

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects
    - If using Option 2, the URLs MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call

    Returns:
    - A URL to the newly triggered pipeline that can be used to monitor its progress
    
```

### list_followed_projects  (annotations: —)
```

    This tool lists all projects that the user is following on CircleCI.
    
    Common use cases:
    - Identify which CircleCI projects are available to the user
    - Select a project for subsequent operations
    - Obtain the projectSlug needed for other CircleCI tools
    
    Returns:
    - A list of projects that the user is following on CircleCI
    - Each entry includes the project name and its projectSlug
    
    Workflow:
    1. Run this tool to see available projects
    2. User selects a project from the list
    3. The LLM should extract and use the projectSlug (not the project name) from the selected project for subsequent tool calls
    4. The projectSlug is required for many other CircleCI tools, and will be used for those tool calls after a project is selected
    
    Note: If pagination limits are reached, the tool will indicate that not all projects could be displayed.
    
    IMPORTANT: Do not automatically run any additional tools after this tool is called. Wait for explicit user instruction before executing further tool calls. The LLM MUST NOT invoke any other CircleCI tools until receiving a clear instruction from the user about what to do next, even if the user selects a project. It is acceptable to list out tool call options for the user to choose from, but do not execute them until instructed.
    
```

### rerun_workflow  (annotations: destructiveHint: true)
```

  This tool is used to rerun a workflow from start or from the failed job.

  Common use cases:
  - Rerun a workflow from a failed job
  - Rerun a workflow from start

Input options (EXACTLY ONE of these TWO options must be used):

Option 1 - Workflow ID:
- workflowId: The ID of the workflow to rerun
- fromFailed: true to rerun from failed, false to rerun from start. If omitted, behavior is based on workflow status. (optional)

Option 2 - Workflow URL:
- workflowURL: The URL of the workflow to rerun
  * Workflow URL: https://app.circleci.com/pipelines/:vcsType/:orgName/:projectName/:pipelineNumber/workflows/:workflowId
  * Workflow Job URL: https://app.circleci.com/pipelines/:vcsType/:orgName/:projectName/:pipelineNumber/workflows/:workflowId/jobs/:buildNumber
- fromFailed: true to rerun from failed, false to rerun from start. If omitted, behavior is based on workflow status. (optional)
  
```

### download_usage_api_data  (annotations: destructiveHint: true)
```

    ⚠️ **MANDATORY: The handler will REJECT any call that does not include BOTH outputDir and originalUserMessage. These parameters are REQUIRED for all tool calls.**
    
    ⚠️ **MANDATORY OUTPUT DIRECTORY SELECTION FOR AI AGENTS:**
    1. If the project root (workspace root) is available (e.g., via `workspaceRoot` or known repository context), you MUST pass it as the `outputDir` parameter.
    2. If the project root is not available, you MUST use the user's Downloads folder (e.g., `~/Downloads` or `%USERPROFILE%\Downloads`) as the `outputDir` parameter.
    3. Only if neither is available, use the current working directory (`process.cwd()`).
    4. **Never omit the `outputDir` parameter. Always make the output location explicit.**
    5. **Omitting `outputDir` is a critical error. Tool calls without `outputDir` may be rejected or flagged as incorrect. Repeated violations may be treated as a bug in the AI agent.**
    6. **AI agents MUST validate their tool calls to ensure `outputDir` is present before execution.**

    Downloads usage data from the CircleCI Usage API for a given organization and date range.
    This tool both starts the export job and downloads the resulting CSV file when ready.
    Required parameters: orgId, startDate, endDate, outputDir.

    **outputDir (required):**
    The directory where the usage data CSV will be saved.
    - You MUST provide `outputDir` for every tool call.
    - The file will be saved in the specified directory.
    - Omitting `outputDir` will result in an error.

    **Directory Selection Instructions for AI Agents:**
    - If the project root is available (e.g., via `workspaceRoot`, `outputDir`, or known repository context), always use it as the output directory for file outputs.
    - If no project root is available (e.g., running in the user's home directory or a generic environment), use the user's Downloads folder (e.g., `~/Downloads` or `%USERPROFILE%\Downloads`)
    - If neither is available, fall back to the current working directory.
    - Never place output files in a location that is hard to discover for the user.
    - **Always double-check that `outputDir` is present in your tool call.**
    - **Always double-check that `originalUserMessage` is present in your tool call.**

    This ensures that downloaded usage data is always saved in a location that is relevant and easy for the user to find, and that the output is always copy-paste friendly for status checks, regardless of the environment in which the tool is run.
  
```

### find_underused_resource_classes  (annotations: —)
```

    Analyzes a CircleCI usage data CSV file to find jobs/resource classes with average or max CPU/RAM usage below a given threshold (default 40%).
    This helps identify underused resource classes that may be oversized for their workload.

    Required parameter:
    - csvFilePath: Path to the usage data CSV file (string). IMPORTANT: This must be an absolute path. If you are given a relative path, you must resolve it to an absolute path before calling this tool.

    Optional parameter:
    - threshold: Usage percentage threshold (number, default 40)

    The tool expects the CSV to have columns: job_name, resource_class, median_cpu_utilization_pct, max_cpu_utilization_pct, median_ram_utilization_pct, max_ram_utilization_pct (case-insensitive). These required columns are a subset of the columns in the CircleCI usage API output and the tool will work with the full set of columns from the usage API CSV.
    It returns a summary report listing all jobs/resource classes where any of these metrics is below the threshold.
  
```

### run_rollback_pipeline  (annotations: destructiveHint: true)
```

    Run a rollback pipeline for a CircleCI project. This tool guides you through the full rollback process, adapting to the information you provide and prompting for any missing details.

    **Initial Requirements:**
    - You need either a `projectSlug` (from `listFollowedProjects`) or a `projectID`. The tool will automatically resolve the project information from either of these.

    **Typical Flow:**
    1. **Start:** User initiates a rollback request.
    2. **Project Selection:** If project id or project slug are not provided, call `listFollowedProjects` to get the list of projects the user follows and present the full list of projects to the user so that they can select the project they want to rollback.
    3. **Project Information:** Provide either `projectSlug` or `projectID`. The tool will automatically resolve the project information as needed.
    4. **Version Selection:** If component environment and version are not provided, call `listComponentVersions` to get the list of versions for the selected component and environment. If there is only one version, proceed automatically and do not ask the user to select a version. Otherwise, present the user with the full list of versions and ask them to select one. Always return all available values without categorizing them.
    5. **Rollback Reason** ask the user for an optional reason for the rollback (e.g., "Critical bug fix"). Skip this step is the user explicitly requests a rollback by workflow rerun.
    6. **Rollback pipeline check** if the tool reports that no rollback pipeline is defined, ask the user if they want to trigger a rollback by workflow rerun or suggest to setup a rollback pipeline following the documentation at https://circleci.com/docs/deploy/rollback-a-project-using-the-rollback-pipeline/.
    7. **Confirmation:** Summarize the rollback request and confirm with the user before submitting.
    8. **Pipeline Rollback:**  if the user requested a rollback by pipeline, call `runRollbackPipeline` passing all parameters including the namespace associated with the version to the tool.
    9. **Workflow Rerun** If the user requested a rollback by workflow rerun, call `rerunWorkflow` passing the workflow ID of the selected version to the tool.
    10.**Completion:** Report the outcome of the operation.

    **Parameters:**
    - `projectSlug` (optional): The project slug from `listFollowedProjects` (e.g., "gh/organization/project"). Either this or `projectID` must be provided.
    - `projectID` (optional): The CircleCI project ID (UUID). Either this or `projectSlug` must be provided.
    - `environmentName` (required): The target environment (e.g., "production", "staging").
    - `componentName` (required): The component to rollback (e.g., "frontend", "backend").
    - `currentVersion` (required): The currently deployed version.
    - `targetVersion` (required): The version to rollback to.
    - `namespace` (required): The namespace of the component.
    - `reason` (optional): Reason for the rollback.
    - `parameters` (optional): Additional rollback parameters as key-value pairs.

    **Behavior:**
    - If there are more than 20 environments or components, ask the user to refine their selection.
    - Never attempt to guess or construct project slugs or URLs; always use values provided by the user or from `listFollowedProjects`.
    - Do not prompt for missing parameters until versions have been listed.
    - Do not call this tool with incomplete parameters.
    - If the selected project lacks rollback pipeline configuration, provide a definitive error message without suggesting alternative projects.

    **Returns:**
    - On success: The rollback ID or a confirmation in case of workflow rerun.
    - On error: A clear message describing what is missing or what went wrong.
    - If the selected project does not have a rollback pipeline configured: The tool will provide a clear error message specific to that project and will NOT suggest trying another project.

    **Important Note:**
    - This tool is designed to work only with the specific project provided by the user.
    - If a project does not have rollback capability configured, the tool will NOT recommend trying other projects.
    - The assistant should NOT suggest trying different projects when a project lacks rollback configuration.
    - Each project must have its own rollback pipeline configuration to be eligible for rollback operations.
    - When a project cannot be rolled back, provide only the configuration guidance for THAT specific project.
    - The tool automatically resolves project information from either `projectSlug` or `projectID`.
    If no version is found, the tool will suggest the user to set up deploy markers following the documentation at:
    https://circleci.com/docs/deploy/configure-deploy-markers/
  
```

### list_component_versions  (annotations: —)
```

     This tool lists all versions for a CircleCI component. It guides you through a multi-step process to gather the required information and provides lists of available options when parameters are missing.

     **Initial Requirements:**
     - You need either a `projectSlug` (from `listFollowedProjects`) or a `projectID`. The tool will automatically resolve the `orgID` from either of these.

     **Typical Flow:**
     1. **Start:** User requests component versions or deployment information.
     2. **Project Information:** Provide either `projectSlug` or `projectID`. The tool will automatically resolve the `orgID` and `projectID` as needed.
     3. **Environment Selection:** If `environmentID` is not provided, the tool will list all available environments for the organization and prompt the user to select one. Always return all available values without categorizing them.
     4. **Component Selection:** If `componentID` is not provided, the tool will list all available components for the project and prompt the user to select one. Always return all available values without categorizing them.
     5. **Version Listing:** Once both `environmentID` and `componentID` are provided, the tool will list all versions for that component in the specified environment.
     6. **Selection:** User selects a version from the list for subsequent operations.

     **Parameters:**
     - `projectSlug` (optional): The project slug from `listFollowedProjects` (e.g., "gh/organization/project"). Either this or `projectID` must be provided.
     - `projectID` (optional): The CircleCI project ID (UUID). Either this or `projectSlug` must be provided.
     - `orgID` (optional): The organization ID. If not provided, it will be automatically resolved from `projectSlug` or `projectID`.
     - `environmentID` (optional): The environment ID. If not provided, available environments will be listed.
     - `componentID` (optional): The component ID. If not provided, available components will be listed.

     **Behavior:**
     - The tool will guide you through the selection process step by step.
     - Automatically resolves `orgID` from `projectSlug` or `projectID` when needed.
     - When `environmentID` is missing, it lists environments and waits for user selection.
     - When `componentID` is missing (but `environmentID` is provided), it lists components and waits for user selection.
     - Only when both `environmentID` and `componentID` are provided will it list the actual component versions.
     - Make multiple calls to this tool as you gather the required parameters.

     **Common Use Cases:**
     - Identify which versions were deployed for a component
     - Identify which versions are live for a component
     - Identify which versions were deployed to an environment for a component
     - Identify which versions are not live for a component in an environment
     - Select a version for rollback or deployment operations
     - Obtain version name, namespace, and environment details for other CircleCI tools

     **Returns:**
     - When missing `environmentID`: A list of available environments with their IDs
     - When missing `componentID`: A list of available components with their IDs  
     - When both `environmentID` and `componentID` provided: A list of component versions with version name, namespace, environment ID, and is_live status

     **Important Notes:**
     - This tool requires multiple calls to gather all necessary information.
     - Either `projectSlug` or `projectID` must be provided; the tool will resolve the missing project information automatically.
     - The tool will prompt for missing `environmentID` and `componentID` by providing selection lists.
     - Always use the exact IDs returned by the tool in subsequent calls.
     - If pagination limits are reached, the tool will indicate that not all items could be displayed.

     **IMPORTANT:** Do not automatically run additional tools after this tool is called. Wait for explicit user instruction before executing further tool calls. The LLM MUST NOT invoke other CircleCI tools until receiving clear instruction from the user about what to do next, even if the user selects an option. It is acceptable to list out tool call options for the user to choose from, but do not execute them until instructed.
     
```

### list_artifacts  (annotations: —)
```

    This tool retrieves the list of artifacts produced by a CircleCI job.

    Common use cases:
    - List all artifacts generated by a specific job
    - Find download URLs for build artifacts (binaries, reports, logs, etc.)
    - Check what artifacts were produced by a pipeline run

    Input options (EXACTLY ONE of these THREE options must be used):

    Option 1 - Project Slug and branch (BOTH required):
    - projectSlug: The project slug obtained from listFollowedProjects tool (e.g., "gh/organization/project")
    - branch: The name of the branch (required when using projectSlug)

    Option 2 - Direct URL (provide ONE of these):
    - projectURL: The URL of the CircleCI job in any of these formats:
      * Job URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def/jobs/789
      * Workflow URL: https://app.circleci.com/pipelines/gh/organization/project/123/workflows/abc-def
      * Pipeline URL: https://app.circleci.com/pipelines/gh/organization/project/123

    Option 3 - Project Detection (ALL of these must be provided together):
    - workspaceRoot: The absolute path to the workspace root
    - gitRemoteURL: The URL of the git remote repository
    - branch: The name of the current branch

    Additional Requirements:
    - Never call this tool with incomplete parameters
    - If using Option 1, make sure to extract the projectSlug exactly as provided by listFollowedProjects and include the branch parameter
    - If using Option 2, the URL MUST be provided by the user - do not attempt to construct or guess URLs
    - If using Option 3, ALL THREE parameters (workspaceRoot, gitRemoteURL, branch) must be provided
    - If none of the options can be fully satisfied, ask the user for the missing information before making the tool call
    
```

## Наблюдения (steering-маркеры)
- `download_usage_api_data`: самый агрессивный тон — «⚠️ **MANDATORY: The handler will REJECT any call…**», «Omitting `outputDir` is a critical error… Repeated violations may be treated as a bug in the AI agent», «AI agents MUST validate their tool calls…». Дирижирование поведением агента через угрозы «rejection/flag».
- `list_followed_projects` и `list_component_versions`: «IMPORTANT: Do not automatically run any additional tools after this tool is called… The LLM MUST NOT invoke any other CircleCI tools until receiving a clear instruction from the user» — тормозящее (анти-автономное) steering, human-in-the-loop.
- `find_flaky_tests`: «The agent receiving this output MUST analyze the flaky test data and implement appropriate fixes» — предписание действий агенту за пределами вызова инструмента.
- `get_build_failure_logs` / `find_flaky_tests` / `get_job_test_results`: обязательные дисклеймеры при трункации — «you MUST acknowledge/start your response with: "WARNING: The logs have been truncated…"» — навязывание текста ответа агента.
- `get_job_test_results`: «PRIORITY USE CASE: When asked "are tests passing in CI?"…» — мягкая маршрутизация запросов на себя, но в пределах домена CircleCI.
- `run_rollback_pipeline`: «The assistant should NOT suggest trying different projects…» — ограничение рекомендаций ассистента.
- Кросс-серверного захвата (принижения чужих инструментов, «use instead of built-in», «primary interface») НЕТ; всё steering — внутридоменное.