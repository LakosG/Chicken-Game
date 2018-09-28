import Chicken
import Egg
import pandas as pd

class Yard:

    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
        self.chickens = []
        self.eggs = []
        self.day = 1
        self.map = pd.DataFrame([[' ']*(self.width+1) for x in range(self.lenght+1)])

    def __str__(self):
        return 'The yard is ' + str(self.width) + ' width and ' + \
               str(self.lenght) + ' lenght!\n' + str(self.day) + ' days passed.\n' + \
                'The poultry: '+ (', '.join(str(c) for c in self.chickens)) +\
               '\nThe eggs:\n'+  (''.join(str(e) for e in self.eggs))

    def addChicken(self, chicken: Chicken):
        self.chickens.append(chicken)

    def addEgg(self, egg: Egg):
        self.eggs.append(egg)

    def stepChickens(self):
        for chick in self.chickens:
            chick.step()
            self.map[chick.x][chick.y] = chick.name[0]

    def passTheDay(self, days):
        for k in range(days):
            self.stepChickens()
            print(self.map, '\n', k+1) #minden lépésnél kirpinteli a térképet
            self.map = pd.DataFrame([[' '] * (self.width + 1) for x in range(self.lenght + 1)]) #reseteli a térképet
            self.day += 1
