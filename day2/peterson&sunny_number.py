# # peterson number checker
# n = int(input("Enter a number: "))
# temp =n
# sum = 0
# fact = 1
# while n > 0:
#     digit = n % 10
#     while digit > 0:
#         fact *= digit
#         digit -= 1
#     sum += fact
#     n //= 10
# if sum == temp:
#      print(temp, "is a peterson number")
# else:
#      print(temp, "is not a peterson number")


#sunny number checker

n = int(input("Enter a number: "))

m=n+1
i=1

while i*i<=m:
     if i*i==m:
          print(n,' is a sunny number')
          break
     i+=1
else:
     print(n,'is not a sunny number')

