#!/usr/bin/python
#Hello World Exercise Listing 1.2
import random
secret = random.randint(1, 99)
guess = 0 
tries = 0
print "Ahoy! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99.  I'll give you tries."
while guess != secret and tries < 6:
	guess = input("What is your guess? ")
	if guess < secret: 
	  print "Too low, you scurvy dog!"
	elif guess > secret: 
	  print "Too high, landlubber!"

	tries = tries + 1

if guess == secret:  
	print "The puzzle has been solved! My secret has been revealed."
else: 
	print "Your luck has come to an end! I must kill you now."
	print "My secret, so that you may not die in vain, was", secret
