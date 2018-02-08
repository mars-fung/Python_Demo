# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/24 10:55
# ====================================


# # 参数不固定的使用方式:  *args 会把多传入的参数变成一个元组形式, **kwargs 会把多传入的参数变成一个dict形式
# def stu_register(name,age,*args):   # *args 会把多传入的参数变成一个元组形式
#     print(name,age,args)
#
# stu_register("Alex",22)
# stu_register("fengjm",30,"IT","mars")
# stu_register("Jack",32,"CN","Python")
#
#
# def stu_register2(name,age,*args,**kwargs): # **kwargs 会把多传入的参数变成一个dict形式
#     print(name,age,args,kwargs)
#
# stu_register2("Alex",22)
# #输出
# #Alex 22 () {}#后面这个{}就是kwargs,只是因为没传值,所以为空
#
# stu_register2("Jack",32,"CN","Python",sex="Male",province="ShanDong")
# #输出
# # Jack 32 ('CN', 'Python') {'province': 'ShanDong', 'sex': 'Male'}
#
#
# # 嵌套函数　
# name = "Alex"
#
# def change_name():
#     name = "Alex2"
#
#     def change_name2():
#         name = "Alex3"
#         print("第3层打印",name)
#
#     change_name2() #调用内层函数
#     print("第2层打印",name)
#
# change_name()
# print("最外层打印",name)


# # 递归函数实际应用案例，二分查找
# data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
#
#
# def binary_search(dataset,find_num):
#     print(dataset)
#
#     if len(dataset) >1:
#         mid = int(len(dataset)/2)
#         if dataset[mid] == find_num:  #find it
#             print("找到数字",dataset[mid])
#         elif dataset[mid] > find_num :# 找的数在mid左面
#             print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
#             return binary_search(dataset[0:mid], find_num)
#         else:# 找的数在mid右面
#             print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
#             return binary_search(dataset[mid+1:],find_num)
#     else:
#         if dataset[0] == find_num:  #find it
#             print("找到数字啦",dataset[0])
#         else:
#             print("没的分了,要找的数字[%s]不在列表里" % find_num)
#
# binary_search(data,66)

# 匿名函数
def calc(n):
    return n**n
print(calc(10))

# 换成匿名函数
calc2 = lambda n:n**n
print(calc2(10))