from Chicken import Chicken
from Rooster import Rooster
from Yard import Yard

myYard = Yard(10, 10)

betty = Chicken(myYard, 'Betty', 'red', 0, 0)
jolanda = Chicken(myYard, 'Jolanda', 'grey', 0, 8)
angel = Chicken(myYard, 'Angel', 'white', 8, 0)
dicky = Rooster(myYard, 'Dicky', 'pink', 3, 3)

cockas = Rooster(myYard, 'Cockas', 'black', 8, 8)

myYard.addChicken(betty)
myYard.addChicken(jolanda)
myYard.addChicken(angel)
myYard.addChicken(cockas)
myYard.addChicken(dicky)

myYard.passTheDay(50)
print(myYard)
