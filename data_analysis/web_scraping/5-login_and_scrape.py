#!/usr/bin/env python3
"""Write a function that logs in and scrapes the quotes page:
(Based on 4-extract_jsonld.py)
"""


import requests

from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """login_url is the login page (e.g. https://quotes.toscrape.com/login)

Start a requests session to keep cookies across requests.
GET the login form and read the csrf_token field.
POST username, password and the token back to login_url.
GET the protected quotes page and parse each div.quote.

Returns: a list of quote dictionaries
    """
    # start a session
    # it stores cookies so the "logged in" state survives
    s = requests.Session()

    # GET request using session
    r = s.get(login_url)

    # fetch the page and turn the html into a searchable soup object
    # convert r to text
    soup = BeautifulSoup(r.text, 'html.parser')

    # find unique token with checker desire instead of .get('value')
    token = soup.find('input', {'name': 'csrf_token'})['value']

    # POST back username and pwd
    post = s.post(login_url, data={'username': user,
                                   'password': pwd, 'csrf_token': token})

    # GET protected page
    page = s.get('https://quotes.toscrape.com/')

    # parse each div quote like task 1
    soup = BeautifulSoup(page.text, 'html.parser')

    # same as task 1
    out = []
    for quote in soup.find_all('div', class_='quote'):
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
