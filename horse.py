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
    print('high')
    high = int(input())
    print('speed')
    speed = int(input())
    dzi = Horse(name, high, speed)
    dzier.append(dzi)

def hanelDzi(dzier):
    print('Type name,   you  can  use this names ')
    printNames(dzier)
    name1 = input()
    print('high')
    high1 = int(input())
    print('speed')
    speed1 = int(input())
    for  name  in  dzier:
        if name==name1:
            dzier.pop(name)
    print(dzier)

def  printNames(dzier):
    for  dzi  in  dzier:
        print(dzi.name)

def  yntrelGorzoxutyun(dzier):
    while True:
        print('1-avelacneldzi,2-printMaxSpeed,3-hanelDzi,4-printNames')
        a = int(input())
        if a == 1:
            avelacnelDzi(dzier)
        elif a==2:
            printMaxSpeed(dzier)
        elif a==3:
            hanelDzi(dzier)
        elif  a==4:
            printNames(dzier)
        else:
            print('please  do  input  another  one')

dzier=[]
yntrelGorzoxutyun(dzier)