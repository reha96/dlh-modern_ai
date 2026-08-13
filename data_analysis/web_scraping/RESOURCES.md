# RESOURCES.md — Data Collection: Web Scraping

Ingested 2026-08-13 from the intranet project page (project 3558).
Sections mirror the intranet: Read or watch / Good to know / References.

## Read or watch

### Introduction to Web Scraping
URL: https://www.geeksforgeeks.org/web-scraping/introduction-to-web-scraping/  ·  Date: 2025-07-31 (article)  ·  Status: summary

A beginner's overview of the whole scraping landscape. It defines web scraping as automated extraction of website data, replacing slow manual copy-paste, and surveys its uses (price monitoring, SEO tracking, building ML datasets), the main techniques, and the popular tools. It also catalogues the practical obstacles a scraping project will hit, from changing HTML structure to anti-bot defenses and legal risks — a useful map of what to expect before writing code.

- Four extraction techniques: HTML parsing, DOM parsing, API access (preferred when available), and headless browsers like Selenium for JavaScript-heavy sites.
- Tool ladder: BeautifulSoup for parsing, Requests for HTTP fetching, Scrapy as a full crawling framework, Selenium/Playwright for dynamic content.
- Key challenges: site redesigns breaking selectors, IP blocking/CAPTCHAs, duplicate or stale data, and rate-limiting to avoid server overload.

### Beautiful Soup: Build a Web Scraper With Python
URL: https://realpython.com/beautiful-soup-web-scraper-python/  ·  Date: 2024-12-01 (article)  ·  Status: summary

A hands-on tutorial that walks through a complete static-site scraping pipeline: fetch HTML with `requests.get()`, build a `BeautifulSoup(page.content, "html.parser")` object, then extract job listings. It emphasizes inspecting the target with browser DevTools first and teaches URL anatomy (base URL, path, query parameters like `?q=...&l=...`) as a scraping skill in itself.

- Core methods: `soup.find(id="ResultsContainer")`, `find_all("div", class_="card-content")`, `.text.strip()` for clean text, and `.prettify()` for readable output.
- Filtering: the `string=` argument matches exactly (so `string="Python"` returns nothing), while `string=lambda text: "python" in text.lower()` matches flexibly.
- Gotchas: pass `.content` (raw bytes) not `.text` to avoid encoding issues; a failed `.find()` returns `None`, causing the classic `AttributeError: 'NoneType' object has no attribute 'text'` — climb to the parent element to get siblings.

### Selenium with Python
URL: https://selenium-python.readthedocs.io/  ·  Date: 2024-04-05 (page last modified)  ·  Status: summary

The de-facto community reference (by Baiju Muthukadan) for driving a real browser from Python — the tool of choice when a site renders its content with JavaScript. It is organized as a tutorial: installation and drivers, getting started, navigation and form filling, then a full chapter on the eight locator strategies, and chapters on waits and the WebDriver API.

- Element location strategies: `find_element(By.ID, ...)`, `By.NAME`, `By.XPATH`, `By.LINK_TEXT`, `By.PARTIAL_LINK_TEXT`, `By.TAG_NAME`, `By.CLASS_NAME`, `By.CSS_SELECTOR` (use `find_elements` for all matches).
- Two wait mechanisms: explicit waits (`WebDriverWait` + `expected_conditions`) and `implicitly_wait()` — essential for pages that load data asynchronously.
- The API chapter documents exceptions (`NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`) and utilities like `ActionChains` for mouse gestures and `Keys` for keyboard input.

### Static vs Dynamic Website
URL: https://www.geeksforgeeks.org/websites-apps/static-vs-dynamic-website/  ·  Date: 2025-07-11 (article)  ·  Status: summary

Explains the architectural difference that decides your scraping tool choice. Static sites serve prebuilt HTML/CSS files unchanged to every visitor — no server-side processing, no database, so the same HTML a browser sees is exactly what `requests` returns. Dynamic sites build pages at request time with server-side languages (PHP, Node.js) and databases, so content varies per request and often requires JavaScript execution.

- Static: content identical on every load, fast, cheap — scraping is just fetch + parse.
- Dynamic: content changes at runtime, DB interaction, server-side scripting — plain HTTP GET may miss or fail to render the final DOM.
- Rule of thumb for scraping: static sites → Requests/BeautifulSoup suffice; dynamic sites → a browser driver like Selenium that executes JavaScript first.

### CSS Selectors in Selenium: Complete Guide With Examples
URL: https://www.testmuai.com/learning-hub/css-selectors/  ·  Date: 2026-07-16 (article)  ·  Status: summary

A thorough cookbook of CSS selector syntax for locating elements, using Selenium's `find_element(By.CSS_SELECTOR, ...)` (Python) as the delivery vehicle. It covers simple selectors, combinators for hierarchy, substring matching for dynamic attributes, and pseudo-classes for positional selection, then compares CSS against XPath and gives maintainability rules.

- Simple selectors: `#id`, `.class`, `tagname`, `[name='value']`, combined forms like `input#username` and `input[id='username'][type='text']`.
- Combinators: descendant `A B` (any depth), child `A > B` (direct only), adjacent sibling `A + B`, general sibling `A ~ B`.
- Dynamic-element tricks: substring operators `^=` (prefix), `$=` (suffix), `*=` (contains), `~=` (word); pseudo-classes `:nth-child(n)`, `:nth-of-type(n)`, `:first-of-type`, `:last-child`.
- CSS vs XPath: CSS is faster and cleaner but cannot match visible text (`:contains()` is invalid) nor traverse upward — use XPath's `text()` or `parent::` only for those cases; validate selectors in DevTools with `$$('selector')` before coding.

### How to Avoid Scraping the Same Content Twice
URL: https://ajantriks.net/how-to-avoid-scraping-the-same-content-twice-essential-strategies-for-efficient-data-extraction/  ·  Date: 2025-09-16 (article)  ·  Status: summary

A strategy guide for deduplication in scraping projects, motivated by the cost of re-collecting data: wasted compute, skewed analysis, storage bloat, and server strain. Duplicates arise from identical pages under different URLs, session parameters, content syndication, or repeated crawl runs. The article layers defenses from URL normalization through hashing, databases, and near-duplicate detection, plus policies for re-scraping updated pages.

- First line of defense: URL normalization (strip parameters, lowercase, standardize format) plus a database of visited URLs with timestamps.
- Exact matching: content fingerprints via MD5/SHA-256, or SimHash for similarity; choose granularity — whole page, section, or single record.
- At scale: Bloom filters give memory-efficient, false-positive-tolerant pre-screening (never false negatives) before exact lookups; index URL and hash columns (B-tree) for fast queries.
- Near-duplicates: fuzzy methods (Jaccard similarity, cosine similarity, edit distance); schedule re-scrapes per content type (news daily, static references monthly) rather than blind re-crawling.

### A Practical Introduction to Web Scraping in Python
URL: https://realpython.com/python-web-scraping-practical-introduction/  ·  Date: 2024-12-21 (article)  ·  Status: summary

This tutorial walks through the three classic ways to pull data out of a page, using a demo site with deliberately messy HTML. It starts with `urllib.request.urlopen()` to fetch raw HTML, then `page.read().decode("utf-8")` to get a string. String methods (`.find()`, slicing) work on clean pages but break on sloppy markup like `<title >`. Regexes via `re` are more robust but greedy — `"<.*>"` matches too much; the non-greedy `.*?` fixes it. The recommended tool is BeautifulSoup, which parses HTML into a navigable tree with `.find_all()`, `Tag` objects, and dictionary-style attribute access like `image["src"]`. Finally, MechanicalSoup (a headless browser built on BeautifulSoup) automates form submission with `browser.get()`, `.select()`, and `browser.submit()`.

- Always check a site's acceptable-use policy before scraping; scraping against a site's wishes is legally gray.
- `urlopen()` returns an `HTTPResponse`; call `.read().decode("utf-8")` to get the HTML as a string.
- BeautifulSoup: `soup.find_all("img")`, `soup.title.string`, `soup.get_text()`, and attribute access via `tag["href"]`.
- MechanicalSoup submits forms: `browser.submit(form, login_page.url)` — verify success by checking the redirected URL.
- Relative URLs (e.g. `/profiles/dionysus`) must be concatenated with a base URL to build full links.

### The complete guide to web scraping with Selenium and Python
URL: https://www.scrapingbee.com/blog/selenium-python/  ·  Date: 2026-07-08 (article)  ·  Status: summary

This guide explains that Selenium drives a real browser, so it can render JavaScript, click, and scroll on pages that `requests` sees only as an empty shell. Since Selenium 4.6, Selenium Manager auto-downloads drivers — just `webdriver.Chrome(options=options)`; use `--headless=new` and `--window-size=1920,1080` (the 800x600 default breaks responsive layouts). For JS-rendered content, the core skill is `WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")))` instead of `time.sleep()`. For infinite scroll, the pattern is a loop: `driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")`, then compare `document.body.scrollHeight` before/after; when height stops growing, you've reached the end. After rendering, snapshot with `driver.page_source` and let BeautifulSoup parse fast without browser round-trips.

- `driver.get()` waits for the page load event, not for JavaScript to finish — on React/Vue pages the data may not be in `page_source` yet.
- Selenium 4.3 removed `find_element_by_*`; use `driver.find_element(By.ID, "search")`. Singular raises `NoSuchElementException`; plural returns `[]`.
- Infinite-scroll loop: scroll, `time.sleep(1)` for the AJAX request, re-read `scrollHeight`; break when `new_height == last_height`.
- Expected conditions: `presence_of_element_located`, `visibility_of_element_located`, `element_to_be_clickable`, `text_to_be_present_in_element`.
- `execute_async_script()` accepts a callback as `arguments[arguments.length - 1]` for in-page fetch/promises.

### Chrome DevTools
URL: https://developer.chrome.com/docs/devtools/  ·  Date: 2026-07-06 (page last modified)  ·  Status: summary

This is the landing page for Chrome DevTools, the debugging toolkit built into the Chrome browser. For a scraping project it matters because DevTools is where you inspect the actual DOM a page produces — the Elements panel shows the live HTML after JavaScript runs, which is what your selectors must target, not the original view-source. The Network panel lets you inspect request and response bodies (often revealing JSON APIs you could call directly instead of scraping), and lets you overwrite headers or responses to test. The Console runs `document.querySelectorAll(...)` to test CSS selectors instantly, and the Sources panel debugs JavaScript. The site also documents panels for Performance, Memory, Application (cookies/storage), Rendering, and Sensors (device emulation), plus a Recorder that records user flows for automation.

- Right-click → Inspect opens the Elements panel with the element highlighted; read its tag, id, classes, and attributes.
- Test selectors in the Console: `document.querySelectorAll("article.product_pod")` — count matches before using them in code.
- Network panel shows what the page actually requested, including XHR/fetch calls to hidden APIs.
- Application panel inspects cookies and storage; useful for debugging session/cookie handling.

### How to handle Cookies in Selenium WebDriver
URL: https://www.browserstack.com/guide/how-to-handle-cookies-in-selenium  ·  Date: 2025-05-30 (article)  ·  Status: summary

This guide covers cookie handling in Selenium, which matters for scraping because cookies carry login sessions: instead of logging in on every run, you can capture session cookies once and restore them. The examples are in Java but map directly to Python methods. The core WebDriver API: `driver.manage().getCookies()` returns all cookies for the current domain; `getCookieNamed(name)` fetches one; `addCookie(cookie)` adds one; `deleteCookie`, `deleteCookieNamed`, and `deleteAllCookies()` remove them. The article shows storing a cookie's name, value, domain, path, expiry, and secure flag to a file (with FileWriter/BufferedWriter) and reusing them to skip login. It also covers clearing the browser cache via `deleteAllCookies()` or the `chrome://settings/clearBrowserData` page, and building advanced cookies with `Cookie.Builder` for HttpOnly, Secure, and SameSite attributes.

- A cookie consists of name, value, domain, path, expiry, and a secure flag — persist all of them to reuse a session.
- Python equivalents: `driver.get_cookies()`, `driver.get_cookie(name)`, `driver.add_cookie(dict)`, `driver.delete_all_cookies()`.
- HttpOnly blocks JavaScript access, Secure means HTTPS-only, SameSite controls cross-site behavior — useful for session validation.
- Best practice: delete/reset cookies before each new test to avoid state leaking between runs.

### The Feynman Learning Technique
URL: https://fs.blog/feynman-learning-technique/  ·  Date: 2021-02-22 (article)  ·  Status: summary

This article explains Richard Feynman's method for turning memorized factoids into real understanding: learn by teaching. The four steps are (1) write everything you know about a topic as if teaching it to a sixth-grader, avoiding jargon; (2) notice where your explanation gets foggy — those are your knowledge gaps — and return to the source material to fill them; (3) organize the notes into a clean narrative and simplify until it flows; (4) optionally, transmit it to a real person and use their questions as feedback. The core insight is that jargon and complicated vocabulary hide a lack of understanding: if you can't explain a concept in simple words you can rearrange and reuse, you don't really know it. For a scraping project, this is the study technique to apply when reviewing each task's concepts before coding.

- Jargon is a mask: if you can't define your terms simply, you don't understand them yet.
- Writing forces clarity because there is nowhere to hide — engineers use the same trick with "rubber duck debugging".
- Identify gaps honestly; that's where the real learning happens (and it maps to defining your circle of competence).
- Teaching someone else — and answering their questions — is the ultimate test and generator of deeper understanding.

## Good to know

### Web Scraping Best Practices in 2026
URL: https://www.scrapingbee.com/blog/web-scraping-best-practices/  ·  Date: 2026-01-04 (article)  ·  Status: summary

A practical checklist for building robust scrapers: study the target site first, pick the right tool, handle JavaScript-rendered pages with headless browsers, and use CSS/XPath selectors for structured extraction. Emphasizes rate limiting, caching, proxy rotation, realistic headers, robots.txt respect, retries with backoff, and error logging. Also covers scaling with queues and monitoring.

- Rate-limit and rotate proxies to mimic legitimate users and avoid blocks.
- Prefer the site's official API or JSON endpoints when they exist — faster and kinder to the server.

### Alerts & Popups in Selenium
URL: https://www.browserstack.com/guide/alerts-and-popups-in-selenium  ·  Date: 2025-12-19 (article)  ·  Status: summary

Distinguishes browser-generated JavaScript alerts from HTML popups. Alerts (simple, prompt, confirmation) block the page until handled via `driver.switchTo().alert()` with `accept()`, `dismiss()`, `getText()`, `sendKeys()`. HTML modals are ordinary DOM elements located with CSS/XPath; separate windows are handled via `getWindowHandles()` and `switchTo().window()`. Includes Java examples for both cases.

- Alerts are outside the DOM; HTML popups are inside it — different handling paths.
- Use window handles to switch between child popup windows and the main window.

### Implicit and Explicit Wait in Selenium with Syntax
URL: https://www.guru99.com/implicit-explicit-waits-selenium.html  ·  Date: 2026-05-09 (page last modified)  ·  Status: summary

Explains the three Selenium wait types. Implicit wait sets a global polling window before `NoSuchElementException`; explicit wait targets a specific element with `WebDriverWait` plus `ExpectedConditions`; fluent wait adds a polling interval and ignored exceptions for unpredictably loading elements. Recommends replacing `Thread.sleep` with conditional waits and not mixing implicit and explicit waits.

- Selenium 4 uses `Duration.ofSeconds(n)`; the old int+TimeUnit signatures are deprecated.
- Prefer explicit wait with conditions like `visibilityOfElementLocated` for Ajax-heavy pages.

### Ethical Web Scraping: Principles and Practices
URL: https://www.datacamp.com/blog/ethical-web-scraping  ·  Date: 2025-04-21 (article)  ·  Status: summary

Frames ethics as both ground rules and engineering practice: read terms of service and robots.txt, respect copyright, protect personal data (GDPR/CCPA), and ask for permission when unclear. Technically: scrape only needed elements, throttle requests, prefer APIs, cap concurrency, use honest user agents with contact info, test small before scaling, and handle failures with exponential backoff and logging.

- Logging and monitoring your footprint makes your scraper auditable and keeps servers healthy.
- Some targets are categorically off-limits (health records, paywalled journals) regardless of technical feasibility.

### Scrapy — open source web scraping framework for Python
URL: https://www.scrapy.org/  ·  Date: unknown  ·  Status: summary

Product homepage for Scrapy, the most-used open-source Python scraping framework, maintained by Zyte. It pitches project scaffolding (`scrapy startproject` / `scrapy crawl`), CSS/XPath selectors, async crawling with polite throttling, item pipelines, feed exports, and community extensions like scrapy-playwright.

- Not a tutorial itself — the student should use it to install Scrapy and follow the official docs tutorial at docs.scrapy.org.
- Key add-ons: scrapy-playwright (rendering), spidermon (monitoring), scrapy-zyte-api (anti-ban).

### Using HTTP cookies
URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies  ·  Date: 2026-08-13 (page last modified)  ·  Status: summary

Reference on how cookies let the stateless HTTP protocol remember state: a server sends `Set-Cookie`, the browser returns matching cookies in a `Cookie` header. Covers session vs permanent cookies (`Expires`/`Max-Age`), updating/deleting them, scoping with `Domain`/`Path`, and security attributes `Secure`, `HttpOnly`, and `SameSite` (Strict/Lax/None).

- For scraping, cookies are how sessions/logins persist — reuse a session's cookie jar across requests.
- Cookie prefixes (`__Secure-`, `__Host-`) and GDPR/ePrivacy/CCPA regulations matter for any site you operate, not just scrape.

### Web Scraping Dynamic Content With Python (JS Rendering Guide)
URL: https://www.scrapingbee.com/blog/web-scraping-dynamic-content/  ·  Date: 2026-05-19 (article)  ·  Status: summary

Explains why `requests`+BeautifulSoup fail on client-rendered pages and how to detect them (missing content in View Source, XHR/Fetch traffic in DevTools). Covers waiting for elements, clicking, and infinite scrolling, plus extraction rules and pagination. Alternative open-source options: Selenium, Playwright, Puppeteer, with stealth plugins needed to mask automation.

- Best shortcut: find the JSON/XHR endpoint behind the page and call it directly — cheaper than full rendering.
- Verify "dynamic" by disabling JavaScript in DevTools and comparing rendered content.

### ScraperAPI: Python Web Scraping Integration Guide
URL: https://scrapeops.io/proxy-providers/scraperapi/python-scraperapi-guide/  ·  Date: 2024-10-03 (article)  ·  Status: summary

A vendor tutorial on integrating ScraperAPI, a scraping-as-a-service API that rotates proxies, solves CAPTCHAs, and renders JavaScript. Shows Python patterns for the API endpoint, proxy port, and SDK; parameter costs for geotargeting, residential proxies, custom headers, and sessions; plus a BeautifulSoup/IMDb case study with retries and concurrency.

- Requests go through `api.scraperapi.com` with your API key; enable `render=true` for dynamic pages.
- Cost model is credit-based per request; residential IPs and JS rendering cost extra credits.

### Best User Agent List for Scraping & How to Rotate Them Effectively
URL: https://www.scrapingbee.com/blog/list-of-user-agents-for-scraping/  ·  Date: 2026-01-05 (article)  ·  Status: summary

User-Agent strings identify the client to the server; default ones like `python-requests/2.x` are instant bot flags. Provides current Chrome/Firefox/Safari/Edge desktop and mobile UA strings, warns that UA alone is weak — header coherence, Client Hints, TLS fingerprints, and IP reputation all matter — and shows rotation patterns in requests/httpx.

- Keep a small pool (20-80 strings), rotate per request, and refresh monthly.
- A stale UA (e.g., Chrome/88) or mismatched headers stands out more than no spoofing at all.

### Detailed Guide on IP Rotation in Web Scraping: 2026 Updated
URL: https://www.nstproxy.com/blog/web-scraping-ip-rotation  ·  Date: 2026-05-21 (article)  ·  Status: summary

Explains IP rotation — spreading requests across changing IPs via a proxy gateway — and when it's needed: rate limits, geo-targeted data, scalability, and block recovery. Contrasts rotating vs static/sticky proxies, then walks through Python (requests + Retry adapter) and Node.js (axios + https-proxy-agent) setups with delays and error handling.

- Rotation frequency is configurable: per request, per time interval, or via sticky sessions for login flows.
- Residential IPs beat datacenter IPs for trust; avoid free proxy lists for anything real.

### Web Scraping Without Getting Blocked: 2026 Guide
URL: https://www.scrapingbee.com/blog/web-scraping-without-getting-blocked/  ·  Date: 2026-07-15 (article)  ·  Status: summary

The deepest of the anti-block guides: detection is layered (IP/ASN reputation, TLS JA3/JA4, HTTP/2 fingerprints, browser fingerprinting, CDP leaks, behavior), and you must pass every layer at once. Fourteen tactics include proxies, stealth browsers (Camoufox, nodriver), header/UA rotation, rate randomization, backoff, honeypot avoidance, and reverse-engineering the site's internal API.

- CAPTCHAs are a symptom of a bad trust score — fix IP, fingerprint, and pacing first.
- `undetected-chromedriver` is now detectable; current alternatives are nodriver, Camoufox, and curl_cffi for TLS impersonation.

## References

- BeautifulSoup 4 Documentation — https://beautiful-soup-4.readthedocs.io/en/latest/#  ·  Date: unknown  ·  Status: link-only
- Selenium WebDriver Documentation — https://www.selenium.dev/documentation/webdriver/  ·  Date: unknown  ·  Status: link-only
- Python Requests Library Documentation — https://requests.readthedocs.io/en/latest/  ·  Date: unknown  ·  Status: link-only
- Chrome DevTools Documentation — https://developer.chrome.com/docs/devtools/  ·  Date: unknown  ·  Status: link-only
- W3Schools CSS Selectors Reference — https://www.w3schools.com/cssref/css_selectors.php  ·  Date: unknown  ·  Status: link-only
- HTTP Status Codes — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status  ·  Date: unknown  ·  Status: link-only
- RFC 6265 - HTTP State Management Mechanism (Cookies) — https://datatracker.ietf.org/doc/html/rfc6265  ·  Date: unknown  ·  Status: link-only
- Scrapy API Reference — https://docs.scrapy.org/en/latest/topics/api.html  ·  Date: unknown  ·  Status: link-only
- Python Selenium API — https://selenium-python.readthedocs.io/api.html  ·  Date: unknown  ·  Status: link-only
- XPath Syntax Reference — https://www.w3schools.com/xml/xpath_syntax.asp  ·  Date: unknown  ·  Status: link-only

## Quiz Hooks

- Web scraping — automated extraction of data from websites, as opposed to manual copy-paste.
- Static page — HTML is the same for every visitor; fetch + parse is enough.
- Dynamic page — page is assembled at request time, often by JavaScript; needs a browser driver like Selenium.
- CSS selector — pattern that targets elements in the DOM: `#id`, `.class`, `tag`, `[attr='v']`, combinators `A B`, `A > B`, substring operators `^=`, `$=`, `*=`.
- XPath — alternative to CSS selectors; can match visible text and traverse upward, which CSS cannot.
- `requests.get()` — performs an HTTP GET; returns a `Response` whose `.text`/`.content` carry the page.
- `raise_for_status()` — raises `HTTPError` when the response status is 4xx or 5xx.
- User-Agent header — identifies the client; a default `python-requests/...` UA is an instant bot flag.
- `BeautifulSoup(html, "html.parser")` — parses HTML into a navigable tree; `find`, `find_all`, `select`.
- `None` attribute trap — a failed `.find()` returns `None`; calling `.text` on it raises `AttributeError`.
- Selenium — drives a real browser so JavaScript executes; use `find_element(By.*, ...)` and `WebDriverWait`.
- Infinite scroll — loop `window.scrollTo(0, scrollHeight)`, re-read `scrollHeight`, stop when height stops growing.
- Cookie — small key-value the server stores client-side; carries login sessions across requests.
- robots.txt — site policy file telling crawlers which paths are off-limits; check before scraping.
- Deduplication — fingerprint pages (hash, Bloom filter) and normalize URLs so the same content isn't scraped twice.
