import easygui
name = easygui.enterbox("你的名字：")
roomNum =easygui.enterbox("房间号：")
area =easygui.enterbox("省地区：")
emailNum =easygui.enterbox("邮编：")

easygui.msgbox(name +"\r"+roomNum +"\r"+area+"\r" +emailNum)
