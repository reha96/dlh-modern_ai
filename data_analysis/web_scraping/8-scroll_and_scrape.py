#!/usr/bin/env python3
"""Write a function that scrolls and scrapes a JS-rendered page:
(Based on 7-product_detail.py)
"""


import time

from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """url is an infinite-scroll product page
    (e.g. https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops)

Start headless Chrome in a 1920 by 1080 window without a sandbox.
Scroll to the bottom until the page height stops growing.
Collect every product card, skipping duplicate (title, price) pairs.

Returns: a list of unique product dictionaries
    """
    pass
