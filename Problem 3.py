from sympy import primerange

num = 600851475143
primes = list(primerange(1, 10000))
factors = []

while num not in primes:
  i = 0
  while num%primes[i]!=0:
    i += 1
    if i==len(primes)-1:
      print('Not enough primes')
  factors.append(primes[i])
  num /= primes[i]
factors.append(int(num))
print(factors)