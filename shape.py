from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractShape(ABC):

    @abstractmethod
    def action_shape_2D(self) -> AbstractShape2D:
        pass

    @abstractmethod
    def action_shape_3D(self) -> AbstractShape3D:
        pass

class RectangleShape(AbstractShape):

    def action_shape_2D(self) -> AbstractShape2D:
        return Rectangle2D()

    def action_shape_3D(self) -> AbstractShape3D:
        return Rectangle3D()

class CircleShape(AbstractShape):

    def action_shape_2D(self) -> AbstractShape2D:
        return Cirle2D()

    def action_shape_3D(self) -> AbstractShape3D:
        return Circle3D()


class AbstractShape2D(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def modify(self):
        pass

class Cirle2D(AbstractShape2D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        r = int(input('Radius R: '))
        return f'Circle(position({x}, {y}), Radius({r}))'

    def delete(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to delete: '))
        del ls[j-1]
        return ls
    
    def modify(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to modify: '))
        ls[j-1] = self.add()
        return ls

class Rectangle2D(AbstractShape2D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        w = int(input('Width W: '))
        h = int(input('Height H: '))
        return f'Rectangle(position({x}, {y}), width({w}), height({h}))'

    def delete(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to delete: '))
        del ls[j-1]
        return ls

    def modify(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to modify: '))
        ls[j-1] = self.add()
        return ls
        
class AbstractShape3D(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def modify(self):
        pass

class Circle3D(AbstractShape3D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        z = int(input('Position Z: '))
        r = int(input('Radius R: '))
        return f'Circle(position({x}, {y}, {z}), Radius({r}))'

    def delete(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to delete: '))
        del ls[j-1]
        return ls

    def modify(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to modify: '))
        ls[j-1] = self.add()
        return ls

class Rectangle3D(AbstractShape3D):
    def add(self):
        x = int(input('Position X: '))
        y = int(input('Position Y: '))
        z = int(input('Position Z: '))
        w = int(input('Width W: '))
        h = int(input('Height H: '))
        l = int(input('Length L: '))
        return f'Circle(position({x}, {y}, {z}), width({w}), height({h}), length({l}))'

    def delete(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to delete: '))
        del ls[j-1]
        return ls

    def modify(self,ls):
        for i in range(len(ls)):
            print(f'({i+1})-{ls[i]}',end='; ')
        print('\n')
        j = int(input('Input number you want to modify: '))
        ls[j-1] = self.add()
        return ls

def print_out2D(ls1,ls2):
    print('2D shape:')
    print('Circle shape(%d):'% len(ls1))
    shape_list(ls1)
    print('\n')
    print('Rectangle shape(%d):'% len(ls2))
    shape_list(ls2)
    print('\n')

def print_out3D(ls1,ls2):
    print('3D shape:')
    print('Circle shape(%d):'% len(ls1))
    shape_list(Cir3D_list)
    print('\n')
    print('Rectangle shape(%d):'% len(ls2))
    shape_list(Rec3D_list)
    print('\n')

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
# 2D shape
        if direction == '2':
            shape_type = input('Which shape? Circle(c), Rectangle(r): ')
# Circle 2D
            if shape_type == 'c':
                action = input('Action? Add(a), Remove(r), Modify(m), Undo(u), Redo(re): ')
                if action == 'a':
                    Cir2D_list.append(CircleShape().action_shape_2D().add())
                    print_out2D(Cir2D_list,Rec2D_list)
                elif action == 'r':
                    Cir2D_list = CircleShape().action_shape_2D().delete(Cir2D_list)
                    print_out2D(Cir2D_list,Rec2D_list)
                elif action == 'm':
                    Cir2D_list = CircleShape().action_shape_2D().modify(Cir2D_list)
                    print_out2D(Cir2D_list,Rec2D_list)

# Rectangle 2D
            elif shape_type == 'r':
                action = input('Action? Add(a), Remove(r), Modify(m), Undo(u), Redo(re): ')
                if action == 'a':
                    Rec2D_list.append(RectangleShape().action_shape_2D().add())
                    print_out2D(Cir2D_list,Rec2D_list)
                elif action == 'r':
                    Rec2D_list = RectangleShape().action_shape_2D().delete(Rec2D_list)
                    print_out2D(Cir2D_list,Rec2D_list)
                elif action == 'm':
                    Rec2D_list = RectangleShape().action_shape_2D().modify(Rec2D_list)
                    print_out2D(Cir2D_list,Rec2D_list)
# 3D shape
        elif direction == '3':
            shape_type = input('Which shape? Circle(c), Rectangle(r): ')
# Circle 3D
            if shape_type == 'c':
                action = input('Action? Add(a), Remove(r), Modify(m), Undo(u), Redo(re): ')
                if action == 'a':
                    Cir3D_list.append(CircleShape().action_shape_3D().add())
                    print_out3D(Cir3D_list,Rec3D_list)
                elif action == 'r':
                    Cir3D_list = CircleShape().action_shape_3D().delete(Cir3D_list)
                    print_out3D(Cir3D_list,Rec3D_list)
                elif action == 'm':
                    Cir3D_list = CircleShape().action_shape_3D().modify(Cir3D_list)
                    print_out3D(Cir3D_list,Rec3D_list)

# Rectangle 3D
            elif shape_type == 'r':
                action = input('Action? Add(a), Remove(r), Modify(m), Undo(u), Redo(re): ')
                if action == 'a':
                    Rec3D_list.append(RectangleShape().action_shape_3D().add())
                    print_out3D(Cir3D_list,Rec3D_list)
                elif action == 'r':
                    Rec3D_list = RectangleShape().action_shape_3D().delete(Rec3D_list)
                    print_out3D(Cir3D_list,Rec3D_list)
                elif action == 'm':
                    Rec3D_list = RectangleShape().action_shape_3D().modify(Rec3D_list)
                    print_out3D(Cir3D_list,Rec3D_list)
