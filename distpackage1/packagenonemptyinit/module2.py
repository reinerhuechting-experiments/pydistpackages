def foo():
    print("This is foo() from module2 in packagenonemptyinit.")

def bar():
    print("This is bar() from module2 in packagenonemptyinit.")
    print("Calling a function from module1 in packagenonemptyinit...")
    from . import module1
    module1.foo()