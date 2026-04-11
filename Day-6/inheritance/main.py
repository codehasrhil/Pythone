class father:
    def skill(self):
        print("Driving")
    
class Son(father):  #skill is taken by father class
    pass

s = Son()
s.skill()



#super : use when parent went to sue its constructor

class parent:
    def __init__(self):
        print("parent constructor")
    
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
    
    
c = child() 