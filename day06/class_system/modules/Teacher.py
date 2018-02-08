# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:56
# ====================================
from day06.class_system.modules.People import People


class Teacher(People):
    def __init__(self,name,age,teacher_salary):
        super(Teacher,self).__init__(name,age)
        self.teacher_salary = teacher_salary
        self.teacher_class_list = []  # 班级列表

    def teacher_add_class(self, class_name, class_obj):
        self.teacher_calss[class_name] = class_obj

