#!/usr/bin/python
#Hello World Listing 
import easygui
flavor = easygui.enterbox("What is your favorite flavor of ice cream? ",
        default = "Vanilla")
easygui.msgbox ("You entered: " + flavor)
