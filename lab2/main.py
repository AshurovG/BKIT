from lab_python_oop import Circle
from lab_python_oop import Square
from lab_python_oop import Rectangle
import cowsay

if __name__ == "__main__":

    a = Rectangle.Rectangle(6, 6, 'Синий', 'Прямоугольник')
    b = Circle.Circle(6, 'Зеленый', 'Круг')
    c = Square.Square(6, 'Красный', 'Квадрат')

    cowsay.trex(str(a)+'\n'+str(b)+'\n'+str(c))
