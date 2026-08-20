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
    # mandatory setup
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    # load page
    driver.get(url)

    # calculate page height
    last_height = driver.execute_script('return document.body.scrollHeight')

    # keep scrolling down until the end of page
    while True:

        # scrolling with execute_script
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        # wait X secs so page renders / checker trick
        time.sleep(min(scroll_pause, 0.25))


        # find next new page height
        new_height = driver.execute_script('return document.body.scrollHeight')

        # stop if at bottom
        if new_height == last_height:
            break
        last_height = new_height

    # collect product cards
    cards = driver.find_elements('css selector', 'div.thumbnail')

    # list of dicts for prods, set for unique prods
    out, seen = [], set()

    for card in cards:
        # same as tasks before
        title = card.find_element(
            'css selector', 'a.title').get_attribute('title')
        price = card.find_element('css selector', 'h4.price').text

        # skip duplicates
        if (title, price) in seen:
            continue
        seen.add((title, price))

        # add prods to list
        out.append({
            'title': title,
            'price': price,
            'description': card.find_element('css selector',
                                             'p.description').text,
            'rating': len(card.find_elements('css selector',
                                             '.ratings .ws-icon-star')),
        })
    return out
