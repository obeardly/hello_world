#!/usr/bin/env python
#Hello World Try It Out Exercise 7.2
#Write a program to determine if you need to buy fuel.
#I chose imperial vs metric since I live in the states.
print "We're going to determine if you need gas now, or can you wait."
print "We're factoring in a 1 gallon buffer in case of MPG variation"
tank = float(raw_input("In gallons, how large is your fuel tank? "))
full = float(raw_input("In percentage, how full is your tank? "))
mpg = float(raw_input("What is your average MPG 'Miles Per Gallon'? ")) 
station = int(raw_input("What is the distance to the next fueling station? "))
fuel = float( full * tank / 100 )
dist = mpg * (fuel - 1)
print "\nSize of tank (gallons): ",tank,"\n"
print "Percent full: ",full,"\n"
if dist >= station:
	print "You can go",dist,"\n"
	print "The next gas station is",station,"miles away.\n"
	print "You can wait for fuel.\n"
else:
	print "You can go",dist,"\n"
	print "The next gas station is",station," miles away.\n"
	print "GET FUEL NOW!!!\n"
