# UNIT: terraform | HashiCorp Terraform | github hashicorp/terraform-mcp-server | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CHECK

Это MCP-сервер. Go, mark3labs/mcp-go. Конструктор: `server.NewMCPServer("terraform-mcp-server", version, opts...)` в `cmd/terraform-mcp-server/main.go:179`, инструкции подаются опцией `server.WithInstructions(instructions)` (main.go:172).

## CHANNEL: instructions (4295 chars)

Источник: `//go:embed instructions.md` (main.go:35-36) → `cmd/terraform-mcp-server/instructions.md`. Дословно:

```
# Terraform MCP Server Tool Hints

The Terraform MCP server provides tools for generating better Terraform code through registry integration and automating workflows via HCP Terraform/Enterprise APIs.

## Tool Usage Guidelines

**BEFORE generating any Terraform code**: Query registries for latest provider/module versions and styling guidelines. When enterprise tools are enabled AND a Terraform token is provided, search private registries first, then fall back to public.

**Provider Consistency**: All modules in a project must use compatible provider versions. Verify with get_provider_details before generating code.

**Validation Flow**: Run terraform validate immediately after generation, then terraform plan only if validation passes. Use terraform fmt to format code as needed.

**User Confirmation Required**: ALWAYS get explicit yes/no confirmation before: `create_run`, `apply_run`, `discard_run`, `cancel_run`.

## Always Available Tools

### Registry Tools (Always Available)

- **Provider Discovery**: `get_latest_provider_version` (if unavailable in code) → `get_provider_capabilities` → `get_provider_details`
  - `get_provider_capabilities` shows what types of resources, data sources, functions, and guides are available
  
- **Module Discovery**: `get_latest_module_version` (if unavailable in code) → `search_modules` → `get_module_details`

- **Policy Discovery**: `search_policies` → `get_policy_details`

- Use these to ensure generated code uses current versions and follows best practices

## HCP Terraform/TFE Tools (When enterprise tools are enabled AND a Terraform token is provided)

### Private Registry Tools
- `search_private_providers` → `get_private_provider_details`
- `search_private_modules` → `get_private_module_details`
- Priority: Check private registries first when token present, public as fallback

### Workspace Management
- **Discovery**: `search_workspaces` (empty query returns all) → `get_workspace_details`
- **Operations**: `create_workspace`, `update_workspace`, `delete_workspace_safely`, `force_unlock_workspace`
- `delete_workspace_safely` only works if workspace has no managed resources

### Run Execution
- **Discovery**: `search_run` (empty query returns all) → `get_run_details` (supports json output)
- **Operations**: `create_run` → `apply_run` OR `discard_run` OR `cancel_run`
- **Monitoring**: `get_plan_details`/`get_plan_logs` for plans, `get_apply_details`/`get_apply_logs` for applies
- Always check run status before attempting operations

### Variable Management
**Workspace Variables**:
- `search_workspace_variables` (empty query returns all)
- `create_workspace_variable`, `update_workspace_variable`, `delete_workspace_variable`

**Variable Sets** (for sharing across workspaces/projects):
- `search_variable_sets` → `get_variable_set_details`
- `create_variable_set`, `update_variable_set`, `delete_variable_set`
- `create_variable_in_variable_set`, `update_variable_in_variable_set`, `delete_variable_from_variable_set`
- `attach/detach_variable_set_to_workspaces`, `attach/detach_variable_set_to_projects`

## Workflow Patterns

**Code Generation**:
1. `search_modules`/`search_providers` for available resources
2. `get_latest_provider_version` if no version available in existing code
3. `get_module_details` for module requirements
4. Generate code with discovered constraints

**Run Management**:
1. `search_workspaces` → select target
2. `create_run` → get_run_details to monitor
3. `get_plan_details/logs` to review changes
4. User confirmation → `apply_run` OR `discard_run`

**Variable Configuration**:
1. `search_workspace_variables` to check existing
2. `create/update_workspace_variable` as needed
3. For multi-workspace: `create_variable_set` → `attach_variable_set_to_workspaces`

## Error Handling
- Registry failures: Try private first (if token), fallback to public
- Run failures: Check `get_run_details`, get_plan_details and logs before retry
- Variable conflicts: `search_workspace_variables` first to avoid duplicates
- Run stuck and holds the lock: `action_run` to cancel or discard the run → `force_unlock_workspace` to unlock the workspace

## Security Notes
- Never expose TFE_TOKEN or other sensitive values in outputs
- Document source (public/private registry) in generated code comments
```

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Найдено 54 определений инструментов (`mcp.NewTool("<name>", mcp.WithDescription(...))`). Ниже приведены ВСЕ 54 с дословными описаниями.

### Marker scan (все описания прогнаны по регексам, 1 совпадение)

- `force_unlock_workspace` — совпадение на шаблоне предпочтения: «Force unlocks a Terraform workspace stuck in a lock. Prefer using the action_run tool with "discard" or "cancel" before force-unlocking a workspace.»

### Все описания (дословно)

#### 1. `get_latest_module_version`  
`pkg/tools/registry/get_latest_module_version.go`

```
Fetches the latest version of a Terraform module from the public registry
```

#### 2. `get_latest_provider_version`  
`pkg/tools/registry/get_latest_provider_version.go`

```
Fetches the latest version of a Terraform provider from the public registry
```

#### 3. `get_module_details`  
`pkg/tools/registry/get_module_details.go`

```
Fetches up-to-date documentation on how to use a Terraform module. You must call 'search_modules' first to obtain the exact valid and compatible module_id required to use this tool.
```

#### 4. `get_policy_details`  
`pkg/tools/registry/get_policy_details.go`

```
Fetches up-to-date documentation for a specific policy from the Terraform registry. You must call 'search_policies' first to obtain the exact terraform_policy_id required to use this tool.
```

#### 5. `get_provider_capabilities`  
`pkg/tools/registry/get_provider_capabilities.go`

```
Get the capabilities of a Terraform provider including the types of resources, data sources, functions, guides, and other features it supports.
This tool analyzes the provider documentation to determine what types of capabilities are available:
- resources: Infrastructure resources that can be created/managed
- data-sources: Read-only data sources for querying existing infrastructure  
- functions: Provider-specific functions for data transformation
- guides: Documentation guides and tutorials for using the provider
- actions: Available provider actions (if any)
- ephemeral resources: Temporary resources for credentials and tokens
- list-resources: List resources for querying existing cloud resources (Terraform Search)

Returns a summary with counts and examples for each capability type.
```

#### 6. `get_provider_details`  
`pkg/tools/registry/get_provider_details.go`

```
Fetches up-to-date documentation for a specific service from a Terraform provider. 
You must call 'search_providers' tool first to obtain the exact tfprovider-compatible provider_doc_id required to use this tool.
```

#### 7. `search_modules`  
`pkg/tools/registry/search_modules.go`

```
Resolves a Terraform module name to obtain a compatible module_id for the get_module_details tool and returns a list of matching Terraform modules.
You MUST call this function before 'get_module_details' to obtain a valid and compatible module_id.
When selecting the best match, consider the following:
	- Name similarity to the query
	- Description relevance
	- Verification status (verified)
	- Download counts (popularity)
Return the selected module_id and explain your choice. If there are multiple good matches, mention this but proceed with the most relevant one.
If no modules were found, reattempt the search with a new moduleName query.
```

#### 8. `search_policies`  
`pkg/tools/registry/search_policies.go`

```
Searches for Terraform policies based on a query string.
This tool returns a list of matching policies, which can be used to retrieve detailed policy information using the 'get_policy_details' tool.
You MUST call this function before 'get_policy_details' to obtain a valid terraform_policy_id.
When selecting the best match, consider the following:
	- Name similarity to the query
	- Title relevance
	- Verification status (verified)
	- Download counts (popularity)
Return the selected policyID and explain your choice. If there are multiple good matches, mention this but proceed with the most relevant one.
If no policies were found, reattempt the search with a new policy_query.
```

#### 9. `search_providers`  
`pkg/tools/registry/search_providers.go`

```
This tool retrieves a list of potential documents based on the 'service_slug' and 'provider_document_type' provided.
You MUST call this function before 'get_provider_details' to obtain a valid tfprovider-compatible 'provider_doc_id'.
Use the most relevant single word as the search query for 'service_slug', if unsure about the 'service_slug', use the 'provider_name' for its value.
When selecting the best match, consider the following:
	- Title similarity to the query
	- Category relevance
Return the selected 'provider_doc_id' and explain your choice.
If there are multiple good matches, mention this but proceed with the most relevant one.
```

#### 10. `action_run`  
`pkg/tools/tfe/action_run.go`

```
Performs a variety of actions on a Terraform run. It can be used to approve and apply, discard or cancel a run.
```

#### 11. `create_no_code_workspace`  
`pkg/tools/tfe/create_no_code_workspace.go`

```
Creates a new Terraform No Code module workspace. The tool uses the MCP elicitation feature to automatically discover and collect required variables from the user.
```

#### 12. `create_project`  
`pkg/tools/tfe/create_project.go`

```
Creates a new Terraform project in the specified organization.
```

#### 13. `create_run`  
`pkg/tools/tfe/create_run.go`

```
Creates a new Terraform run in the specified workspace.
```

#### 14. `create_run`  
`pkg/tools/tfe/create_run.go`

```
Creates a new Terraform run in the specified workspace.
```

#### 15. `create_workspace`  
`pkg/tools/tfe/create_workspace.go`

```
Creates a new Terraform workspace in the specified organization. This is a destructive operation that will create new infrastructure resources.
```

#### 16. `delete_project`  
`pkg/tools/tfe/delete_project.go`

```
Deletes a Terraform project by ID. This is a destructive operation. The request will fail if the project still contains workspaces or stacks. If the project ID isn't already known, call list_terraform_projects first to look it up rather than asking the user to find it themselves.
```

#### 17. `delete_workspace_safely`  
`pkg/tools/tfe/delete_workspace_safely.go`

```
Safely deletes a Terraform workspace by ID only if it is not managing any resources. This prevents accidental deletion of workspaces that still have active infrastructure. This is a destructive operation.
```

#### 18. `force_unlock_workspace`  
`pkg/tools/tfe/force_unlock_workspace.go`

```
Force unlocks a Terraform workspace stuck in a lock. Prefer using the action_run tool with "discard" or "cancel" before force-unlocking a workspace. Requires workspace admin permissions (e.g. an Owners team token).
```

#### 19. `get_apply_details`  
`pkg/tools/tfe/get_apply_details.go`

```
Fetches detailed information about a specific Terraform apply.
```

#### 20. `get_apply_logs`  
`pkg/tools/tfe/get_apply_logs.go`

```
Retrieves the logs of a specific Terraform apply.
```

#### 21. `get_plan_details`  
`pkg/tools/tfe/get_plan_details.go`

```
Fetches detailed information about a specific Terraform plan.
```

#### 22. `get_plan_json_output`  
`pkg/tools/tfe/get_plan_json_output.go`

```
Retrieves the structured JSON output of a specific Terraform plan. This includes detailed information about resource changes (create, update, delete), attribute values before and after, and plan metadata. This is more structured and easier to parse than plain logs.
```

#### 23. `get_plan_logs`  
`pkg/tools/tfe/get_plan_logs.go`

```
Retrieves the logs of a specific Terraform plan.
```

#### 24. `get_private_module_details`  
`pkg/tools/tfe/get_private_module_details.go`

```
This tool retrieves detailed information about a specific private module in your Terraform Cloud/Enterprise organization.
It provides comprehensive details including inputs, outputs, dependencies, versions, and usage examples. The private_module_id format is 'module-namespace/module-name/module-provider-name'.
This can be obtained by calling 'search_private_modules' first to obtain the exact private_module_id required to use this tool. This tool requires a valid Terraform token to be configured.
```

#### 25. `get_private_provider_details`  
`pkg/tools/tfe/get_private_provider_details.go`

```
This tool retrieves information about a specific private provider in your Terraform Cloud/Enterprise organization.
It provides details on how to use the provider, permissions, available versions, and more. This tool requires a valid Terraform token to be configured.
```

#### 26. `get_run_comments`  
`pkg/tools/tfe/get_run_comments.go`

```
Lists all user-submitted comments on a specific Terraform run. Use this tool when you need to review feedback, approvals, or notes that collaborators have left on a run. Returns each comment's ID and body text. To get the run's status, plan, and apply details instead, use get_run_details.
```

#### 27. `get_run_details`  
`pkg/tools/tfe/get_run_details.go`

```
Fetches detailed information about a specific Terraform run.
```

#### 28. `get_sentinel_mock`  
`pkg/tools/tfe/get_sentinel_mock.go`

```
Exports and downloads Sentinel mock bundle data for a Terraform plan. This data can be used to test Sentinel policies against plan output. The export is asynchronous - this tool handles polling until the export is ready.
```

#### 29. `get_stack_details`  
`pkg/tools/tfe/get_stack_details.go`

```
Fetches detailed information about a specific Terraform Stack.
```

#### 30. `get_state_version`  
`pkg/tools/tfe/get_state_version.go`

```
Retrieves a Terraform state version. If state_version_id is provided, retrieves that specific state version. Otherwise, retrieves the latest state version for the specified workspace. One of state_version_id or workspace_id must be provided
```

#### 31. `get_token_permissions`  
`pkg/tools/tfe/get_token_permissions.go`

```
Fetches the permissions the current token has for the specified terraform organization.
```

#### 32. `get_workspace_details`  
`pkg/tools/tfe/get_workspace_details.go`

```
Fetches detailed information about a specific Terraform workspace, including configuration, variables, and current state information.
```

#### 33. `list_runs`  
`pkg/tools/tfe/list_runs.go`

```
List or search Terraform runs in a specific workspace with optional filtering.
```

#### 34. `list_stacks`  
`pkg/tools/tfe/list_stacks.go`

```
List Stacks within a specified organization. Returns all stacks when no project or search query is supplied. Supports pagination for large result sets.
```

#### 35. `list_state_versions`  
`pkg/tools/tfe/list_state_versions.go`

```
List all the State Versions for a given workspace and org name.
```

#### 36. `list_terraform_orgs`  
`pkg/tools/tfe/list_terraform_orgs.go`

```
Fetches a list of all Terraform organizations. Supports Pagination for large result sets.
```

#### 37. `list_terraform_projects`  
`pkg/tools/tfe/list_terraform_projects.go`

```
Fetches a list of all Terraform projects. Supports pagination for large result sets.
```

#### 38. `list_workspaces`  
`pkg/tools/tfe/list_workspaces.go`

```
Search and list Terraform workspaces within a specified organization. Returns all workspaces when no filters are applied, or filters results based on name patterns, tags, or search queries. Supports pagination for large result sets. Returns a truncated summary of the workspace, use get_workspace_details to get the full details for a specific workspace.
```

#### 39. `attach_policy_set_to_workspaces`  
`pkg/tools/tfe/policy_sets.go`

```
Attach a policy set to one or more workspaces. Note: Policy sets marked as global cannot be attached to individual workspaces.
```

#### 40. `list_workspace_policy_sets`  
`pkg/tools/tfe/policy_sets.go`

```
Read all policy sets attached to a workspace. Returns both directly attached policy sets and global policy sets that apply to all workspaces.
```

#### 41. `search_private_modules`  
`pkg/tools/tfe/search_private_modules.go`

```
This tool searches for private modules in your Terraform Cloud/Enterprise organization.
It retrieves a list of private modules that match the search criteria. This tool requires a valid Terraform token to be configured.
```

#### 42. `search_private_providers`  
`pkg/tools/tfe/search_private_providers.go`

```
This tool searches for private providers in your Terraform Cloud/Enterprise organization.
It retrieves a list of private providers that match the search criteria. This tool requires a valid Terraform token to be configured.
```

#### 43. `update_workspace`  
`pkg/tools/tfe/update_workspace.go`

```
Updates an existing Terraform workspace configuration. This is a potentially destructive operation that may affect infrastructure resources.
```

#### 44. `list_variable_sets`  
`pkg/tools/tfe/variable_sets.go`

```
List all variable sets in an organization. Returns all if query is empty.
```

#### 45. `create_variable_set`  
`pkg/tools/tfe/variable_sets.go`

```
Create a new variable set in an organization.
```

#### 46. `create_variable_in_variable_set`  
`pkg/tools/tfe/variable_sets.go`

```
Create a new variable in a variable set.
```

#### 47. `delete_variable_in_variable_set`  
`pkg/tools/tfe/variable_sets.go`

```
Delete a variable in a variable set.
```

#### 48. `attach_variable_set_to_workspaces`  
`pkg/tools/tfe/variable_sets.go`

```
Attach a variable set to one or more workspaces.
```

#### 49. `detach_variable_set_from_workspaces`  
`pkg/tools/tfe/variable_sets.go`

```
Detach a variable set from one or more workspaces.
```

#### 50. `create_workspace_tags`  
`pkg/tools/tfe/workspace_tags.go`

```
Add tags to a Terraform workspace.
```

#### 51. `read_workspace_tags`  
`pkg/tools/tfe/workspace_tags.go`

```
Read all tags from a Terraform workspace.
```

#### 52. `list_workspace_variables`  
`pkg/tools/tfe/workspace_variables.go`

```
List all variables in a Terraform workspace. Returns all variables if query is empty.
```

#### 53. `create_workspace_variable`  
`pkg/tools/tfe/workspace_variables.go`

```
Create a new variable in a Terraform workspace.
```

#### 54. `update_workspace_variable`  
`pkg/tools/tfe/workspace_variables.go`

```
Update an existing variable in a Terraform workspace.
```
