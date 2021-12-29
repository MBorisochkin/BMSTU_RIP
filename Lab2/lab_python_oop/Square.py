from lab_python_oop.Rectangle import Rectangle


class Sqaure(Rectangle):
    """
    Класс "Квадрат" (наследуется от класса "Прямогугольник")
    """
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return "{} {} цвета со стороной {} и площадью {}.".format(Sqaure.get_figure_type(), self.fc.color, self.side,
                                                                  self.square())
