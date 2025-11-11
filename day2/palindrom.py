#palindrome checker

'''
what is palindrome?
A palindrome is a word, phrase, number, or other sequences of characters 
that reads the same forward
 and backward (ignoring spaces, punctuation, and capitalization).
 Examples of palindromic words
 include "madam", "racecar", and "level". Palindromic

 eg: numbers: 121, 1331, 12321 are also palindromes.
'''


n = int(input("Enter the number:"))
original_number = n
rev =0

while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n = n // 10

if original_number == rev:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")