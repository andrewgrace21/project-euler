from sympy import divisors

abundant = []
check = [False] *28124
for n in range(1,28124):
    if sum(divisors(n))-n > n:
        abundant.append(n)

for i in range(0,len(abundant)):
    for j in range(i,len(abundant)):
        if abundant[i]+abundant[j] < 28124:
            check[abundant[i]+abundant[j]-1] = True

check = [i+1 for i,x in enumerate(check) if x]
print(sum(range(1,28124)) - sum(check))