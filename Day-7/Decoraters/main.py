#decorators : in pyhton is a function that add extra behavior to another function without changing its original code


#like puting gam on bread like same 

def greet():
    print("hello world")
    
greet()

def my_decorator(func):
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper
    
@my_decorator
def greet():
    print("hello")
    
greet()    
    