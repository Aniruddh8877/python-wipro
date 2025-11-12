#basic try and except
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print(result)
except ZeroDivisionError:
     print("cannot divide by zero")

except ValueError:
     print("invalid input")