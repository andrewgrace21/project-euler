a = 1
b = 1
c = 998

while a**2 + b**2 != c**2:
    if b==998:
        a += 1
        b = 1
        c = 1000-a-b
    else:
        c -= 1
        b += 1

print(a,b,c)
print(a*b*c)