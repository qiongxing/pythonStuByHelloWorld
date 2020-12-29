dir ={}

while True:
    operate =raw_input("Add or look up a word (a/l/stop)?")
    if operate == 'a':
        key = raw_input("Type the word：")
        value = raw_input("Type the definition：")
        dir[key] = value
        print "Word added"
    elif operate == 'l':
        key = raw_input("Type the word：")
        if key in dir:
            print dir[key]
        else:
            print "That word is't in dictionary yet."

    else:
        break
print "stop app"