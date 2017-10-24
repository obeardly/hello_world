#!/usr/bin/env python
#Hello World Try It Out Exercise 7.1
#Ask the purchase price then display discount and final price.
price = float(raw_input("What is your purchase price: ")) 
if price <= 10: 
	print "Your discount will be 10%."
else:
	print "Your discount will be 20%."
if price <= 10:
	final = float( price ) * 0.9
else: 
	final = float( price ) * 0.8
print "Your final price will be: ",final, 
