numBlocks =int(raw_input("how mant blocks of starts do you want?"))
for i in range(1,numBlocks+1):
    for line in range(1,i*2):
        for star in range(1,(i+line)*2):
            print "*",
        print
    print 