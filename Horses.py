class Horse:
    '''This class describes  horse'''
    def __init__(self, theName, theHigh, theSpeed):
        self.name = theName
        self.high = theHigh
        self.speed = theSpeed
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

dzier=[]
dzi = Horse('Grom', 180, 33)
dzier.append(dzi)
dzi2=Horse('Sky',200,150)
dzier.append(dzi2)
dzi3=Horse('Miraj', 180,140)
dzier.append(dzi3)

dzier[0].printName()
dzier[1].increaseHigh(100)
print(dzier[1].high)

printMaxSpeed(dzier)