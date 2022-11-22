def foo():
    print("This is foo() from module2 in my_package_namespace.")

def bar():
    print("This is bar() from module2 in my_package_namespace.")
    print("Calling a function from module1 in my_package_namespace...")
    from . import module1
    module1.foo()