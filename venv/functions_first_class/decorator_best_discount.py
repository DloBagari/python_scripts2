discounts = []


def discount(func):
    discounts.append(func)


@discount
def option1(order):
    return 20 if order > 10 else 0


@discount
def option2(order):
    return 30 if order > 15 else 0


@discount
def option3(order):
    return 40 if order > 20 else 0


def best_discount(order):
    return max(func(order) for func in discounts)


if __name__ == "__main__":
    print(best_discount(30))

