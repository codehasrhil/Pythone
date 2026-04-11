#Polymorphism :- it means one function or method can work in diffrent ways

print(len("hello"))
print(len([1,2,3]))



#function

def add(a,b):
    return a + b

print(add(2,3))
print(add("hi","Rana"))


#polymorphism with classes

class animal:
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog bite")
        
class cat(animal):
    def sound(self):
        print("Cat meows")
        
a = animal()
d = dog()
c = cat()

a.sound()
d.sound()
c.sound()