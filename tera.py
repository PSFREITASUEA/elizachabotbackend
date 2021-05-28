import re

from dictionary import *


def getAnswers(sentence):
    sentence = sentence.lower()
    answer = ""

    sentence = sentence.lower()
    answer = verifyWelcomeMessage(sentence)
    answer = verifyFeelings(sentence)

    if answer == "":
       return "Não sei se compreendi corretamente!"
    else:
        return answer

    
def verifyWelcomeMessage(sentence):
    for word in welcome_message:
        has_welcome_message = re.search(rf"\b(?=\w){word}\b(?!\w)", sentence)
        if has_welcome_message:
            return welcome_message[word]
    return ""

def verifyFeelings(sentence):
    for word in feelings_message:
        has_feelings = re.search(rf"\b(?=\w){word}\b(?!\w)", sentence)
        if has_feelings:
            return feelings_message[word]
    return ""