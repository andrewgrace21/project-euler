prod = 0
nums = [0,0]
for i in range(1000):
  for j in range(1000):
    if str(i*j)==str(i*j)[::-1]:
      if i*j > prod:
        prod = i*j
        nums = [i,j]
print(prod)
print(nums)