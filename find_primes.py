#!/usr/bin/env python3
"""
path:   /home/klassiker/.local/share/repos/python/find_primes.py
author: klassiker [mrdotx]
github: https://github.com/mrdotx/python
date:   2021-03-18T15:47:06+0100
"""

import sys
import multiprocessing as mp
import time

ARGS_NUMBER = len(sys.argv)
# 0 and 1 are not prime numbers
START_NUMBER = 2
END_NUMBER = 100000

if ARGS_NUMBER == 2:
    END_NUMBER = int(sys.argv[1])
elif ARGS_NUMBER == 3:
    START_NUMBER = int(sys.argv[1])
    END_NUMBER = int(sys.argv[2])

num_processes = mp.cpu_count() * 4

def chunks(seq, procs):
    """
    calculate chunks
    """
    size = len(seq)
    start = 0
    for i in range(1, procs + 1):
        stop = i * size // procs
        yield seq[start:stop]
        start = stop

def calc_primes(numbers):
    """
    prove that a number is a prime number
    """
    num_primes = 0
    primes = []

    for number in numbers:
        found_prime = True
        for div_number in range(2, number):
            if number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(number)
            num_primes += 1
    return num_primes

def main():
    """
    main function
    """
    print('cpu processes      : ' + str(num_processes))
    print('primes between     : ' + str(START_NUMBER) + '-' + str(END_NUMBER))

    start = time.time()

    pool = mp.Pool(num_processes)

    parts = chunks(range(START_NUMBER, END_NUMBER, 1), num_processes)
    results = pool.map(calc_primes, parts)
    total_primes = sum(results)

    pool.close()

    end = round(time.time() - start, 3)

    print('primes found       : ' + str(total_primes))
    print('time elasped (sec) : ' + str(end))

if __name__ == "__main__":
    main()
