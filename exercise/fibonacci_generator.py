def fibonicci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1


fib = fibonicci_generator(10)
for i in fib:
    print(i)

    