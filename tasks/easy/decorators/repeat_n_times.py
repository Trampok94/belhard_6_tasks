"""
Написать функцию bang, которая печатает "Boom"
Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


def decorator(n=1):
    def wrapper(func):
        def inner():
            for _ in range(n):
                func()
        return inner
    return wrapper


@decorator(4)
def bang():
    print("Boom")


bang()
