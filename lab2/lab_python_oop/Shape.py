from abc import ABC
from abc import abstractmethod
from .ShapeColor import ShapeColor


class Shape(ABC):
    def __init__(self, name):
        self.color = ShapeColor()
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def get_name(self):
        return self.name

    def __repr__(self):
        return "{}'Площадь {:.3f} и цвет {}".format(self.get_name(), self.area(), self.color.value)
