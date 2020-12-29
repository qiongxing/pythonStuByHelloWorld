import random,easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""生成了一个随机数,1-99之间!
给6次机会""")
while guess !=secret and tries < 6:
    guess = easygui.integerbox("What's yer guess?")
    if not guess:break
    if guess < secret:
        easygui.msgbox(str(guess) +" is too low")
    elif guess > secret:
        easygui.msgbox(str(guess) +" is too high")
    tries += 1
if guess == secret:
        easygui.msgbox(str(guess) +" pick")
else:
        easygui.msgbox("猜错了，没机会了,神秘数字为 "+str(secret))
