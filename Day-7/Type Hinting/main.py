#typehinting is used to specify the data type of var and function argument and return values

def add(a: int, b:int) -> int:
    return a + b

print(add(2,3))


#LIST TYPE EX

def total(nums:list[int]) -> int:
    return sum(nums)

print(add("2","3"))