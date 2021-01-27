from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractShape(ABC):

    @abstractmethod
    def create_shape_2D(self) -> AbstractShape2D:
        pass

    @abstractmethod
    def create_shape_3D(self) -> AbstractShape3D:
        pass

class RectangleShape(AbstractShape):

    def create_shape_2D(self) -> AbstractShape2D:
        return Rectangle2D()

    def create_shape_3D(self) -> AbstractShape3D:
        return Rectangle3D()

class CircleShape(AbstractShape):

    def create_shape_2D(self) -> AbstractShape2D:
        return Cirle2D()

    def create_shape_3D(self) -> AbstractShape3D:
        return Circle3D()


class AbstractShape2D(ABC):

    @abstractmethod
    def add(self):
        pass

class Cirle2D(AbstractShape2D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        r = int(input('Radius R: '))
        return f'Circle(position({x}, {y}), Radius({r}))'

class Rectangle2D(AbstractShape2D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        w = int(input('Width W: '))
        h = int(input('Height H: '))
        return f'Rectangle(position({x}, {y}), width({w}), height({h}))'


class AbstractShape3D(ABC):
    @abstractmethod
    def add(self):
        pass

class Circle3D(AbstractShape3D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        z = int(input('Position Z: '))
        r = int(input('Radius R: '))
        return f'Circle(position({x}, {y}, {z}), Radius({r}))'

class Rectangle3D(AbstractShape3D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        z = int(input('Position Z: '))
        w = int(input('Width W: '))
        h = int(input('Height H: '))
        l = int(input('Length L: '))
        return f'Circle(position({x}, {y}, {z}), width({w}), height({z}), length({l}))'

def client_code(factory) -> None:

    product_2D = factory.create_shape_2D().add()


def shape_list(shape_l):
    for i in shape_l:
        print(i, end=', ')

if __name__ == "__main__":

    Cir2D_list = []
    Cir3D_list = []
    Rec2D_list = []
    Rec3D_list = []

    while True:
        direction = input('Which direction? 2D(2), 3D(3): ')
        if direction == '2':
            shape_type = input('Which shape? Circle(c), Rectangle(r): ')
            if shape_type == 'c':
                action = input('Action? Add(a), Remove(r), Undo(u), Redo(re): ')
                if action == 'a':
                    Cir2D_list.append(CircleShape().create_shape_2D().add())
                    print('2D shape:')
                    print('Circle shape(%d):'% len(Cir2D_list))
                    shape_list(Cir2D_list)
                    print('\n')

                    print('Rectangle shape(%d):'% len(Rec2D_list))
                    shape_list(Rec2D_list)
                    print('\n')
            elif shape_type == 'r':
                action = input('Action? Add(a), Remove(r), Undo(u), Redo(re): ')
                if action == 'a':
                    Rec2D_list.append(RectangleShape().create_shape_2D().add())
                    print('2D shape:')
                    print('Circle shape(%d):'% len(Cir2D_list))
                    shape_list(Cir2D_list)
                    print('\n')

                    print('Rectangle shape(%d):'% len(Rec2D_list))
                    shape_list(Rec2D_list)
                    print('\n')
        elif direction == '3':
            shape_type = input('Which shape? Circle(c), Rectangle(r): ')
            if shape_type == 'c':
                action = input('Action? Add(a), Remove(r), Undo(u), Redo(re): ')
                if action == 'a':
                    Cir3D_list.append(CircleShape().create_shape_3D().add())
                    print('3D shape:')
                    print('Circle shape(%d):'% len(Cir3D_list))
                    shape_list(Cir3D_list)
                    print('\n')

                    print('Rectangle shape(%d):'% len(Rec3D_list))
                    shape_list(Rec3D_list)
                    print('\n')
            elif shape_type == 'r':
                action = input('Action? Add(a), Remove(r), Undo(u), Redo(re): ')
                if action == 'a':
                    Rec3D_list.append(RectangleShape().create_shape_3D().add())
                    print('3D shape:')
                    print('Circle shape(%d):'% len(Cir3D_list))
                    shape_list(Cir3D_list)
                    print('\n')

                    print('Rectangle shape(%d):'% len(Rec3D_list))
                    shape_list(Rec3D_list)
                    print('\n')

#    client_code(CircleShape())
#    client_code(RectangleShape())
