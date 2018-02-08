# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/24 16:12
# ====================================

list = ['html','python','java','ruby','c']

# 遍历方法1
print("方法1： ")
for i in list :
    print("序号%s   值：%s" %(list.index(i)+1,i))


# 遍历方法2
print("方法2： ")
for i in range(len(list)) :
    print("序号%s   值：%s" %(i+1,list[i]))