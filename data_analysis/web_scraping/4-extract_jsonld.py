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
    # fetch the page and turn the html into a searchable soup object
    soup = BeautifulSoup(fetch_html(url), 'html.parser')

    # find each application/ld+json script
    # use find_all because page has many
    scripts = soup.find_all('script', type='application/ld+json')

    out = []
    for script in scripts:
        # parse script
        # json.loads needs a string so use .get_text()
        payload = json.loads(script.get_text())

        # extract
        if payload.get("@type") == "Quote":
            out.append({
                "text": payload.get("text"),
                # {} is fallback for empty author (return empty dict)
                "author": payload.get("author", {}).get("name"),
                # [] is fallback for empty tags (return empty list)
                "tags": payload.get("keywords", [])
            })

    return out
