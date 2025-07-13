def mydev(func):
    def wrapper(a,b):
        if a<b:
            a,b = b,a
            func(a,b)
    return wrapper

#@mydev
def div(a,b):
    print( a / b )   

div1 = mydev(div)
div1(2,4)
# def task_print():
#     print('printigngnngn machine')

# def out_function():
#     def ritu_the_girl(a):
#         print("fucntion calling from ritu ",a)
#         return task_print
#     return ritu_the_girl

# a=out_function()
# b=a("insdie")
# b()