#!/usr/bin/env python3
"""Write a function that scrapes a static product page with Selenium:
(Based on 5-login_and_scrape.py)
"""


import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_products_list(url):
    """url is a static product category page
    (e.g. https://webscraper.io/test-sites/e-commerce/static/computers/laptops)

Start headless Chrome in a 1920 by 1080 window without a sandbox.
Load the page and collect every product card.
Extract the title, price, description, and rating from each card.

Returns: a list of product dictionaries
    """
    pass
