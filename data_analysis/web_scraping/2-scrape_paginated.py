#!/usr/bin/env python3
"""Write a function that scrapes all pages of quotes from
quotes.toscrape.com:
(Based on 1-scrape_basic.py)
"""


import time
from urllib import parse

from bs4 import BeautifulSoup


fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """base_url is the first page URL (e.g. https://quotes.toscrape.com/)

Use fetch_html() and scrape_basic() to collect quotes from every page.
Follow the "Next" link until no next page remains.
Add a delay between requests.

Returns: the full list of quote dictionaries
    """
    # setup for multiple pages
    current_url = base_url
    out = []

    # fetch the base page and turn the html into a searchable soup object
    soup = BeautifulSoup(fetch_html(current_url), 'html.parser')

    # scrape current url, and extend list for avoiding list of list
    out.extend(scrape_basic(current_url))

    # find the next button on the current page
    # use find for the Next button because each page has only one
    next_page = soup.find('li', class_='next')
