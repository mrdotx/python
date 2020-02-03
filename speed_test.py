#!/usr/bin/env python3
"""
path:       ~/projects/python/speed_test.py
author:     klassiker [mrdotx]
github:     https://github.com/mrdotx/python
date:       2020-02-03T13:23:47+0100
"""

import os
import re
import subprocess
import time
from pathlib import Path

DIR = str(Path.home())
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
    F = open(DIR + "/" + CSV, 'a+')
    if os.stat(DIR + "/" + CSV).st_size == 0:
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
        time.strftime('%H:%M:%S'),
        PING,
        DOWNLOAD,
        UPLOAD
        )
)
