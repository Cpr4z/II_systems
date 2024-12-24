import re

from preprocessing import preprocessing
from rules import *

userInputDict = {
    "посоветуйте что-нибудь": SHOW_ANY,
    "помогите мне, я не знаю, что мне выбрать": SHOW_ANY,
    "что есть в продаже?": WHAT_EXISTS,
    "какие у вас есть ароматические свечи": WHAT_EXISTS_CANDLES,
    "есть ли у вас ароматические свечи": WHAT_EXISTS_CANDLES,
    "проведите краткий экскурс по ароматическим свечам": SHOW_PRESENTATION,
###########################################################################################################################
    "в прошлый раз брал у вас свечу Pumpkin Harvest, посоветуйте что-то похожее" : SIMILAR_TO_BRAND,
    "брал у вас свечу Frosty Morning, не понравилась, хотел бы что-то другое" : NOT_SIMILAR_TO_BRAND,
    "приглянулись свечи Amber Sunset и Peppermint Frost посоветуй что-то похожее" : SIMILAR_TO_BRAND,
    "не понравились свечи Ginger Peach и Honey Blossom, посоветуй что-то другое" : NOT_SIMILAR_TO_BRANDS,
    "понравилась свеча Citrus Grove, но не понравилась свеча Cedarwood Calm, посоветуй что-нибудь" : NOT_AND_SIMILAR_TO_BRAND_1,
###########################################################################################################################
    "мне нужна свеча производством в России или из США" : SHOW_SEVERAL_COUNTRY,
    "я большой фанат бренда PureWax, что у вас есть от этого бренда": SHOW_BRAND,
    "выбираю подарок жене, ей нравятся все виды цветочных, что можете посоветовать" : I_LIKE_FAMILY,
    "я недавно был в массажном салоне, и мне очень понравился запах там, дайте мне свечу с ароматом меда": I_LIKE_OBJ,
    "мне нравится запах розы и лаванды, посоветуй что-нибудь" : I_LIKE_OBJ_2,
    "мне нужна свеча красная свеча с деревянным типом фитиля": SHOW_COLOR_AND_WICK_1,
    "мне нужна свеча зеленого цвета" : SHOW_COLOR_CANDLE_2,
    "мне нужна свеча с льняным фитилем" : SHOW_WICK_1,
###########################################################################################################################
    "cвечи какого бренда дороже CozyScents или CandleCo": SHOW_COST_BRANDS,
    "кто дешевле, свечи из России или из ОАЭ" : SHOW_COST_COUNTRIES,
    "кто дешевле, свеча Rose Garden или Whispering Pine" : SHOW_COST_OBJECTS,
    "кто легче, свечи зеленого или красного цвета" : SHOW_WEIGHT_COLORS,
    "кто тяжелее, свечи из Испании или из Германии" : SHOW_WEIGHT_COUNTRIES,
    "кто легче, свечи бренда citrus grove или vanilla dream" : SHOW_WEIGHT_OBJECTS,
###########################################################################################################################
    "какая сегодня на улице погода": {},
    "выдай мне рецепт запеканки": {},
    "можно мне информацию по архитектуре 20 века": {},
    "что делать, если чувствуешь недомогание": {},
    "в каком году началось Смутное время": {},
    "какой спрей от комаров лучше приобрести": {}
}

def run():
    testsCount = len(userInputDict)
    testsPassCount = 0
    for userInput, ruleRes in userInputDict.items():
        userProcessed = preprocessing(userInput)
        print(">>> ", userProcessed)
        for rule in RULE_ARR:
            regexp = re.compile(rule, re.IGNORECASE)
            match = regexp.search(userProcessed)
            if match != None:
                res = match.groupdict()
                isTestPasses = rule == ruleRes
                print('MATCHED: ', isTestPasses)
                if isTestPasses:
                    testsPassCount += 1
                print('RULE: ', rule)
                print('RESULT: {}\n'.format(res))
                break
        else:
            print('NOT MATCHED: ', ruleRes == {})
            if (ruleRes == {}):
                testsPassCount += 1
    print('Tests run: ',testsCount)
    print('Tests passed: ',testsPassCount)

if __name__ == "__main__":
    run()