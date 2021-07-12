"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(set_1: set, set_2: set, set_3: set, symmetric=False) -> set:
    if symmetric is False:
        return set_1.difference(set_2, set_3)
    elif symmetric is True:
        return set_1.symmetric_difference(set_2, set_3)
    else:
        raise TypeError("Значение symmetric должно быть True или False")
