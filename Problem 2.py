sequence = [1,2]

while sequence[-1] <= 4000000:
  sequence.append(sequence[-1] + sequence[-2])

sum = 0
for i in range(1,len(sequence),3):
  sum += sequence[i]

print(sum)