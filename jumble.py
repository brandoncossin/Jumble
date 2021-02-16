#function definition                                                                                                                                                         
#jumble header file                                                                                                                                                          
from itertools import permutations
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words
def do_calculation(scrambled_word):
    p = map("".join, permutations(scrambled_word))
    answerList = []
    english_words = load_words()
    for j in list(p):
        if(j in english_words):
            if(j not in answerList):
                answerList.append(j)
    return answerList
