__author__ = 'rory.sie@gmail.com'


class Robot:

    def __init__(self):
        self.huidigePositieX = 0
        self.huidigePositieY = 0
        self.aantalStappen = 0
        self.pallet = []

        self.bestelling = ["G01", "HD02", "M01", "M02"]

        self.matrix = []

    def lees_map(self):
        """Leest de map in van het magazijn, en stopt hem in een matrix"""
        file = open('map.csv', 'r')

        for regel in file.readlines():
            regellijst = regel.strip().split(",")
            self.matrix.append(regellijst)
        file.close()

    def checkPositie(self, x, y):
        if x <= (self.huidigePositieX + 1) and x <= (self.huidigePositieX - 1) and x > -1 & x < 10:
            return False
        elif x <= (self.huidigePositieY + 1) and y <= (self.huidigePositieY - 1) and y > -1 & y < 10:
            return False
        else:
            return self.matrix[x][y]

    def rechtsVrij(self):
        if self.matrix[self.huidigePositieY][self.huidigePositieX+1] == "1": # als de plaats rechts een 1 bevat
            return False
        elif self.huidigePositieX+1 == len(self.matrix):
            return False
        return True

    def linksVrij(self):
        if self.matrix[self.huidigePositieY][self.huidigePositieX-1] == "1": # als de plaats links een 1 bevat
            return False
        elif self.huidigePositieX-1 == -1:
            return False
        return True

    def bovenVrij(self):
        if self.matrix[self.huidigePositieY-1][self.huidigePositieX] == "1": # als de plaats boven een 1 bevat
            return False
        elif self.huidigePositieY-1 == -1:
            return False
        return True

    def onderVrij(self):
        if self.matrix[self.huidigePositieY+1][self.huidigePositieX] == "1": # als de plaats links een 1 bevat
            return False
        elif self.huidigePositieY+1 == len(self.matrix):
            return False
        return True

    def printMagazijn(self):
        print("-"*100)
        print("Het huidige magazijn ziet er zo uit (locatie van de robot is \"x\"):")
        for i in range(0,10): # ga omlaag in de map
            print("_"*76)
            for j in range(0,10): # ga opzij in de map
                if i == self.huidigePositieY and j == self.huidigePositieX:
                    print("x", end="\t|\t")
                elif len(self.matrix[i][j]) == 4:
                    print(self.matrix[i][j], end="|\t")
                else:
                    print(self.matrix[i][j], end="\t|\t")
            print()
        print("_"*76)
        print("-"*100)

    def printHuidigePositie(self):
        print("De huidige positie is", self.huidigePositieX, "naar rechts", self.huidigePositieY, "naar beneden")

    def getHuidigePositie(self):
        return [self.huidigePositieX,self.huidigePositieY]

    def gaLinks(self):
        if not self.linksVrij():
            print("Actie niet mogelijk")
        else:
            self.huidigePositieX -= 1
            self.aantalStappen += 1
            return True

    def gaRechts(self):
        if not self.rechtsVrij():
            print("Actie niet mogelijk")
        else:
            self.huidigePositieX += 1
            self.aantalStappen += 1
            return True

    def gaBoven(self):
        if not self.bovenVrij():
            print("Actie niet mogelijk")
        else:
            self.huidigePositieY -= 1
            self.aantalStappen += 1
            return True

    def gaOnder(self):
        if not self.onderVrij():
            print("Actie niet mogelijk")
        else:
            self.huidigePositieY += 1
            self.aantalStappen += 1
            return True

    def pakOp(self):
        if self.matrix[self.huidigePositieY][self.huidigePositieX] == "0":
            print("Geen product aanwezig")
        else:
            product = self.matrix[self.huidigePositieY][self.huidigePositieX] # omgedraaid, want je gaat eerst naar onder (y) en dan naar rechts (x)
            self.pallet.append(product)
            self.matrix[self.huidigePositieY][self.huidigePositieX] = "0"

    def printPallet(self):
        print("De robot heeft de volgende producten op zijn pallet staan:")
        print(self.pallet)

    def checkPallet(self):
        for item in self.bestelling:
            if item not in self.pallet:
                print("Nog niet alle producten staan op het pallet")
                return
        print("Alle producten staan op het pallet, gefeliciteerd!")
