goods = [{'title': 'Ковёр', 'price': 2000, 'color': 'green'},
         {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
         {'title': 'Рабочий стол', 'price': None, 'color': None},
         {'title': None, 'price': 1000, 'color': 'blue'},
         {'price': 1999, 'color': None},
         {'title': None, 'price': None, 'color': None}
         ]


def field(items, *args):
    """
    Генератор для работы со списками словарей

    :param items: Список словарей
    :param args: Ключи словарей
    :return: Значения полей при одном аргументе или словари при нескольких
    """
    assert len(args) > 0

    # Случай одного аргумента
    if len(args) == 1:
        return (item[args[0]] for item in items if args[0] in item.keys() and item[args[0]] is not None)

    return [{key: value for key, value in item.items() if value is not None}
            for item in items if args <= tuple(item.keys()) and any(v is not None for v in item.values())]


def main():
    for i in field(goods, 'title'):
        print(i)

    print()

    for i in field(goods, 'price', 'color'):
        print(i)

    print()

    for i in field(goods, 'title', 'price', 'color'):
        print(i)


if __name__ == '__main__':
    main()
