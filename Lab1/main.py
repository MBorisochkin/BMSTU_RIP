import sys
import math


def check_coef(index, coef_str):
    """
    Функция проверки коэффициента для его конвертации в формат float

    :param index: Номер параметра
    :param coef_str: Коэффициент в формате string
    :return: True, если коэффициент конверируется в float, иначе — False
    """
    # Провераяем возможность конвертации коэффициента в float
    try:
        coef = float(coef_str)
    except ValueError:
        return False

    # Дополнительная проверка первого коэффициента
    if index == 1 and coef == 0.0:
        return False

    return True


def get_coef(index, promt):
    """
    Функция считывания коэффициента с командной строки или его ввод с клавиатуры

    :param index: Номер параметра
    :param promt: Приглашения для ввода параметра
    :return: Коэффициент биквадратного уравнения в формате float
    """
    # Ввод коэффициента в качестве параметра командной строки
    try:
        coef_str = sys.argv[index]

    # Ввод коэффициента с клавиатуры
    except:
        print(promt)
        coef_str = input()

        # Проверка правильности введённого коэффициента и его повторный ввод при ошибке
        while not check_coef(index, coef_str):
            print("Введён некорректный коэффициент. Пожалуйста, введите новый:")
            coef_str = input()

    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    """
    Функция вычисления корней биквадратного уравнения

    :param a: Коэффициент A в формате float
    :param b: Коэффициент B в формате float
    :param c: Коэффициент C в формате float
    :return: Список корней (list[float])
    """

    result = []
    # Подсчёт дискриминанта
    D = b * b - 4 * a * c
    # Вычисление корней
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
        elif root == 0:
            result.append(0)
    elif D > 0.0:
        sqD = math.sqrt(D)

        root1 = (-b + sqD) / (2.0 * a)
        if root1 == 0:
            result.append(0)
        elif root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))

        root2 = (-b - sqD) / (2.0 * a)
        if root2 == 0:
            result.append(0)
        elif root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))

    return result


def main():
    # Ввод коэффициентов
    a = get_coef(1, "Введите коэффициент A:")
    b = get_coef(2, "Введите коэффициент B:")
    c = get_coef(3, "Введите коэффициент C:")

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Вывод корней
    len_roots = len(roots)

    # Вывод корней
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1:
        print("Один корень: {}".format(roots[0]))
    elif len_roots == 2:
        print("Два корня: {} и {}".format(roots[0], roots[1]))
    elif len_roots == 3:
        print("Три корня: {}, {} и {}".format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print("Четыре корня: {}, {}, {}, {}".format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()