def decorator(func):
    def wraffer():
        print("Before the function")
        func()
        print("After the function")
    return wraffer
    
def hello():
    print("Hello")

hello1 = decorator(hello)

hello1()