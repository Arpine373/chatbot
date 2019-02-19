import random
class Chatbot:
    '''This  class  describe chatbot'''
    def __init__(self, theStandardAnswers, theQuestionAnswers):
        self.StandardAnswers = theStandardAnswers
        self.QuestionAnswers = theQuestionAnswers
    def answer(self, text):
        if '?' in text:
            index = random.randint(0, len(self.QuestionAnswers) - 1)
            print(self.QuestionAnswers[index])
            return (self.QuestionAnswers[index])

        else:
            index = random.randint(0, len(self.QuestionAnswers) - 1)
            print(self.StandardAnswers[index])
            return (self.StandardAnswers[index])
mybot1 = Chatbot(["di?","aa"], ["Oho?", "Ok"])
mybot2=Chatbot(['spokoistvie tolko  spokoistvie','interesting'],['smile','dilemma'])
text=''
for  i  in  range(1,  11):
    if i % 2 == 0:
        text = mybot1.answer(text)
    else:
        text = mybot2.answer(text)
