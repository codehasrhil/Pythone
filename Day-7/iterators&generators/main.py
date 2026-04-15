
#An iterator is an object that lets you go through (loop over) elements one by one.

nums = [10,20,30]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))


#generator is an easier way to creat iterators using yield

def my_gen():
    yield 1
    yield 2
    yield 3
    
    
g = my_gen()


print(next(g))
print(next(g))
print(next(g))


