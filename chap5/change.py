#!/usr/bin/python
#Hello World Chapter 5 Try It Out Exercise 5
print "I'm going to help you add up your change."
q1 = raw_input("How many quarters do you have? ")
q2 = int(q1) * 0.25
d1 = raw_input("How many dimes do you have? ")
d2 = int(d1) * 0.10
n1 = raw_input("How many nickels do you have? ")
n2 = int(n1) * 0.05
p1 = raw_input("How many pennies do you have? ")
p2 = int(d1) * 0.01
change =  q2 + d2 + n2 + p2
print "You have ",change,"cents"
