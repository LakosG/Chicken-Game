from Chicken import Chicken
from Egg import Egg

class Rooster(Chicken):
    def step(self):
        super(Rooster, self).step()
        self.doIt()

    def doIt(self):
        for chick in self.getSamePositionChickens():
            self.yard.addEgg(Egg(chick, self.x, self.y, self.yard.day))