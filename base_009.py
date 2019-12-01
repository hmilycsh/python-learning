# 题目：暂停一秒输出。


import time

myDict = {1: "a", 2: "b"}
for key, value in myDict.items():
    print(key, value)
    time.sleep(1)
