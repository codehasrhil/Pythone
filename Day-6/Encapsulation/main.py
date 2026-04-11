#encapsulation means wrapping data and methods into one unit and restricting direct access to some data
class student:
    def __init__(self):
        self.name = "Rana"

s= student()
print(s.name)  # access allowed

#protected

class studets:
    def __init__(self):
        self._mark = 90
    
s = studets()
print(s._mark)  # you can acces but not recommended


#private : use double underscore
'''
class std:
    def __init__(self):
        self.__salary = 50000

s = std()
print(s.__salary)  # its intire privet so it can not be able to print
'''


# now going to looking for the way to have access of privet data

class std:
    def __init__(self):
        self.__salary = 50000
        
    def get_salary(self):    #using another function
        return self.__salary 

s = std()
print(s.get_salary())


# now going to see setter and getter method

class stud:
    def __init__(self):
        self.__marks = 0

    def set_marks(self,m):
        if m >= 0:
            self .__marks = m
    
    def get_marks(self):
        return self.__marks

s  = stud()
s.set_marks(85)
print(s.get_marks())