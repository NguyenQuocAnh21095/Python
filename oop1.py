from enum import Enum

class MobilePhone:
    
    def __init__(self, model, manufacturer, price, owner):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.owner = owner
    
    class Battery:

        def __init__(self, model, hours_idle, hours_talk):
            self.model = model
            self.hours_idle = hours_idle
            self.hours_talk = hours_talk

        class BatteryType(Enum):
            type1 = 'Li-ion'
            type2 = 'NiMH'
            type3 = 'NiCd'

    class Display:

        def __init__(self, size, nums_color):
            self.size = size
            self.nums_color = nums_color

    class Gsm(Battery, Display):
        pass