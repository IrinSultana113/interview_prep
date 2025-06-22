def sum(*args):
    total = 0
    for num in args:
        total += num
    
    print("Total: ", total)

sum(1,3,5)
sum(1,3,5,7)