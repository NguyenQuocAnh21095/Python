from enum import Enum

class Gsm:
    
    CallHistory = []

    def __init__(self, model, manufacturer, price=None, owner=None):
        self.__model = model
        self.__manufacturer = manufacturer
        self.__price = price
        self.__owner = owner

    def __str__(self):
        return 'Mobile information.\nModel: {}\nManufacturer: {}\nPrice: {}\nOwner: {}\n'\
            .format(self.__model, self.__manufacturer,self.__price,self.__owner)    

#battery characteristics (model, hours idle and hours talk)
    class Battery:

        def __init__(self, model=None, hours_idle=None, hours_talk=None):
            self.__model = model
            self.__hours_idle = hours_idle
            self.__hours_talk = hours_talk

        def battery_type(self, type):
            __battyp = BatteryType
            return 'Battery type: %s' %__battyp(type)
        
        def __str__(self):
            return 'Battery information.\nBattery model: {}\nHours idle: {}\nHours talk: {}\n'.format(self.__model,\
                self.__hours_idle, self.__hours_talk)

#display characteristics (size and number of colors)
    class Display:

        def __init__(self, size=None, nums_color=None):
            self.__size = size
            self.__nums_color = nums_color

        def __str__(self):
            return "Display characteristics.\nDisplay size {}\nNumbers of color: {}\n".format(self.__size, self.__nums_color)

#add history        
    def add_history(self,date,time,num,dur):
        self.CallHistory.append(Call(date,time,num,dur))

#delete history
    def delete_history(self,position):
        del self.CallHistory[position]

#clear history
    def clear_history(self):
        n = len(self.CallHistory)
        del self.CallHistory[0:n]

#Caculate total price, prices per min = ppm
    def total_price(self, ppm):
        price = 0
        for his in self.CallHistory:
            price = price + his.duration/60*ppm
        return price

#Add an enumeration BatteryType (Li-Ion, NiMH, NiCd, …)
class BatteryType(Enum):
            Li_Ion = 1
            NiMH = 2
            NiCd = 3

class GsmTest:
    
    def __init__(self, *gsms):
        self.list_gsms = list(gsms)

    def gsm_list(self):
        return self.list_gsms

#Create a class Call to hold a call performed through a GSM
class Call:

    def __init__(self, date, time, dialed_num, duration):
        self.date = date
        self.time = time
        self.dialed_num = dialed_num
        self.duration = duration

    def __str__(self):
        return 'Date: {}\nTime: {}\nDialed number: {}\nDuration: {}\n'\
            .format(self.date,self.time,self.dialed_num,self.duration)

nokia = Gsm('1250','China')
nokia.Battery('5000mAh')
nokia.add_history('26/11','3:20','09321',50)
nokia.add_history('27/11','3:20','09321',50)
nokia.add_history('28/11','3:20','09321',50)
nokia.add_history('29/11','3:20','09321',50)
# nokia.delete_history(0)
pr = nokia.total_price(3)
print(pr)
# print(nokia.CallHistory[0].duration)
# for entry in nokia.CallHistory:
#     print(entry)
# print(len(nokia.CallHistory))
# gsmlist = GsmTest('nokia','samsung','iphone')
# print(gsmlist.gsm_list())
# print(nokia.Display('5000mAh'))