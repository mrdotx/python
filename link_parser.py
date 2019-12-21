#!/usr/bin/env python3
"""
path:       ~/projects/python/link_parser.py
user:       klassiker [mrdotx]
github:     https://github.com/mrdotx/python
date:       2019-12-21 14:46:51
"""

import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

HELP = """link_parser.sh -- script to grab links from websites
  Usage:
    link_parser.py [url]
  Setting:
    [url] = url to grab links from
  Example:
    link_parser.py https://www.youtube.com/user/.../videos"""

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
    print(HELP)
