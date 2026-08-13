#!/usr/bin/env python3
"""Write a function that scrapes the first page of quotes from
quotes.toscrape.com:
(Based on 0-fetch_html.py)
"""


from bs4 import BeautifulSoup


fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """url is the Quotes List endpoint (e.g. https://quotes.toscrape.com/)

Use fetch_html() to retrieve the HTML then parse it with BeautifulSoup

Extract for each quote block:
"text": the quote text
"author": the quote's author
"tags": a list of tag strings

You are not allowed to use regular expressions for this task

Imports: from bs4 import BeautifulSoup and
fetch_html = __import__('0-fetch_html').fetch_html

Returns: a list of dicts, e.g.
[{ "text": "...", "author": "...", "tags": [...] }, ...]
    """
    pass
