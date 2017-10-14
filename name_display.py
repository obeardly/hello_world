#!/usr/bin/env python
#Hello World Chapter 6 Try It Out Exercise 2
import easygui
name = easygui.enterbox("What is your name? Please enter in format of First M. Last.")
addr = easygui.enterbox("What is your street address?")
city = easygui.enterbox("What is the name of your city?")
state = easygui.enterbox("What state, province, or territory do you live in?")
zc = easygui.enterbox("What is your ZIP code?")
dis_addr = name + "\n" + addr + "\n" + city + "," + state + " " + zc
easygui.msgbox ( dis_addr )
