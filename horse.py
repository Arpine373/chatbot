class Horse:
    '''This class describes  horse'''
    def __init__(self, theName, theHigh, theSpeed):
        self.name = theName
        self.high = theHigh
        self.speed = theSpeed
        print('Shnorhavorum  em  avelacaq  evs mekov')
    def printName(self):
        print(self.name)
    def increaseHigh(self, newhigh):
        self.high += newhigh

def printMaxSpeed(dzier):
    maximum = 0
    for dzi in dzier:
        if dzi.speed > maximum:
            maximum=dzi.speed
    print(maximum)
def  avelacnelDzi(dzier):
    print('Type name,   you  can  use this names ')
    printNames(dzier)
    name = input()
    high = int(input())
    speed = int(input())
    dzi = Horse(name, high, speed)
    dzier.append(dzi)

dzier=[]
dzi = Horse('Grom', 180, 33)
dzier.append(dzi)
dzi2=Horse('Sky',200,150)
dzier.append(dzi2)
dzi3=Horse('Miraj', 180,140)
dzier.append(dzi3)

def  printNames(dizer):
    for  dzi  in  dzier:
        print(dzi.name)


dzier[0].printName()
dzier[1].increaseHigh(100)
print(dzier[1].high)

avelacnelDzi(dzier)
avelacnelDzi(dzier)

printMaxSpeed(dzier)