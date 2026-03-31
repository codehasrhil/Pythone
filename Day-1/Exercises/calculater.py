

num1 = int(input("Enter the number 1: "))
op = input("Enter the operator(+,-,*,/): ")
num2 = int(input("Enter the second num: "))

if op == "+":
    sum1 = num1 + num2
elif op == "-":
    sum1 = num1 - num2
elif op == "*":
    sum1 = num1*num2
elif op == "/":
    sum1 = num1/num2
else:
    print("Invalid operator")
    


print(f"The ans is of {num1} {op} {num2}: {sum1} ")
