#coding:utf-8
from copy import deepcopy
d = {}
d['a'] = 1
d['b'] = 2
print d
a = d.copy()
print a
a['c'] = ['d','e']
print a
a['c'].remove('d')
print a
#深度复制

a = 'absolute'
b = 'blue'
c = 'core'
print a,b,c
e = f = a
print e,f,a
name = raw_input("what is your name?")
if name.endswith("wu"):
    print "Hello wu"
else:
    print "You ting"