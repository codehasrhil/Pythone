'''class student:
    def greet(self):
        print("hello student")
        
s1 = student()
s1.greet()
'''

#constracuter

class Student:
    def __init__(self,name,marks):
        print("constructor called")
        self.name = name
        self.marks = marks
        
s1 = Student("Rana",90)
s2 = Student("harshil",100)

print(s1.name)
print(s1.marks)

print(s2.name)
print(s2.marks)