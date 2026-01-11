#!/usr/bin/env python3
"""
path:   /home/klassiker/.local/share/repos/python/find_primes.py
author: klassiker [mrdotx]
url:    https://github.com/mrdotx/python
date:   2026-01-11T06:59:17+0100
"""

import argparse
import multiprocessing as mp
import time

def chunks(seq, procs):
    """
    calculate chunks by processes
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
        # 0 and 1 are not prime numbers
        if found_prime and number > 1:
            primes.append(number)
    return primes

def main():
    """
    main function
    """

    # create a parser object
    parser = argparse.ArgumentParser(description = "a tool to find primes \
            in a range of numbers")

    # add arguments
    parser.add_argument("-n", "--numbers", action = 'store_true',
                        default = False, dest = "numbers",
                        help = "print prime numbers that were found")

    parser.add_argument("-b", "--begin", type = int, nargs = 1,
                        metavar = "number", dest = "begin",
                        help = "positive number to begin with \
                                [default: 0]")

    parser.add_argument("-e", "--end", type = int, nargs = 1,
                        metavar = "number", dest = "end",
                        help = "positive number to stop at \
                                [default: 99999]")

    parser.add_argument("-p", "--processes", type = int, nargs = 1,
                        metavar = "number", dest = "processes",
                        help = "number of processes to be used per cpu \
                                [default: " + str(mp.cpu_count()) + "]")

    # parse the arguments from standard input
    args = parser.parse_args()

    # set constants depending on arguments
    if args.begin is None:
        begin_number = 0
    else:
        begin_number = args.begin[0]

    if args.end is None:
        end_number = 99999
    else:
        end_number = args.end[0]

    if args.processes is None:
        num_processes = mp.cpu_count() * mp.cpu_count()
    else:
        num_processes = mp.cpu_count() * args.processes[0]

    # begin output
    print('processes               : ' + str(num_processes))
    print('prime numbers between   : ' + str(begin_number) + '-' + str(end_number))

    # store start time
    start = time.time()

    # open process pool
    pool = mp.Pool(num_processes)

    # prove primes
    parts = chunks(range(begin_number, end_number, 1), num_processes)
    results = pool.map(calc_primes, parts)

    # close process pool
    pool.close()

    # time elapsed in seconds
    elapsed = round(time.time() - start, 3)

    # flat results from used processes
    flat_results = sum(results, [])

    # output results
    print('prime numbers found     : ' + str(len(flat_results)))

    if args.numbers is True:
        print('prime numbers           : ' + str(flat_results))

    print('\ntime elapsed in seconds : ' + str(elapsed))

if __name__ == "__main__":
    main()
