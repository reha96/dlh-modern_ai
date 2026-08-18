#!/usr/bin/env python3
"""Write a function that extracts quote data from JSON-LD:
(Based on 3-scrape_via_api.py)
"""


import json

from bs4 import BeautifulSoup


fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """url is the Quotes List endpoint (e.g. https://quotes.toscrape.com/)

Use fetch_html() to retrieve the HTML.
Find each application/ld+json script and parse it with json.loads().
Extract text, the author's name, and tags from Quote objects.

Returns: a list of quote dictionaries
    """
    pass
