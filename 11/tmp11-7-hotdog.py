
dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print "\tDog\tBun\tKetchup\tMustard\tOnions\tTotal Cal"
#决策树
count = 1
for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onion in [0,1]:
                    total_cal = dog *dog_cal +bun*bun_cal + ketchup*ket_cal + mustard*mus_cal + onion *onion_cal
                    print "#",count,"\t",
                    print dog,"\t",bun,"\t",ketchup,"\t",mustard,"\t",onion,"\t",total_cal
                    count =count+1