
#use to read file

file  = open("time.txt",'r')
content = file.read()
print(content)
file.close()

# use to write

file = open('time.txt','w')
file.write("hello Rana!\n")
file.close()


#use append

file = open('time.txt','a')
file.write("New line added.")
file.close()