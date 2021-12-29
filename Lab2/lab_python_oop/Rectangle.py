from lab_python_oop.Figure import Figure
from lab_python_oop.FigureColor import FigureColor


class Rectangle(Figure):
    """
    Класс "Прямогугольник" (наследуется от класса "Фигура")
    """
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()
        self.fc.color = color_param

    def square(self):
        """Метод вычисления площади прямоугольгика (переопределение соответсвующего метода класса "Фигура")"""
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} площадью {}.".format(Rectangle.get_figure_type(), self.fc.color,
                                                                         self.width, self.height, self.square())
