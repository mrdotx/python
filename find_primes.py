#!/usr/bin/env python3
"""
path:   /home/klassiker/.local/share/repos/python/find_primes.py
author: klassiker [mrdotx]
github: https://github.com/mrdotx/python
date:   2021-03-20T18:18:12+0100
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
    primes = []

    for number in numbers:
        found_prime = True
        for div_number in range(2, number):
            if number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(number)
    return primes

def main():
    """
    main function
    """
    print('cpu processes      : ' + str(num_processes))
    print('')
    print('primes between     : ' + str(START_NUMBER) + '-' + str(END_NUMBER))

    start = time.time()

    pool = mp.Pool(num_processes)

    parts = chunks(range(START_NUMBER, END_NUMBER, 1), num_processes)
    results = pool.map(calc_primes, parts)
    flat_results = [i for x in results for i in x]

    pool.close()

    end = round(time.time() - start, 3)

    print('primes found       : ' + str(len(flat_results)))
    # print('primes             : ' + str(results))
    print('')
    print('time elasped (sec) : ' + str(end))

if __name__ == "__main__":
    main()
