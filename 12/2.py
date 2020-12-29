names =[]
print "Enter 5 names"
for i in range(5):
    names.append(raw_input("name："))
print "The names are",
names.sort()
sortedNames =names.reverse()
print names
for name in names:
    print name,
print
print "The reverse names are",
for name in sortedNames:
    print name,
