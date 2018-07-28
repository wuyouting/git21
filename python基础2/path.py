#coding:utf-8
import string

dir = '','usr','local','bin'
print '/'.join(dir)
print 'C:'+'\\'.join(dir)
seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq)
print 'That is all forks'.title()
print string.capwords('That is all forks')

print 'this is a dog'.replace('is','has')
print '1+2+3+4+5+6+7+8+9'.split('+')
print '   test   '.strip()
print '*** test !**'.strip( *!)