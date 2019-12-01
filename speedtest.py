#!/usr/bin/env python
"""
path:       ~/coding/python/speedtest.py
user:       klassiker [mrdotx]
github:     https://github.com/mrdotx/python
date:       2019-12-01 22:55:17
"""

import os
import re
import subprocess
import time

from pathlib import Path
HOME = str(Path.home())
CSV = 'speedtest.csv'

RESPONSE = subprocess.Popen('/usr/bin/speedtest-cli --simple --server 4087',
                            shell=True, stdout=subprocess.PIPE).stdout.read()

RESPONSE = RESPONSE.decode('utf-8')

PING = re.findall('Ping:\s(.*?)\s', RESPONSE, re.MULTILINE)
DOWNLOAD = re.findall('Download:\s(.*?)\s', RESPONSE, re.MULTILINE)
UPLOAD = re.findall('Upload:\s(.*?)\s', RESPONSE, re.MULTILINE)

PING = PING[0].replace(',', '.')
DOWNLOAD = DOWNLOAD[0].replace(',', '.')
UPLOAD = UPLOAD[0].replace(',', '.')

try:
    F = open(HOME + "/" + CSV, 'a+')
    if os.stat(HOME + "/" + CSV).st_size == 0:
        F.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
except:
    pass

F.write('{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'),
                                    time.strftime('%H:%M'), PING, DOWNLOAD,
                                    UPLOAD))
