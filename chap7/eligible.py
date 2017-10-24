#!/usr/bin/env python
#Hello World Try It Out Exercise 7.2
#Write a program to determine soccer team eligibility
print "We are going to determine your eligibility for Girls Club Soccer Team."
print "Are you a boy, girl, or other?"
sex = str(raw_input("Please use input m for boy and f for girl: ")) 
age = int(raw_input("What is your age?  "))
if age >= 10 and age <= 12 and sex == "f":
	print "You are eligible for the Girls Club Soccer Team."
else:
	print " You are NOT eligible for the Girls Club Soccer Team."
