from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс "Фигура"
    """
    @abstractmethod
    def square(self):
        """
        Виртуальный метод для вычисления площади
        """
        pass
