# UNIT: @salesforce/mcp-provider-code-analyzer | npm v0.9.0 (published 2026-05-21T17:46:08.416Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## ТИП ПАКЕТА

Не самостоятельный MCP-сервер, а **provider-плагин** для хостового Salesforce MCP-сервера: `CodeAnalyzerMcpProvider extends McpProvider` из `@salesforce/mcp-provider-api`, метод `provideTools(services)` возвращает 6 инстансов `McpTool`. В пакете нет ни `new Server(...)`, ни `new McpServer(...)`, ни транспорта — тулы регистрирует хост (`@salesforce/mcp`, repo `salesforcecli/mcp`). package.json: «(For Internal Use Only) Provides MCP Tools for Salesforce Code Analyzer to a MCP Server». Поскольку пакет несёт реальные MCP tool-описания, попадающие в контекст модели через хост-сервер, канал tool descriptions задокументирован полностью; канал instructions пакету структурно недоступен.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Grep по `instructions|serverInfo|new McpServer|new Server(` по всему dist/ — 0 совпадений: пакет не конструирует сервер и не передаёт instructions.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Зарегистрировано 6 тулов (provider.js); 7-й (`create_regex_rule`) закомментирован и НЕ регистрируется. Описания — статические template literals; интерполяции только константные: `${CodeAnalyzerRunMcpTool.NAME}` → `run_code_analyzer`, `${DEFAULT_TOPN_POLICY_LIMIT}` → `10` (dist/policies.js:1). Ниже — дословно, с подстановкой этих констант.

### 1. run_code_analyzer

```
A tool for performing static analysis against code.
This tool can validate that code conforms to best practices, check for security vulnerabilities, and identify possible
performance issues. It returns a JSON containing the absolute path to a results file if such a file was created,
and a string indicating the overall success or failure of the operation.

When to use this tool:
- When the user asks you to generate files, use this tool to scan those files.
- When the user asks you to check code for problems, use this tool to do that.

REQUIRED INPUT - Directory:
- You MUST provide the "directory" parameter with the absolute path to the project/workspace root.
- The tool will automatically search for code-analyzer.yml or code-analyzer.yaml config files in this directory.
- Config files contain custom rule configurations, severities, and ignore patterns that will be respected.
- If no config file is found in the directory, default configuration will be used.

OPTIONAL - Custom Config Path:
- Use "configPath" parameter only if the config file has a custom name or is in a non-standard location.
- If provided, configPath takes precedence over config files in directory.

Optional: Provide a "selector" to choose which rules to run. Supports:
- Rule names: "WhileLoopsMustUseBraces", "no-unused-vars"
- Engines: "pmd", "eslint", "regex"
- Tags: "Security", "Performance", "Recommended"
- Severities: "Critical", "High", "1", "2"
- Combinations: "Security:pmd", "(Security,Performance):eslint"

Examples:
- "WhileLoopsMustUseBraces" → run specific rule by name
- "Security:pmd" → run Security-tagged PMD rules
- "Critical" → run all Critical-severity rules
- "(Security,Performance):eslint" → ESLint rules tagged Security or Performance

After completion: Use the "query_code_analyzer_results" tool to filter and explain results, e.g., top-N most severe violations or violations by category/tag.
```

### 2. describe_code_analyzer_rule

```
A tool for getting the description of a Code Analyzer rule.
This tool can return a JSON that describes the properties of a Code Analyzer rule, which may include information about
how it can be fixed.

When to use this tool:
- When the results file from the run_code_analyzer tool does not provide enough information to fix a violation yourself.
- When the user asks for information about a specific rule or violation.
```

### 3. list_code_analyzer_rules

```
A tool for selecting Code Analyzer rules based on a number of criteria.
This tool returns a JSON array describing Code Analyzer rules that match a "selector".
A selector is a colon-separated (:) string of tokens; tags and severity names are case-insensitive.
You can OR multiple tokens of the same type by grouping them in parentheses and separating with commas, e.g. "(Performance,Security)".

Policy: To prevent overly broad results, the full unfiltered list of rules is not returned unless you explicitly set allowFullList=true.
This flag defaults to false and its use is not recommended.
Note: Listing large rule sets can significantly increase token consumption.

Examples:
- "Recommended" → all rules tagged as Recommended.
- "Performance:pmd:Critical" → rules in the PMD engine with the Performance tag and Critical severity.
- "pmd:(Performance,Security):2" → PMD rules with Performance OR Security tags and severity 2.
- "(Apex,JavaScript):Recommended" → rules for Apex OR JavaScript languages that are Recommended.
- "Security:High" → rules tagged Security with High severity.
- "Apex:Recommended" → rules for the Apex language that are Recommended.
- "DevPreview" → rules marked as DevPreview.
- Prompt: "tell me about all performance rules" → selector: "Performance".

Supported selector tokens:
- Engines: eslint, regex, retire-js, flow, pmd, cpd, sfge
- Severities (names): Critical, High, Moderate, Low, Info
- Severities (numbers): 1, 2, 3, 4, 5
- General tags: Recommended, Custom, All
- Categories: BestPractices, CodeStyle, Design, Documentation, ErrorProne, Security, Performance
- Languages: Apex, CSS, HTML, JavaScript, TypeScript, Visualforce, XML
- Engine-specific tags: DevPreview, LWC

Tip: Use the "describe_code_analyzer_rule" tool to get details for any listed rule.
```

### 4. query_code_analyzer_results

```
Query a Code Analyzer results JSON file and return filtered violations.
Supports filters like severity, category/tag, engine, rule, and file name, plus top-N and sorting.
Use this after running "run_code_analyzer" to read the generated results file.
After completion, this tool will summarize and explain the filtered results to the user.

Policy: To avoid overwhelming results, this tool returns no more than the top 10 violations by default.
Requesting more than 10 requires an explicit opt-in via allowLargeResultSet=true and is not recommended.
Note: Querying larger result sets can significantly increase token consumption.

Examples (natural language → selector/topN):
- "Top 5 security in PMD" → selector: "Security:pmd", topN: 5
- "Top 10 critical" → selector: "Critical", topN: 10
- "Top 5 security or performance in ESLint" → selector: "(Security,Performance):eslint", topN: 5
- "Top 5 PMD High severity" → selector: "pmd:High", topN: 5
- "Top 5 for rule MyRuleName" → selector: "rule=MyRuleName", topN: 5
- "Top 5 in files under src/app" → selector: "file=src/app", topN: 5
```

### 5. get_ast_nodes_to_generate_xpath (файл generate_xpath_prompt.js)

```
Purpose: First step for creating a PMD XPath-based custom rule.
  Use this tool when the user asks to create a custom rule (especially PMD/XPath).
  
  Inputs (required):
  - sampleCode: A short snippet that SHOULD violate the intended rule.
    - Ensure this snippet truly triggers the exact pattern you want to catch.
    - Keep it minimal yet self-contained (parsable/compilable); remove unrelated noise.
    - Prefer realistic code over contrived examples to avoid brittle XPath.
  - language: Programming language of sampleCode (e.g., "apex", "xml").
  - engine: Analysis engine (e.g., "pmd").
  
  Output:
  - prompt: A concise, high-signal prompt that guides an LLM to extract the AST context needed for XPath authoring from the sampleCode.
  
  Use this tool when the user asks for rules like:
  - Ban all System.debug statements in production code.
  - Enforce that all Apex classes must end with Service, Controller, Handler, or Helper suffix.
  - Detect hardcoded Salesforce IDs in Apex classes.
  - Require that all test methods include assertions and cannot be empty.
  - Prevent usage of @future methods without proper error handling.
  - Enforce that all public methods must have proper documentation comments.
  - Prevent nested if statements deeper than 3 levels.
  - Require that all DML operations are wrapped in try-catch blocks.
  - Ensure all SOQL queries use bind variables instead of string concatenation.
  - Classes implementing Batchable must have proper error handling in execute().
  - All methods with @TestVisible must be in test classes only.
  - Enforce that all custom exceptions extend Exception class properly.
  - Require that all Database.query calls use escapeSingleQuotes for user input.
  - Ban the use of Test.isRunningTest() in production code.
  
  Note: This tool only prepares the prompt. A subsequent tool will use these details to generate the final XPath-based custom rule.
```

### 6. create_custom_rule

```
Purpose: Create a custom rule for code analysis.

Supports two engines:
1. PMD (XPath-based rules) - for Apex, Visualforce, and other languages
2. Regex (Pattern-based rules) - for pattern matching across file types

=== For PMD Engine ===
Workflow for Apex and Visualforce:
- First call "get_ast_nodes_to_generate_xpath" to generate the XPath
- Then call this tool with the generated XPath

Required inputs:
- engine: "pmd"
- xpath: The XPath expression that should match the violation
- ruleName: Name for the custom rule
- description: A short description/message for the rule
- language: Language for the rule (e.g., "apex", "visualforce")
- priority: PMD priority (1-5)
- workingDirectory: Workspace directory where files will be created

Output: Creates a ruleset XML file and updates code-analyzer.yml

=== For Regex Engine ===
Required inputs:
- engine: "regex"
- regex: The regex pattern as string (e.g., "/todo/gi")
- ruleName: Name for the custom rule
- description: Rule description
- violationMessage: Message shown when violation is found
- tags: Array of tags (e.g., ["Security", "BestPractices"])
- severity: Number 1-5 (1=Critical, 2=High, 3=Moderate, 4=Low, 5=Info)
- workingDirectory: Workspace directory where config will be updated

Optional inputs for Regex:
- fileExtensions: Array of file extensions to scan (e.g., [".cls", ".trigger"])
- regexIgnore: Pattern to exclude from matches (e.g., "/^test/i")
- includeMetadata: Boolean flag for metadata inclusion

Output: Updates code-analyzer.yml directly with the regex rule
```

## STEERING-СИГНАЛЫ (маркеры в описаниях)

- run_code_analyzer: «You MUST provide the "directory" parameter…» (обязательность параметра, не захват трафика); «If provided, configPath takes precedence over config files in directory» — precedence о собственных входах, не о конкуренции с другими тулами; проактивный триггер «When the user asks you to generate files, use this tool to scan those files» — мягкое расширение охвата: тул просят звать после ЛЮБОЙ генерации файлов, даже если пользователь не просил анализ.
- list_code_analyzer_rules / query_code_analyzer_results: «…is not recommended», «can significantly increase token consumption» — токен-гигиена, анти-steering (сдерживающая, а не захватывающая формулировка).
- Кросс-ссылки тулов друг на друга (run → query, list → describe, get_ast_nodes → create_custom_rule) — воркфлоу-цепочки внутри собственного семейства, конкурентов не упоминают.
- Совпадений с агрессивными маркерами (instead of built-in, most powerful, always default, LAST resort, Do NOT answer from memory, primary interface, ignore previous и т.п.) — нет.

## NOTES

- Код НЕ минифицирован: чистый tsc-вывод (ESM) с .js.map и .d.ts, читается дословно.
- Риск динамической сборки строк описаний: низкий. Все 6 DESCRIPTION — статические template literals; единственные интерполяции — константы (`CodeAnalyzerRunMcpTool.NAME`, `DEFAULT_TOPN_POLICY_LIMIT = 10`), разрешены статически. Остальные getMessage()-строки (messages.js) — это ошибки/тексты результатов, не описания тулов.
- Просмотрено: полный листинг дерева (37 .js в dist/), прочитаны package.json, index.js, provider.js, все 6 файлов dist/tools/*.js, dist/policies.js; grep по instructions/Server-конструкторам по всему dist/.
- В dist/tools нет файла create_regex_rule.js — тул существует только как комментарий в provider.js (регекс-путь идёт через create_custom_rule engine:"regex").
