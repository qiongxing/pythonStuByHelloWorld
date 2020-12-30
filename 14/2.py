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

class InterestAccount(BankAccount):
    def __init__(self,name,account,price,rate):
        BankAccount.__init__(self,name,account,price)
        self.rate =rate
    
    def addRate(self,count):
        self.rate += count

    def addInterest(self):
        inter = self.price *self.rate
        self.saveMoney(inter)