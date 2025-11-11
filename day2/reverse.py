#reverse a number

n = int(input("Enter the number:"))
rev =0


'''
12345>0
digit = n % 10  # 5
rev = rev * 10 + digit  # 5
n = 12345 // 10  # 1234

1234>0
digit = n % 10  # 4
rev = rev * 10 + digit  # 54
n = 1234 // 10  # 123

1234>0
digit = n % 10  # 3
rev = rev * 10 + digit  # 543
n = 123 // 10  # 12

12>0
digit = n % 10  # 2
rev = rev * 10 + digit  # 5432
n = 12// 10  # 1


1>0
digit = n % 10  # 1
rev = rev * 10 + digit  # 54321
n = 1// 10  # 0

'''

while n > 0:
     digit = n % 10
     rev = rev * 10 + digit
     n = n // 10

print("Reversed Number is:", rev)