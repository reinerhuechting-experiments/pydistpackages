def foo():
    print("This is foo() from module2 in package2.")

def bar():
    print("This is bar() from module2 in package2.")
    print("Calling a function from module in package2...")
    from . import module1
    module1.foo()