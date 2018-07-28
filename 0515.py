#coding:utf-8

def hello(world):
    print "hello",world
hello('world')
def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])

    return result

print fibs(16)
def add(x,y):
    return x+y

param = (1,2)

print add(*param)

params = {'a':'1','b':'2'}

print add(**params)