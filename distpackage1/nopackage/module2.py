def foo():
    print("This is foo() from module2 in nopackage.")

def bar():
    print("This is bar() from module2 in nopackage.")
    print("Calling a function from module1 in nopackage...")
    from . import module1
    module1.foo()