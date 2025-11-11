# name = input("Enter your name: ")
# print("Hello, " + str(len(name)) + "!" + " Welcome to the class.")

a = 10
b = 3.5
c = "5"
d = True

# print(type(a))      
# print(type(b))      
# print(type(c))      
# print(type(d))


# x=y=5
# print('this is x =',x)
# print('this is y =',y)

# x, y, z = 1, 2.5, "Hello"
# print('this is x =',x)
# print('this is y =',y)
# print('this is z =',z)

# print(a==a)

# abc = 5
# ABC = 10
# print(abc)
# print(ABC)
# print(abc==ABC)

# _a = 15
# print(_a)
# __b = 20
# print(__b)


# age = 25
# if age >= 18:
#     print("You are an adult and can vote.")
# else:
#     print("You are a minor and cannot vote.")


# addition of two numbers

# num1 = int(input("Enter first number: ")) # type casting int()
# num2 = int(input("Enter second number: "))
# num3 = input("Enter third number: ")  # by default input() takes string
# result = num1 + num2 + int(num3)  # type casting int()
# print("adding two numbers:", result)


# # list, tuple, set, dictionary

# fruits = ["apple", "banana", "cherry"]  # list
# print(fruits) # this is mutable can be changed
# print(type(fruits))

# coordinates = (10.0, 20.0)  # tuple this is immutable can not be changed
# print(coordinates)
# print(type(coordinates))

# unique_numbers = {1, 2, 3, 4, 5}  # set this is mutable and unordered
# print(unique_numbers)
# print(type(unique_numbers))

# person = {"name": "John", "age": 30}  # dictionary this is mutable and key-value pair
# print(person)
# print(type(person))

#string manipulation
# message = "Hello, World!"
# print(message.upper())        # Convert to uppercase
# print(message.lower())        # Convert to lowercase
# print(message.replace("World", "Python"))  # Replace substring
# print(message.split(", "))    # Split string into a list

# print(message)
# print(message[0])          # Access first character
# print(message[7:12])      # Access substring "World"
# print(len(message))       # Get length of the string
# print(message.index("W"))  # Find index of character 'W'
# print(message[::-1])     # Reverse the string
# print(message*2)   # Repeat the string twice
# print(message[-7:-1])  # Access substring "World" using negative indexing
# print(message+"!!!")  # Concatenate strings


# mam code for list
# #List is mutable - you can update the value
# x = [10,12.55,'Hi',True]
# print(x) #[10,12.55,'Hi',True]
# print(x[0]) #10
# print(x[1:]) #12.55,'Hi',True
# x[1] = 200
# print(x) #[10, 200, 'Hi', True]
# print(x[::-1]) #Reverse order
# print(*x) #without square bracket
# tinylist = [123,'john']
# print(x + tinylist) #print concetenated lists



#tuple code this is immutable - you cannot update the value
# tuple1 = (10,20,'hi',12.45)
# print(tuple1)
# print(tuple1[1:])
# print(tuple1[::-1])
# # tuple1[1] = 200  # This will raise an error because tuples are immutable
# print(*tuple1)




#disctionary code
# # #Dictionary is mutable - you can update the value
# d1 = {'name':'John', 'age':25, 'is_student':True}
# print(d1)
# print(d1['name'])

# d1['age'] = 26  # Update age
# print(d1)

# print(d1.keys())    # Get all keys
# print(d1.values())  # Get all values
# print(d1.items())   # Get all key-value pairs

# # concatination of two dictionaries
# d2 = {'course':'Python', 'grade':'A'}
# d3 = {**d1, **d2}  # Merging two dictionaries
# print(d3)




# #arithmetic operators
# a = 15
# b = 4

# print("Addition:", a + b)          # Addition
# print("Subtraction:", a - b)       # Subtraction
# print("Multiplication:", a * b)    # Multiplication
# print("Division:", a / b)          # Division
# print("Floor Division:", a // b)   # Floor Division
# print("Modulus:", a % b)           # Modulus
# print("Exponentiation:", a ** b)   # Exponentiation



#assignment operators
# x = 10
# print("Initial value:", x)
# x += 5
# print("Value after addition:", x)
# x -= 3
# print("Value after subtraction:", x)
# x *= 2
# print("Value after multiplication:", x)
# x /= 4
# print("Value after division:", x)
# x **= 3
# print("Value after exponentiation:", x)
# x %= 5
# print("Value after modulus:", x)
# x //= 2
# print("Value after floor division:", x)



#conparistion operators
# a = 10
# b = 20

# print("a == b:", a == b)  # Equal to
# print("a != b:", a != b)  # Not equal to
# print("a > b:", a > b)    # Greater than
# print("a < b:", a < b)    # Less than
# print("a >= b:", a >= b)  # Greater than or equal to
# print("a <= b:", a <= b)  # Less than or equal to



# #logical operators
# x = True
# y = False

# print("Logical AND:", x and y)  # Logical AND
# print("Logical OR:", x or y)    # Logical OR
# print("Logical NOT:", not x)    # Logical NOT
# print("Logical NOT:", not y)    # Logical NOT



#identity operators
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print("a is b:", a is b)  # Identity check
# print("a is not b:", a is not b)  # Identity check
# print("a is c:", a is c)  # Identity check


#membership operators
# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)  # Membership check
# print("grape" not in fruits)  # Membership check


#bitwise operators
a = 5  # binary: 0101
b = 3  # binary: 0011

print("Bitwise AND:", a & b)  # Bitwise AND
print("Bitwise OR:", a | b)   # Bitwise OR
print("Bitwise XOR:", a ^ b)  # Bitwise XOR
print("Bitwise NOT:", ~a)     # Bitwise NOT
print("Left Shift:", a << 2)  # Left Shift
print("Right Shift:", a >> 1)  # Right Shift