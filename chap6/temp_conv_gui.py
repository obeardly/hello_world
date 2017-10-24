#!/usr/bin/python
#Hello World End of Chapter 6 Exercise 1
#Convert Celsius to Farhrenheit
import easygui
F = easygui.integerbox("Please enter temperature in degrees Farhenheit: ")
C = 5.0 / 9 * ( F - 32 )
easygui.msgbox("Your current temperature is " + str(C))
