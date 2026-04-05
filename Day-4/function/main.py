
#syntax

'''
def function_name(parameters)
    #code block
    return value
'''


def greet():
    print("hello Rana")
    
    
greet()
greet()
greet()


#return

def add(a,b):
    return a + b

print(add(2,3))

#parameter vs argumuments

def gree(name):     #parameter
    print("hello",name)
    
gree("harshil")   # argument




# lambda function

sq = lambda x: x*x
print(sq(5))


#args

def number(*args):
    return sum(args)


print(number(1,23,4,4,))