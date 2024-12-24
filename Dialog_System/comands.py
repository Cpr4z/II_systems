from Dialog_System.rec_system import country
from rec_system import df0
from params import *
from prepareData import find, _replaceBrandType, _replaceCountry, _replaceBrand, _replaceColor

def cmdOffer():
    print(DEFAULT_DATA)


def cmdWelcome():
    print(WELCOME_PHRASE)


def cmdGoodBye():
    print(GOODBYE_PHRASE)


def cmdDescribe():
    print(DESCRIBE)


def cmdWasFound():
    print(FOUND_QUESTION)


def cmdYesNoValidation():
    print(YES_NO)


def cmdAddDefinition():
    print(ADD_DEFINITION)


def cmdResetDefinition():
    print(RESET_PHRASE)


def cmdResetDefinitionComplete():
    print(RESET_PHRASE_COMPLETE)


def cmdMissunderstanding():
    print(MISUNDERSTANDING)


def cmdGiveMustRecomendation():
    print(MUST_LIKE)


def cmdGiveMayRecomendation():
    print(MAY_LIKE)

def cmdReserLastFilter():
    print(RESET_LAST_FILTER)

def cmdResetFilterByName():
    print(RESET_FILTER_BY_NAME)

def _printRecomendations(recArr):
    iArr = []
    n = min(len(recArr), 5)
    for item in recArr:
        key = list(item.keys())[0]
        iArr.append(df0.index[df0["название"] == key].tolist()[0])
    print(df0.loc[iArr, ["название", "бренд", "цвет", "тип фитиля", "страна"]])

def showAll():
    nameArray = df0['название'].tolist()
    print("В данный момент в наличие есть следующие ароматические свечи:")
    for name in nameArray:
        print(name)

def defineComparator(comparator:str)-> int:
    comparatorDict = {"мешьше": 0, "больше": 1, "дешёвый": 0, "дорогой": 1,
                      "легче" : 0, "тяжелее" : 1, "легкий": 0, "тяжелый":1}
    return comparatorDict.get(comparator, comparator)

def compareBrandsByCost(brandsArr, comparator:str):
    res = defineComparator(comparator)

    brandsArr = _replaceBrandType(brandsArr)
    brandsCost = df0[df0["бренд"].isin(brandsArr)].groupby("бренд")["цена (рублей)"].sum()
    brand1, brand2 = brandsArr
    cost1, cost2 = brandsCost.get(brand1, 0), brandsCost.get(brand2, 0)

    if res:
        if cost1 > cost2:
            print("Дороже ароматические свечи бренда: ", brand1, " - ", cost1)
        else:
            print("Дороже ароматические свечи бренда: ", brand2, " - ", cost2)
    else:
        if cost1 < cost2:
            print("Дешевле ароматические свечи бренда: ", brand1, " - ", cost1)
        else:
            print("Дешевле ароматические свечи бренда: ", brand2, " - ", cost2)

def compareCountriesByCost(countriesArr, comparator:str):
    res = defineComparator(comparator)

    countriesArr = _replaceCountry(countriesArr)
    countriesCost = df0[df0["страна"].isin(countriesArr)].groupby("страна")["цена (рублей)"].sum()
    country1, country2 = countriesArr
    cost1, cost2 = countriesCost.get(country1, 0), countriesCost.get(country2, 0)

    if res:
        if cost1 > cost2:
            print("Дороже ароматические свечи из страны: ", country1, " - ", cost1)
        else:
            print("Дороже ароматические свечи из страны: ", country2, " - ", cost2)
    else:
        if cost1 < cost2:
            print("Дешевле ароматические свечи из страны: ", country1, " - ", cost1)
        else:
            print("Дешевле ароматические свечи из страны: ", country2, " - ", cost2)

def compareObjectsByCost(objectsArr, comparator:str):
    res = defineComparator(comparator)

    objectsArr = _replaceBrand(objectsArr)
    objectsCost = df0[df0["название"].isin(objectsArr)].groupby("название")["цена (рублей)"].sum()
    object1, object2 = objectsArr
    cost1, cost2 = objectsCost.get(object1, 0), objectsCost.get(object2, 0)

    if res:
        if cost1 > cost2:
            print("Дороже ароматическая свеча: ", object1, " - ", cost1)
        else:
            print("Дороже ароматическая свеча: ", object2, " - ", cost2)
    else:
        if cost1 < cost2:
            print("Дешевле ароматическая свеча: ", object1, " - ", cost1)
        else:
            print("Дешевле ароматическая свеча: ", object2, " - ", cost2)

def compareColorsByWeight(colorsArr, comparator:str):
    res = defineComparator(comparator)

    colorsArr = _replaceColor(colorsArr)
    colorsWeight = df0[df0["цвет"].isin(colorsArr)].groupby("цвет")["вес (грамм)"].sum()
    color1, color2 = colorsArr
    weight1, weight2 = colorsWeight.get(color1, 0), colorsWeight.get(color2, 0)

    if res:
        if weight1 > weight2:
            print("Тяжелее ароматические свечи цвета: ", color1, " - ", weight1)
        else:
            print("Тяжелее ароматические свеча цвета: ", color2, " - ", weight2)
    else:
        if weight1 < weight2:
            print("Легче ароматические свеча цвета: ", color1, " - ", weight1)
        else:
            print("Легче ароматические свеча цвета: ", color2, " - ", weight2)

def compareCountriesByWeight(countriesArr, comparator:str):
    res = defineComparator(comparator)

    countriesArr = _replaceCountry(countriesArr)
    countriesWeight = df0[df0["страна"].isin(countriesArr)].groupby("страна")["вес (грамм)"].sum()
    country1, country2 = countriesArr
    weight1, weight2 = countriesWeight.get(country1, 0), countriesWeight.get(country2, 0)

    if res:
        if weight1 > weight2:
            print("Тяжелее ароматические свеча из страны: ", country1, " - ", weight1)
        else:
            print("Тяжелее ароматические свеча из страны: ", country2, " - ", weight2)
    else:
        if weight1 < weight2:
            print("Легче ароматические свеча из страны: ", country1, " - ", weight1)
        else:
            print("Легче ароматические свеча из страны: ", country2, " - ", weight2)


def compareObjectsByWeight(objectsArr, comparator:str):
    res = defineComparator(comparator)

    objectsArr = _replaceBrand(objectsArr)
    objectsWeight = df0[df0["название"].isin(objectsArr)].groupby("название")["вес (грамм)"].sum()
    object1, object2 = objectsArr
    weight1, weight2 = objectsWeight.get(object1, 0), objectsWeight.get(object2, 0)

    if res:
        if weight1 > weight2:
            print("Тяжелее ароматическая свеча: ", object1, " - ", weight1)
        else:
            print("Тяжелее ароматическая свеча: ", object2, " - ", weight2)
    else:
        if weight1 < weight2:
            print("Легче ароматическая свеча: ", object1, " - ", weight1)
        else:
            print("Легче ароматическая свеча: ", object2, " - ", weight2)



def cmdFind(dictPrefer):
    recMust, recMaybe = find(dictPrefer)

    if len(recMust):
        cmdGiveMustRecomendation()
        _printRecomendations(recMust)

    if len(recMaybe):
        cmdGiveMayRecomendation()
        _printRecomendations(recMaybe)
    recMust.clear()
    recMaybe.clear()