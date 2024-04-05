def func1():
    return "First function"

def func2():
    f1 = func1()
    return f1

def func3():
    
    f2 = func2()
    return f2

def main():
    return func3()

message = main()

print(message)