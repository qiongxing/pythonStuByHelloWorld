import easygui
flavor =easygui.choicebox("What is your favorite ice cream flavor?",choices=['Vanlia','Choc','Straw'])
easygui.msgbox("You picked " + flavor)