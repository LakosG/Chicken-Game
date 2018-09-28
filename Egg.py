import Chicken


class Egg:
    def __init__(self, mother: Chicken, x, y, doItDay):
        self.mother = mother
        self.x = x
        self.y = y
        self.doItDay = doItDay

    def __str__(self):
        return str(self.doItDay) + " - Mother of " + self.mother.name + " (" + str(self.x) + "," + str(self.y) + ")\n"