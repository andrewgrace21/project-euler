prime = [2]

while len(prime) <= 10000:
    check = False
    i = prime[-1] + 1
    while check == False:
        if all(i % p != 0 for p in prime):
            prime.append(i)
            check = True
        else:
            i += 1
    
print(prime[-1])