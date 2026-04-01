# match-case  :- cleaner alternative to multiple if-elif

#syntax

'''
match value:
    case pattern1:
        #code
    case pattern2:
        #code
    
    case pattern3:
        #code

'''

day=2


match day:
    case 1:
        print("monday")
    case 2:
        print('tuesday')
    case _:
        print("invalid")