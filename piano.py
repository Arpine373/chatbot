class Piano:
    '''This class describes  piano'''
    def __init__(self, theName, theHigh, theWeight):
        self.name= theName
        self.high=theHigh
        self.weight=theWeight
    def printName(self):
        print(self.name)
    def increaseHigh(self, newhigh):
        self.high+=newhigh
def printMaxWeight(dashnamurner):
    maximum = 0
    for  dashnamur in  dashnamurner:
        if dashnamur.weight>maximum:
            maximum=dashnamur.weight
    print(maximum)

dashnamurner=[]

dashnamur = Piano('Apollo', 150, 70)
dashnamurner.append(dashnamur)
dashnamur1=Piano('Allgäuer',200,100)
dashnamurner.append(dashnamur1)

dashnamurner[0].printName()
dashnamurner[1].increaseHigh(20)
print(dashnamurner[1].high)

printMaxWeight(dashnamurner)