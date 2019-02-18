class Piano:
    '''This class describes  piano'''

    def __init__(self, theName, theHigh, theWeights):

        self.Name = theName

        self.High = theHigh

        self.Weights = theWeights

    def printName(self):

        print(self.Name)

    def IncreaseHigh(self, newhigh):

        self.High += newhigh

    def MaxWeight(self, Weights):

        maximum = 0

        for i in self.Weights:

            if i > maximum:
                i = i + maximum

        print(i)


dashnamur = Piano('Apollo', 150, [50, 60, 70])

dashnamur.printName()

dashnamur.IncreaseHigh(27)

print(dashnamur.High)

dashnamur.MaxWeight('Weights')