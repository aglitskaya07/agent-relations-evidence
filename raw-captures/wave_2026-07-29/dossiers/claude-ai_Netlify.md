# UNIT: claude-ai:Netlify | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (11 tools, via ToolSearch)

### tool: get-netlify-coding-context
ALWAYS call when writing code. Required step before creating or editing any type of functions, Netlify sdk/library usage, etc. Use other operations for project management.

### tool: import-claude-design-from-url
Deploy a Claude Design design to Netlify. This is the "Send to Netlify" destination for Claude Design: it takes a publicly fetchable URL to a self-contained HTML bundle (images, fonts, and styles inlined), creates a Netlify site, deploys the HTML, and returns a live URL. Intended for Claude Design exports, not general-purpose web hosting.

### tool: get-design-import-job-status
Check the status of a Claude Design import started by import-claude-design-from-url. Returns processing | done | failed, plus the design URL once done.

### tool: netlify-deploy-services-reader
Select and run one of the following Netlify read operations (read-only) get-deploy, get-deploy-for-site

### tool: netlify-deploy-services-updater
Select and run one of the following Netlify write operations deploy-site

### tool: netlify-extension-services-reader
Select and run one of the following Netlify read operations (read-only) get-extensions, get-full-extension-details

### tool: netlify-extension-services-updater
Select and run one of the following Netlify write operations change-extension-installation, initialize-database

### tool: netlify-project-services-reader
Select and run one of the following Netlify read operations (read-only) get-project, get-projects, get-forms-for-project

### tool: netlify-project-services-updater
Select and run one of the following Netlify write operations update-visitor-access-controls, update-forms, manage-form-submissions, update-project-name, manage-env-vars, create-new-project

### tool: netlify-team-services-reader
Select and run one of the following Netlify read operations (read-only) get-teams, get-team

### tool: netlify-user-services-reader
Select and run one of the following Netlify read operations (read-only) get-user

## NOTES: parameter-level steering (внутри схем, не в описаниях)
- get-netlify-coding-context: описание содержит императив «ALWAYS call when writing code. Required step before…» — steering-маркер уровня описания инструмента.
- netlify-deploy-services-updater / deploy-site / param siteId: «If the agent cannot find the siteId, the user must confirm this is a new site. NEVER assume the user wants a new site.»
- Схемы reader/updater-инструментов включают поля aiAgentName и llmModelName (телеметрия: сбор идентичности агента/модели).
