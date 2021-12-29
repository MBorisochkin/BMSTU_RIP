from lab_python_oop.Figure import Figure
from lab_python_oop.FigureColor import FigureColor
import math


class Circle(Figure):
    """
    Класс "Круг" (наследуется от класса "Фигура")
    """
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, radius_param):
        self.radius = radius_param
        self.fc = FigureColor()
        self.fc.color = color_param

    def square(self):
        """Метод вычисления площади круга (переопределение соответсвующего метода класса "Фигура")"""
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} цвета радиусом {} и площадью {}.".format(Circle.get_figure_type(), self.fc.color, self.radius,
                                                               self.square())
