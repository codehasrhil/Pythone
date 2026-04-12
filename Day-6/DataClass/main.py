#dataclass is python make it easy to creat class are mainly used to store data
from dataclasses import dataclass

@dataclass
class students:
     name: str
     marks: int

s1 = students("Rana",75)
print(s1)

'''

🔹 What Dataclass Automatically Gives You

When you use @dataclass, Python automatically creates:

__init__() → constructor
__repr__() → print object nicely
__eq__() → compare objects


'''