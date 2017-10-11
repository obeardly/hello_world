#!/usr/bin/python
# Hello World End of Chapter 3 Exercise 3
dist = raw_input("In miles, please tell me how far you are going today: ")
speed = raw_input("In MPH, please tell me how fast you will be driving: ")
time = float(dist) / float(speed)
print "Your travel time today will be approximately ",time," hours."
