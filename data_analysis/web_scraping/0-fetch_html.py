#!/usr/bin/env python3
"""Write a function that fetches a web page and returns its HTML as text:
"""


import requests


def fetch_html(url, headers=None, timeout=10):
    """url is the page to retrieve

headers is an optional dict of HTTP headers (e.g. {"User-Agent": "..."})

timeout is the number of seconds to wait before aborting

Must raise an exception on any HTTP status >= 400

Only import: import requests

Returns: the full HTML of the response as a string
    """
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text
