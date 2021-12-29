def print_result(func):
    """
    Декоратор для вывода результата функций

    :param func: Фунция
    :return: Результат функции
    """
    def wrapper(*args):
        result = func(*args)
        print(func.__name__)

        if type(result) == list:
            for value in result:
                print(value)
        elif type(result) == dict:
            for key, value in result.items():
                print("{} = {}".format(key, value))
        else:
            print(result)

        return result

    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
