# UNIT: server-filesystem@2026.7.10 | npm @modelcontextprotocol/server-filesystem (референс-сервер MCP) | captured 2026-07-29 (static, tarball)

## CHANNEL: instructions, npm (static)
(см. экстракцию ниже — если в коде нет, раздел будет помечен «не обнаружены»)

Экстракция: instructions НЕ ОБНАРУЖЕНЫ. Конструктор в `dist/index.js` (строки 130–133):

```js
const server = new McpServer({
    name: "secure-filesystem-server",
    version: "0.2.0",
});
```

Поле `instructions` не передаётся ни конструктору, ни в ответ initialize. Grep по всем файлам `dist/` на `instructions` — ноль совпадений. Других инструкционных строк/профилей в коде нет.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Все 14 инструментов зарегистрированы через `server.registerTool(...)` в `dist/index.js`. Описания дословно (в исходнике — конкатенация строковых литералов, склеено):

1. **read_file** (title: "Read File (Deprecated)")
   > Read the complete contents of a file as text. DEPRECATED: Use read_text_file instead.

2. **read_text_file** (title: "Read Text File")
   > Read the complete contents of a file from the file system as text. Handles various text encodings and provides detailed error messages if the file cannot be read. Use this tool when you need to examine the contents of a single file. Use the 'head' parameter to read only the first N lines of a file, or the 'tail' parameter to read only the last N lines of a file. Operates on the file as text regardless of extension. Only works within allowed directories.

3. **read_media_file** (title: "Read Media File")
   > Read a file and return it as a base64-encoded content block with its MIME type. Image and audio files are returned as image/audio content; any other file type is returned as an embedded resource. Only works within allowed directories.

4. **read_multiple_files** (title: "Read Multiple Files")
   > Read the contents of multiple files simultaneously. This is more efficient than reading files one by one when you need to analyze or compare multiple files. Each file's content is returned with its path as a reference. Failed reads for individual files won't stop the entire operation. Only works within allowed directories.

5. **write_file** (title: "Write File")
   > Create a new file or completely overwrite an existing file with new content. Use with caution as it will overwrite existing files without warning. Handles text content with proper encoding. Only works within allowed directories.

6. **edit_file** (title: "Edit File")
   > Make line-based edits to a text file. Each edit replaces exact line sequences with new content. Returns a git-style diff showing the changes made. Only works within allowed directories.

7. **create_directory** (title: "Create Directory")
   > Create a new directory or ensure a directory exists. Can create multiple nested directories in one operation. If the directory already exists, this operation will succeed silently. Perfect for setting up directory structures for projects or ensuring required paths exist. Only works within allowed directories.

8. **list_directory** (title: "List Directory")
   > Get a detailed listing of all files and directories in a specified path. Results clearly distinguish between files and directories with [FILE] and [DIR] prefixes. This tool is essential for understanding directory structure and finding specific files within a directory. Only works within allowed directories.

9. **list_directory_with_sizes** (title: "List Directory with Sizes")
   > Get a detailed listing of all files and directories in a specified path, including sizes. Results clearly distinguish between files and directories with [FILE] and [DIR] prefixes. This tool is useful for understanding directory structure and finding specific files within a directory. Only works within allowed directories.

10. **directory_tree** (title: "Directory Tree")
    > Get a recursive tree view of files and directories as a JSON structure. Each entry includes 'name', 'type' (file/directory), and 'children' for directories. Files have no children array, while directories always have a children array (which may be empty). The output is formatted with 2-space indentation for readability. Only works within allowed directories.

11. **move_file** (title: "Move File")
    > Move or rename files and directories. Can move files between directories and rename them in a single operation. If the destination exists, the operation will fail. Works across different directories and can be used for simple renaming within the same directory. Both source and destination must be within allowed directories.

12. **search_files** (title: "Search Files")
    > Recursively search for files and directories matching a pattern. The patterns should be glob-style patterns that match paths relative to the working directory. Use pattern like '*.ext' to match files in current directory, and '**/*.ext' to match files in all subdirectories. Returns full paths to all matching items. Great for finding files when you don't know their exact location. Only searches within allowed directories.

13. **get_file_info** (title: "Get File Info")
    > Retrieve detailed metadata about a file or directory. Returns comprehensive information including size, creation time, last modified time, permissions, and type. This tool is perfect for understanding file characteristics without reading the actual content. Only works within allowed directories.

14. **list_allowed_directories** (title: "List Allowed Directories")
    > Returns the list of directories that this server is allowed to access. Subdirectories within these allowed directories are also accessible. Use this to understand which directories and their nested paths are available before trying to access files.

### Наблюдения по steering-маркерам
- Нет ни одного агрессивного маркера (PRECEDENCE, LAST resort, always default, MUST use, primary interface и т.п.).
- Мягкие маркеры внутри описаний: «This is more efficient than reading files one by one» (read_multiple_files), «essential for understanding directory structure» (list_directory), «Perfect for setting up…» (create_directory), «perfect for understanding file characteristics» (get_file_info), «Great for finding files» (search_files) — типичная лёгкая реклама пригодности инструмента, без кросс-серверного вытеснения.
- Повторяющийся ограничитель «Only works within allowed directories» — safety-фрейминг, не steering.
- Все инструменты имеют MCP annotations (readOnlyHint/destructiveHint/openWorldHint: false).

## NOTES (static analysis)
- Код НЕ минифицирован: читаемый tsc-выхлоп с комментариями.
- Все описания — статические строковые литералы (конкатенация «+»), интерполяции/шаблонов в описаниях нет; риск динамической сборки инструкционных строк — отсутствует.
- Просмотрены файлы: dist/index.js (полностью), dist/lib.js, dist/path-utils.js, dist/path-validation.js, dist/roots-utils.js (grep на instructions/registerTool — пусто), package.json, README.md не содержит runtime-строк.
- Расхождение версий: package.json version = 2026.7.10, но в конструкторе сервер объявляет себя как version "0.2.0", name "secure-filesystem-server".
