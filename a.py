import  random

class Chatbot:

    '''This  class  describe chatbot'''

    def __init__(self,theStandardAnswers,theQuestionAnswers):

        self.StandardAnswers=theStandardAnswers

        self.QuestionAnswers=theQuestionAnswers

    def answer(self,text):
        if '?' in text:
 
           index=random.randint(0, len(self.QuestionAnswers)-1)
           print(self.QuestionAnswers(index))

        else:

            index=random.randint(0, len(self.QuestionAnswers)-1)

            print(self.StandardAnswers[index])

mybot=Chatbot(["ts interesting","so so"],["Hello"])

while True:

    text=input()

    mybot.answer(text)