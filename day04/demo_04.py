# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/24 16:59
# ====================================
user_status = False

# ## 无参数的写法
# def login(func): #把要执行的模块从这里传进来
#
#     def inner():#再定义一层函数
#         _username = "admin" #假装这是DB里存的用户信息
#         _password = "123" #假装这是DB里存的用户信息
#         global user_status
#
#         if user_status == False:
#             username = input("user:")
#             password = input("pasword:")
#
#             if username == _username and password == _password:
#                 print("welcome login....")
#                 user_status = True
#             else:
#                 print("wrong username or password!")
#
#         if user_status == True:
#             func() # 看这里看这里，只要验证通过了，就调用相应功能
#
#     return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数


# 有参数的写法
def login(func): #把要执行的模块从这里传进来

    def inner(*args,**kwargs):#再定义一层函数
        _username = "admin" #假装这是DB里存的用户信息
        _password = "123" #假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能

    return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

@login
def america():
    #login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

@login
def henan(i):
    #login() #执行前加上验证
    print("----河南专区----  ",i)


if __name__ == '__main__':
    america()
    japan()
    henan("3P")