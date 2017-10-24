#!/usr/bin/python
#Hello World Listing 6.5
import random, easygui
secret = random.randint(1, 99)
guess = 0 
tries = 0
easygui.msgbox("""Ahoy! I'm the Dread Pirate Roberts, and I have a secret! It is a number from 1 to 99.  I'll give you 6 tries.""")
while guess != secret and tries < 6:
	guess = easygui.integerbox("What is your guess? ")
        if not guess: break
	if guess < secret: 
	  easygui.msgbox(str(guess) + "is too low, you scurvy dog! Try again or walk the plank! ")
	elif guess > secret: 
	  easygui.msgbox(str(guess) + "is too high, landlubber! Try again or walk the plank! ")
	tries = tries + 1
if guess == secret:  
	easygui.msgbox("The puzzle has been solved! My secret has been revealed.")
else: 
	easygui.msgbox("Your luck has come to an end! I must kill you now. My secret, so that you may not die in vain, was " + str(secret))
