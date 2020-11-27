from enum import Enum


#class GSM holding instances of the classes Battery and Display
class Gsm:

    def __init__(self, model, manufacturer, price=None, owner=None):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.owner = owner

#battery characteristics (model, hours idle and hours talk)
    class Battery:

        def __init__(self, model=None, hours_idle=None, hours_talk=None):
            self.model = model
            self.hours_idle = hours_idle
            self.hours_talk = hours_talk

        def BatteryType(self):
            self.BatType = BatteryTypeList
            return self.BatType(1)

#display characteristics (size and number of colors)    
    class Display:

        def __init__(self, size, nums_color):
            self.size = size
            self.nums_color = nums_color


    def __str__(self):
        return 'Information of device\nModel: {}\nManufacturer: {}\nPrice: {}\nOwner: {}'.format(self.model, self.manufacturer, self.price, self.owner)
#Add an enumeration BatteryType 
class BatteryTypeList(Enum):
    Li_Ion = 1
    NiMH = 2
    NiCd = 3

nokia = Gsm('1260','China')
print(nokia.Battery().BatteryType())
print(nokia)