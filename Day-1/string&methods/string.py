#string is used to store charcter and values  its immutabel and cannot be changed methods creat new string so you need to store it 

text="Hello world"

print(text)

# string method

# text = text.lower()
#text = text.upper()
#text = text.strip()
text = text.replace("world","Rana")  # first is value that you select to change and second the value that you went

text = text.split()  # use to covert in to list


print(text)

#string formatting

name = "rana"
age = 20

print(f"My name is {name} and i am {age}")  # it's called f-string used to get and print variable

