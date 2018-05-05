#_*_coding: utf-8_*_

import os
def main():
    print "hello world"

    print "这是Alice\' 的问题。"
    foo(5, 10)
    print '=' * 10
    print '这将直接执行'+os.getcwd()

    counter = 0
    counter += 1

    food = ['苹果', '杏子', '李子', '梨']

    for i in food:
        print '我就是爱吃' +i
    for i in range(10):
        print i
def foo(paraml,secondParam):
    res = paraml + secondParam
    
    if res < 50:
        print '这个'
    elif (res >= 50 ) and((paraml == 42) or (secondParam==24)):
        print '那个'

    else:
        print '恩，，，'
    return res

if __name__ == '__main__':
    main()