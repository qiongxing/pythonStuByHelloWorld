import easygui
flavor =easygui.buttonbox("What is your favorite ice cream flavor?",choices=['Vanlia','Choc','Straw'])
easygui.msgbox("You picked " + flavor)