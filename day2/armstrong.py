#armstrong

'''
number =153

sum =1 cube +5 cube +3 cube

and sum== number
'''

n = int(input('ENter the number to chack armstrong number: '))

temp = n
m = len(str(n))
print(m)
sum = 0
# for(int i=0,i<=n,i++){
while temp > 0:
     digit = temp % 10
     sum += digit ** len(str(n))
     temp //= 10
# }
if n == sum:
     print(n,' is an armstrong number')
else:
     print(n,' is not an armstrong number')

