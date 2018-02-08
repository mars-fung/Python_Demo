# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/23 15:58
# ====================================

# # 启动程序后，让用户输入工资，然后打印商品列表
# # 允许用户根据商品编号购买商品
# # 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# # 可随时退出，退出时，打印已购买商品和余额
#
# while True:
#     salay = input('请输入您的工资：')
#     if salay.isdigit():
#         salay = int(salay)
#         break
#     else:
#         print("输入有误")
#
# shopping_car = []
# List = [["iphone", 8000], ["meizu", 4000], ["xiaomi", 3000], ["oppo", 1000]]
# for i in List:
#     print("商品编号: %s  商品名称：%s 价格: %s" %(List.index(i)+1, i[0], i[1]))
#
# while True:
#     list_car = input("请选择需要的商品（q退出）").strip()
#     if list_car == '': continue
#     if list_car == "q":
#         print("购买的所有商品： %s" % shopping_car)
#         break
#
#     if list_car.isdigit():
#         list_car = int(list_car)-1
#         if (salay - int(List[list_car][1]) > 0) :
#             salay = salay - int(List[list_car][1])
#             shopping_car.append(List[list_car])
#             print("商品 %s 添加成功" %(List[list_car][0]))
#             print("******* 剩余余额为 %s *******" %salay)
#         else:
#             print("~~~~~~  钱不够，请及时充值!  ~~~~~~")
#             print("剩余余额为 %s" %salay)


# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
#
# av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
# print(av_catalog["大陆"]["1024"])
#
# print(av_catalog.get("欧美"))  #显示欧美的value
# print(av_catalog.get("欧美").get("www.youporn.com"))
# print(av_catalog.keys())
# print(av_catalog.values())
#
# av_catalog["test"] = "www.baidu.com"
# print(av_catalog)
#
#
# # 循环dict
# #方法1
# print("循环dict---方法1")
# for key in av_catalog:
#     print(key,av_catalog[key])
#
# #方法2
# print("循环dict---方法2")
# for k,v in av_catalog.items(): #会先把dict转成list,数据里大时莫用
#     print(k,v)
#
# #方法3
# print("循环dict---方法3")
# for key in av_catalog:
#     print(key,av_catalog.get(key))

import os
# print(os.getcwd())  #获取当前目录

#  &&&&&&&&&&&&&& 文件处理  &&&&&&&&&&&&&&&&&&&&&
import os

basePath = os.getcwd()
filePath = basePath +"\\"+"test.txt"
print(filePath)
f = open(filePath) #打开文件
first_line = f.readline()
print('first line:',first_line) #读一行
print('我是分隔线'.center(50,'-'))
data = f.read()# 读取剩下的所有内容,文件大时不要用
print(data) #打印文件

f.close() #关闭文件








