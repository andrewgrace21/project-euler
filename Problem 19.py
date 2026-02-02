day = 1+365
count = 0

def check(num):
    global count
    if num%7 == 0:
        count += 1

for year in range(1,101):
    for month in [31,28,31,30,31,30,31,31,30,31,30,31]:
        #print(day)
        check(day)
        day += month
        if month==28 and year%4==0:
            day += 1

print(count)