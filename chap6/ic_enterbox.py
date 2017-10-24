#!/usr/bin/env python
#Hello World Listing 6.3
import easygui
flavor = easygui.enterbox("What is your favorite flavor of ice cream? ",
        default = "Vanilla")
easygui.msgbox ("You entered: " + flavor)
