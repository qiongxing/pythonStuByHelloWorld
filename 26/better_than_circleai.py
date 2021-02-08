class AI:
    def __init__(self):
        self.currentlyDoing = "forward"
    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        elif self.robot.lookInFront() == "wall":
            self.robot.turnRight()
            self.currentlyDoing = "turnRight"
        elif self.currentlyDoing =="turnRight":
            self.robot.turnRight()
            self.currentlyDoing = "forward"
        else:
            self.robot.goForth()