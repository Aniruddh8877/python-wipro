#string palindrome


str = input("Enter a string: ")
original_str = str[::-1]
if str == original_str:
    print(f'"{str}" is a palindrome.')
else:
    print(f'"{str}" is not a palindrome.')