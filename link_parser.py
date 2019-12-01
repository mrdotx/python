#!/usr/bin/env python
"""
path:       ~/coding/python/link_parser.py
user:       klassiker [mrdotx]
github:     https://github.com/mrdotx/python
date:       2019-12-01 22:57:15
"""

# todo: page load

import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

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
