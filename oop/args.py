#When a function wants accept any number of nonkeyword arugument, you can use args
#*args is stored as a tuple by default.


def sum(*args):
    total = 0
    for num in args:
        total += num
    
    print("Total: ", total)

sum(1,3,5)
sum(1,3,5,7)