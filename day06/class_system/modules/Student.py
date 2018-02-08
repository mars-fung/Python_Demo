# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:24
# ====================================
from day06.class_system.modules.People import People


class Student(People):
    '''学生类，包含姓名，年龄, 继承people类'''
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)
