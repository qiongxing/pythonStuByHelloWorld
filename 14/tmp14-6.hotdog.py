class HotDog:
    def __init__(self):
        self.cooked_level =0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg ="hot dog"
        if len(self.condiments) >0 :
            msg =msg + " with "
        for i in self.condiments:
            msg =msg +i +", "
        msg =msg.strip(", ")
        msg =self.cooked_string +" "+msg +"."
        return msg

    def cook(self,time):
        self.cooked_level =self.cooked_level +time
        if self.cooked_level >8: 
            self.cooked_string ="Charcoal"
        elif self.cooked_level >5: 
            self.cooked_string = "Well-done"
        elif self.cooked_level >3:
            self.cooked_string = "Medium"
        else :
            self.cooked_string = "Raw"

    def addCondiments(self,condiment):
        self.condiments.append(condiment)

myDog = HotDog()
print myDog
print "cook function 4min..."
myDog.cook(4)
print myDog
print "cook function 3min..."
myDog.cook(3)
print myDog
print "cook function 10min more..."
myDog.cook(10)
print myDog
myDog.addCondiments("ketchup")
myDog.addCondiments("mustard")
print myDog
