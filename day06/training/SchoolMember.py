# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:45
# ====================================

class SchoolMember(object):
    members = 0 #初始学校人数为0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def  tell(self):
        pass

    def enroll(self):
        '''注册'''
        SchoolMember.members +=1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " %(self.name,SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" %self.name)




