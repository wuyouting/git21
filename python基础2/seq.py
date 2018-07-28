#coding:utf-8

tag = '<a href="http://www.python.com"> Python web site</a>'
print tag[9:30]
print "%-1s %s" % (tag[32:-4],'test')
#分片操作需要提供两个索引做为边界，第一个索引的元素包含在分片之内的，而第二个元素则不包含在分片之内

number = [1,2,3,4,5,6,7,8,9]
print number[:]
print number[:3]
print number[::2]
print number[::-2]
print number[::]

y = [4,5,23,7,2,3,9,3]
y.sort()
print y
x = sorted(y)
print x

t1 = ['dd','dus','demo','wuyouting','a']
t1.sort(key=len)

print t1
y.sort(reverse=True)

print y