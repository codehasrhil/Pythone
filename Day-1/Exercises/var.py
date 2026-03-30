'''
#ex-1 cerate 3 variables


name =  "harshil"
age = 19
city = 'dholka'

#print(f"My name is {name}, i am {age} years old , i live in {city}")


#ex-2 take user input

uname = input("enter your name: ")
favourtenumber = int(input("Enter your num: "))

print(f"Hello {uname},your luky number is {favourtenumber}")


#ex-3  Take two numbers from user and:
#Add
#Multiply
#Find remainder

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# add the number

sum1 = num1 + num2

#multiply

sum2 = num1*num2

#remainder

sum3 = num1%num2

print(f"This is you add: {sum1}")
print(f"This is you multiply: {sum2}")
print(f"The remainder is: {sum3}")

'''

#ex-4 takee a sentence from user 

sen = input("ENter any sentence: ")

# makeing it uppercase
sen1 = sen.upper()

#replace with "" to _

sen2 = sen.replace(" ", "_")



print(sen1)
print(sen2)
