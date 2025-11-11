import math 

#calculate the circular area and hypotenuse

r=5
area = math.pi * r**2
print(f"The area of circle with radius {r} is {round(area,2)}")
print(f"The hypotenuse of triangle with sides 3 and 4 is {round(math.hypot(3,4),2)}")

#factorial using math module
n=5
print(f"The factorial of {n} is {math.factorial(n)}")

#square root using math module
num=16
print(f"The square root of {num} is {math.sqrt(num)}")

#power using math module
print(f"2 raised to the power 3 is {math.pow(2,3)}")

#rounding using math module
n = 7.8
print(f"{n} rounded down is {math.floor(n)}")
print(f"{n} rounded up is {math.ceil(n)}")

#trigonometric functions using math module
angle = math.pi/2
print(f"Sine of 90 degrees is {math.sin(angle)}")
print(f"Cosine of 90 degrees is {math.cos(angle)}")


#greatest common divisor 
a,b = 48, 18
print(f"The GCD of {a} and {b} is {math.gcd(a,b)}")

#least common multiple
x,y = 4, 5
lcm = abs(x*y) // math.gcd(x,y)
print(f"The LCM of {x} and {y} is {lcm}")





