#coding:utf-8


sentence = raw_input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print "Sentence:%s"%sentence

print ' '*left_margin+'+'+'-'*(box_width-4)+'+'
print ' '*left_margin+'|'+' '*text_width   +'  |'
print ' '*left_margin+'|'+' '+sentence   +' |'

print ' '*left_margin+'|'+' '*text_width   +'  |'
print ' '*left_margin+'+'+'-'*(box_width-4)+'+'
