#!/usr/bin/env python3
"""Write a function that scrapes quote data through the API:
(Based on 2-scrape_paginated.py)
"""


import json


fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """base_url is the root URL of the site (e.g. https://quotes.toscrape.com)

Build each API endpoint starting from /api/quotes?page=1.
Use fetch_html() to retrieve each JSON payload.
Extract text, the author's name, and tags from each quote.

Returns: a list of quote dictionaries
    """
    pass
