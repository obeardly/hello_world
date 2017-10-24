#!/usr/bin/env python
#Hello World Try It Out Exercise 7.4
guess = raw_input("Please guess the password! " )
if guess == 'password':
	print "That's not the answer, dumbass!"
elif guess == 'open sesame':
	print "You have successfully hacked the program!"
elif guess == "morgan freeman" or 'morganfreeman':
	print "Morgan Freeman is god!"
else:
	print "Guess again, you jackass!"
