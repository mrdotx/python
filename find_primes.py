#!/usr/bin/env python3
"""
path:   /home/klassiker/.local/share/repos/python/find_primes.py
author: klassiker [mrdotx]
github: https://github.com/mrdotx/python
date:   2021-03-21T09:06:24+0100
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
        if found_prime:
            primes.append(number)
    return primes

def main():
    """
    main function
    """

    # create a parser object
    parser = argparse.ArgumentParser(description = "a programm to find \
            primes in a range of numbers")

    # add arguments
    parser.add_argument("-n", "--numbers", action = 'store_true',
                        default = False, dest = "numbers",
                        help = "print prime numbers that were found")

    parser.add_argument("-b", "--begin", type = int, nargs = 1,
                        metavar = "number", dest = "begin",
                        help = "number to begin with \
                                [default: 2]")

    parser.add_argument("-e", "--end", type = int, nargs = 1,
                        metavar = "number", dest = "end",
                        help = "number to stop at \
                                [default: 100000]")

    parser.add_argument("-p", "--processes", type = int, nargs = 1,
                        metavar = "number", dest = "processes",
                        help = "number of processes per cpu to use \
                                [default: 4]")

    # parse the arguments from standard input
    args = parser.parse_args()

    # set constants depending on arguments
    if args.begin is None:
        begin_number = 2
    else:
        begin_number = args.begin[0]

    if args.end is None:
        end_number = 100000
    else:
        end_number = args.end[0]

    if args.processes is None:
        num_processes = mp.cpu_count() * 4
    else:
        num_processes = mp.cpu_count() * args.processes[0]

    # begin output
    print('cpu processes      : ' + str(num_processes))
    print('primes between     : ' + str(begin_number) + '-' + str(end_number))

    # store start time
    start = time.time()

    # open process pool
    pool = mp.Pool(num_processes)

    # prove primes
    parts = chunks(range(begin_number, end_number, 1), num_processes)
    results = pool.map(calc_primes, parts)
    flat_results = sum(results, [])

    # close process pool
    pool.close()

    # time elapsed in seconds
    elapsed = round(time.time() - start, 3)

    # output results
    print('primes found       : ' + str(len(flat_results)))

    if args.numbers is True:
        print('primes             : ' + str(flat_results))

    print('\ntime elapsed (sec) : ' + str(elapsed))

if __name__ == "__main__":
    main()
