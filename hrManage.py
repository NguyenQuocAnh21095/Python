class Human:
    def __init__(self, f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name

class Student(Human):

    def __init__(self, f_name, l_name, grade):
        self.grade = grade
        Human.__init__(self, f_name, l_name)

    def __str__(self):
        return 'Student {} {} grade is {}'.format(self.firstname, self.lastname, self.grade)

class Worker(Human):

    def __init__(self, f_name, l_name, week_salary, hours_per_day):
        self.__week_salary = week_salary
        self.__hours_per_day = hours_per_day
        Human.__init__(self, f_name, l_name)

    def money_per_hour(self):
        self.mph = self.__week_salary / self.__hours_per_day / 7
        return self.mph
    def __str__(self):
        return 'Worker {} {} money per hour is {}'.format(self.firstname, self.lastname, self.money_per_hour())

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

#print(student_obj)
def sort_list_asc(a):
    for i in range (len(a)-1):
        for j in range (len(a)-1):
            if a[j].grade > a[j+1].grade:
                a[j], a[j+1] = a[j+1], a[j]
    return a

#print(sort_list_asc(student_obj))

def sort_list_desc(a):
    for i in range (len(a)-1):
        for j in range (len(a)-1):
            if a[j].money_per_hour() < a[j+1].money_per_hour():
                a[j], a[j+1] = a[j+1], a[j]
    return a

worker_obj = []

for i in range(10):
    worker_obj.append(Worker(wor_l[i][0], wor_l[i][1], wor_l[i][2], wor_l[i][3]))

for i in range(10):
    print(worker_obj[i])

print('\n')
worker_obj2 = sort_list_desc(worker_obj)
for i in range(10):
    print(worker_obj2[i])
# abc = Worker(wor_l[0][0], wor_l[0][1], wor_l[0][2], wor_l[0][3])
# print(abc)
# xyz = Student(stu_l[0][0], stu_l[0][1], stu_l[0][2])
# print(xyz)