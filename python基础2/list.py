#coding:utf-8


#append：在列表末尾追加新的对象 count:统计元素在列表中出现的次数 extend:在列表末尾一次性追加另一个列表中的多个值



a = [1,2,3]
b = [4,5,6]
a[len(a):] = b
print a