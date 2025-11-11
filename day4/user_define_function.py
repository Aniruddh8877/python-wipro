def my_function():
    print("Hello from my_function!")

# my_function()

def add_numbers(a, b):
     print(a + b)

# add_numbers(2,4)


def fun1(fname):
     print('hello '+fname )

l1 = ['ani','sharma','kumar']

# for i in l1:
#      fun1(i)


#default value
def fun2(country = "India"):
     print("I am from "+country)

# fun2("USA")
# fun2()
# fun2("UK")


# return value 
def fun3(x):
     return 5 * x

# print(fun3(3))


# factorial funcion 

# def factorial(n):
#      if n==0 or n==1:
#           return 1
#      else:
#           return n * factorial(n-1)

def factorial(n):
     fact =1
     for i in range(1,n+1):
          fact = fact * i
     return fact


# print(factorial(5))

# dyamic factorial 

# n = int(input("Enter a number to find factorial: "))
# print(f"The factorial of {n} is {factorial(n)}")

# functino to check number is odd or even
even=[]
odd=[]

# def odd_even(n):
#      if n%2==0:
#           even.append(n)
#           return "Even"
#      else:
#           odd.append(n)
#           return "Odd"
     
# number = [12,43,5,4,657,5,74,57,46]

# for n in number:
#     print(f'the {n} is {odd_even(n)}')

# print('even',even,"odd",odd)

# num = int(input("Enter a number to check odd or even: "))
# print(f"The number {num} is {odd_even(num)}")



# education

def count_vowels(s):
     count =0
     vowels = "aeiouAEIOU"
     for char in s:
          if char in vowels:
               count +=1
     print(f"The number of vowels in '{s}' is {count}")

str = 'education'
# count_vowels(str)

# find element_frequency of element in a list

def element_freq(seq):
     """Return a dict mapping each element in seq to its frequency.

     Args:
          seq: an iterable of hashable items

     Returns:
          dict: {item: count}
     """
     freq = {}
     for item in seq:
          freq[item] = freq.get(item, 0) + 1
     return freq

data =[1,2,2,3,3,3,4]
# print("element frequency:",element_freq(data))


# function to check prime number

def is_prime(n):
     if n<=1:
          return False
     for i in range(2,int(n**0.5)+1):
          if n%i==0:
               return False
     return True 


num = int(input("Enter a number to check prime: "))
if is_prime(num):
     print(f"The number {num} is prime")
else:
     print(f"The number {num} is not prime")