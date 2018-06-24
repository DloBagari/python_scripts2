"""
first class function is:
> it can be assigned to a variable
> it can be passed as parameter to another function
> it can be returned as result of a function
> it can be created in run-time
"""


def power(n):
    return n * n


p = power
print(p(3))
print(list(map(p, [1, 2, 3, 4])))
# sorting a list be the length
list_a = ["ai", "python", "java", "scala", "spark"]
print(sorted(list_a, key=len))  # key=lambda x: len(x)


# reverse a word
def reverse(word):
    return word[::-1]


print(sorted(list_a, key=reverse))

