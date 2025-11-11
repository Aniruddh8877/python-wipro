'''
use a list comprehension to find odd number in a list. the 
list  is input by a sequence of comma-separated numbers.
supose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
then, the output should be:
1,3,5,7,9
'''

# input_numbers=input("Enter a sequence of comma-separated numbers: ")
# number_list = [int(num) for num in input_numbers.split(",")]
# odd_numbers = [str(num) for num in number_list if num % 2 != 0]
# print("Odd numbers:", ",".join(odd_numbers))



'''
write a program that conputes the net amount of a bank account based a transaction log from console input. the transaction
 log from console input. the transaction log format is shown as following:

 d 100
 w 200
 d mean deposit while w mean  

 suppose the following input is supplied to the program:
 d 300
 d 300
 w 200
 d 100
     then, the output should be:
     500
'''

# transactions = []

# while True:
#     action = input("Enter transaction type (d for deposit / w for withdraw) or 'q' to quit: ").lower()
    
#     if action == 'q':
#         break
#     elif action not in ('d', 'w'):
#         print("Invalid choice! Please enter 'd' or 'w'.")
#         continue

#     amount = int(input("Enter amount: "))
#     transactions.append((action, amount))

# # Calculate net amount
# net_amount = 0
# for action, amount in transactions:
#     if action == 'd':
#         net_amount += amount
#     elif action == 'w':
#         net_amount -= amount

# print("\nAll Transactions:", transactions)
# print("Net amount:", net_amount)



'''
a website require the user to input usernam and password to register, 
write a program to check the valiidity of password input by users.
'''

password = input("Enter your password: ")
if len(password) < 6 or len(password) > 12:
    print("Password must be between 6 and 12 characters long.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
elif not any(char in '!@#$%^&*()-_+=' for char in password):
    print("Password must contain at least one special character (!@#$%^&*()-_+=).")
else:
    print("Password is valid.")