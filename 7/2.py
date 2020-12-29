sex =raw_input("sex(m=man,f=women) : ")

if sex =='f':
    age =float(raw_input("age : "))
    if 10<=age<=12:
        print "you can join football team"
    else :
        print "年龄不符"
else :
    print "性别不符"