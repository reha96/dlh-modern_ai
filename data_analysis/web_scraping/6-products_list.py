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
Extract the title, price, description, and rating

Returns: a list of product dictionaries
    """
    # mandatory setup
    options = webdriver.ChromeOptions()
    # no visible window
    options.add_argument('--headless')
    # required in restricted environments
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    # load page
    driver.get(url)

    # find all card elements using By
    # every product card has <div class="card thumbnail">...</div>
    # selenium renames bs4's find/find_all to find_element/find_elements
    cards = driver.find_elements(By.CSS_SELECTOR, 'div.thumbnail')

    # similar to task 1
    out = []

    for card in cards:

        # fill dict with title / price / description / rating
        one_product = {

            # css selector packs tag + class into one string (a.title),
            # unlike bs4
            # get_attribute reads a value written in the tag;
            # no get_text in selenium

            'title': card.find_element(By.CSS_SELECTOR,
                                       'a.title').get_attribute('title'),

            # .text reads visible text, bs4's get_text() equivalent
            'price': card.find_element(By.CSS_SELECTOR,
                                       'h4.price').text,


            'description': card.find_element(By.CSS_SELECTOR,
                                             'p.description').text,

            # data-rating is an attribute we turn into number
            'rating': int(card.find_element(
                By.CSS_SELECTOR,
                '.ratings p[data-rating]'
            )).get_attribute('data-rating')
        }

        out.append(one_product)

    return out
