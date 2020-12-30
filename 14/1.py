class BankAccount:
    def __init__(self,name,account,price):
        self.name =name
        self.account= account
        self.price = price
    
    def showPrice(self):
        return self.price

    def saveMoney(self,money):
        self.price = self.price + money
    
    def drawMoney(self,money):
        if money >self.price:
            print "your money too less"
        else: 
            self.price = self.price - money