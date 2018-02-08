# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/24 11:15
# ====================================
"""
一、作业要求：详细描述参考
实现增删改查操作：
1、 可进行模糊查询，语法至少支持下面3种:
select name,age from staff_table where age > 22
select * from staff_table where dept = "IT"
select * from staff_table where enroll_date like "2013"
2、 查到的信息，打印后，最后面还要显示查到的条数
3、 可创建新员工纪录，以phone做唯一键，staff_id需自增
4、 可删除指定员工信息纪录，输入员工id，即可删除
5、 可修改员工信息，语法如下:
    UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"
staff_table表数据：
staff_id,name,age,phone,dept,enroll_date
1,Alex Li,22,13651054608,IT,2013-04-01
2,Jack Wang,30,13304320533,HR,2015-05-03
3,Rain Liu,25,1383235322,Sales,2016-04-22
4,Mack Cao,40,1356145343,HR,2009-03-01
注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
"""
'''
思路： 应该做的像一个系统，进入页面后，显示可操作的选项(增加、删除、查询、修改、退出)，
       1、 查询： 可以选择：age、dept、enroll_date 三个选项进行对应的查询，并且显示查询信息和查询的条数
       2、 增加： 遍历进行phone的判断，如不存在，则可以增加，且staff_id自动+1；否则：提示 phone 已存在
       3、 删除： 点击删除后，应显示所有信息，然后输入员工id后，则进行删除
       4、 修改： 选择列名，输入被替换信息，输入替换后的信息
       5、 退出： 点击后，直接打印bye bye！
'''

# 方法定义 ===========================================================

def writerTxt():
    f = open("staff_table.txt",'w+',encoding="utf-8")
    f.writelines("1,Alex Li,22,13651054608,IT,2013-04-01" + '\n')
    f.writelines("2,Jack Wang,30,13304320533,HR,2015-05-03"+ '\n')
    f.writelines("3,Rain Liu,25,1383235322,Sales,2016-04-22"+ '\n')
    f.writelines("4,Mack Cao,40,1356145343,HR,2009-03-01"+ '\n')
    f.close()

def readTxtReList():
    rf = open("staff_table.txt", 'r+', encoding="utf-8")
    list_rf = []
    for r in rf.readlines():
        list_rf.append(r.rstrip("\n"))
    return list_rf

# 只写了age的查询方式，其他选项其实也是一样的
def selectFunction():
    print("欢迎进入查询页面")

    list_rf = readTxtReList()
#    print(list_rf)
    while True:
        print("""
        ***********************
        可选择的条件有：
        1. age
        2. dept
        3. enroll_date
        4. 返回到主页面
        ***********************
        """)
        select_choice = input("请选择编号: ").strip()
        if not select_choice.isdigit():
            print("输入有误")
            continue
        if int(select_choice) == 4 :
            break
        if int(select_choice) == 1 :
            print("进入age页面 ")
            age = input("输入age的数值，显示的结果会大于该数值: ")
            context_list = []
            count = 0
            size = len(list_rf)
            for i in range(size):
                context = list_rf[i]
                if age <= context.split(",")[2]:
                    context_list.append(context)
                    count += 1
            print("超过年龄的总数有: ",count)
            for i  in range(len(context_list)):
                print("人数信息是: %s " %context_list[i])



def addFunction():
    print("欢迎进入添加人员信息页面")
    list_rf = readTxtReList()
    while True:
        pass

def deleteFunction():
     print("欢迎进入删除人员信息页面")

def alterFunction():
    print("欢迎进入修改信息页面")

def exitFunction():
    print("Bye Bye !!!! 期待下次光临")

# # 定义查询的方法
# def selectAll(col,data):


if __name__ == '__main__':

    # 初始化staff_table表数据
    writerTxt()

    # 定义编号与选项的对应关系
    functionDict = {"1": "selectFunction", "2": "addFunction", "3": "deleteFunction", "4": "alterFunction", "5": "exitFunction"}


    while True:
        print('''
            请选择你所需要的功能编号:
            1. 查询
            2. 增加
            3. 删除
            4. 修改
            5. 退出
        ''')
        choice = input("输入序号 >>>>>>>> : ").strip()
        if not choice.isdigit():
            print("输入有误，请重新输入")
        elif int(choice) > 5 or int(choice) < 1:
            print("输入有误，请重新输入")
        elif int(choice) == 5 :
            exitFunction()
            break
        elif int(choice) == 1:
            selectFunction()
        elif int(choice) == 2:
            addFunction()
        elif int(choice) == 3:
            deleteFunction()
        elif int(choice) == 4:
            alterFunction()



