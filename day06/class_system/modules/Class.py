# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:54
# ====================================

class Class(object):
    '''班级类，包含名称，课程，学生'''
    def __init__(self,class_name,course_obj):
        self.class_name = class_name
        self.class_courese = course_obj
        self.class_student = {}         #学生字典