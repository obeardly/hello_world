#!/usr/bin/python
#Hello World Listing 6.2
import easygui
flavor = easygui.choicebox("What is your favorite flavor of ice cream?",
        choices = [ 'Vanilla', 'Chocolate', 'Strawberry', 'Neopolitan' ] )
easygui.msgbox("You picked: " + flavor)
