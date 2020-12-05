from enum import Enum

#battery characteristics (model, hours idle and hours talk)
class Battery:

    def __init__(self, model=None, hours_idle=None, hours_talk=None, type_bat=1):
        self.__model = model
        self.__hours_idle = hours_idle
        self.__hours_talk = hours_talk
        self.__type_bat = type_bat

    def battery_type(self):
        __battyp = BatteryType
        return 'Battery type: %s\n' %__battyp(self.__type_bat)

    def __str__(self):
        return 'Battery information.\nBattery model: {}\nHours idle: {}\nHours talk: {}\n'.format(self.__model,\
            self.__hours_idle, self.__hours_talk) + self.battery_type()

#display characteristics (size and number of colors)
class Display:

    def __init__(self, size=None, nums_color=None):
        self.__size = size
        self.__nums_color = nums_color

    def __str__(self):
        return "Display characteristics.\nDisplay size: {}\nNumbers of color: {}\n".format(self.__size, self.__nums_color)

#Gsm class
class Gsm(Display,Battery):
    
    CallHistory = []

    def __init__(self, model, manufacturer, price=None, owner=None, model_bat=None, hours_idle=None, hours_talk=None, type_bat=1, size=None, nums_color=None):
        self.__model = model
        self.__manufacturer = manufacturer
        self.__price = price
        self.__owner = owner
        Battery.__init__(self, model, hours_idle, hours_talk, type_bat)
        Display.__init__(self, size, nums_color)


    def __str__(self):
        return 'Mobile information.\nModel: {}\nManufacturer: {}\nPrice: {}\nOwner: {}\n'\
            .format(self.__model, self.__manufacturer,self.__price,self.__owner) +'\n' + Battery.__str__(self) + '\n' + Display.__str__(self)

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

#Write a class GSMTest to test the GSM class: 
class GsmTest:
    
    gsm_list = []

#Create an array of few instances of the GSM class
    def create_gsms(self):
        n = int(input('Numbers of gsm:'))
        for i in range (n):
            model = input('Model name of gsm %d:' % i)
            manufacturer = input('Manufacturer of gsm %d:' % i)
            price = input('Price of gsm %d:' % i)
            owner = input('Owner of gsm %d:' % i)

            bat_model = input('Battery name of gsm %d:' % i)
            hours_idle = input('Hours idle of battery of gsm %d:' % i)
            hours_talk = input('Hours talk of battery of gsm %d:' % i)

            bat_type = int(input('Battery type of gsm %d (input 1->3):' % i))
            size = input('Display size of gsm %d:' % i)
            nums_color = input('Numbers of color of gsm %d:' % i)
            self.gsm_list.append(Gsm(model,manufacturer,price,owner,bat_model,hours_idle,hours_talk,bat_type,size,nums_color))
        return self.gsm_list

    def display_gsms(self):
        for i in range(len(self.gsm_list)):
            print('Information of GSM %d\n' % i, self.gsm_list[i])

#Display the information about the GSMs in the array.
 


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


#Write a class GSMCallHistoryTest to test the call history functionality of the GSM class.
class GSMCallHistoryTest:
    calls_list = []
    ins_gsm = None

#Create an instance of the GSM class.
    def create_ins_gsm(self):
        model = input('Model name of gsm: ')
        manufacturer = input('Manufacturer of gsm: ' )
        price = input('Price of gsm: ')
        owner = input('Owner of gsm: ' )

        bat_model = input('Battery name of gsm: ')
        hours_idle = input('Hours idle of battery of gsm: ')
        hours_talk = input('Hours talk of battery of gsm: ')

        bat_type = int(input('Battery type of gsm (type 1->3): '))
        size = input('Display size of gsm: ')
        nums_color = input('Numbers of color of gsm: ')
        self.ins_gsm = Gsm(model,manufacturer,price,owner,bat_model,hours_idle,hours_talk,bat_type,size,nums_color)
        return self.ins_gsm

#Add few calls.
    def add_few_calls(self):
        n = int(input('Number of calls: '))
        for i in range(n):
            print('Information of call %d' % i)
            date = input('Date of call %d:' %i)
            time = input('Time of call %d:' %i)
            dialed_num = input('Dialed number phone %d:' %i)
            duration = int(input('Duration of call in seconds %d:' %i))
            self.ins_gsm.add_history(date, time, dialed_num, duration)
        print(self.ins_gsm.CallHistory.__str__())
        return self.ins_gsm.CallHistory

    # def display_infor_call(self):
    #     for i in range(len(self.calls_list)):
    #         print('Infor of the call %d' %i, self.calls_list[i])




# gsm_list_test = GsmTest()
# gsm_list_test.create_gsms()
# gsm_list_test.display_gsms()
# print(gsm_list_test.gsm_list)

#Display static iphone 4s
# print('Input iphone 4s infor')
# iphone4s = GsmTest()
# iphone4s.create_gsms()
# iphone4s.display_gsms()
xyz = GSMCallHistoryTest()
xyz.create_ins_gsm()
xyz.add_few_calls()

# call_entries.display_infor_call()
# print(a)