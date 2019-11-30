#!/usr/bin/env python
# vim:fileencoding=utf-8:ft=python:foldmethod=marker

# path:       ~/coding/python/link_parser.py
# user:       klassiker [mrdotx]
# github:     https://github.com/mrdotx/python
# date:       2019-11-30 23:35:43

import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = sys.argv[1]
url_part = urlparse(url)

site = url_part.scheme + "://" + url_part.netloc
site_path = url_part.path

page = requests.get(str(site + site_path))
soup = BeautifulSoup(page.content, 'html.parser')
link_list = soup.find_all('a')

for link in link_list:
    if 'href' in link.attrs:
        print(str(site + link.attrs['href']))
