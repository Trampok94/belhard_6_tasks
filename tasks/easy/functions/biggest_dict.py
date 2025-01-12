"""
Написать функцию biggest_dict, которая принимает словарь (необязательный аргумент)
и неограниченное количество аргументов вида ключ-значение.

Если был передан словарь, то одна добавляет к нему все аргументы ключ-значение.
Если не был передан словарь, то создает новый из аргументов ключ-значение она составляет
словарь и возвращает словарь
"""


def biggest_dict(in_dict: dict = None, **kwargs) -> dict:
    if in_dict is None:
        in_dict = {k: v for k, v in kwargs}
    else:
        in_dict.update(kwargs)
    return in_dict
