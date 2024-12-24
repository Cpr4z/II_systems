HELP = r'(?P<help>(посоветовать|помочь|предложить|подсказать|показать|порекомендовать|посмотреть|ознакомиться))'
NOT_KNOW_GENERAL = r'(?P<not_know_general>(не.*знать).*(хотеть|надо))'

PRESENTATION = r'(?P<presentation>(экскурс|обзор|ревью))'

GENERAL_QUESTION = r'(?P<general_question>(что|какой))'
KIND_AROMA_CANDLE = r'(?P<kind_candles>(ароматический свеча|свеча|парфюмерный свеча))'
EXIST = r'(?P<exist>(есть|в наличие|в продажа|купить|мочь|предложить|представить))'

SHOW_PRESENTATION = r'.*{}.*{}.*'.format(PRESENTATION, KIND_AROMA_CANDLE)

WANT = r'(?P<want>(хотеться|хотеть|нужно|нужный|надо|искать|есть))'

TAG = r'((свежий|романтичный|мягкий|успокаивающий|травяной|сладкий|экзотический|сочный|освежающий|кислый|бодрящий|тёплый|землистый|природный|лесной|чистый|острый|согревающий|уютный|пряный|натуральный|прохладный))'
OBJ = r'(?P<obj>(роза|лаванда|жасмин|яблоко|лимон|грейпфрут|кедр|сосна|дуб|имбирь|корица|кардамон|ваниль|карамель|мёд|мята|шалфей))'
OBJ_WITHOUT_GROUP = r'(роза|лаванда|жасмин|яблоко|лимон|грейпфрут|кедр|сосна|дуб|имбирь|корица|кардамон|ваниль|карамель|мёд|мята|шалфей)'

FAMILY = r'(?P<family>(цветочный|фруктовый|цитрусовый|древесный|хвойный|пряный|cладкий|травяной))'

KIND_CANDLES_ADD = r'(?P<kind_candle_add>(запах|аромат))'
KIND_CANDLES_EXT = r'({}|{})'.format(KIND_AROMA_CANDLE, KIND_CANDLES_ADD)

GENERAL_EXT = r'({}|{})'.format(GENERAL_QUESTION, WANT)

LIKE = r'(?P<like>(понравиться|нравиться|обожать|любить|нужна|нужный))'
DISLIKE = r'(?P<dislike>(не переносить|не нравиться|не подходить|не любить|терпеть не мочь|ненавидеть|не понравиться))'

NOT = r'(?P<not>(но не|а не))'
SMELL_AS = r'(?P<smell_as>(с запах|пахнуть))'

SIMILAR_TO = r'(?P<similar_to>(похожий|на подобие|аналог|тип))'
NOT_SIMILAT_TO = r'(?P<not_similar_to>(не похожий|отличный от))'
NAME = r'(?P<similar_name>midnight jasmine|citrus grove|vanilla dream|ocean mist|cinnamon spice|pumpkin harvest|lavender fields|rose garden|amber sunset|peppermint frost|whispering pine|ginger peach|honey blossom|frosty morning|twilight musk|golden amber|cedarwood calm)'
NAME_WITHOUT_GROUP = r'(midnight jasmine|citrus grove|vanilla dream|ocean mist|cinnamon spice|pumpkin harvest|lavender fields|rose garden|amber sunset|peppermint frost|whispering pine|ginger peach|honey blossom|frosty morning|twilight musk|golden amber|cedarwood calm)'
DISLIKE_EXT = r'({}|{})'.format(DISLIKE, NOT_SIMILAT_TO)

COUNTRY = r'(?P<country>(италия|франция|оаэ|сша|россия|германия|испания))'
COUNTRY_ADD = r'(?P<country_ext>(итальянский|российский|немецкий|германский|французский|арабский|американский|испанский))'
COUNTRY_EXT = r'.*({}|{}).*'.format(COUNTRY, COUNTRY_ADD)
SHOW_COUNTRY_1 = r'.*{}.*{}.*'.format(COUNTRY_EXT, KIND_AROMA_CANDLE)
SHOW_COUNTRY_2 = r'.*{}.*{}.*'.format(KIND_AROMA_CANDLE, COUNTRY_EXT)

COUNTRY_WITHOUT_GROUP = r'(италия|франция|оаэ|сша|россия|германия|испания|итальянский|российский|немецкий|германский|французский|арабский|американский|испанский)'

COUNTRY_EXT_KINDCANDLES_1 = r'.*{}.*{}.*'.format(COUNTRY_EXT, KIND_AROMA_CANDLE)
COUNTRY_EXT_KINDCANDLES_2 = r'.*{}.*{}.*'.format(KIND_AROMA_CANDLE, COUNTRY_EXT)

SHOW_ANY = r'.*({}|{}).*'.format(HELP, NOT_KNOW_GENERAL)

WICK_TYPE = r'(?P<wick>(льняной|хлопковый|деревянный))'
SHOW_WICK_1 = r'.*{}.*{}.*'.format(KIND_AROMA_CANDLE, WICK_TYPE)
SHOW_WICK_2 = r'.*{}.*{}.*'.format(WICK_TYPE, KIND_AROMA_CANDLE)

BRAND_TYPE = r'(?P<brand>(blisscandles|cozyscents|candleco|aromalight|purewax))'
BRAND_WITHOUT_GROUP = r'(blisscandles|cozyscents|candleco|aromalight|purewax)'
SHOW_BRAND = r'.*{}.*'.format(BRAND_TYPE)

COLOR_TYPE = r'(?P<color>(белый|жёлтый|зелёный|красный|оранжевый|синий|фиолетовый))'
COLOR_WITHOUT_GROUP = r'(белый|жёлтый|зелёный|красный|оранжевый|синий|фиолетовый)'
SHOW_COLOR_CANDLE_1 = r'.*{}.*{}.*'.format(COLOR_TYPE, KIND_AROMA_CANDLE)
SHOW_COLOR_CANDLE_2 = r'.*{}.*{}.*'.format(KIND_AROMA_CANDLE, COLOR_TYPE)

SHOW_COLOR_AND_WICK_1 = r'.*{}.*{}.*'.format(COLOR_TYPE, WICK_TYPE)
SHOW_COLOR_AND_WICK_2 = r'.*{}.*{}.*'.format(WICK_TYPE, COLOR_TYPE)

COST = r'(?P<cost>(дорогой|дешёвый|стоят меньше|стоят больше))'
SHOW_COST_BRANDS = r'.*{}.*(?P<brand1>{}).*(?P<brand2>{}).*'.format(COST, BRAND_WITHOUT_GROUP, BRAND_WITHOUT_GROUP)
SHOW_COST_OBJECTS = r'.*{}.*(?P<object1>{}).*(?P<object2>{}).*'.format(COST, NAME_WITHOUT_GROUP, NAME_WITHOUT_GROUP)
SHOW_COST_COUNTRIES = r'.*{}.*(?P<country1>{}).*(?P<country2>{}).*'.format(COST, COUNTRY_WITHOUT_GROUP, COUNTRY_WITHOUT_GROUP)

WEIGHT = r'(?P<weight>(легче|тяжелее|меньше весит|больше весит|лёгкий|тяжёлый))'
SHOW_WEIGHT_COUNTRY = 'r.*{}.*{}.*'.format(WEIGHT, COUNTRY)
SHOW_WEIGHT_NAME = 'r.*{}.*{}.*{}.*'.format(WEIGHT, KIND_AROMA_CANDLE, NAME)

SHOW_WEIGHT_COLORS = r'.*{}.*(?P<color1>{}).*(?P<color2>{}).*'.format(WEIGHT, COLOR_WITHOUT_GROUP, COLOR_WITHOUT_GROUP)
SHOW_WEIGHT_COUNTRIES = r'.*{}.*(?P<country1>{}).*(?P<country2>{}).*'.format(WEIGHT, COUNTRY_WITHOUT_GROUP, COUNTRY_WITHOUT_GROUP)
SHOW_WEIGHT_OBJECTS = r'.*{}.*(?P<object1>{}).*(?P<object2>{}).*'.format(WEIGHT, NAME_WITHOUT_GROUP, NAME_WITHOUT_GROUP)


WHAT_EXISTS = r'.*{}.*{}.*'.format(GENERAL_QUESTION, EXIST)
WHAT_EXISTS_CANDLES = r'.*{}.*{}.*'.format(GENERAL_EXT, KIND_AROMA_CANDLE)

WANT_ABSTRACT = r'.*{}.*(?P<tag1>{}).*{}.*'.format(WANT, TAG, KIND_CANDLES_EXT)

WANT_ABSTRACT_OBJ = r'.*{}.*{}.*{}.*'.format(WANT, SMELL_AS, OBJ)
WANT_ABSTRACT_OBJ_KINDCANDLE = r'.*{}.*{}.*{}.*{}.*'.format(WANT, KIND_CANDLES_EXT, SMELL_AS, OBJ)

I_LIKE_TAG = r'.*{} (?P<tag1>{}).*'.format(LIKE, TAG)
I_LIKE_OBJ = r'.*{}.*{}.*'.format(LIKE, OBJ)

I_LIKE_OBJ_2 = r'.*{}.*(?P<object1>{}).*(?P<object2>{}).*'.format(LIKE, OBJ_WITHOUT_GROUP, OBJ_WITHOUT_GROUP)
I_DISLIKE_OBJ = r'.*{}.*{}.*'.format(DISLIKE, OBJ)
I_DISLIKE_OBJ_2 = r'.*{}.*(?P<object1>{}).*(?P<object2>{}).*'.format(DISLIKE, OBJ_WITHOUT_GROUP, OBJ_WITHOUT_GROUP)

I_LIKE_FAMILY = r'.*{}.*{}.*'.format(LIKE, FAMILY)
I_LIKE_FAMILY_CANDLE = r'.*{}.*{}.*{}.*'.format(LIKE, KIND_CANDLES_EXT, FAMILY)
I_LIKE_BRAND = r'.*{} {}.*'.format(LIKE, NAME)
I_DISLIKE_BRAND = r'.*{} {}.*'.format(DISLIKE, NAME)

LIKE_EXT = r'({}|{})'.format(LIKE, SIMILAR_TO)

SIMILAR_TO_BRAND = r'.*{}.*{}.*'.format(NAME, SIMILAR_TO)
SIMILAR_TO_BRAND_1 = r'.*{}.*{}.*'.format(SIMILAR_TO, NAME)
NOT_SIMILAR_TO_BRAND = r'.*{}.*{}.*'.format(NAME, DISLIKE_EXT)
NOT_SIMILAR_TO_BRAND_1 = r'.*{}.*{}.*'.format(DISLIKE_EXT, NAME)


NOT_SIMILAR_TO_BRANDS = r'.*{}.*(?P<dislike_elem1>{}).*(?P<dislike_elem2>{})'.format(DISLIKE_EXT, NAME_WITHOUT_GROUP, NAME_WITHOUT_GROUP)

NOT_AND_SIMILAR_TO_BRAND_1 = r'.*(?P<like_phrase>{}).*(?P<like_elem>{}).*(?P<dislike_phrase>{}).*(?P<dislike_elem>{})'.format(LIKE, NAME_WITHOUT_GROUP, DISLIKE, NAME_WITHOUT_GROUP)

NOT_AND_SIMILAR_TO_BRAND_2 = r"(?P<dislike_phrase>{})\s+(?P<brand_like>{}).*?(?P<like_phrase>{})\s+(?P<brand_dislike>{})".format(
    DISLIKE, NAME_WITHOUT_GROUP, LIKE, NAME_WITHOUT_GROUP
)

SHOW_SEVERAL_COUNTRY = r'.*{}.*(?P<country1>{}).*(?P<country2>{})'.format(KIND_AROMA_CANDLE, COUNTRY_WITHOUT_GROUP, COUNTRY_WITHOUT_GROUP)

RULE_ARR = [SHOW_WEIGHT_COUNTRIES,
            NOT_AND_SIMILAR_TO_BRAND_1,
            SHOW_COST_BRANDS,
            SHOW_WEIGHT_COLORS,
            SHOW_WEIGHT_OBJECTS,
            SHOW_COST_OBJECTS,
            NOT_SIMILAR_TO_BRANDS,
            SHOW_COST_COUNTRIES,
            SHOW_SEVERAL_COUNTRY,
            SHOW_COLOR_AND_WICK_1,
            SHOW_COLOR_AND_WICK_2,
            SHOW_COLOR_CANDLE_1,
            SHOW_COLOR_CANDLE_2,
            SHOW_COLOR_AND_WICK_1,
            SHOW_WICK_1,
            SHOW_WICK_2,
            NOT_SIMILAR_TO_BRAND,
            NOT_SIMILAR_TO_BRAND_1,
            SHOW_PRESENTATION,
            NOT_AND_SIMILAR_TO_BRAND_2,
            SIMILAR_TO_BRAND,
            SIMILAR_TO_BRAND_1,
            I_LIKE_FAMILY_CANDLE,
            WANT_ABSTRACT_OBJ_KINDCANDLE,
            WANT_ABSTRACT_OBJ,
            #WANT_ABSTRACT_NOT_KINDPARFUM,
            #WANT_ABSTRACT_NOT,
            COUNTRY_EXT_KINDCANDLES_1,
            COUNTRY_EXT_KINDCANDLES_2,
            WANT_ABSTRACT,
            WHAT_EXISTS_CANDLES,
            #I_DISLIKE_TAG,
            #I_DISLIKE_OBJ,
            I_DISLIKE_OBJ_2,
            I_LIKE_OBJ_2,
            I_DISLIKE_OBJ,
            I_DISLIKE_BRAND,
            I_LIKE_FAMILY,
            I_LIKE_TAG,
            I_LIKE_OBJ,
            I_LIKE_BRAND,
            COUNTRY_EXT,
            SHOW_BRAND,
            WHAT_EXISTS,
            SHOW_ANY,
            SHOW_WEIGHT_COUNTRY,
            SHOW_COUNTRY_1,
            SHOW_COUNTRY_2,
            SHOW_WEIGHT_NAME,
            KIND_AROMA_CANDLE,
            NAME]