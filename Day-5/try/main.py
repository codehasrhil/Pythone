#try/except

#syntax

'''
try:
    #code that my cause error
except:
    #code to handle error
    
'''

#ex

try:
    x = int("abc") # invalid converstion
except:
    print("Error occured!")


#

try:
    num = int(input("Enter the number: "))
    print(10/num)
except ValueError:
    print("invalid number!")
except zeroDivisionError:
    print("cannot divide by zero")