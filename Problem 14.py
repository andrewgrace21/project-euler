high = 0
save = 0

for n in range(1,1000000):
    print(n)
    count = 0
    temp = n
    while temp!=1:
        count += 1
        if temp%2 == 0:
            temp /= 2
        else:
            temp = 3 * temp + 1
    if count > high:
        high, save = count, n

print(save)