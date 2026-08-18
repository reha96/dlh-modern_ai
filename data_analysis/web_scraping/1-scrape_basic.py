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
    # fetch the page and turn the html into a searchable soup object
    soup = BeautifulSoup(fetch_html(url), 'html.parser')

    # find all quote blocks on the 1st page
    quotes = soup.find_all('div', class_='quote')

    # store one dictionary for each quote
    out = []

    # go through each quote block
    for quote in quotes:
        # collect the text, author, and tags from this quote
        one_quote = {
            # get the quote text
            'text': quote.find('span', class_='text').get_text(strip=True),
            # get the author's name
            'author': quote.find('small', class_='author').get_text(
                strip=True),
            # get the text from each tag link
            'tags': [
                tag.get_text(strip=True)
                for tag in quote.find('div', class_='tags').find_all(
                    'a', class_='tag')
            ]
        }

        # add this quote dictionary to the output list
        out.append(one_quote)

    return out
