# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 16:47
# ====================================
from day06.training.Teacher import Teacher
from day06.training.Student import Student


if __name__ == '__main__':
    t1 = Teacher("Alex",22,'Python',20000)
    t2 = Teacher("TengLan",29,'Linux',3000)

    s1 = Student("Qinghua", 24,"Python S12",1483)
    s2 = Student("SanJiang", 26,"Python S12",1484)

    t1.teaching()
    t2.teaching()
    t1.tell()