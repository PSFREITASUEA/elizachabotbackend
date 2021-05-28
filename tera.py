import re

from dictionary import *


class Tera:
    def getAnswers(sentence):
        answer = ""
        sentence = sentence.lower()
        answer = self.verifyWelcomeMessage(sentence)

    
    def verifyWelcomeMessage(self, sentence):
        for word in welcome_message:
            has_welcome_message = re.search(rf"\b(?=\w){word}\b(?!\w)", sentence)
            if has_welcome_message:
                return welcome_message[word]
        return ""