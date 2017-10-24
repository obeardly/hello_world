#!/usr/bin/python
#Hello World Chapter 5 Try It Out Exercise 4
print "I'm going to help you determine the amount of carpet you need."
l = int(raw_input('What is the length of your room in feet? '))
w = int(raw_input('What is the width of your room in feet? '))
a = w * l
print 'You are going to require',a,'square feet of carpet.'
y = int(a) / 9
print 'You are going to require',y,'yards of carpet.'
print "Now I'll help you determine the cost of your carpet."
print "What is the cost of your carpet per yard?"
print "Please enter your cost in dollars and cents format."
print ""
c = raw_input()
print ""
t = float(c) * y
print "Your carpet is going to cost $" ,t, "."
