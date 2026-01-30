# Types of number of python :- there are 2 type of numbers in python

"1 int = whole number not decimal"

a = 10
b = 5

print(f"{a},{b}")

"2 float = numbers with the decimal"

price = 99.50
pi = 3.14

print(f"{price},{pi}")


# Basic Arithmetic Operators

print(f"{a} + {b} =",a+b);  # + = addition
print(f"{a} - {b} =",a-b);  # - = subtraction
print(f"{a} * {b} =",a*b);  # * = Multipliccation
print(f"{a} / {b} =",a/b);  # / = Division
 
# Special Operators (very Important)

print(f"{a} // {b} =",a//b); # // give whole number , removes decimal
print(f"{a} %  {b} =",a%b);  # %  use to find the rimainder
print(f"{a} ** {b} =",a**b); # ** use to exponent the power

#Operator Precdence = 1 = () if you put any math inside this bracket it become important so it execute first
#                     2 = ** power is the second one
#                     3 = * , / , // , %  then this all execute in left to right


#Type Conversion

"int = it cuts the value after .(decimal)"

num = int(3.8)
print(num)

"float = add .0 after any value"

n = float(4)
print(n)

"str = use for converting num into text"

s = str(100)
print(s)

#round = make value roundfigure

round = round(3.6)
print(round)

"abs = make value always positive"

ab = abs(-10)
print(ab)

#Power and Square Root

import math

"square root"

mat = math.sqrt(16);
print(mat)

"Power"

pow = math.pow(2,3); # work like 2*2=4*2=8
print(pow) 


"Min & Max"

find = min(3,5,1)
maxfind = max(32,34,35)

print(f"smallest one {find} ,  biggest one {maxfind}")


"Random number - genrate random number"

import random

ran = random.randint(1,6)  # it will genrate number between 1 to 6

print(ran)

"Extra"

# checking the type of number

n = type(10)
print(n)
m = type(20.3)
print(m)
 
 
"Thing to have in mind"

# "10"+5 get error string + num not gone work
# why to make work  int("10") + 5


