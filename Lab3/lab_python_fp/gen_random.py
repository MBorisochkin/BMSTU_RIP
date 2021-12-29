from random import randint


def gen_random(quantity, min_value, max_value):
    """
    Генератор посдледовательности случайных чисел

    :param quantity: Длина последовательности
    :param min_value: Минимальное значение числа в последовательности
    :param max_value: Максимальное значение числа в последовательности
    :return: Последовательность случайных чисел
    """
    return (randint(min_value, max_value) for _ in range(quantity))


def main():
    for i in gen_random(10, 0, 9):
        print(i, end=" ")


if __name__ == '__main__':
    main()
