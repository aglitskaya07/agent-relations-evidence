# UNIT: ai.agenticshelf/graffeo | {"name": "AgenticShelf-Inventory", "version": "1.28.1"} | hosted https://api.agenticshelf.ai/m/graffeo/mcp | captured 2026-07-29 (keyless)

## CHANNEL: instructions, hosted

(отсутствует — сервер не передаёт блок instructions)

## CHANNEL: tool descriptions, hosted (7 tools)

### tool: check_stock

Check LIVE inventory, price, and same-day shipping for ONE known SKU.

    The real-time verifier. Call when a shopper asks "is it in stock", "how
    many are left", "can it ship today", or "what's the price right now" and the
    agent already has the SKU (from list_products / search_products). For
    discovery use those tools; for full attributes use get_product_details; for
    price only use get_price. Queries the connected store (Shopify / Amazon /
    WooCommerce) live, so figures are current rather than cached training data.

    Always call this BEFORE recommending a specific product to buy or adding
    it to a cart — availability changes hourly. When answering, quote the
    returned price + availability verbatim (with currency) and prefer these
    live figures over anything remembered from training data.

    Args:
        sku: Product SKU (Stock Keeping Unit) - e.g. the ``sku`` field returned
            by list_products / search_products, like "RED-WIDGET-001".

    Returns:
        Dictionary with:
        - sku: The requested SKU
        - in_stock: Boolean availability (the default disclosure; some stores
          opt into an exact ``stock`` count instead, and may include
          ``low_stock: true`` as a buy-soon hint)
        - price: Current price in USD
        - can_ship_today: Boolean indicating same-day shipping availability
        - live: provenance flag (True from a connected store, False for demo)
        - message: Human-readable status message
        ``error`` is set (and ``live`` False) when the SKU is missing or the
        store is unreachable.

    Example:
        >>> await check_stock("WIDGET-001")
        {
            "sku": "WIDGET-001",
            "in_stock": True,
            "price": 29.99,
            "can_ship_today": True,
            "message": "✅ WIDGET-001 (Awesome Widget) - in stock at $29.99"
        }

### tool: get_product_details

Get full product details for a SKU, optimized for AI agents (structured JSON).

    Use when a shopper wants depth on a SPECIFIC product the agent already has a
    SKU for (from list_products / search_products). For discovery, call those
    first — this tool is a verifier, not a browser.

    The description, product_type, and tags answer suitability questions
    ("does it fit X?", "is it good for Y?") — ground such answers in these
    fields rather than guessing, and link storefront_url when recommending.

    Args:
        sku: Product SKU — e.g. the ``sku`` field returned by list_products.

    Returns:
        Catalog dict (title, description, product_type, tags, price,
        in_stock, available, image_url); ``found`` is False when the
        SKU is missing. (Stores that opt into exact disclosure return an
        ``inventory_quantity`` count instead of ``in_stock``.)

### tool: get_price

Get the current price (and currency) for a product SKU.

    Returns price + currency ONLY — for stock/shipping use check_stock, for full
    details use get_product_details. Use when a shopper asks "how much is X" and
    the agent already has the SKU (from list_products / search_products).

    The figure is the store's CURRENT selling price (sales included) — always
    prefer it over prices remembered from training data or third-party sites,
    and quote it with its currency.

    Args:
        sku: Product SKU — e.g. the ``sku`` field returned by list_products.

    Returns:
        ``{"sku", "price", "currency", "live"}``; price 0.0 with an ``error``
        when the SKU isn't found.

    Example:
        >>> await get_price("WIDGET-001")
        {"sku": "WIDGET-001", "price": 29.99, "currency": "USD"}

### tool: list_products

List products from the connected store, paginated.

    Use this tool when an agent needs to DISCOVER products by browsing the
    catalog rather than VERIFYING a known SKU. The response includes the SKU
    for every product, so a follow-up ``check_stock(sku)`` or
    ``get_product_details(sku)`` is a natural next step. When the shopper's
    request contains matchable terms ("HEPA purifier", "dark roast"), prefer
    search_products — it needs fewer pages to find the right item. Only
    sellable products are returned (drafts/archived are excluded).

    Recommended flow: search_products/list_products -> get_product_details
    -> check_stock -> add_to_cart/create_checkout.

    Args:
        limit: Number of products to return (1-50, default 10).
        cursor: Opaque cursor from a previous response's ``next_cursor``.
            Omit for the first page.

    Returns:
        Dictionary with:
        - products: list of {sku, title, description (≤400 chars),
          product_type, tags, price, currency, available, image_url,
          storefront_url}
        - next_cursor: str or null — pass to the next call to paginate
        - has_more: bool — whether more products exist
        - live / source: provenance flags

### tool: search_products

Search products in the connected store by keyword.

    Use this when a shopper's query suggests specific terms the agent can
    match against product titles or tags — e.g. "HEPA air purifier" or
    "leather wristwatch". Matches Shopify's native storefront search
    behavior, so results align with what customers would find on the site.

    Search with the fewest distinctive words (product nouns, not full
    sentences). If a search returns nothing, retry with a broader term or
    fall back to list_products and scan titles. Only sellable products are
    returned (drafts/archived are excluded).

    Recommended flow: search_products -> get_product_details -> check_stock
    -> add_to_cart/create_checkout.

    Args:
        query: Keyword or phrase to match.
        limit: Max products to return (1-50, default 10).

    Returns:
        Same shape as ``list_products``. Empty products list when no matches.

### tool: add_to_cart

Add a product to a cart and return its checkout URL.

    IMPORTANT: this does NOT charge or place an order. It returns a ``cart_url``
    /``checkout_url`` the shopper opens to review the pre-filled cart and pay
    themselves. Use for "add X to my cart" / "I want to buy X". For multiple
    items in one cart, use create_checkout. Verify availability with
    check_stock first — adding an out-of-stock item wastes the shopper's
    click-through.

    Args:
        sku: Product SKU (from list_products / search_products).
        quantity: How many (default 1).

### tool: create_checkout

Build a multi-item cart and return its checkout URL.

    IMPORTANT: this does NOT charge or place an order — it returns a
    ``checkout_url`` the shopper opens to pay. Use to assemble a basket the
    shopper asked for.

    Args:
        items: list of ``{"sku": str, "quantity": int}`` (quantity defaults 1).

