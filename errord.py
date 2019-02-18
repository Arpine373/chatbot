import random
class Chatbot:
    '''This  class  describe chatbot'''
    def __init__(self, theStandardAnswers, theQuestionAnswers):
        self.StandardAnswers = theStandardAnswers
        self.QuestionAnswers = theQuestionAnswers
    def answer(self, text):
        if '?' in text:
            index = random.randint(0, len(self.QuestionAnswers) - 1)
            print(self.QuestionAnswers(index))
        elif 'hello' in text:
            print('hello')
        elif 'goodbye' in text:
            print('goodbye')
        elif 'hi' in text:
            print('hi')
        else:
            index = random.randint(0, len(self.QuestionAnswers) - 1)
            print(self.StandardAnswers[index])
mybot = Chatbot(["it is interesting", "so so"], ["nice"])
while True:
    text = input()
    mybot.answer(text)