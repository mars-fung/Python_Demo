# ====================================
# @Project : Python_Demo
# @Author  :  fengjm
# @Time    : 2018/1/25 15:55
# ====================================
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_Path = os.path.join(BASE_DIR,"DB")
# Techer_db =BASE_DIR + r"\DB\techer.txt"
techer_db = os.path.join(DB_Path,"techer")   # 讲师的数据
student_db = os.path.join(DB_Path,"student")   # 学生的数据
school_db = os.path.join(DB_Path,"school")    # 学校的数据

print(techer_db)

