length=float(raw_input("长度为："))
width = float(raw_input("宽度为："))
price = float(raw_input("地毯价格为多少/平方米："))
area = length * width
sqArea = area / 9
total = area * price
print "共需要:",area,"平方米地毯，相当于",sqArea,"平方尺","总价:",total