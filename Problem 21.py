from sympy import divisors

amicable = []
for a in range(1,10000):
    b = sum(divisors(a))-a
    if sum(divisors(b))-b == a and a!=b:
        amicable.append(a)
        
print(amicable)
print(sum(amicable))