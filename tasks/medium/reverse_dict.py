"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(dict_1: dict) -> dict:
    res_dict = {v: k for k, v in dict_1.items()}
    return res_dict


print(reverse_dict({1: 2, 3: 4}))
