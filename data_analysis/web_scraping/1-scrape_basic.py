#!/usr/bin/env python3
"""Write a function that scrapes the first page of quotes from
quotes.toscrape.com:
(Based on 0-fetch_html.py)
"""


from bs4 import BeautifulSoup


fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """url is the Quotes List endpoint (e.g. https://quotes.toscrape.com/)

Use fetch_html() to retrieve the HTML then parse it with BeautifulSoup

Extract for each quote block:
"text": the quote text
"author": the quote's author
"tags": a list of tag strings

You are not allowed to use regular expressions for this task

Returns: a list of dicts, e.g.
[{ "text": "...", "author": "...", "tags": [...] }, ...]
    """
    fetch_html = __import__('0-fetch_html').fetch_html
    soup = BeautifulSoup(fetch_html(url), 'html.parser')
    text = {}
    author = {}
    tags = {}
    # span is the tag name, then find classes
    for i in soup.find_all('span', class_='text'):
        text.update(i)
    for i in soup.find_all('span', class_='author'):
        author.update(i)
    for i in soup.find_all('span', class_='tags'):
        tags.update(i)
