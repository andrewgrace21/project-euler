'''
def primes(num):
    primes = []
    for i in range(2,num):
        check = True
        for p in primes:
            if i%p==0:
                check = False
                break
        if check:
            primes.append(i)
    return primes

print(sum(primes(2000000)))
'''
'''
def primes(num):
    composites = [1]
    primes = []
    while len(list(set(range(1,num)) - set(composites)))>0:
        n = min(list(set(range(1,num)) - set(composites)))
        primes.append(n)
        for i in range(n,num,n):
            composites.append(i)
    return(primes)

print(sum(primes(2000000)))
'''
'''
import numpy as np

def primes(num):
    possible = np.full((num),True)
    possible[0] = False
    primes = np.array([1])
    while any(possible):
        new = primes[-1] + next((i for i,x in enumerate(possible[primes[-1]:]) if x), None) + 1
        primes = np.append(primes,new)
        possible[np.flip(np.arange(new-1,num,new))] = False
        if len(primes)%10000==0:
            print(primes[-1])
    primes = np.delete(primes, 0)
    return primes

print(np.sum(primes(2000000)))
'''  

import sympy

print(sum(list(sympy.primerange(0,2000000))))