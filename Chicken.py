import Yard
import random

class Chicken:

    def __init__(self, yard: Yard, name, color, x, y):
        self.yard = yard
        self.name = name
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return self.name + '(' + str(self.x) + ',' + str(self.y) + ')'

    def step(self):
        xMove = random.randint(-1, 1)
        yMove = random.randint(-1, 1)
        self.x += xMove
        self.y += yMove

        if self.x < 0:
            self.x = 0
        elif self.x > self.yard.width:
            self.x = self.yard.width

        if self.y < 0:
            self.y = 0
        elif self.y > self.yard.lenght:
            self.y = self.yard.lenght

    def getSamePositionChickens(self):
        samePositionChickens = []
        for chick in self.yard.chickens:
            if chick != self and chick.x == self.x and chick.y == self.y and type(chick) is Chicken:
                samePositionChickens.append(chick)
        return samePositionChickens


