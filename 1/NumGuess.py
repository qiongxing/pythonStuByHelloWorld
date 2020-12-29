import random
secret = random.randint(1,99)
guess=0
tries = 0
print "神秘数字"
print "在1-99之间,6次机会"
while guess != secret and tries < 6:
    guess = input("请输入数字")
    if guess < secret:
        print "太小了"
    elif guess >secret :
        print "太大了"
    tries += 1
if  guess == secret:
        print "猜对了",secret
else:
        print "没有机会了"
        print "神秘数字为",secret