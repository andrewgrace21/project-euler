from num2words import num2words

print(sum([len(num2words(digit).replace(' ','').replace('-','')) for digit in range(1,1001)]))
print(num2words(115).replace(' ','').replace('-',''))