#spy numbers
'''
a positive interger is called a spy number if the sum and product 
of its digits are equal. in other words, a number whose sum and product of all digits
are equal is called a spy number.


exapmle:
sum =1+1+2+4=8
product=1*1*2*4=8
so 124 is a spy number
'''

def is_spy_number(n):
    digits = [int(d) for d in str(n)]
    digit_sum = sum(digits)
    digit_product = 1
    for d in digits:
        digit_product *= d
    return digit_sum == digit_product

# test the function

number = int(input("Enter a positive integer to check if it's a spy number: "))
print(is_spy_number(number))