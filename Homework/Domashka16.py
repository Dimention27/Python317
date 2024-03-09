self = [2, 3, 3, 4]


def decorator(func):
    def wrapper(self):
        print('Среднее арифметическое чисел: ', sum(self) / len(self))
        func()

    return wrapper


@decorator
def basic():
    print('Сумма чисел: ', sum(self))
    return sum(self)


basic(self)

