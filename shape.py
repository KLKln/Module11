class Shape:
    """Shape class"""
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'RED', 'YELLOW']

    def __init__(self, color='BLUE'):
        if color not in self.colors:
            raise InvalidColorError
        self.color = color

    def change_color(self, new_color):
        if new_color not in self.colors:
            raise InvalidColorError
        self.color = new_color

    def __str__(self):
        return str(self.color)


class InvalidColorError(Exception):
    """InvalidColorError is derived class of Excpetion base class"""
    pass


class Rectangle(Shape):   # Base class is Shape
    """Rectangle derived class of Shape base class"""
    def __init__(self, c='RED', l=0, w=0):  # default values
        super().__init__(c)  # calls the base constructor
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def display_color(self):
        return str('Rectangle color ' + self.color)
