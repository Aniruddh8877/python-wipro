'''
a positive integer whose sum of digits of its square is equal to the
number itself is called a __neon number__.
'''

def is_neon_number(n):
    square = n ** 2
    digit_sum = sum(int(d) for d in str(square))
    return digit_sum == n

number = int(input("enter the number"))
print(is_neon_number(number))