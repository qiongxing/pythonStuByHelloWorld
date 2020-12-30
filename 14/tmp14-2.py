class Ball:

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

#创建实例
myBall = Ball()
myBall.direction = "down"
myBall.color ="red"
myBall.size ="small"

print myBall.direction
myBall.bounce()
print "调用方法后："+ myBall.direction