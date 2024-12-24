import re
from collections import deque

#мне нравится свеча из ОАЭ

#мне нужна свеча с льняным фитилем

from comands import *
from prepareData import initPrefer, resetPrefer, delFiterByName, \
    _replaceCountry, _replaceBrand, _replaceBrandType, _replaceFamily, \
    _replaceSmell, _replaceColor, _replaceWickType
from preprocessing import preprocessing
from rules import *

def _getAnswer():
    while True:
        answer = input().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False

        cmdYesNoValidation()

def isFound():
    cmdWasFound()
    return _getAnswer()

def printCommandsAfterNo():
    print("Выберите одно из следующих действий:")
    print("1. Добавить описание")
    print("2. Сбросить все фильтры")
    print("3. Сбросить последний фильтр")
    print("4. Сбросить фильтр по имени")


def isAdd():
    cmdAddDefinition()
    return _getAnswer()


def isReset():
    cmdResetDefinition()
    return _getAnswer()

def isResetLastFiler():
    cmdReserLastFilter()
    return _getAnswer()

def isResetFilterByName():
    cmdResetFilterByName()
    return _getAnswer()

def removeNoneFromHistoryStorage(historyStorage):
    for sublist in historyStorage:
        for dictionary in sublist:
            for key, value in dictionary.items():
                if isinstance(value, list):
                    dictionary[key] = [item for item in value if item is not None]
    return historyStorage


def toNormalizedForm(wordToNormalize:list, filterName:str):
    newArray = []
    if  filterName == "country":
        newArray = _replaceCountry(wordToNormalize)
    elif filterName == "like":
        newArray = _replaceBrand(wordToNormalize)
    elif filterName == "dislike":
        newArray = _replaceBrand(wordToNormalize)
    elif filterName == "brand":
        newArray = _replaceBrandType(wordToNormalize)
    elif filterName == "family":
        newArray = _replaceFamily(wordToNormalize)
    elif filterName == "smell":
        newArray = _replaceSmell(wordToNormalize)
    elif filterName == "color":
        newArray = _replaceColor(wordToNormalize)
    elif filterName == "wick_type":
        newArray = _replaceWickType(wordToNormalize)

    return newArray

def removeElementsFromDict(dictPrefer, filterName:str, normalizedArray):
    if filterName in dictPrefer and isinstance(dictPrefer[filterName], list):
        dictPrefer[filterName] = [item for item in dictPrefer[filterName] if item not in normalizedArray]
    return dictPrefer

def resetLastFiler(historyStorage, dictPrefer):
    removeNoneFromHistoryStorage(historyStorage)
    last_elem = historyStorage.pop()

    if len(last_elem) > 1:
        filterName1 = list(last_elem[0].keys())[0]
        filtersArray1 = last_elem[0][filterName1]
        normalizedArray1 = toNormalizedForm(filtersArray1, filterName1)
        removeElementsFromDict(dictPrefer, filterName1, normalizedArray1)

        filterName2 = list(last_elem[1].keys())[0]
        filtersArray2 = last_elem[1][filterName2]
        normalizedArray2 = toNormalizedForm(filtersArray2, filterName2)
        removeElementsFromDict(dictPrefer, filterName2, normalizedArray2)
    else:
        filterName = list(last_elem[0].keys())[0]
        filtersArray = last_elem[0][filterName]
        normalizedArray = toNormalizedForm(filtersArray, filterName)
        removeElementsFromDict(dictPrefer, filterName, normalizedArray)


def isPreferDictEmpty(preferDict):
    for key, value in preferDict.items():
        if isinstance(value, list):
            if len(value) != 0:
                return False
    return True


def resetFilterByName(dictPrefer, name:str):
    delFiterByName(dictPrefer, name)

def processDefinition(dictPrefer, data, historyStorage):
    f = 0
    isNeedFind = True
    for rule in RULE_ARR:
        regexp = re.compile(rule, re.IGNORECASE)
        match = regexp.search(data)
        if match is not None:
            resDict = match.groupdict()

            if rule == SHOW_ANY or rule == WHAT_EXISTS or rule == WHAT_EXISTS_CANDLES or rule == SHOW_PRESENTATION:
                isNeedFind = False
                showAll()
            elif rule == SIMILAR_TO_BRAND or rule == SIMILAR_TO_BRAND_1:
                dictPrefer["likes"].append(resDict["similar_name"])

                historyStorage.append([{"likes" : [resDict["similar_name"]]}])

            elif rule == NOT_SIMILAR_TO_BRAND or rule == NOT_SIMILAR_TO_BRAND_1:
                dictPrefer["dislikes"].append(resDict["similar_name"])

                historyStorage.append([{"dislikes" : [resDict["similar_name"]]}])

            elif rule == NOT_AND_SIMILAR_TO_BRAND_1:
                dictPrefer["likes"].append(resDict["like_elem"])
                dictPrefer["dislikes"].append(resDict["dislike_elem"])

                historyStorage.append([{"likes" : [resDict["like_elem"]]},
                                       {"dislikes" : [resDict["dislike_elem"]]}])
            elif rule == NOT_SIMILAR_TO_BRANDS:
                dictPrefer["dislikes"].append(resDict["dislike_elem1"])
                dictPrefer["dislikes"].append(resDict["dislike_elem2"])

                historyStorage.append([{"dislikes" : [resDict["dislike_elem1"],
                                                      resDict["dislike_elem2"]]}])

            elif rule == SHOW_SEVERAL_COUNTRY:
                dictPrefer["country"].append(resDict["country1"])
                dictPrefer["country"].append(resDict["country2"])

                historyStorage.append([{"country" : [resDict["country1"], resDict["country2"]]}])

            elif rule == SHOW_BRAND:
                dictPrefer["brand"].append(resDict["brand"])

                historyStorage.append([{"brand" : [resDict["brand"]]}])

            elif rule == I_LIKE_FAMILY or rule == I_LIKE_FAMILY_CANDLE:
                dictPrefer["family"].append(resDict["family"])

                historyStorage.append([{"family" : [resDict["family"]]}])

            elif rule == I_LIKE_OBJ:
                dictPrefer["smell"].append(resDict["obj"])

                historyStorage.append([{"smell" : [resDict["obj"]]}])

            elif rule == SHOW_COLOR_AND_WICK_1 or rule == SHOW_COLOR_AND_WICK_2:
                dictPrefer["color"].append(resDict["color"])
                dictPrefer["wick_type"].append(resDict["wick"])

                historyStorage.append([{"color" : [resDict["color"]]},
                                       {"wick_type" : [resDict["wick"]]}])

            elif rule == SHOW_COST_BRANDS:
                isNeedFind = False
                compareBrandsByCost([resDict["brand1"], resDict["brand2"]], resDict["cost"])
            elif rule == SHOW_COST_COUNTRIES:
                isNeedFind = False
                compareCountriesByCost([resDict["country1"], resDict["country2"]], resDict["cost"])
            elif rule == SHOW_COST_OBJECTS:
                isNeedFind = False
                compareObjectsByCost([resDict["object1"], resDict["object2"]], resDict["cost"])
            elif rule == SHOW_WEIGHT_COLORS:
                isNeedFind = False
                compareColorsByWeight([resDict["color1"], resDict["color2"]], resDict["weight"])
            elif rule == SHOW_WEIGHT_COUNTRIES:
                isNeedFind = False
                compareCountriesByWeight([resDict["country1"], resDict["country2"]], resDict["weight"])
            elif rule == SHOW_WEIGHT_OBJECTS:
                isNeedFind = False
                compareObjectsByWeight([resDict["object1"], resDict["object2"]], resDict["weight"])
            elif rule == SHOW_COLOR_CANDLE_1 or rule == SHOW_COLOR_CANDLE_2:
                dictPrefer["color"].append(resDict["color"])

                historyStorage.append([{"color" : [resDict["color"]]},])

            elif rule == SHOW_COUNTRY_1 or rule == SHOW_COUNTRY_2:
                dictPrefer["country"].append(resDict["country"])
                dictPrefer["country"].append(resDict["country_ext"])

                historyStorage.append([{"country" : [resDict["country"], resDict["country_ext"]]},])

            elif rule == SHOW_WICK_1 or rule == SHOW_WICK_2:
                dictPrefer["wick_type"].append(resDict["wick"])

                historyStorage.append([{"wick_type" : [resDict["wick"]]}])

            elif rule == I_DISLIKE_OBJ:
                dictPrefer["dislikes"].append(resDict["obj"])

                historyStorage.append([{"dislikes" : [resDict["obj"]]}])

            elif rule == I_DISLIKE_OBJ_2:
                dictPrefer["dislikes"].append(resDict["object1"])
                dictPrefer["dislikes"].append(resDict["object2"])

                historyStorage.append([{"dislikes" : [resDict["object1"],
                                                      resDict["object2"]]},])

            elif rule == I_LIKE_OBJ_2:
                dictPrefer["smell"].append(resDict["object1"])
                dictPrefer["smell"].append(resDict["object2"])

                historyStorage.append([{"smell" : [resDict["object1"],
                                                   resDict["object2"]]}])

            f = 1
            break

    if f == 0:
        cmdMissunderstanding()
    if isNeedFind:
        cmdFind(dictPrefer)

def dialog():
    dictPrefer = initPrefer()

    while True:
        cmdDescribe()
        historyStorage = []
        data = input()
        dataProcessed = preprocessing(data)
        processDefinition(dictPrefer, dataProcessed, historyStorage)
        print()
        while True:
            if isFound():
                cmdGoodBye()
                return
            elif isAdd():
                break
            elif isResetLastFiler():
                resetLastFiler(historyStorage = historyStorage, dictPrefer = dictPrefer)
                if isPreferDictEmpty(dictPrefer):
                    showAll()
                else:
                    cmdFind(dictPrefer)

                if isFound():
                    return
                else:
                    pass

            elif isResetFilterByName():
                filterName = input("Введите название фильтра для сброса: ")
                resetFilterByName(dictPrefer, filterName)
                cmdFind(dictPrefer)
                if isPreferDictEmpty(dictPrefer):
                    showAll()
                else:
                    cmdFind(dictPrefer)

                if isFound():
                    return
                else:
                    pass

            elif isReset():
                resetPrefer(dictPrefer)
                cmdResetDefinitionComplete()
                break


def main():
    cmdWelcome()
    dialog()


if __name__ == "__main__":
    main()