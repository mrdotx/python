#!/usr/bin/env python
"""
path:       ~/coding/python/speed_test.py
user:       klassiker [mrdotx]
github:     https://github.com/mrdotx/python
date:       2019-12-02 15:32:52
"""

import os
import re
import subprocess
import time

from pathlib import Path
HOME = str(Path.home())
CSV = 'speed_test.csv'

RESPONSE = subprocess.Popen('/usr/bin/speedtest-cli --simple --server 4087',
                            shell=True, stdout=subprocess.PIPE).stdout.read()

RESPONSE = RESPONSE.decode('utf-8')

PING = re.findall(r'Ping:\s(.*?)\s', RESPONSE, re.MULTILINE)
DOWNLOAD = re.findall(r'Download:\s(.*?)\s', RESPONSE, re.MULTILINE)
UPLOAD = re.findall(r'Upload:\s(.*?)\s', RESPONSE, re.MULTILINE)

PING = PING[0].replace(',', '.')
DOWNLOAD = DOWNLOAD[0].replace(',', '.')
UPLOAD = UPLOAD[0].replace(',', '.')

try:
    F = open(HOME + "/" + CSV, 'a+')
    if os.stat(HOME + "/" + CSV).st_size == 0:
        F.write(
            'Date,'
            'Time,'
            'Ping (ms),'
            'Download (Mbit/s),'
            'Upload (Mbit/s)\r\n'
        )
except ValueError:
    pass

F.write(
    '{},{},{},{},{}\r\n'.format(
        time.strftime('%d.%m.%Y'),
        time.strftime('%H:%M'),
        PING,
        DOWNLOAD,
        UPLOAD
        )
)
