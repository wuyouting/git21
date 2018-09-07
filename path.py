#coding:utf-8
import os
print(os.getcwd())

filePath = '/usr/tt'
#判断文件是否存在
print(os.path.isfile(filePath))

#判断目录是否存在
print(os.path.isdir(filePath))

#使用path模块
print(os.path.exists(filePath))
#使用access模块
print(os.access(filePath, os.F_OK))


def file_exit(filename):
    try:
        with open(filename) as f:
            return True
    except IOError:
            return False
print("-----------------")
print(file_exit(filePath))




