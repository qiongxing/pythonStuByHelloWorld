print "你要开始哪个数的乘法"
num = int(raw_input())
print "你希望最大到多少"
maxNum =int(raw_input())
print "下面是乘法"
flag = 1
while flag <=maxNum:
    print "%d x %d\t = %d "%(num,flag,num*flag)
    flag +=1