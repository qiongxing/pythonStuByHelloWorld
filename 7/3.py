distance = 200
tankSize = float(raw_input("Size of tank:"))
percent = float(raw_input("percent full:"))
literKm = float(raw_input("km per liter:"))
canDistance =tankSize *percent *0.01 *literKm
print "The next gas station is 200km away,u can go another",str(canDistance),"km "
if canDistance < distance :
    print "需要加油"
else :
    print "you can wait for the next station"
