"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(n: int):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))
