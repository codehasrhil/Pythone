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

