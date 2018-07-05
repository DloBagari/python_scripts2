"""
create a decorator to replace a function
"""


# decorator function, its returned value must be callable
def decora(func):
    def replaced_func():
        print("text from replaced function")
    return replaced_func

@decora
def orginal_function():
    print("text from original function")


orginal_function()
