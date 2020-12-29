pwd ="123456"
inputPwd =""
while inputPwd !=pwd:
    inputPwd = raw_input("input u password：")
    if inputPwd !=pwd:
        print "error password"
print "you're in"