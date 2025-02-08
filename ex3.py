from random import randint
class PiratIsland():
    def __init__(self):
        self.chest = []
        for i in range(randint(5, 10)):
            tip = randint(1, 3)
            if tip == 1:
                self.chest.append(chest())
            elif tip == 2:
                self.chest.append(BadChest())
            else:
                self.chest.append(GoodChest())




class pirat:
    AlPirats = []
    def __init__(self, name, PiratShip):
        self.name = name
        self.PiratShip = PiratShip
        self.chest = []
        self.chestcount = 0
        pirat.AlPirats.append(self)
        self.gold = 0
        self.ill = 0
        self.nonchests = 0


class chest:
    allchest = []
    def __init__(self):
        self.weight = randint(4, 10)
        chest.allchest.append(self)


    def Get_Chest(self, pirat, island):
        if pirat.PiratShip >= self.weight:
            pirat.chest.append(self)
            pirat.PiratShip -= self.weight
            pirat.chestcount += 1
            island.chest.remove(self)
            pirat.nonchests += 1


class BadChest(chest):
    def __init__(self):
        super().__init__()
        self.ill = randint(3, 10)

    def Get_Chest(self, pirat, island):
        if pirat.PiratShip >= self.weight:
            super().Get_Chest(pirat, island)
            pirat.ill += self.ill



class GoodChest(chest):
    def __init__(self):
        super().__init__()
        self.gold = randint(15, 100)

    def Get_Chest(self, pirat, island):
        if pirat.PiratShip >= self.weight:
            super().Get_Chest(pirat, island)
            pirat.gold += self.gold






p1 = pirat('Чёрная Борода', 20)
p2 = pirat('Белоус', 30)
p3 = pirat('Костлявая Нога', 25)
p4 = pirat('Одноглазый', 26)

island = PiratIsland()

print(len(island.chest))
for i in pirat.AlPirats:
    for j in island.chest:
        j.Get_Chest(i, island)


print('пират Чёраня борода привёз:', p1.chestcount, 'сундуков')
print('пират Белоус привёз:', p2.chestcount, 'сундуков')
print('пират Костлявая Нога привёз:', p3.chestcount, 'сундуков')
print('пират Одноглазый привёз:', p4.chestcount, 'сундуков')

maxgold = -1
coolestpirat = []

for i in pirat.AlPirats:
    if i.gold > maxgold:
        maxgold = i.gold
        coolestpirat.append(i.name)

print(coolestpirat, 'нашёл больше всего золота:', maxgold)

maxdays = -1
coolestpirat = []

for i in pirat.AlPirats:
    if i.ill > maxdays:
        maxdays = i.ill
        coolestpirat.append(i.name)

print(coolestpirat, 'болел больше всех:', maxdays)

minchests = 11
coolestpirat = []

for i in pirat.AlPirats:
    if i.nonchests < minchests:
        minchests = i.nonchests
        coolestpirat.append(i.name)

print(coolestpirat, 'нашёл меньше всех пустых сундуков:', minchests)







