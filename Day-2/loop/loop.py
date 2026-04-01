#loop is used to do reapet task

'''for loop'''

#syntax

'''
for variable in sequence:
 #code

'''

#for i in range(5):  # by defualt start from 0-4 becuse last is 5 so going to 4
#    print(i) #0,1,2,3,4
    

'''

#range()

# range(start,stop,step)

for i in range(5,10):  # by defualt start from 0-4 becuse last is 5 so going to 4
   print(i) #5,6,7,8,9
    
for i in range(1,10,2):  # by defualt start from 0-4 becuse last is 5 so going to 4
    print(i)  # 1,3,5,7,9
    
'''

'''   while loop  '''

#runs untile the condtion is false

#syntax

'''

while condition:
    #code

'''

i = 1

while i<=5:
    print(i)
    i += 1
    
# controal flow statments : break,continue,pass

for i in range(5):
    if i == 3:
       break  # stops loops completely
    print(i)
    
for i in range(5):
    if i == 3:
        continue  # skip the current iteration and move to next loop
    print(i)
    
