num1 = float(input('Enter num 1: '))
num2 = float(input('Enter num 2: '))
num3 = float(input('Enter num 3: '))

average = (num1 + num2 + num2) / 3
total = (num1 + num2 + num2)

print('-----Students Performance Report-----')

print('Average Marks: ', average)
print('total Marks: ', total)


if average >= 85 :
  print('Merit Eligible: ', True)
else :
  print('Merit Eligible: ', False)