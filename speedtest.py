#!/usr/bin/env python3
"""
path:   /home/klassiker/.local/share/repos/python/speedtest.py
author: klassiker [mrdotx]
github: https://github.com/mrdotx/python
date:   2024-04-29T15:09:45+0200
"""

import os
import re
import subprocess
import time
from pathlib import Path

DIR = str(Path.home())
CSV = '/Public/speedtest/speedtest.csv'
HOST = os.uname()[1]

RESPONSE = subprocess.Popen('/usr/bin/speedtest-cli --simple',
                            shell=True, stdout=subprocess.PIPE).stdout.read()

RESPONSE = RESPONSE.decode('utf-8')

PING = re.findall(r'Ping:\s(.*?)\s', RESPONSE, re.MULTILINE)
DOWNLOAD = re.findall(r'Download:\s(.*?)\s', RESPONSE, re.MULTILINE)
UPLOAD = re.findall(r'Upload:\s(.*?)\s', RESPONSE, re.MULTILINE)

PING = PING[0].replace(',', '.')
DOWNLOAD = DOWNLOAD[0].replace(',', '.')
UPLOAD = UPLOAD[0].replace(',', '.')

try:
    F = open(DIR + CSV, 'a+')
    if os.stat(DIR + CSV).st_size == 0:
        F.write(
            'Date,'
            'Time,'
            'Ping (ms),'
            'Download (Mbit/s),'
            'Upload (Mbit/s),'
            'Hostname\n'
        )

    F.write(
        '{},{},{},{},{},{}\n'.format(
            time.strftime('%d.%m.%Y'),
            time.strftime('%H:%M:%S'),
            PING,
            DOWNLOAD,
            UPLOAD,
            HOST,
        )
    )
except ValueError:
    pass
