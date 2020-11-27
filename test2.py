from enum import Enum
class A():
    __abc = 1
    xyz = 2
    def __init__(self, name, age = None):
        self.BType = BatteryType

    def printB(self):
        print(self.BType.Li_Ion)

    # def __str__()
    def set_abc(self, abc):
        self.__abc = abc

    def print_abc(self):
        print(self.__abc)

class BatteryType(Enum):
    # Li-Ion, NiMH, NiCd
    Li_Ion = "lili"
    NiMH = 2
    NiCd = 3

a = A("Nam")
a.print_abc()
a.set_abc(5)
print(a.print_abc())