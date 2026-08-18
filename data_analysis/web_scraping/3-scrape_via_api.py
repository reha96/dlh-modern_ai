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
    # create page counter
    count = 1
    # create API endpoint, remove trailing backslash
    api_url = base_url.rstrip('/') + f"/api/quotes?page={count}"

    out = []

    while api_url:

        # fetch the JSON text
        response_text = fetch_html(api_url)

        # convert JSON text into Python data
        payload = json.loads(response_text)

        # add each quote from this page
        for quote in payload['quotes']:
            out.append({
                'text': quote['text'],
                'author': quote['author']['name'],
                'tags': quote['tags']
            })

        # stop when this is the last page
        if not payload['has_next']:
            break

        # build the next API endpoint
        count += 1
        api_url = base_url.rstrip('/') + f'/api/quotes?page={count}'

    return out
