"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(in_str: str) -> dict:
    from collections import Counter
    res = Counter(STR_VAL)
    return dict(res)


print(dict_from_str(STR_VAL))
