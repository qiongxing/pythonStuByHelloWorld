import time
count =int(raw_input("从多少计数"))
for i in range(count,0,-1):
    print i
    time.sleep(1)
print "stop"