#String = A string is a sequence of characters written inside quotes.

name  = "Harshil"
Surname = "Rana"
Towan = "Dholka"

print(f"My name is {name} {Surname}")

print(f"i live in {Towan}")


"""1 - Length = use to get length of string"""

print(len(name))

"""2 - UpperCase = use to make string uppercase"""

print(name.upper())

"""3 - LowerCase = use to make string lowerCase"""

print(name.lower())

"""4 - Strip = use to remove extra space"""

names = " hArshil "

print(names.strip())

"""5 - replace = use to replace the part of string"""

text = "I love BMW"

print(text.replace("BMW","Car"))

"""6 - Join = use to join the to strig"""

words = ["hello","world"]

print("".join(words))

"""7 - split = break the string into list"""

msg = "Time pass ff"

print(msg.split())

"""find = use to find the position of word"""

word = "Hello World"

print(word.find("Hello"))
print(word.find("World"))

"StartWith  = use to check how string start"

url = "https://google.com"
print(url.startswith("https")) # so it give replay on true or false

"EndsWith = use to check the end of strign"

file = "photo.jpg"
print(file.endswith(".jpg"))  # it's work on the same way that give you some true or false

"isgigit = Check the string has the number or not"

age = "ranma"
print(age.isdigit())  # give ans in true or false