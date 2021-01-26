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
    def get_input(self):
        pass

    @abstractmethod
    def draw_shape(self):
        pass

class Cirle2D(AbstractShape2D):
    def get_input(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        r = int(input('Radius R: '))
        return x,y,r
    
    def draw_shape(self,x,y,r):
        return f'Circle({x}, {y}, {r})'

class Rectangle2D(AbstractShape2D):
    def get_input(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        w = int(input('Width R: '))
        h = int(input('Hieght H: '))
        return x,y,w,h

    def draw_shape(self,x,y,w,h):
        return f'Rectangle({x}, {y}, {w}, {h})'

class AbstractShape3D(ABC):
    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def draw_shape(self):
        pass

class Circle3D(AbstractShape3D):
    def get_input(self):
        return

    def draw_shape(self):
        return 

class Rectangle3D(AbstractShape3D):
    def get_input(self):
        return

    def draw_shape(self):
        return


def client_code(factory) -> None:

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":

    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())