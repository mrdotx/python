#!/usr/bin/env python
"""
path:       ~/coding/python/link_parser.py
user:       klassiker [mrdotx]
github:     https://github.com/mrdotx/python
date:       2019-12-02 19:57:45
"""

import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

USAGE = """Usage:
  link_parser.py [url]
Example:
  link_parser.py https://www.youtube.com/user/.../videos
"""

try:
    URL = sys.argv[1]
    URL_PART = urlparse(URL)

    SITE = URL_PART.scheme + "://" + URL_PART.netloc
    SITE_PATH = URL_PART.path

    PAGE = requests.get(str(SITE + SITE_PATH))
    SOUP = BeautifulSoup(PAGE.content, 'html.parser')
    LINK_LIST = SOUP.find_all('a')

    for link in LINK_LIST:
        if 'href' in link.attrs:
            print(str(SITE + link.attrs['href']))
except IndexError:
    print(USAGE)
