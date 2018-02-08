# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:46
# ====================================
from day06.training.SchoolMember import SchoolMember


class Teacher(SchoolMember):
    def __init__(self,name,age,course,salary):
        super(Teacher,self).__init__(name,age)
        self.course = course
        self.salary = salary
        self.enroll()


    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" %(self.name,self.course,'s12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' %(self.name,'Oldboy', self.course)
        print(msg)