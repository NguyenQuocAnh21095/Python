class Human:
    def __init__(self, f_name, l_name):
        self.__firstname = f_name
        self.__lastname = l_name

class Student(Human):

    def __init__(self, f_name, l_name, grade):
        self.__grade = grade
        Human.__init__(self, f_name, l_name)

    def __str__(self):
        pass

class Worker(Human):

    def __init__(self, f_name, l_name, week_salary, hours_per_day):
        self.__week_salary = week_salary
        self.__hours_per_day = hours_per_day
        Human.__init__(self, f_name, l_name)

    def money_per_hour(self):
        self.mph = self.__week_salary / self.__week_salary / 7
        return 'Money per hour: ',self.mph

stu_l = [
    ['Anh','Nguyen',10],
    ['Nam','Huynh',8],
    ['Nguyet','Truong',9],
    ['Kiet','Le',5],
    ['Tuyen','Vo',7],
    ['Loan','Dang',6],
    ['Vien','Dao',7],
    ['Tuong','Nguyen',4],
    ['Them','Doan',3],
    ['Cong','Nguyen',4]
]

wor_l = [
    ['Anh','Nguyen', 500, 8],
    ['Nam','Huynh', 600, 9],
    ['Nguyet','Truong',700, 8.5],
    ['Kiet','Le', 800, 10],
    ['Tuyen','Vo', 1500, 12],
    ['Loan','Dang', 600, 7],
    ['Vien','Dao', 500, 7.5],
    ['Tuong','Nguyen', 550, 8],
    ['Them','Doan', 1200, 9.5],
    ['Cong','Nguyen',1300, 10.5]
]

student_obj = []
for i in range(10):
    student_obj.append(Student(stu_l[i][0], stu_l[i][1], stu_l[i][2]))

print(student_obj)