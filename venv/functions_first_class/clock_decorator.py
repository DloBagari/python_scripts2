import time
import functools


# decorators accepts the same argument of a function which will be decorated
def timer(func):
    def clock(*args):
        started = time.perf_counter()
        result = func(*args)
        finished = time.perf_counter() - started
        func_name = func.__name__
        arguments = ", ".join(repr(arg) for arg in args)
        print("{:0.8f} {}({}) --> {!r}".format(finished, func_name, arguments, result))
        return result
    return clock


@timer
def seconds(sec):
    time.sleep(sec)
    return "slept"


# using functools.wraps to copy the relevant attributes from func to clock
def timer2(func):
    @functools.wraps(func)
    def clock(*args, **kwargs):  # default parameter will not account in kwargs
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter() - start
        func_name = func.__name__
        arguments = []
        if args:
            arguments.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            kws = ["{}={}".format(k, w) for k, w in kwargs.items()]
            arguments.append(", ".join(kws))
        print("{:0.8f} {}({}) --> {!r}".format(finish, func_name, ", ".join(arguments), result))
        return result
    return clock


@timer2
def counts(a, b, c):
    return a**b**c


if __name__ == "__main__":
    seconds(2)
    # decorator does this: seconds = timer(seconds)
    # if we check the name of the seconds function we will get clock
    print(seconds.__name__) # seconds hold a reference to the clock function
    counts(2, 3, c=3)



