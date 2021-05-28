import re

from dictionary import *


def getAnswers(sentence):
    sentence = sentence.lower()
    return verifyWelcomeMessage(sentence)

    
def verifyWelcomeMessage(sentence):
    for word in welcome_message:
        has_welcome_message = re.search(rf"\b(?=\w){word}\b(?!\w)", sentence)
        if has_welcome_message:
            return welcome_message[word]
    return ""