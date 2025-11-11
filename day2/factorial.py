#factorial of a number

'''
n=5
fact = 1*2*3*4*5
fact = 120
fact =1

while n>0:
    fact = fact * n
    n = n - 1

print("Factorial is:", fact)

'''


n = int(input("Enter a positive number: "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1

print("Factorial is:", fact)