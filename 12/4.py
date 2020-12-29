names =[]
print "Enter 5 names"
for i in range(5):
    names.append(raw_input("name："))

index=int(raw_input("Replace one name.Whice one?(1-5):"))
newName =raw_input("New Name:")
names[index-1] =newName

print "The names are",
for name in names:
    print name,
