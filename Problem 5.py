from sympy import primerange

def factor(num):
    primes = list(primerange(1, 10000))
    factors = []

    while num not in primes:
        i = 0
        while num%primes[i]!=0:
            i += 1
            if i==len(primes)-1:
                print('Not enough primes')
        factors.append(primes[i])
        num //= primes[i]
    factors.append(int(num))
    return(factors)


prod = 1
for i in range(2,21):
    factors1 = factor(i)
    factors2 = [1]
    if prod>1:
        factors2 = factor(prod)
    for j in factors1[::-1]:
        if j in factors2:
            factors2.remove(j)
            factors1.remove(j)
    for j in factors1:
        prod *= j
print(prod)