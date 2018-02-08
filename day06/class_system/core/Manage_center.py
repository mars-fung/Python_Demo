# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 17:09
# ====================================
from day06.class_system.core.Manage_school import Manage_school
from day06.class_system.core.Manage_student import Manage_student
from day06.class_system.core.Manage_teacher import Manage_teacher


class Manage_center(object):
    def mainPage(self):
        while True:
            print("""
            ********  欢迎进入学生选课系统  ********
            &&&&&&&&    1. 学生视图    &&&&&&&&
            &&&&&&&&    2. 讲师视图    &&&&&&&&
            &&&&&&&&    3. 学校视图    &&&&&&&&
            &&&&&&&&    4. 退    出    &&&&&&&&
            """)
            user_choice = input("\033[34;0m请输入您要登录的视图 :\033[0m")

            if int(user_choice) == 1 :
                Manage_student()
            elif int(user_choice) == 2:
                Manage_teacher()
            elif int(user_choice) == 3:
                Manage_school()
            elif int(user_choice) == 4:
                print("\033[31;1m  退出系统，期待下次光临 !!! \033[0m")
                break
            else:
                 print("\033[31;1m 输入有误，请重新输入正确编号 \033[0m")

Manage_center().mainPage()
