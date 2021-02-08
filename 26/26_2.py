class AI:
    def __init__(self):
        pass
    def turn(self):
        if self.robot.lookInFront() =="bot":
            self.robot.attack()
        else:
            self.goTowards(self.robot.locateEnemy()[0],self.robot.locateEnemy()[1])

    def goTowards(self,enemyLocation,direction):
        myLocation = self.robot.position
        delta = (enemyLocation[0] - myLocation[0],enemyLocation[1] - myLocation[1])
        if abs(delta[0]) > abs(delta[1]):
            if delta[0] <0:  
                targetOrientation = 3
            else:
                targetOrientation = 1
        else:
            if delta[1] < 0:
                targetOrientation = 0 
            else:
                targetOrientation = 2
        if self.robot.rotation ==targetOrientation:
            checkBlockBottom= self.robot._getSpace((myLocation[0]-1,myLocation[1]+2))
            checkBlockTop= self.robot._getSpace((myLocation[0]+1,myLocation[1]-2))
            if checkBlockBottom == "bot" or checkBlockTop== "bot": 
                self.robot.goBack()
                # self.robot.goForth()
            else:
                self.robot.goForth()
        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) %4
            if leftTurnsNeeded <=2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()