import getpass
# name = input("请输入你的账号：")
# password = getpass.getpass("请输入你的密码:")
# print("Hello ; %s, 密码是: %s" %(name, password))
#
#
# print('{0},{1},{1}'.format('a', 'b'))
# pwd = getpass.getpass("请输入密码：")
# print(pwd)


## 账号密码的练习
# name = input("账号为：")
# passwd = input("密码是：")
# if name == "fengjm" and passwd == "123":
#     print("测试通过")
# elif name == "fengjm" or passwd == "123":
#     print("账号或密码错误")

# ## 猜年龄练习
# age = 30
# user_input = int(input("请输入猜想的年龄："))
# if age == user_input:
#     print("猜对了")
# elif user_input > age:
#     print("猜大了")
# else:
#     print("猜小了")


# 作业二：编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
#

import pickle
import os
import random
# 初始化用户以及密码
user_dict = {'admin':{'passwd':'admin','flag':'unlock'}}

# 把账号、密码保存到文件中
with open('account.pkl','wb') as f:
    pickle.dump(user_dict, f)


with open('account.pkl','rb') as f:  # 载入用户账户密码信息
    user_dict = pickle.load(f)
    print(user_dict)

exit_flag = False  # 初始化锁定的状态为false
count_lock = 0  # 初始化账号锁定次数为0次
print('**********************************')

while True:
    user = input('请输入账号: ').strip()
    if user == '':continue  # 用户名为空，重新输入
    password = input('请输入密码: ').strip()

    # 判断是否存在输入的账号
    if user_dict.get(user):
    # 判断账号是否锁定，锁定则退出。
        if user_dict[user]["flag"] == "lock":
            print("账号已被锁，请申请解封！")
            break
        if password == user_dict[user]["passwd"]:
            print("欢迎你，登录成功，请进入猜年龄游戏")
            while True:
                guess_choise = input('你要开始玩猜数字游戏么?(选择yes或no): ').strip()

                if guess_choise == 'no':
                    exit_flag = True
                    break
                elif guess_choise == "yes" :
                    print('欢迎登陆Python自动化开发--猜数字系统')
                    print('*******************************************')
                    print('猜数字的范围在1到100之间.')
                    # 设定一个猜的数字
                    real_num = random.randrange(1, 100)
                    retry_count = 0
                    while retry_count < 3:  # 有3次机会猜数字
                        guess_num = input('请输入你猜的数字: ').strip()
                        if guess_num == '': continue
                        if guess_num.isdigit():
                            guess_num = int(guess_num)
                            if guess_num > real_num:
                                print('错误，请输入一个小一点的数字！')
                            elif guess_num < real_num:
                                print('错误，请输入一个大一点的数字！')
                            else:
                                print('恭喜你，猜到你幸运的数字 %s ！！！' % real_num)
                                break
                        else:
                            print('输入的不是数字，请重新输入一个数字')
                            continue

                        retry_count += 1
                    else:
                        print('哦哦，幸运数字是 %s，下次肯定会猜中的哦！' % real_num)
                        print('-------------------------------------')
                else:
                    print("输入不合法，请重新输入，谢谢")
                    continue

        else:
            count_lock += 1  # 密码不正确，统计输错次数
            if (3 - count_lock):
                print('账号或密码错误，还有 %s 次机会尝试登陆！' % (3 - count_lock))
        if count_lock == 3:  # 若锁定次数有3次，就锁定账号
            with open('account.pkl', 'wb') as f:
                user_dict['admin']['flag'] = 'lock'  # 标志账号admin为锁定状态
                user_dict = pickle.dump(user_dict, f)  # 修改后数据写到 account.pkl中
            print('*******************************************')
            print('账号被锁定，请解锁！')
            break
    else:
        print("账号不存在，请重新输入。")
        continue
    if exit_flag:  # 在猜数字游戏中，选择no，则直接退出整个程序
        break

print('Bye bye!')




# # 作业三：多级菜单
# # 三级菜单
# # 可依次选择进入各子菜单
# # 所需新知识点：列表、字典
# city_dict = {'广州': {'天河': ['天河体育馆', '金山大夏'],
#                     '越秀': ['越秀公园', '光孝寺'],
#                     '番禺': ['长隆欢乐世界', '大夫山']},
#              '深圳': {'福田': ['莲花山', '赛格'],
#                     '龙华': ['元山公园', '龙城广场'],
#                     '南山': ['世界之窗', '欢乐谷']},
#              '佛山': {'禅城': ['梁园', '孔庙'],
#                     '南海': ['千灯湖', '南国桃园'],
#                     '顺德': ['清晖园', '西山庙']}}
# # 创建城市索引列表
# city_index = [(index, key) for index, key in enumerate(city_dict)]
# city_index.append((len(city_index), '退出')) # 增加退出选项
# print(city_index)
#
# while True:
#     print('欢迎查询城市信息')
#     print('--------------------------------')
#     for i in city_index:  # 打印城市索引菜单
#       #  print(i)    #打印所有城市的key-value
#         for j in i:
#             print(j, end=' ')
#         print('')
#     get_city = input('请选择查询的索引号：')
#     if not get_city.isdigit():
#         print('请输入一个数字索引号。')
#         continue
#     elif int(get_city) >= len(city_index):
#         print("索引超长了")
#         continue
#     elif int(get_city) == len(city_index)-1:
#         print("Bye Bye!!!")
#         break
#     else:
#         choose_city = city_index[int(get_city)][1]  # 获取选择的城市名称
#         ## 创建 区 的索引列表
#         area_index = [(index, key) for index, key in enumerate(city_dict[choose_city])]
#         area_index.append((len(area_index), '返回'))  # 增加返回上一级菜单选项
#         while True:
#             for i in area_index:
#                 for j in i:
#                     print(j,end=" ")
#                 print("")
#             get_area = input('请选择地区的索引号：')
#             if not get_area.isdigit():
#                 print('请输入一个数字索引号。')
#                 continue
#             elif int(get_area) >= len(area_index):  # 输入索引号大于城市索引号
#                 print('输入的数字太大，请重输入。')
#                 continue
#             elif int(get_area) == len(area_index) - 1:  # 最大的索引号为 上级菜单对应的索引号
#                 print('返回到上一级菜单。')
#                 break
#             else:
#                 choose_area = area_index[int(get_area)][1]  # 获取选择区的名称
#                 print(city_dict[choose_city][choose_area])  # 打印该区的信息
#                 print('--------------------------------')
