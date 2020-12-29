import time
count =int(raw_input("从多少计数"))
for i in range(count,0,-1):
    print i,
    for j in range(i):
        print "*",
    time.sleep(1)
    print
print "stop"