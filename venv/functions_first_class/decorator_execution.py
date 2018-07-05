"""
decorators are executed once the module is loaded
"""
registration = []


def deco(func):
    print("text from decorator")
    registration.append(func)
    return func


@deco
def func1():
    print("text from func1")


@deco
def func2():
    print("text from func2")


def main():
    print("main method")
    print("registration: ->", registration)
    func1()
    func2()


if __name__ == "__main__":
    main()

