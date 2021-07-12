"""
Написать функцию get_dict_from_lists, которая принимает 2 значения - 2 списка
одинаковой длины: LIST_1 и LIST_2.

Необходимо, чтобы функция составляла и возвращала словарь, у которого ключи -
элементы LIST_1, а значения - элементы LIST_2
"""
LIST_1 = [str(i) for i in range(20)]
LIST_2 = [i for i in range(20)]


def get_dict_from_lists(l_1: list, l_2: list) -> dict:
    res_dict = {}
    for i in range(len(l_1)):
        res_dict[l_1[i]] = l_2[i]
    return res_dict


print(get_dict_from_lists(LIST_1, LIST_2))
