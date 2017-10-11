#!/usr/bin/python
#Hello World Listing 6.1
import easygui
flavor = easygui.buttonbox("What is your favorite flavor of ice cream?",
        choices = [ 'Vanilla', 'Chocolate', 'Strawberry', 'Neopolitan' ] )
easygui.msgbox("You picked: " + flavor)
