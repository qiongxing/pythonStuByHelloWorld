# fahrenheit = float(raw_input())
# celsius = (fahrenheit - 32) *5.0/9
# print "Is",celsius,"des"

import easygui
fahrenheit =float(easygui.enterbox("请输入华氏度"))
celsius = (fahrenheit - 32) *5.0/9
easygui.msgbox("转换后的摄氏度为："+str(celsius))