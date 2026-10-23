# UNIT: redis | Redis | github redis/mcp-redis | тип автора: официальный | captured 2026-07-29 (static source)

## CHANNEL: instructions
(не обнаружены статически)

Конструктор: `src/common/server.py` — `mcp = FastMCP("Redis MCP Server", dependencies=["redis", "python-dotenv", "numpy", "aiohttp"])`. Параметр `instructions` не передаётся; в `src/main.py` сервер запускается через `mcp.run()` без переопределения. Ни в `server.json`, ни в `gemini-extension.json` поля instructions нет (только `description`, которое не является MCP-каналом instructions).

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов: 53 (>40, поэтому маркер-скан всех описаний + 10 репрезентативных полных).

### Полный список имён (файл → имя)

- `hset` (hash.py)
- `hget` (hash.py)
- `hdel` (hash.py)
- `hgetall` (hash.py)
- `hexists` (hash.py)
- `set_vector_in_hash` (hash.py)
- `get_vector_from_hash` (hash.py)
- `json_set` (json.py)
- `json_get` (json.py)
- `json_del` (json.py)
- `lpush` (list.py)
- `rpush` (list.py)
- `lpop` (list.py)
- `rpop` (list.py)
- `lrange` (list.py)
- `llen` (list.py)
- `lrem` (list.py)
- `delete` (misc.py)
- `type` (misc.py)
- `expire` (misc.py)
- `rename` (misc.py)
- `scan_keys` (misc.py)
- `scan_all_keys` (misc.py)
- `search_redis_documents` (misc.py)
- `publish` (pub_sub.py)
- `subscribe` (pub_sub.py)
- `psubscribe` (pub_sub.py)
- `read_messages` (pub_sub.py)
- `unsubscribe` (pub_sub.py)
- `get_indexes` (redis_query_engine.py)
- `get_index_info` (redis_query_engine.py)
- `get_indexed_keys_number` (redis_query_engine.py)
- `create_vector_index_hash` (redis_query_engine.py)
- `vector_search_hash` (redis_query_engine.py)
- `hybrid_search` (redis_query_engine.py)
- `dbsize` (server_management.py)
- `info` (server_management.py)
- `client_list` (server_management.py)
- `sadd` (set.py)
- `srem` (set.py)
- `smembers` (set.py)
- `zadd` (sorted_set.py)
- `zrange` (sorted_set.py)
- `zrem` (sorted_set.py)
- `xadd` (stream.py)
- `xrange` (stream.py)
- `xdel` (stream.py)
- `xgroup_create` (stream.py)
- `xgroup_destroy` (stream.py)
- `xreadgroup` (stream.py)
- `xack` (stream.py)
- `set` (string.py)
- `get` (string.py)

### Маркер-скан всех 53 описаний

Совпадений: **0**. Ни одно описание инструмента не содержит формулировок приоритизации, вытеснения других инструментов, обязательности или самопродвижения по применённым регексам.

Ближайшая по духу, но НЕ попавшая под регексы формулировка (для полноты фиксирую дословно, инструмент `search_redis_documents`):

> This tool exposes updated and curated documentation, and must be invoked every time the user wants to learn more in areas including:

### 10 репрезентативных полных описаний (дословно)

#### `set_vector_in_hash` (hash.py)
```
Store a vector as a field in a Redis hash.

Args:
    name: The Redis hash key.
    vector_field: The field name inside the hash. Unless specifically required, use the default field name
    vector: The vector (list of numbers) to store in the hash.

Returns:
    True if the vector was successfully stored, False otherwise.
```

#### `json_set` (json.py)
```
Set a JSON value in Redis at a given path with an optional expiration time.

Args:
    name: The Redis key where the JSON document is stored.
    path: The JSON path where the value should be set.
    value: The JSON value to store (as JSON string, or will be auto-converted).
    expire_seconds: Optional; time in seconds after which the key should expire.

Returns:
    A success message or an error message.
```

#### `scan_keys` (misc.py)
```
Scan keys in the Redis database using the SCAN command (non-blocking, production-safe).

⚠️  IMPORTANT: This returns PARTIAL results from one iteration. Use scan_all_keys()
to get ALL matching keys, or call this function multiple times with the returned cursor
until cursor becomes 0.

The SCAN command iterates through the keyspace in small chunks, making it safe to use
on large databases without blocking other operations.

Args:
    pattern: Pattern to match keys against (default is "*" for all keys).
            Common patterns: "user:*", "cache:*", "*:123", etc.
    count: Hint for the number of keys to return per iteration (default 100).
           Redis may return more or fewer keys than this hint.
    cursor: The cursor position to start scanning from (0 to start from beginning).
            To continue scanning, use the cursor value returned from previous call.

Returns:
    A dictionary containing:
    - 'cursor': Next cursor position (0 means scan is complete)
    - 'keys': List of keys found in this iteration (PARTIAL RESULTS)
    - 'total_scanned': Number of keys returned in this batch
    - 'scan_complete': Boolean indicating if scan is finished
    Or an error message if something goes wrong.

Example usage:
    First call: scan_keys("user:*") -> returns cursor=1234, keys=[...], scan_complete=False
    Next call: scan_keys("user:*", cursor=1234) -> continues from where it left off
    Final call: returns cursor=0, scan_complete=True when done
```

#### `scan_all_keys` (misc.py)
```
Scan and return ALL keys matching a pattern using multiple SCAN iterations.

This function automatically handles the SCAN cursor iteration to collect all matching keys.
It's safer than KEYS * for large databases but will still collect all results in memory.

⚠️  WARNING: With very large datasets (millions of keys), this may consume significant memory.
For large-scale operations, consider using scan_keys() with manual iteration instead.

Args:
    pattern: Pattern to match keys against (default is "*" for all keys).
    batch_size: Number of keys to scan per iteration (default 100).

Returns:
    A list of all keys matching the pattern or an error message.
```

#### `search_redis_documents` (misc.py)
```
Search Redis documentation and knowledge base to learn about Redis concepts and use cases.

This tool exposes updated and curated documentation, and must be invoked every time the user wants to learn more in areas including:

**Common Use Cases:**
- Session Management: User session storage and management
- Caching: Application-level and database query caching
- Rate Limiting: API throttling and request limiting
- Leaderboards: Gaming and ranking systems
- Semantic Search: AI-powered similarity search
- Agentic Workflows: AI agent state and memory management
- RAG (Retrieval-Augmented Generation): Vector storage for AI applications
- Real-time Analytics: Counters, metrics, and time-series data
- Message Queues: Task queues and job processing
- Geospatial: Location-based queries and proximity search

Args:
    question: The question about Redis concepts, data structures, features, or use cases

Returns:
    Union[List[Dict[str, Any]], Dict[str, Any]]: A list of documentation results from the API, or a dict with an error message.
```

#### `subscribe` (pub_sub.py)
```
Subscribe to a Redis channel and return a reusable subscription handle.

Args:
    channel: The Redis channel to subscribe to.

Returns:
    A dictionary containing the subscription ID or an error message.
```

#### `create_vector_index_hash` (redis_query_engine.py)
```
Create a Redis 8 vector similarity index using HNSW on a Redis hash.

This function sets up a Redis index for approximate nearest neighbor (ANN)
search using the HNSW algorithm and float32 vector embeddings.

Args:
    index_name: The name of the Redis index to create. Unless specifically required, use the default name for the index.
    prefix: The key prefix used to identify documents to index (e.g., 'doc:'). Unless specifically required, use the default prefix.
    vector_field: The name of the vector field to be indexed for similarity search. Unless specifically required, use the default field name
    dim: The dimensionality of the vectors stored under the vector_field.
    distance_metric: The distance function to use (e.g., 'COSINE', 'L2', 'IP').

Returns:
    A string indicating whether the index was created successfully or an error message.
```

#### `vector_search_hash` (redis_query_engine.py)
```
Perform a KNN vector similarity search using Redis 8 or later version on vectors stored in hash data structures.

Args:
    query_vector: List of floats to use as the query vector.
    index_name: Name of the Redis index. Unless specifically specified, use the default index name.
    vector_field: Name of the indexed vector field. Unless specifically required, use the default field name
    k: Number of nearest neighbors to return.
    return_fields: List of fields to return (optional).

Returns:
    A list of matched documents or an error message.
```

#### `hybrid_search` (redis_query_engine.py)
```
Perform a hybrid search combining a Redis filter expression with KNN vector similarity.

Hybrid search pre-filters documents by metadata before ranking by vector similarity —
the standard pattern for production RAG and semantic search pipelines.

Filter expression examples:
    "*"                              → no filter, pure vector search (same as vector_search_hash)
    "@category:{news}"              → tag filter
    "@year:[2020 2024]"             → numeric range
    "@lang:{en} @year:[2022 +inf]"  → combined tag + range
    "@title:redis"                  → full-text match on a text field

Full filter syntax: https://redis.io/docs/latest/develop/interact/search-and-query/query/

Args:
    query_vector:       List of floats to use as the query vector.
    filter_expression:  Redis filter expression to restrict candidates before KNN ranking.
                        Defaults to '*' (no filter).
    index_name:         Name of the Redis index (default: 'vector_index').
    vector_field:       Name of the indexed vector field (default: 'vector').
    k:                  Number of nearest neighbors to return.
    return_fields:      Additional fields to include in results (optional).

Returns:
    A list of matched documents with their similarity score, or an error message.
```

#### `xreadgroup` (stream.py)
```
Read entries from a Redis stream using a consumer group.

Args:
    key (str): The stream key.
    group_name (str): The consumer group name.
    consumer_name (str): The consumer name.
    count (int, optional): Maximum number of entries to retrieve.
    block_ms (int, optional): Maximum time to block waiting for entries.
        Use None for a non-blocking read. 0 is rejected because Redis treats
        BLOCK 0 as an indefinite wait.
    stream_id (str, optional): Stream ID to read from. Use ">" for new messages.

Returns:
    str: The retrieved stream entries or an error message.
```
