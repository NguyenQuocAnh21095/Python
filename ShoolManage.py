class School:
    
    def __init__(self, nums_class):
        self.__nums_class = nums_class

    def __str__(self):
        return 'School has {} class(es)'.format(self.__nums_class)

class Aclass:
    
    def __init__(self, nums_teacher):
        self.__nums_teacher = nums_teacher

    def __str__(self):
        return 'Class has {} teacher(s)'.format(self.__nums_teacher)

class People:
    
    def __init__(self, name):
        self.__name = name

class Teacher(People):
    
    def __init__(self,name, nums_discip):
        People.__init__(self,name)
        self.__nums_discip = nums_discip
       
    def __str__(self):
        return 'Teacher {} teach {} discipline(s)'.format(self.__name, self.__nums_discip)

class Student(People):
    
    def __init__(self,name, class_id):
        People.__init__(self,name)
        self.__class_id = class_id

    def __str__(self):
        return 'Student {} are in class {}'.format(self.__name, self.__class_id)

class Discipline:

    def __init__(self, name, nums_lecture, nums_exercise):
        self.__name = name
        self.__nums_lecture = nums_lecture
        self.__nums_exercise = nums_exercise


