arr = []

class Call:

    def __init__(self, date, time, dialed_num, duration):
        self.date = date
        self.time = time
        self.dialed_num = dialed_num
        self.duration = duration

    def __str__(self):
        return 'Date: {}\nTime: {}\nDialed number: {}\nDuration: {}\n'\
            .format(self.date,self.time,self.dialed_num,self.duration)

class Gsm:
    def add_history(self,date,time,num,dur):
        self.CallHistory.append(Call(date,time,num,dur))
    def delete_history(self,date,time,num,dur):
        i = 0
        buff = Call(date,time,num,dur)
        for his in self.CallHistory:
            if his == buff:
                del self.CallHistory[i]
                break
            else:
                i +=1

arr.append(Call(C))
arr.append(Call('29/11','3:20','09321',50))
print(arr[0],arr[1])
buff = Call('29/11','3:20','09321',50)
print(arr[0])