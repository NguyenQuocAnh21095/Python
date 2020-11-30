class Batterty():
    def __init__(self, Binfo):
        self.Binfo = Binfo

    def __str__(self):
        return f"battery info: {self.Binfo} "

class Display():
    def __init__(self, Dinfo):
            self.Dinfo = Dinfo

    def __str__(self):
        return f"display info: {self.Dinfo} "

class GSM(Batterty, Display):
    def __init__(self, GMSname, Binfo, Dinfo):
        self.GMSname = GMSname
        Batterty.__init__(self, Binfo)
        Display.__init__(self, Dinfo)

    def __str__(self):
    #     # return f"GSM info: {self.nameg} " + Batterty.__str__(self) + Display.__str__(self)
        return f"GSM info: {self.GMSname} " + " ".join(map(str, [parent.__str__(self) for parent in GSM.__bases__]))   
    #     for parent in GSM.__bases__(self):
    #         print(parent)


item_array = {
    "iphone": ["7S", "Lion", "5.5"],
    "android": ["Note7", "ABC", "6"]
}

GSM_instances = []

for item in item_array:
    x = GSM(item_array[item][0],item_array[item][1], item_array[item][2])
    GSM_instances.append(x)

for item in GSM_instances:
    print(item)