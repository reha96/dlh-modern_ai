#!/usr/bin/env python3
"""Write a function that scrapes a single product detail page:
(Based on 6-products_list.py)
"""


import time

from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """url is a single product detail page
    (e.g. https://webscraper.io/test-sites/e-commerce/static/product/32)

Start headless Chrome in a 1920 by 1080 window without a sandbox.
Load the page, wait delay seconds, and collect the product details.
Extract the title, price, description, and rating.

Returns: a product dictionary
    """
    # mandatory setup
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    # load page
    driver.get(url)
    # wait X seconds
    time.sleep(delay)

    # find item
    # scope to the product's own caption block, not page-wide headings
    title = driver.find_element(
        # the caption holds the price h4 first, the title h4 second
        'css selector', '.caption h4:nth-of-type(2)').text

    # first h4.price in the page is this product's price
    price = driver.find_element('css selector', 'h4.price').text

    # the full spec sheet sits in the description paragraph
    description = driver.find_element('css selector', 'p.description').text

    # stars are spans (not p, despite the spec text) inside .ratings
    # count them with find_elements + len
    rating = len(driver.find_elements(
        'css selector', '.ratings .ws-icon-star'))

    return {'title': title, 'price': price,
            'description': description, 'rating': rating}
