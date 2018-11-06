#!/usr/bin/env python

from __future__ import division
import math
import argparse
import doctest
import sys

def logfactorial(n, k = 0):
    """
    Function should create list of integers from k+1 to n
    for loop goes through values in list, take log of those,
    then add that to counter (count).
    
    Log factorial examples:
    n = 5, k < n:
    >>> logfactorial(5,2)
    n input was: 5
    k input was: 2
    logfactorial answer is: 4.0943445622221
    4.0943445622221
    
    n = k = 5:
    >>> logfactorial(5,5)
    n input was: 5
    k input was: 5
    logfactorial answer is: 0
    0
    
    n = 5, k = 6:
    >>> logfactorial(5,6)
    n input was: 5
    k input was: 6
    logfactorial answer is: 0
    0

    n = 5, no k input
     >>> logfactorial(5)
    n input was: 5
    k input was: 0
    logfactorial answer is: 4.0943445622221
    4.0943445622221
    """
    print("n input:", n)
    print("k input:", k)
    count = 0
    assert type(n) == int, "error message: n needs to be a positive integer"
    assert type(k) == int, "error message: k needs to be a positive integer"
    assert k >= 0, "error message: k needs to be a positive integer"
    for i in range(k+1, n+1):
        count = math.log(i,10) + count
    print("logfactorial answer is:", count)
    return(count)

def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r
    # non-recursive way to calculate factorials

def logChoose(n, k, log=False):
    print("Running n =", n, "| k =", k, "| take log? (True/False) =", log)
    '''
    Log examples:
    n = 150 ,k = 40, log = False
    >>> logChoose(150,40,False)
    Running n = 150 | k = 40 | take log? (True/False) False
    Answer = 4.408904561912225e+36
    4.408904561912225e+36
    
    n = 150 ,k = 40, log = True
    >>> logChoose(150,40,True)
    Running n = 150 | k = 40 | take log? (True/False) = True
    Answer = 36.644330697900145
    36.644330697900145
    '''
    assert type(n) == int, "error message: n needs to be a positive integer"
    assert type(k) == int, "error message: k needs to be a positive integer"
    assert k >= 0, "error message: k needs to be a positive integer"
    nfac = factorial(n)
    dem  = factorial(k) * factorial(n - k)
    if log: 
        x = math.log(nfac / dem, 10)        
    else:
        x = nfac / dem
    print("Answer =", x)
    return x

def docTest():
    print("Running test for script...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("Done with tests.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="integer to calculate log(n!)")
    parser.add_argument("-k", type=int, help="integer to calculate log(n!/k!)")
    parser.add_argument("--test", action="store_true", help="tests the module and quits")
    parser.add_argument("--log", action="store_true", help="takes log of binomial")
    args = parser.parse_args()
    
    if args.test:
        docTest()
    else:
        nval = 0 # assumes all arguments are false, changes values below if not false
        kval = 0
        lval = False

        if args.n:
            nval = args.n

        if args.k:
            kval = args.k 

        if args.log:
            lval = args.log

        logChoose(nval, kval, lval)