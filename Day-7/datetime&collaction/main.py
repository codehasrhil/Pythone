#datetime is used to see the right date and time

import datetime

now  = datetime.datetime.now()
print(now)


today = datetime.date.today()
print(today)


#collections :- module provide speacial data structure and easier data handling 

from collections import Counter

data = [1,2,2,3,3,3]

count = Counter({3:3,2:2,1:1})

print(count)  # so it goign to print like 3:3 and then 2:2 time that how it take less storga to make it


from collections import deque

d = deque([1,2,3])

d.appendleft(0)
print(d)


#functools :- module is used for working with functions

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))

from functools import reduce

nums = [10,2,3,4]

result = reduce(lambda x,y:x+y,nums)
print(result)