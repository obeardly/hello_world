#!/usr/bin/python
#Hello World Exercise 5.4
import urllib2
file = urllib2.urlopen('http://helloworldbook2.com/data/message.txt')
message = file.read()
print message
