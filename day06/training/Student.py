# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:46
# ====================================

from day06.training.SchoolMember import SchoolMember

class Student(SchoolMember):
    def __init__(self, name,age,grade,sid):
        super(Student,self).__init__(name,age)
        self.grade = grade
        self.sid = sid
        self.enroll()


    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' %(self.name, self.grade,'Oldboy')
        print(msg)