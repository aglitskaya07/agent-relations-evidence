# UNIT: linkedin | LinkedIn | github stickerdaniel/linkedin-mcp-server | тип автора: комьюнити | captured 2026-07-29 (static source)

Это MCP-сервер: Python, FastMCP. Конструктор — `linkedin_mcp_server/server.py:153` (`mcp = FastMCP("mcp-server-linkedin", version=..., lifespan=..., mask_error_details=True, auth=...)`). Инструменты регистрируются декоратором `@mcp.tool(...)` в `linkedin_mcp_server/tools/{person,company,job,messaging,feed,post}.py` и один в `server.py`.

## CHANNEL: instructions
(не обнаружены статически)

Параметр `instructions=` конструктору FastMCP не передаётся; единственное вхождение слова «instructions» в репозитории — в CONTRIBUTING.md про setup. Ответ initialize нигде вручную не формируется.

## CHANNEL: tool descriptions (coverage=full)

19 инструментов, описания = docstring функции (FastMCP берёт docstring как description; `description=` нигде не задан).

### close_session
title: "Close Session"; annotations: {'destructiveHint': True}
```
Close the current browser session and clean up resources.
```

### get_company_profile
title: "Get Company Profile"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get a specific company's LinkedIn profile.

Args:
    company_name: LinkedIn company name (e.g., "docker", "anthropic", "microsoft")
    ctx: FastMCP context for progress reporting
    sections: Comma-separated list of extra sections to scrape.
        The about page is always included.
        Available sections: posts, jobs
        Examples: "posts", "posts,jobs"
        Default (None) scrapes only the about page.

Returns:
    Dict with url, sections (name -> raw text), and optional references.
    Includes unknown_sections list when unrecognised names are passed.
    The LLM should parse the raw text in each section.

    When the about section is included, references["about"] may
    include a {kind: "company_urn", value: "<numeric-id>"} entry —
    present whenever the page exposes the "See all employees" link
    (typically all but the smallest companies). The value is the
    numeric id LinkedIn's people-search uses in its currentCompany
    URL facet; plain-text company names are silently ignored by
    that facet.
```

### get_company_posts
title: "Get Company Posts"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get recent posts from a company's LinkedIn feed.

Args:
    company_name: LinkedIn company name (e.g., "docker", "anthropic", "microsoft")
    ctx: FastMCP context for progress reporting

Returns:
    Dict with url, sections (name -> raw text), and optional references.
    The LLM should parse the raw text to extract individual posts.
```

### search_companies
title: "Search Companies"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Search for companies on LinkedIn.

Args:
    keywords: Search keywords (e.g., "fintech", "anthropic", "electric vehicles")
    ctx: FastMCP context for progress reporting

Returns:
    Dict with url, sections (search_results -> raw text), and optional references.
    The LLM should parse the raw text to extract individual companies and their pages.
```

### get_company_employees
title: "Get Company Employees"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
List employees at a company from the LinkedIn /people/ page, including
the demographics aggregate that this view exposes: where employees
live, where they studied, and a function breakdown (Engineering, Sales,
Operations, etc.). The demographics are unique to this tool.

For filtered search by network degree (1st/2nd/3rd) or location, prefer
search_people with current_company set to the company URN id. That path
also returns more result pages than the /people/ tab.

The optional keywords filter narrows results by name, title, or skill.

company_name must be the exact LinkedIn URL slug (the path segment after
/company/), not the display name. LinkedIn assigns unique slugs and the
display name often does not match. For example, the AI lab Anthropic
lives at /company/anthropicresearch/, not /company/anthropic/. If you
are unsure of the slug, call search_companies first and pick the slug
from the returned references.

Args:
    company_name: LinkedIn company URL slug (e.g., "docker", "anthropicresearch", "microsoft")
    ctx: FastMCP context for progress reporting
    keywords: Optional filter by name, job title, or skill (e.g., "engineer", "sales")

Returns:
    Dict with url, sections (employees -> raw text), and optional references.
    References include /in/ profile paths for listed employees.
```

### get_feed
title: "Get Feed"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get posts from the authenticated user's LinkedIn feed.

Args:
    ctx: FastMCP context for progress reporting
    num_posts: Number of posts to fetch (1-50, default 10).
               Posts are loaded in batches of ~5 as the page scrolls,
               so the actual count may slightly exceed the target.

Returns:
    Dict with url, sections (name -> raw text), and optional keys:
    - references["feed"]: list of {kind: "feed_post", url, ...}
      entries. URLs are relative paths and may carry either
      ``/feed/update/<urn>/`` (DOM-anchor-derived) or
      ``/posts/<slug>`` (SDUI-derived) shape — both are valid
      LinkedIn permalinks.
    - section_errors: present when the feed is rate-limited or
      extraction fails.

    Truncated posts are not auto-expanded; full text for any post
    is reachable via its permalink in references["feed"]. The LLM
    should parse sections["feed"] for post bodies.
```

### get_job_details
title: "Get Job Details"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get job details for a specific job posting on LinkedIn.

Args:
    job_id: LinkedIn job ID (e.g., "4252026496", "3856789012")
    ctx: FastMCP context for progress reporting

Returns:
    Dict with url, sections (name -> raw text), and optional references.
    The LLM should parse the raw text to extract job details.
```

### search_jobs
title: "Search Jobs"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Search for jobs on LinkedIn.

Returns job_ids that can be passed to get_job_details for full info.

Args:
    keywords: Search keywords (e.g., "software engineer", "data scientist")
    ctx: FastMCP context for progress reporting
    location: Optional location filter (e.g., "San Francisco", "Remote")
    max_pages: Maximum number of result pages to load (1-10, default 3)
    date_posted: Filter by posting date (past_hour, past_24_hours, past_week, past_month)
    job_type: Filter by job type, comma-separated (full_time, part_time, contract, temporary, volunteer, internship, other)
    experience_level: Filter by experience level, comma-separated (internship, entry, associate, mid_senior, director, executive)
    work_type: Filter by work type, comma-separated (on_site, remote, hybrid)
    easy_apply: Only show Easy Apply jobs (default false)
    sort_by: Sort results (date, relevance)

Returns:
    Dict with url, sections (name -> raw text), job_ids (list of
    numeric job ID strings usable with get_job_details), and optional references.
```

### get_saved_jobs
title: "Get Saved Jobs"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
List job postings saved by the authenticated LinkedIn user.

Returns job_ids that can be passed to get_job_details for full info.

Args:
    ctx: FastMCP context for progress reporting
    max_pages: Maximum number of saved-jobs pages to load (1-10, default 3)

Returns:
    Dict with url, sections (name -> raw text), job_ids (list of
    numeric job ID strings usable with get_job_details), and optional references.
```

### get_inbox
title: "Get Inbox"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
List recent conversations from the LinkedIn messaging inbox.

Args:
    ctx: FastMCP context for progress reporting
    limit: Maximum number of conversations to load (1-50, default 20)

Returns:
    Dict with url, sections (inbox -> raw text), and optional references.
```

### get_conversation
title: "Get Conversation"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Read a specific messaging conversation.

Provide either linkedin_username or thread_id to identify the conversation.

When looked up by linkedin_username, resolution searches the messaging
inbox for the participant's display name and click-visits every
matching row to capture its thread ID — LinkedIn's sidebar has no
anchor hrefs or thread-id attributes, so this is the only available
path. Each visit selects the row in the LinkedIn UI and may mark it
as read. Pass thread_id directly to skip this enumeration.

Args:
    ctx: FastMCP context for progress reporting
    linkedin_username: LinkedIn username of the conversation participant
    thread_id: LinkedIn messaging thread ID
    index: 0-based selector for which thread to open when the
        participant has multiple threads (e.g. an organic 1-on-1 plus
        an InMail). Ignored when thread_id is provided. To enumerate
        thread IDs first, call search_conversations.

Returns:
    Dict with url, sections (conversation -> raw text), and optional references.
```

### search_conversations
title: "Search Conversations"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Search messages by keyword.

Args:
    keywords: Search keywords to filter conversations
    ctx: FastMCP context for progress reporting
    limit: Maximum number of search-result rows to enumerate as
        conversation references (1-50, default 20). Each enumeration
        selects the row in LinkedIn's UI and may mark it as read, so
        a low cap is preferable for noisy queries.

Returns:
    Dict with url, sections (search_results -> raw text), and optional references.
```

### send_message
title: "Send Message"; annotations: {'destructiveHint': True, 'openWorldHint': True}
```
Send a message to a LinkedIn user.

The recipient must be directly messageable from the profile page. This is a
write operation when confirm_send is True.

Args:
    linkedin_username: LinkedIn username of the recipient
    message: The message text to send
    confirm_send: Must be True to send the message
    ctx: FastMCP context for progress reporting
    profile_urn: Optional profile URN (e.g. ACoAAB...) to construct the
        compose URL directly. Providing this bypasses the Message-button
        lookup and is more reliable when available. Obtain via
        get_person_profile. Note: inbox may not always show all
        messages; use search_conversations as a fallback.

Returns:
    Dict with url, status, message, recipient_selected, and sent.
```

### get_person_profile
title: "Get Person Profile"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get a specific person's LinkedIn profile.

Args:
    linkedin_username: LinkedIn username (e.g., "stickerdaniel", "williamhgates")
    ctx: FastMCP context for progress reporting
    sections: Comma-separated list of extra sections to scrape.
        The main profile page is always included.
        Available sections: experience, education, interests, honors, languages, certifications, skills, projects, contact_info, posts
        Examples: "experience,education", "contact_info", "skills,projects", "honors,languages", "posts"
        Default (None) scrapes only the main profile page.
    max_scrolls: Maximum pagination attempts per section to load more content.
        On detail sections (experience, certifications, skills, etc.) this
        is the max number of "Show more" button clicks. On activity/posts
        it is the max scroll-to-bottom iterations. Applies to all sections
        in this call. Default (None) uses 5 for detail sections and 10 for
        posts. Increase when a profile has many items in a section
        (e.g., 30+ certifications, max_scrolls=20). To avoid slowing down
        other sections, request heavy sections in a separate call.

Returns:
    Dict with url, sections (name -> raw text), and optional references.
    Sections may be absent if extraction yielded no content for that page.
    Includes unknown_sections list when unrecognised names are passed.
    The LLM should parse the raw text in each section.
```

### search_people
title: "Search People"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Search for people on LinkedIn.

Args:
    keywords: Search keywords (e.g., "software engineer", "recruiter at Google")
    ctx: FastMCP context for progress reporting
    location: Optional location filter (e.g., "New York", "Remote")
    network: Optional connection-degree filter. Each element is one of
        "F" (1st-degree), "S" (2nd-degree), "O" (3rd-degree and beyond).
        Example: ["F"] to only return 1st-degree connections.
    current_company: Optional current-employer filter. LinkedIn's
        currentCompany facet only filters on the numeric company URN id
        (e.g. "1115" for SAP); plain company names are accepted by the
        URL but ignored by LinkedIn and return the unfiltered result
        set. Look up a company's URN via get_company_profile -- it is
        exposed under references["about"]. For company-wide employee
        demographics (location/education/function breakdown) plus a
        slug-based lookup, use get_company_employees instead.

Returns:
    Dict with url, sections (name -> raw text), and optional references.
    The LLM should parse the raw text to extract individual people and their profiles.
```

### connect_with_person
title: "Connect With Person"; annotations: {'destructiveHint': True, 'openWorldHint': True}
```
Send a LinkedIn connection request or accept an incoming one.

The tool is annotated with destructiveHint so MCP clients will
prompt for user confirmation before execution.

Args:
    linkedin_username: LinkedIn username (e.g., "stickerdaniel", "williamhgates")
    ctx: FastMCP context for progress reporting
    note: Optional note to include with the invitation

Returns:
    Dict with url, status, message, and note_sent.
    Statuses: pending, already_connected, follow_only,
    connect_unavailable, unavailable, send_failed,
    note_not_supported, custom_note_limit_reached,
    connected, or accepted.

    When status is ``custom_note_limit_reached`` LinkedIn rejected
    personalized invite notes because the free note quota for the
    account is exhausted. The ``message`` is the raw Premium dialog
    text read from LinkedIn.
```

### get_sidebar_profiles
title: "Get Sidebar Profiles"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get profile links from sidebar recommendation sections on a LinkedIn profile page.

Extracts profiles from "More profiles for you", "Explore premium profiles",
and "People you may know" sidebar sections. Follows "Show all" links to
return the full list from each section. Sections that redirect to
linkedin.com/premium are skipped.

Args:
    linkedin_username: LinkedIn username of the profile page to scrape
        (e.g., "stickerdaniel", "williamhgates")
    ctx: FastMCP context for progress reporting

Returns:
    Dict with url and sidebar_profiles mapping section key to a list of
    /in/username/ paths. Only sections present on the page are included.
```

### get_my_profile
title: "Get My Profile"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Get the authenticated user's own LinkedIn profile.

Navigates to /in/me/ and resolves the redirect to obtain the real
username before scraping, so the url field in the result is the actual
profile URL (e.g. linkedin.com/in/johndoe/) rather than /in/me/.

Args:
    ctx: FastMCP context for progress reporting
    sections: Comma-separated list of extra sections to scrape.
        The main profile page is always included.
        Available sections: experience, education, interests, honors, languages, certifications, skills, projects, contact_info, posts
        Examples: "experience,education", "contact_info", "skills,projects"
        Default (None) scrapes only the main profile page.
    max_scrolls: Maximum pagination attempts per section (same as get_person_profile).

Returns:
    Dict with url, sections (name -> raw text), and optional references.
    The url field reflects the resolved profile URL, revealing the real username.
```

### search_posts
title: "Search Posts"; annotations: {'readOnlyHint': True, 'openWorldHint': True}
```
Search LinkedIn posts/content globally by keyword (the "Posts" tab).

Use this to catch informal hiring posts ("we're hiring", "Buscamos
...", "estamos contratando", "join our team") that often appear before
a formal job listing exists. This is global content search, distinct
from get_feed (your own home feed) and get_company_posts (one
company's page).

Args:
    keywords: Search keywords (e.g., "Buscamos Unity", "AI automation hiring")
    ctx: FastMCP context for progress reporting
    date_posted: Optional recency filter. One of "past-24h",
        "past-week", "past-month"; the "past_24_hours" / "past_week" /
        "past_month" spellings used by search_jobs are accepted too.
        Omit for any time.
    max_pages: Scroll depth as result "pages" of ~5 scrolls each
        (1-10, default 3). Content search is an infinite scroll, so
        this caps how far the page is scrolled rather than fetching
        discrete pages.

Returns:
    Dict with url, sections (search_results -> raw text), and optional
    references (post authors, companies, linked jobs) and
    section_errors. The results page carries no per-post permalinks,
    so reach a post through its author. The LLM should parse the raw
    text to extract each post's author, headline/role, company, body,
    posted date, and reaction/comment counts.
```

## Дополнительный канал (не instructions, не tool description)

`manifest.json` (MCPB-бандл) содержит собственные короткие `tools[].description` и `description`/`long_description` бандла — это метаданные упаковки для каталога клиента, они не совпадают с runtime-описаниями выше. Пример `description` бандла: "MCP server that gives Claude access to LinkedIn profiles, companies, job details, and people search through your own account".

`linkedin_mcp_server/update_check.py` + `UpdateNoticeMiddleware` (server.py:171) один раз за процесс добавляют к результату инструмента дополнительный текстовый блок с уведомлением об обновлении — динамически собираемый текст, попадающий в контекст модели.
