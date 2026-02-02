import math

target = 1000000
values = math.factorial(10)
digits = []

for i in range(10):
    available = sorted(set(range(0,10)) - set(digits))
    print(available)
    new = int(values/target)
    print(int(values/target))
    print(available[int(values/target)])
    digits.append(available[new-1])
    values = math.factorial(9-i)
    target -= math.factorial(9-i) * new
    print(digits, values, target)

print(''.join(map(str,digits)))