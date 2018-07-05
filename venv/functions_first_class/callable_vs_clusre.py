from collections.abc import Callable


class Average(Callable):
    def __init__(self):
        self.__numbers = []

    def __call__(self, number):
        self.__numbers.append(number)
        return sum(self.__numbers) /len(self.__numbers)


def average2():
    # free variable
    numbers = []

    def get_avg(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    # return reference of get_avg function
    return get_avg

# in average2 we used a list to memorize the given numbers which will take more memory.
# using nonlocal decoration to reduce the amount of used memory, by storing the total and the count for numbers


def average3():
    count = 0
    total = 0

    def get_avg(number):
        # define count and total as nonlocal variables
        nonlocal count, total
        count += 1
        total += number
        return total / count
    return get_avg


if __name__ == "__main__":
    avg1 = Average()
    print(avg1(1))
    print(avg1(6))
    avg2 = average2()
    print(avg2(10))
    print(avg2(17))
    # compile variables
    print(avg2.__code__.co_varnames)
    # free variable: variables that are not bound in local scope
    print(avg2.__code__.co_freevars)
    avg3 = average3()
    print(avg3(4))
    print(avg3(9))
    print(avg3(7))



