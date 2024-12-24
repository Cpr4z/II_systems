import re
import pymorphy3
import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt_tab')
morph = pymorphy3.MorphAnalyzer(lang='ru')

def getNormalFormWord(word):
    return morph.parse(word)[0].normal_form

def delUselessSigns(phrase):
    return re.sub("[^а-яa-z0-9'№ -]", "", phrase)


def getNormalFormPhrase(phrase):
    wordArr = word_tokenize(phrase, language="russian")
    return ' '.join(getNormalFormWord(word) for word in wordArr)


def toLower(phrase):
    return phrase.lower()


def preprocessing(phrase):
    phrase = toLower(phrase)
    phrase = delUselessSigns(phrase)
    return getNormalFormPhrase(phrase)