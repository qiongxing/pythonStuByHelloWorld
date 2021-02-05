suit_totals = [3,1,1,0]
long_suit = 0
for i in range(4):
    if suit_totals[i]>long_suit:
        long_suit=i
print long_suit