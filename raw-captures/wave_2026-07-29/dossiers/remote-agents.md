# UNIT: remote-agents | npm v0.1.37 (published 2026-07-12T11:24:48.243Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: server exists, but NOT in the tarball (binary-download launcher)

Продукт — действительно MCP-сервер («Unified MCP server for controlling fleets of remote machines», режим `remote-agents mcp` = MCP stdio server). Но npm-тарболл содержит только:

- `run.js` — лаунчер: `spawn(./bin/remote-agent, argv, {stdio:"inherit"})` + notify-only проверка обновлений через registry.npmjs.org
- `install.js` — postinstall: скачивает прекомпилированный Rust-бинарь `remote-agent-<triple>` с `https://github.com/47-ronn/tunshell_mcp_agents/releases/download/v0.1.37/...` (SHA-256 sidecar-верификация, но sidecar может отсутствовать — тогда skip)
- `README.md`, `package.json`, `LICENSE`

Весь серверный MCP-код (регистрация инструментов, instructions, схемы) — внутри скачиваемого нативного бинаря (Rust, `crates/mcp-server` по README). В тарболле его нет; статическая экстракция каналов управления моделью из этого артефакта невозможна.

## CHANNEL: instructions, npm (static)
(не обнаружены статически — серверный код отсутствует в тарболле; instructions, если есть, компилируются в Rust-бинарь)

## CHANNEL: tool descriptions, npm (static, coverage=none)
Фактические description-строки инструментов не извлекаемы (в бинаре). Для контекста — README документирует 28 инструментов (это ДОКУМЕНТАЦИЯ, не runtime-описания):
`exec`, `read_file`, `write_file`, `list_dir`, `get_info`, `set_mode`, `git_status`, `git_pull`, `git_commit`, `git_push`, `schedule_add`, `schedule_remove`, `schedule_list`, `task_dispatch`, `task_get`, `task_list`, `task_wait`, `list_agents`, `fleet_exec`, `fleet_read`, `fleet_write`, `fleet_git`, `fleet_search`, `file_search`, `file_stat`, `send_file`, `transfer_get`, `sync_dir`, `tunnel_start`, `tunnel_list`, `tunnel_stop`, `mapreduce`.
README-тон нейтрально-технический; маркер-скан README по стирринг-регексам совпадений не дал (нет «primary», «takes precedence», «instead of built-in» и т.п.).

## SECURITY / SUPPLY-CHAIN NOTES
- Postinstall network fetch исполняемого бинаря с GitHub Releases — классический supply-chain вектор: содержимое релиза может меняться независимо от npm-публикации (checksum-sidecar лежит рядом с бинарём в том же релизе, т.е. защищает от порчи, не от подмены релиза).
- Сам продукт по назначению — удалённое исполнение команд/файлов/cron/туннелей на флоте машин через relay; режим `bypass` = unrestricted.
- Код тарболла не минифицирован, читаемый, без динамической сборки строк; но это только обвязка.
- Файлов просмотрено: 5 из 5 (весь тарболл).
