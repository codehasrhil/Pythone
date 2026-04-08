class AgeError(Exception):
    "Raised when person age is lee than 18"
    pass
try:
    age = int(input("enter the age: "))
    if age < 18:
        raise AgeError
except AgeError:
    print("person is not eligible to vote")
else:
    print("person is eligible to vote")