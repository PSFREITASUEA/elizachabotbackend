import re

from dictionary import *


def getAnswers(sentence):
    sentence = sentence.lower()
    answer = ""

    sentence = sentence.lower()
    answer += verifyWelcomeMessage(sentence)
    answer += verifyFeelings(sentence)
    answer += verifyFeelingsMotivation(sentence)

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

def verifyFeelingsMotivation(sentence):
    words_sentence = sentence.replace(",", " ").replace(".", " ").split()
    remaining_sentence = ""
    not_found = True
    index_start_sentence = 0

    for index in range(0, len(words_sentence)):
        if not_found:
            for verb in verbs_message:
                if words_sentence[index] == verb:
                    index_start_sentence = index + 1
                    not_found = False
                    break
        else:
            break

    for index in range(index_start_sentence, len(words_sentence)):
        remaining_sentence += words_sentence[index] + " "

    if not_found:
        return ""
    else:
        return f"E como {remaining_sentence}te afeta?"
