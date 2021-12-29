class FigureColor:
    """
    Класс "Цвет фигуры"
    """

    def __init__(self):
        self._color = None

    @property
    def color(self):
        """Get-аксессор"""
        return self._color

    @color.setter
    def color(self, value):
        """Set-аксессор"""
        self._color = value
