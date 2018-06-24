"""
the only thing python does with annotations is storing annotations in __annotations__ attribute
which means the annotations has no meaning for python interpreter. they are just metadata which used by tools
such as IDEs.
"""


def print_line(name: str, age: 'int > 0'= 1) -> str:
    return "%s %s" % (name, age)


print(print_line("Dlo", 28))

# annotations are stored in __annotations__ attribute
print(print_line.__annotations__)

