#coding:utf-8

from math import pi
from string import Template

format = "PI with three demcials: %.24f"

print format % pi

s = Template("$x ,glorious $x!")
print s.substitute(x = 'slurm')


print '%10.4f' % pi
print '%-10.4f' % pi