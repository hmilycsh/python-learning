# 题目：暂停一秒输出，并格式化当前时间。


import time, datetime

for i in range(100):
    print(datetime.datetime.now())
    # print(datetime.datetime.now().strtime('%Y-%m-%d %H:%M:%S'))
