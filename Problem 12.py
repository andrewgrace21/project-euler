from sympy import primerange
from sympy import factorint
import itertools
import numpy as np


index = 2
triangle = 3
while True:
    #print(triangle)
    factors = factorint(triangle).values()
    #print(factors)
    total = 1
    for i in factors:
        total *= i+1
    
    if total > 500:
        print(triangle)
        break
    index += 1
    triangle += index