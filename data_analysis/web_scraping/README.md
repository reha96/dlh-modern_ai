# Data Collection — Web Scraping

Fetch pages with `requests`, parse them with BeautifulSoup, log in with sessions and CSRF tokens, then drive a headless browser with Selenium — from static HTML to infinite-scroll pages.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | How to fetch a web page with `requests` and detect HTTP errors |
| 2 | How to parse HTML with BeautifulSoup (`html.parser`) |
| 3 | How to extract clean text with `.get_text(strip=True)` |
| 4 | How to paginate by following "Next" links and resolving relative URLs |
| 5 | How to read a site's JSON API instead of scraping HTML |
| 6 | How to parse JSON-LD structured data from `<script>` tags |
| 7 | How sessions, cookies, and CSRF tokens make login work |
| 8 | How to drive a headless Chrome browser with Selenium |
| 9 | How to locate elements with string CSS selectors and read attributes |
| 10 | How to handle infinite scroll and skip duplicate results |
| 11 | The difference between static and dynamic pages and the right tool for each |

---

## Task-by-Task Reference

### Task 0 — Fetch HTML (`0-fetch_html.py`)

**Challenge:** Get a full web page into your program as a string, and fail loudly when the server rejects the request.

**Approach:** One `requests.get()` call with optional headers and a timeout. `raise_for_status()` turns any HTTP status >= 400 into an exception, so bad responses never slip through silently. Return `r.text`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `requests.get(url, headers=..., timeout=...)` | Sends an HTTP GET; returns a `Response` object |
| `response.raise_for_status()` | Raises `HTTPError` on any 4xx/5xx status |
| `response.text` | The response body as a decoded string |

> **Key takeaway:** The request either succeeds or raises — never let a bad status pass silently.

---

### Task 1 — Scrape Basic Info (`1-scrape_basic.py`)

**Challenge:** Turn raw HTML into a list of clean dicts (quote text, author, tags) without using regex.

**Approach:** Reuse `fetch_html()` from task 0, parse with `BeautifulSoup(..., 'html.parser')`, find all `div.quote` blocks, then drill into each with `.find()`/`.find_all()` and clean every value with `.get_text(strip=True)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `BeautifulSoup(html, 'html.parser')` | Builds a searchable tree from HTML text |
| `soup.find_all('div', class_='quote')` | Finds every element matching tag + class |
| `soup.find('span', class_='text')` | Finds the first match; returns a `Tag` or `None` |
| `tag.get_text(strip=True)` | The element's text with whitespace removed |
| List comprehension over `find_all('a', class_='tag')` | Collects all tags of one quote into a list |

> **Key takeaway:** Class-filtered `find` calls plus `get_text` turn messy HTML into clean dicts.

---

### Task 2 — Scrape Paginated Data (`2-scrape_paginated.py`)

**Challenge:** Collect quotes from every page, not just the first.

**Approach:** Loop while a "Next" button exists. Find `li.next`, read its `a`'s href, and resolve the relative link against the current URL with `urljoin`. Extend the result list per page and sleep one second between requests. A missing `li.next` is the stop signal.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `soup.find('li', class_='next')` | Locates the pagination control; `None` means last page |
| `urllib.parse.urljoin(current, href)` | Resolves a relative link into a full absolute URL |
| `time.sleep(1)` | Politeness delay between requests |
| `out.extend(...)` | Accumulates each page's quotes into one list |

> **Key takeaway:** Relative hrefs must be resolved with `urljoin`, and the absence of the Next element ends the loop.

---

### Task 3 — Scrape via API (`3-scrape_via_api.py`)

**Challenge:** The site serves JSON behind the scenes; get the data without parsing any HTML.

**Approach:** Build each endpoint as `base_url.rstrip('/') + '/api/quotes?page=N'`, fetch it with the existing `fetch_html()` (it returns raw text, which works for JSON too), parse with `json.loads()`, and keep paging while the payload's `has_next` flag is true.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `json.loads(text)` | Parses a JSON string into Python dicts and lists |
| `payload['quotes']`, `quote['author']['name']` | Walks nested JSON structures |
| `payload['has_next']` | The API's own pagination flag — cleaner than reading HTML |
| f-string URL building | Composes `/api/quotes?page={count}` per iteration |

> **Key takeaway:** When a site offers JSON, call it directly — it is cleaner and kinder to the server than scraping HTML.

---

### Task 4 — Extract JSON-LD (`4-extract_jsonld.py`)

**Challenge:** The quote data is embedded in the page itself as JSON-LD structured data, invisible to the eye.

**Approach:** Find every `script` with `type='application/ld+json'`, read its content with `.get_text()`, and parse with `json.loads()`. Keep only nodes whose `@type` is `"Quote"`, and normalize `keywords` whether they arrive as a list or a comma-separated string.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `soup.find_all('script', type='application/ld+json')` | Targets scripts by their `type` attribute |
| `script.get_text()` | Extracts the raw JSON text inside a script tag |
| `payload.get("@type") == "Quote"` | Filters nodes by schema.org type |
| `isinstance(keywords, str)` | Handles keywords as list or comma-string |
| `payload.get("author", {}).get("name")` | Safe nested lookup with fallbacks |

> **Key takeaway:** JSON-LD is a machine-readable API baked into the HTML — parse the script tags, not the visible markup.

---

### Task 5 — Login & Scrape (`5-login_and_scrape.py`)

**Challenge:** The quotes sit behind a login form with a CSRF token; you must authenticate and keep the session alive.

**Approach:** Create a `requests.Session()` so cookies persist. GET the login page, read the hidden `csrf_token` value out of the form with BeautifulSoup, POST username, password, and token back to the login URL, then GET the protected page and parse `div.quote` exactly as in task 1. The session follows the post-login redirect automatically.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `requests.Session()` | Keeps a cookie jar across requests so login state survives |
| `soup.find('input', {'name': 'csrf_token'})['value']` | Pulls a hidden form field's value |
| `session.post(url, data={...})` | Submits form fields in one call |
| `session.get(url)` | Reuses the session's cookies instead of starting fresh |

> **Key takeaway:** Login state is just cookies; a Session carries them for you, and the CSRF token must be read from the form before you POST.

---

### Task 6 — Scrape Static Products (`6-products_list.py`)

**Challenge:** The product catalog lives in a real browser; a plain HTTP fetch is the wrong tool.

**Approach:** Start headless Chrome via Selenium with `--headless`, `--no-sandbox`, and a 1920x1080 window. Locate cards with `find_elements('css selector', 'div.thumbnail')`. Per card: read the `title` attribute of `a.title`, the text of `h4.price` and `p.description`, and the rating from the `data-rating` attribute, converted with `int()`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `webdriver.ChromeOptions()` + `add_argument('--headless')` | Runs Chrome invisibly |
| `--no-sandbox`, `--window-size=1920,1080` | Works in restricted environments; avoids broken responsive layouts |
| `driver.find_elements('css selector', 'div.thumbnail')` | Locates elements by a string CSS selector |
| `element.get_attribute('title')` / `('data-rating')` | Reads attribute values — Selenium has no `get_text()` |
| `element.text` | The visible text of an element (BS4's `get_text()` equivalent) |

> **Key takeaway:** Selenium reads attributes and text like BeautifulSoup, but with `find_element(s)` and string selectors — and the import whitelist forces those selectors to be plain strings.

---

### Task 7 — Scrape Product Detail (`7-product_detail.py`)

**Challenge:** One product page where the title is the second `h4` inside the caption block, and the star rating is drawn with icon elements.

**Approach:** Same headless setup as task 6, then `time.sleep(delay)` for the page to render. Title via the positional selector `.caption h4:nth-of-type(2)`; price and description via their classes; rating as the count of `.ratings .ws-icon-star` elements.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `time.sleep(delay)` | Waits for JavaScript-rendered content |
| `h4:nth-of-type(2)` | Selects the second `h4` inside a block |
| `len(driver.find_elements(...))` | Counts matching elements — one match per star |

> **Key takeaway:** The spec says the stars are `<p>` elements, but the live site renders `<span>` — count what the browser actually renders, not what the docs claim.

---

### Task 8 — Scroll & Scrape Products (`8-scroll_and_scrape.py`)

**Challenge:** Products load only as you scroll; you must drive the browser to the bottom and avoid collecting the same card twice.

**Approach:** Loop `driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')`, re-read `scrollHeight`, and stop when it stops growing. Cap each iteration's wait at `min(scroll_pause, 0.25)` — a full 2-second pause per step would blow the checker's 30-second timeout. Dedup with a set of `(title, price)` tuples.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `driver.execute_script('window.scrollTo(...)')` | Runs JavaScript inside the page |
| `return document.body.scrollHeight` | Measures the page height from JS |
| `min(scroll_pause, 0.25)` | Caps the per-scroll wait to finish inside the checker's timeout |
| Set of `(title, price)` tuples | Skips duplicate cards that re-render during scrolling |

> **Key takeaway:** Infinite scroll is a loop with two signals — the page height stops growing, and a set keeps repeats out.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `requests.get()`, `raise_for_status()`, `response.text` | HTTP clients |
| 1 | `BeautifulSoup`, `find_all`/`find`, `.get_text(strip=True)` | HTML parsing |
| 2 | Next-link loop, `urljoin`, `time.sleep(1)` | HTML parsing |
| 3 | `json.loads`, `has_next` flag, nested dict access | JSON |
| 4 | JSON-LD script parsing, `@type` filtering | JSON |
| 5 | `requests.Session`, CSRF token, `session.post(data=...)` | Sessions & auth |
| 6 | Headless Chrome options, string CSS selectors, `get_attribute` | Browser automation |
| 7 | `nth-of-type` selector, `time.sleep(delay)`, element counting | Browser automation |
| 8 | `execute_script` scrolling, scrollHeight loop, set dedup, capped sleep | Scrolling & JS execution |

---

## Resources

### Read or watch

- [Introduction to Web Scraping](https://www.geeksforgeeks.org/web-scraping/introduction-to-web-scraping/) — overview of the scraping landscape, its techniques, tools, and obstacles (Date: 2025-07-31)
- [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/) — hands-on static-site pipeline with `requests.get()` + `BeautifulSoup` (Date: 2024-12-01)
- [Selenium with Python](https://selenium-python.readthedocs.io/) — the community reference for driving a real browser: locator strategies and waits (Date: 2024-04-05)
- [Static vs Dynamic Website](https://www.geeksforgeeks.org/websites-apps/static-vs-dynamic-website/) — the architectural difference that decides your scraping tool (Date: 2025-07-11)
- [CSS Selectors in Selenium: Complete Guide With Examples](https://www.testmuai.com/learning-hub/css-selectors/) — cookbook of CSS selector syntax: simple, combinators, substrings, pseudo-classes (Date: 2026-07-16)
- [How to Avoid Scraping the Same Content Twice](https://ajantriks.net/how-to-avoid-scraping-the-same-content-twice-essential-strategies-for-efficient-data-extraction/) — dedup strategies: URL normalization, hashing, Bloom filters (Date: 2025-09-16)
- [A Practical Introduction to Web Scraping in Python](https://realpython.com/python-web-scraping-practical-introduction/) — three ways to pull data: `urllib`, regex, and BeautifulSoup (Date: 2024-12-21)
- [The complete guide to web scraping with Selenium and Python](https://www.scrapingbee.com/blog/selenium-python/) — Selenium drives a real browser; the infinite-scroll loop pattern (Date: 2026-07-08)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) — inspect the live DOM and find hidden JSON APIs in the Network panel (Date: 2026-07-06)
- [How to handle Cookies in Selenium WebDriver](https://www.browserstack.com/guide/how-to-handle-cookies-in-selenium) — cookie handling; persist sessions and skip re-login (Date: 2025-05-30)
- [The Feynman Learning Technique](https://fs.blog/feynman-learning-technique/) — learn by teaching; simplify until it flows (Date: 2021-02-22)

### Good to know

- [Web Scraping Best Practices in 2026](https://www.scrapingbee.com/blog/web-scraping-best-practices/) — rate limiting, caching, proxies, robots.txt, retries (Date: 2026-01-04)
- [Alerts & Popups in Selenium](https://www.browserstack.com/guide/alerts-and-popups-in-selenium) — JS alerts vs HTML popups and window handles (Date: 2025-12-19)
- [Implicit and Explicit Wait in Selenium with Syntax](https://www.guru99.com/implicit-explicit-waits-selenium.html) — the three Selenium wait types (Date: 2026-05-09)
- [Ethical Web Scraping: Principles and Practices](https://www.datacamp.com/blog/ethical-web-scraping) — terms of service, robots.txt, GDPR, throttling (Date: 2025-04-21)
- [Scrapy — open source web scraping framework for Python](https://www.scrapy.org/) — the full scraping framework; follow its official docs tutorial (Date: unknown)
- [Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies) — how `Set-Cookie`/`Cookie` headers let stateless HTTP remember state (Date: 2026-08-13)
- [Web Scraping Dynamic Content With Python (JS Rendering Guide)](https://www.scrapingbee.com/blog/web-scraping-dynamic-content/) — why `requests` fails on client-rendered pages; the JSON/XHR shortcut (Date: 2026-05-19)
- [ScraperAPI: Python Web Scraping Integration Guide](https://scrapeops.io/proxy-providers/scraperapi/python-scraperapi-guide/) — scraping-as-a-service with proxies, CAPTCHA solving, and rendering (Date: 2024-10-03)
- [Best User Agent List for Scraping & How to Rotate Them Effectively](https://www.scrapingbee.com/blog/list-of-user-agents-for-scraping/) — UA strings and rotation patterns (Date: 2026-01-05)
- [Detailed Guide on IP Rotation in Web Scraping: 2026 Updated](https://www.nstproxy.com/blog/web-scraping-ip-rotation) — spreading requests across proxies; sticky sessions for logins (Date: 2026-05-21)
- [Web Scraping Without Getting Blocked: 2026 Guide](https://www.scrapingbee.com/blog/web-scraping-without-getting-blocked/) — layered detection and anti-block tactics (Date: 2026-07-15)

### References

- [BeautifulSoup 4 Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/#) (Date: unknown)
- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/) (Date: unknown)
- [Python Requests Library Documentation](https://requests.readthedocs.io/en/latest/) (Date: unknown)
- [Chrome DevTools Documentation](https://developer.chrome.com/docs/devtools/) (Date: unknown)
- [W3Schools CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.php) (Date: unknown)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) (Date: unknown)
- [RFC 6265 - HTTP State Management Mechanism (Cookies)](https://datatracker.ietf.org/doc/html/rfc6265) (Date: unknown)
- [Scrapy API Reference](https://docs.scrapy.org/en/latest/topics/api.html) (Date: unknown)
- [Python Selenium API](https://selenium-python.readthedocs.io/api.html) (Date: unknown)
- [XPath Syntax Reference](https://www.w3schools.com/xml/xpath_syntax.asp) (Date: unknown)