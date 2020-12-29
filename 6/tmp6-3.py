import easygui
flavor =easygui.enterbox("What is your favorite ice cream flavor?",default="Valid")
easygui.msgbox("You picked " + flavor)