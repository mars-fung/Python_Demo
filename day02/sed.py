# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/24 9:44
# ====================================


# 程序1: 实现简单的shell sed替换功能
#
# 　　file1 的内容copy到file2
#
# 　　输入参数./sed.py  $1  $2
#
# 　　　　$1替换成$2 （把a替换成% ）

import os

# basePath = os.getcwd()
# filePath = basePath + "\\" + "test.txt"
# new_filePath = basePath + "\\" + "test2.txt"

f_old = open('test.txt', 'r', encoding='utf-8')
f_new = open('test2.txt', 'w', encoding='utf-8')
txt = input("请输入需要替换的内容: ")
new_txt = input("请输入替换后的内容: ")
for i in f_old.readlines():
    print(i)
    k = i.replace(txt,new_txt)
    print(k)
    f_new.writelines(k)
f_old.close()
f_new.close()