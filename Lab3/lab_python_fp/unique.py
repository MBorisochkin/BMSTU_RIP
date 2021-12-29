from gen_random import gen_random


class Unique(object):
    """ Итератор для удаления дубликатов"""
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.data = items
        self.index = 0

        # Установка флага ignore_case
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1

                # Проверка флага ignore_case
                if self.ignore_case and current.lower() not in self.used_elements:
                    self.used_elements.add(current.lower())
                    return current
                elif not self.ignore_case and current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

    for value in Unique(data):
        print(value, end=" ")
    print()

    data = list(gen_random(10, 1, 3))

    for value in data:
        print(value, end=" ")
    print()

    for value in Unique(data):
        print(value, end=" ")
    print()

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    for value in Unique(data):
        print(value, end=" ")
    print()

    for value in Unique(data, ignore_case=True):
        print(value, end=" ")
    print()


if __name__ == '__main__':
    main()
