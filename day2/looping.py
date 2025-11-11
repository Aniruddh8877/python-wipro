#while loop

#sum of first n natural numbers
n = int(input("Enter a positive integer: "))
i=1
total =0
while i <= n:
    total += i
    i += 1

print('sum of ', n, 'natural numbers is:', total)