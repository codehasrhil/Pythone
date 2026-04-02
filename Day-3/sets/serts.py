#set :- set is a collection of unique elements and its mutable  

# so evray value is unique you cant have same value

my_set = {1,2,3,3,3}  #see there are 3 time  3 but still print 1 time it remove the same value so yes

print(my_set)


#methods

#add elements

s ={1,2}

s.add(3)

print(s)

#add multipale elements

s.update([4,5,6])
print(s)

# remove elements

s.remove(3)

print(s)

# in set pop remove any value

s.pop()

print(s)

