#!/usr/bin/env python3
"""
path:   /home/klassiker/.local/share/repos/python/find_primes.py
author: klassiker [mrdotx]
github: https://github.com/mrdotx/python
date:   2021-03-18T10:46:42+0100
"""

import time

START_NUMBER = 0
END_NUMBER = 9999
I_PRIMES = 0

primes = []
start = time.time()

print('primes between        : ' + str(START_NUMBER) + '-' + str(END_NUMBER))

for number in range(START_NUMBER, END_NUMBER, 1):
    FOUND_PRIME = True
    for div_number in range(2, number):
        if number % div_number == 0:
            FOUND_PRIME = False
            break
    if FOUND_PRIME:
        primes.append(number)
        I_PRIMES += 1

end = round(time.time() - start, 2)

print('primes found          : ' + str(I_PRIMES))
# print('primes                : ' + str(primes))
print('\ntime elasped (seconds): ' + str(end))
