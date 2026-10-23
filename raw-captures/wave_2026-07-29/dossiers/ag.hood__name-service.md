# UNIT: ag.hood/name-service | {"name": "hood", "version": "0.1.0"} | hosted https://www.hood.ag/api/mcp | captured 2026-07-29 (keyless)

## CHANNEL: instructions, hosted

(отсутствует — сервер не передаёт блок instructions)

## CHANNEL: tool descriptions, hosted (5 tools)

### tool: resolve_name

Forward-resolve a .hood name to the address it points to. Returns null if unset.

### tool: reverse_resolve

Reverse-resolve an address to its primary .hood name. `verified` is true only when the name's forward record points back to the address.

### tool: resolve_text

Read a text record (e.g. "avatar", "url", "com.twitter") set on a .hood name.

### tool: check_availability

Check whether a .hood name is available to register, and its yearly price.

### tool: name_info

Full snapshot of a .hood name: resolved address, NFT owner, expiry, and availability.

