from Dialog_System.rec_system import familyArr
from rec_system import namesUI, giveRecommendationFull, merge_df

def initPrefer():
    return {"likes": [], "dislikes": [], "brand": [],
            "smell": [], "country": [], "wick_type": [],
            "color": [], "family": []}

def resetPrefer(dictPrefer):
    for key in dictPrefer.keys():
        dictPrefer[key] = []
    return dictPrefer

def delFiterByName(dictPrefer, name:str):
    if name in dictPrefer.keys():
        dictPrefer[name] = []

def _replaceBrand(inputArr):
    brandArr = []
    brandUI = {}
    for i in range(len(namesUI)):
        brandUI[namesUI[i].lower()] = i

    for brand in inputArr:
        curName = brand.lower()
        if curName in brandUI.keys():
            brandArr.append(namesUI[brandUI[curName]])
    return brandArr


def _replaceCountry(inputArr):
    countryArr = []
    inputArr = [item for item in inputArr if item is not None]
    countryDict = {"россия": "Россия", "франция": "Франция", "оаэ": "ОАЭ",
                   "сша": "США", "италия": "Италия", "германия": "Германия", "испания" : "Испания",
                   "итальянский": "Италия", "российский": "Россия", "немецкий": "Германия",
                   "германский": "Германия", "французский": "Франция", "арабский": "ОАЭ",
                   "американский": "США", "испанский" : "Испанский"}

    for country in inputArr:
        curCountry = country.lower()
        if curCountry in countryDict.keys():
            countryArr.append(countryDict[curCountry])
    return countryArr


def _replaceBrandType(inputArr):
    brandDict = {"blisscandles" : "BlissCandles", "candleco" : "CandleCo",
                 "aromalight": "AromaLight", "purewax": "PureWax",
                 "cozyscents": "CozyScents"}

    return [brandDict.get(brand, brand) for brand in inputArr]

def _replaceFamily(inputArr):
    familyDict = {"цветочный": "Цветочные", "фруктовый": "Фруктовые", "древесный": "Древесные",
                 "хвойный": "Хвойные", "пряный": "Пряные", "cладкий":"Сладкие", "травяной":"Травяные"}

    return [familyDict.get(family, family) for family in inputArr]

def _replaceSmell(inputArr):
    smellDict = {"роза" : "Розы", "лаванда": "Лаванда", "жасмина" : "Жасмин", "жасмин": "Жасмин",
                 "яблоко": "Яблоко", "лимон" : "Лимон", "грейпфрут" : "Грейпфрут", "кедр" : "Кедр",
                 "сосна" : "Сосна", "дуб": "Дуб", "имбирь": "Имбирь", "корица": "Корица", "кардамон": "Кардамон",
                 "ваниль" : "Ваниль", "карамель" : "Карамель", "мёд" : "Мед", "мята" : "Мята", "шалфей" : "Шалфей"}

    return [smellDict.get(smell, smell) for smell in inputArr]

def _replaceColor(inputArr):
    colorDict = {"белый" : "Белый", "жёлтый" : "Желтый", "зелёный" : "Зеленый",
                 "красный" : "Красный", "оранжевый" : "Оранжевый", "синий":"Синий",
                 "фиолетовый":"Фиолетовый"}

    return [colorDict.get(color, color) for color in inputArr]


def _replaceWickType(inputArr):
    wickDict = {"льняной":"Льняной", "хлопковый": "Хлопковый", "деревянный" : "Деревянный" }

    return [wickDict.get(wick, wick) for wick in inputArr]

def find(paramDict):
    paramDict["likes"] = _replaceBrand(paramDict["likes"])
    paramDict["dislikes"] = _replaceBrand(paramDict["dislikes"])
    paramDict["country"] = _replaceCountry(paramDict["country"])
    paramDict["brand"] = _replaceBrandType(paramDict["brand"])
    paramDict["family"] = _replaceFamily(paramDict["family"])
    paramDict["smell"] = _replaceSmell(paramDict["smell"])
    paramDict["color"] = _replaceColor(paramDict["color"])
    paramDict["wick_type"] = _replaceWickType(paramDict["wick_type"])
    return giveRecommendationFull([], paramDict["country"], paramDict["brand"],
                           paramDict["wick_type"], paramDict["family"], paramDict["smell"],
                           paramDict["likes"], paramDict["dislikes"], paramDict["color"], merge_df)