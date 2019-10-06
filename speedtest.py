#!/usr/bin/env python
# vim:fileencoding=utf-8:ft=python:foldmethod=marker

# Path:     ~/coding/python/speedtest.py
# User:     klassiker [mrdotx]
# GitHub:   https://github.com/mrdotx/python

import os
import re
import subprocess
import time

from pathlib import Path
home = str(Path.home())

csv = 'coding/python/speedtest.csv'

response = subprocess.Popen('/usr/bin/speedtest-cli --simple --server 4087', shell=True, stdout=subprocess.PIPE).stdout.read()

response = response.decode('utf-8')

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

try:
    f = open(home + "/" + csv, 'a+')
    if os.stat(home + "/" + csv).st_size == 0:
            f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
except:
    pass

f.write('{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping, download, upload))