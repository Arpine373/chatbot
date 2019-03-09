import numpy

class GoToSport:
    def __init__(self, theHealth= 1.0, theDesire = 1.0, theTime = 1.0):
        # input signals values
        self.health = theHealth
        self.desire = theDesire
        self.time = theTime

    def solve(self):
     #create inputs array
        inputs = numpy.array([self.health, self.desire, self.time])

        #weights from input to hidden layer
        weightsInputToHidden1 = [0.9, 0.2, 0.9]
        weightsInputToHidden2 = [0.5, 0.9, 0.4]#neyroni  meji  gzeri  qaherna
        weightsInputToHidden = numpy.array([weightsInputToHidden1, weightsInputToHidden2])

        #weights from hidden to output layer
        weightsHiddenToOutput = numpy.array([0.4, 0.6])
        #we calculate what will come as input to hidden layer
        # multiplying weights to inputs and adding separately for 2 inputs
        hiddenInput = numpy.dot(weightsInputToHidden, inputs)
        print("summator result input to hidden: " + str(hiddenInput))

        #we apply activation function to every hidden input (2 elements)#2  sumatorneri  arjeqnern  en  2  elementnery
        hiddenOutput = numpy.array([self.activationFunction(x) for x in hiddenInput])
        print("activation result from hidden: " + str(hiddenOutput))
        #we calculate output signal
        summatorResultHiddenToOutput = numpy.dot(weightsHiddenToOutput, hiddenOutput)
        print("summator result hidden to output: " + str(summatorResultHiddenToOutput))
        return self.activationFunction(summatorResultHiddenToOutput)

    def activationFunction(self, x):
        if x >= 0.5:
            return 1
        else:
            return 0


someNeuralNetwork = GoToSport()
print("result: " + str(someNeuralNetwork.solve()))