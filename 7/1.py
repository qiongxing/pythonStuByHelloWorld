amountMoney = float(raw_input("amount money："))
discountPrice = 0.0
if amountMoney <= 10:
    discountPrice = amountMoney * 0.9
    print "10%iscount",discountPrice
else:
    discountPrice =amountMoney *0.8
    print "10%iscount",discountPrice

