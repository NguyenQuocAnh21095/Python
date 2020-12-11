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
        return 'Worker {} {} money per hour is {:.3f}'.format(self.firstname, self.lastname, self.money_per_hour())


# Sort student's grade as ascending
def sort_list_asc(a):
    for i in range (len(a)-1):
        for j in range (len(a)-1):
            if a[j].grade > a[j+1].grade:
                a[j], a[j+1] = a[j+1], a[j]
    return a

#print(sort_list_asc(student_obj))

# Sort worker's money per hour as descending
def sort_list_desc(a):
    for i in range (len(a)-1):
        for j in range (len(a)-1):
            if a[j].money_per_hour() < a[j+1].money_per_hour():
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Sort merge list follow firstname, lastname as ascending
def sort_merge_asc(a):
    for i in range (len(a)-1):
        for j in range (len(a)-1):
            if a[j].firstname.lower() > a[j+1].firstname.lower():
                a[j], a[j+1] = a[j+1], a[j]
            elif a[j].firstname.lower() == a[j+1].firstname.lower():
                if a[j].lastname.lower() > a[j+1].lastname.lower():
                    a[j], a[j+1] = a[j+1], a[j]
    return a

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
# Create object workers
worker_obj = []
for i in range(len(stu_l)):
    worker_obj.append(Worker(wor_l[i][0], wor_l[i][1], wor_l[i][2], wor_l[i][3]))

# Create object students
student_obj = []
for i in range(len(wor_l)):
    student_obj.append(Student(stu_l[i][0], stu_l[i][1], stu_l[i][2]))


print('\nStudent list sort by grade ascending\n')
# Display student after sort
student_obj_sort = sort_list_asc(student_obj)

for i in range(len(student_obj_sort)):
    print(student_obj_sort[i])

print('\nWorker list sort by money per hour descending\n')
# Display worker after sort
worker_obj_sort = sort_list_desc(worker_obj)

for i in range(len(worker_obj_sort)):
    print(worker_obj_sort[i])

# Merge 2 lists
merge_obj = []
for i in range(len(student_obj)):
    merge_obj.append(student_obj[i])
for i in range(len(worker_obj)):
    merge_obj.append(worker_obj[i])

# # Display merge list before sorting
# for i in range(len(merge_obj)):
#     print(merge_obj[i])

print('\nMerge list sort by firstname, lastname ascending\n')
# Display merge list after sorting
merge_obj_sort = sort_merge_asc(merge_obj)

for i in range(len(merge_obj_sort)):
    print(merge_obj_sort[i])

#completed