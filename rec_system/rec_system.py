import csv
import random
import os
from math import isnan
from itertools import chain
from graphviz import Digraph
import pandas as pd
import numpy as np
from numpy.linalg import norm
import plotly.express as px
from collections import defaultdict
from colors import Colors


import panel as pn

#lab1 dataset and tree visualization
#create dataset
main_categories = ["Цветочные", "Фруктовые", "Древесные", "Пряные", "Сладкие"]

sub_categories = ["Цитрусовые", "Хвойные", "Травяные"]

categories_and_sub = main_categories + sub_categories

category_hierarchy = {
    "Цитрусовые": "Фруктовые",
        "Хвойные": "Древесные",
    "Травяные": "Пряные"
}

smells_base = ["Розы", "Лаванда", "Жасмин",
          "Яблоко", "Лимон", "Грейпфрут",
          "Кедр", "Сосна", "Дуб",
          "Имбирь", "Корица", "Кардамон",
          "Ваниль", "Карамель", "Мед",
          "Мята", "Шалфей"]


candles_material = ["Парафиновый воск", "Соевый воск", "Пчелиный воск"]

color = ["Желтый", "Синий", "Оранжевый", "Белый", "Зеленый", "Фиолетовый", "Красный"]

brand = ["BlissCandles", "PureWax", "AromaLight", "CandleCo", "CozyScents"]

wick_type = ["Хлопковый", "Деревянный", "Бамбуковый", "Льняной"]

country = ["Россия", "Франция", "Италия", "США", "Германия", "ОАЭ", "Испания"]

names = ["Midnight Jasmine", "Citrus Grove", "Vanilla Dream", "Ocean Mist",
         "Cinnamon Spice", "Pumpkin Harvest", "Lavender Fields", "Rose Garden",
         "Amber Sunset", "Peppermint Frost", "Whispering Pine", "Ginger Peach",
         "Honey Blossom", "Frosty Morning", "Twilight Musk", "Golden Amber",
         "Cedarwood Calm"]

smell_category_data = [
    {"категория": "Цветочные", "запах": "Розы", "характеристика": "свежий, романтичный, мягкий"},
    {"категория": "Цветочные", "запах": "Лаванда", "характеристика": "успокаивающий, травяной, сладкий"},
    {"категория": "Цветочные", "запах": "Жасмин", "характеристика": "экзотический, сладкий, тёплый"},
    {"категория": "Фруктовые", "запах": "Яблоко", "характеристика": "сочный, сладкий, освежающий"},
    {"категория": "Цитрусовые", "запах": "Лимон", "характеристика": "кислый, свежий, бодрящий"},
    {"категория": "Цитрусовые", "запах": "Грейпфрут", "характеристика": "свежий, кисло-сладкий, бодрящий"},
    {"категория": "Древесные", "запах": "Дуб", "характеристика": "тёплый, глубокий, землистый"},
    {"категория": "Хвойные", "запах": "Кедр", "характеристика": "свежий, смолистый, природный"},
    {"категория": "Хвойные", "запах": "Сосна", "характеристика": "свежий, лесной, чистый"},
    {"категория": "Пряные", "запах": "Имбирь", "характеристика": "острый, бодрящий, согревающий"},
    {"категория": "Пряные", "запах": "Корица", "характеристика": "сладкий, тёплый, уютный"},
    {"категория": "Пряные", "запах": "Кардамон", "характеристика": "пряный, экзотический, тёплый"},
    {"категория": "Сладкие", "запах": "Ваниль", "характеристика": "сладкий, мягкий, сливочный"},
    {"категория": "Сладкие", "запах": "Карамель", "характеристика": "тёплый, сладкий, густой"},
    {"категория": "Сладкие", "запах": "Мед", "характеристика": "сладкий, натуральный, мягкий"},
    {"категория": "Травяные", "запах": "Мята", "характеристика": "свежий, прохладный, бодрящий"},
    {"категория": "Травяные", "запах": "Шалфей", "характеристика": "травяной, успокаивающий, землистый"},
]

csv_file_path = "../dataset/characteristics_dataset.csv"

def make_hierarchy(smell, smell_category):
    if smell_category in category_hierarchy:
        hierarchy = [category_hierarchy[smell_category], smell_category, smell]
        return ", ".join(hierarchy)
    else:
        return ", ".join([smell_category, smell])

if not os.path.exists(csv_file_path):
    with open(csv_file_path, "w", encoding="utf-8", errors="ignore") as csv_file:
        write = csv.DictWriter(csv_file, fieldnames=["категория", "запах", "характеристика"])
        write.writeheader()
        write.writerows(smell_category_data)

    dataset = []
    for i in range(17):
        item = {
            "название" : names[i % len(names)],
            "бренд" : random.choice(brand),
            "цвет" : random.choice(color),
            "тип фитиля" : random.choice(wick_type),
            "материал" : random.choice(candles_material),
            "страна" : random.choice(country),
            "цена (рублей)" : random.randint(500, 1200),
            "вес (грамм)" : random.randint(100, 400),
            "ручная работа" : random.choice([True, False]),
            "натуральные материалы" : random.choice([True, False]),
            "иерархия" : make_hierarchy(smell_category_data[i]["запах"], smell_category_data[i]["категория"]),
        }
        dataset.append(item)

csv_file_path = "../dataset/candles_dataset.csv"

if not os.path.exists(csv_file_path):
    with open(csv_file_path, "w", encoding="utf-8", errors="ignore") as csv_file:
        fieldnames = ["название", "бренд", "цвет", "тип фитиля", "материал", "страна",
                      "цена (рублей)", "вес (грамм)", "ручная работа", "натуральные материалы", "иерархия"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dataset)

    smell_category = []
    with open("../dataset/characteristics_dataset.csv", 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            smell_category.append({"категория": row["категория"], "запах": row["запах"]})

    dot = Digraph(comment="Иерархия запахов")
    dot.node("root", "Дерево ароматов")  # Корневой узел

    added_edges = set()

    for item in smell_category:
        category = item['категория']
        smell = item['запах']

        if category in sub_categories:
            main_category = category_hierarchy[category]
            dot.node(main_category, main_category)

            if (main_category, category) not in added_edges:
                dot.node(category, category)
                dot.edge(main_category, category)
                added_edges.add((main_category, category))

            dot.node(smell, smell)
            dot.edge(category, smell)
        elif category in main_categories:
            dot.node(category, category)
            dot.node(smell, smell)
            dot.edge(category, smell)

    for main_cat in main_categories:
        dot.edge("root", main_cat)

    dot.render('smell_hierarchy_tree', format='png')

# aroma_df = pd.read_csv("../dataset/candles_dataset.")
smells_df = pd.read_csv("../dataset/characteristics_dataset.csv")

smells_df["запах"] = smells_df["запах"].map(lambda value: str(value).lower() + ', ') + \
    smells_df["характеристика"].map(lambda value: ', '.join(map(str, str(value).lower().split(', '))))

smells_df = smells_df.groupby("категория", as_index=False).agg({
    "запах": ', '.join,
    "характеристика": ', '.join,
})

smells_df["запах"] = smells_df["запах"].apply(lambda value: set(value.split(', ')))
smells_df["характеристика"] = smells_df["характеристика"].apply(lambda value: set(value.split(', ')))

exploded_df = smells_df.explode("запах").explode("характеристика")

smells_dummies = pd.get_dummies(exploded_df["запах"]).groupby(exploded_df["категория"]).max()
characteristics_dummies = pd.get_dummies(exploded_df["характеристика"]).groupby(exploded_df["категория"]).max()

smell_df = pd.concat([smells_dummies, characteristics_dummies], axis=1).fillna(0).astype(int).reset_index()

smell_df_file = '../dataset/candles_smells_df.csv'
with open(smell_df_file, mode='w', newline='', encoding='utf-8') as file:
    smell_df.to_csv(file, index=False)

#lab2
smells0 = pd.read_csv('../dataset/characteristics_dataset.csv', delimiter=',', encoding ="utf-8")
smells = smells0.copy(deep = True)

smells["категория"] = smells["категория"].str.lower().str.strip()
smells["запах"] = smells["запах"].str.lower().str.strip()
smells["характеристика"] = smells["характеристика"].str.lower().str.strip()

smells["ассоциации"] = smells["запах"] + ',' + smells["характеристика"]

unique_associations = set(chain.from_iterable(smells["ассоциации"].str.split(',')))

result_df = pd.DataFrame(0, index=smells["категория"].unique(), columns=list(unique_associations))

for _, row in smells.iterrows():
    category = row["категория"]
    associations = row["ассоциации"].split(',')
    result_df.loc[category, associations] = 1

result_df.reset_index(inplace=True)
result_df.rename(columns={'index': 'категория'}, inplace=True)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df0 = pd.read_csv('../dataset/candles_dataset.csv', delimiter=',', encoding ="utf-8")
df = df0.copy(deep=True)

df["иерархия"] = df["иерархия"].map(lambda elem: elem.split(","))

F_NAME = "название"
F_DIST = "расстояние"

nameArr = df["название"]

dfTree = pd.DataFrame(
    columns=["название", "иерархия"],
    data=df[["название", "иерархия"]].values
)

df["цена (рублей)"] = (df["цена (рублей)"].values - min(df["цена (рублей)"].values)) / (max(df["цена (рублей)"].values) - min(df["цена (рублей)"].values))
df["вес (грамм)"] = (df["вес (грамм)"].values - min(df["вес (грамм)"].values)) / (max(df["вес (грамм)"].values) - min(df["вес (грамм)"].values))

country_dict = {"Россия" : 0, "Франция": 1, "Италия": 2, "США": 3, "Германия": 4, "ОАЭ": 5, "Испания": 6}

countryMatr = np.zeros((len(country_dict), len(country_dict)), dtype=float)

for key in country_dict:
    countryMatr[country_dict[key]][country_dict[key]] = 0

countryMatr[country_dict["Россия"]][country_dict["Франция"]] = countryMatr[country_dict["Франция"]][country_dict["Россия"]] = 0.6
countryMatr[country_dict["Россия"]][country_dict["Италия"]] = countryMatr[country_dict["Италия"]][country_dict["Россия"]] = 0.5
countryMatr[country_dict["Россия"]][country_dict["США"]] = countryMatr[country_dict["США"]][country_dict["Россия"]] = 0.3
countryMatr[country_dict["Россия"]][country_dict["Германия"]] = countryMatr[country_dict["Германия"]][country_dict["Россия"]] = 0.6
countryMatr[country_dict["Россия"]][country_dict["ОАЭ"]] = countryMatr[country_dict["ОАЭ"]][country_dict["Россия"]] = 0.1
countryMatr[country_dict["Россия"]][country_dict["Испания"]] = countryMatr[country_dict["Испания"]][country_dict["Россия"]] = 0.3

countryMatr[country_dict["Франция"]][country_dict["Италия"]] = countryMatr[country_dict["Италия"]][country_dict["Франция"]] = 0.8
countryMatr[country_dict["Франция"]][country_dict["США"]] = countryMatr[country_dict["США"]][country_dict["Франция"]] = 0.4
countryMatr[country_dict["Франция"]][country_dict["Германия"]] = countryMatr[country_dict["Германия"]][country_dict["Франция"]] = 0.5
countryMatr[country_dict["Франция"]][country_dict["ОАЭ"]] = countryMatr[country_dict["ОАЭ"]][country_dict["Франция"]] = 0.1
countryMatr[country_dict["Франция"]][country_dict["Испания"]] = countryMatr[country_dict["Испания"]][country_dict["Франция"]] = 0.6

countryMatr[country_dict["Италия"]][country_dict["США"]] = countryMatr[country_dict["США"]][country_dict["Италия"]] = 0.5
countryMatr[country_dict["Италия"]][country_dict["Германия"]] = countryMatr[country_dict["Германия"]][country_dict["Италия"]] = 0.6
countryMatr[country_dict["Италия"]][country_dict["ОАЭ"]] = countryMatr[country_dict["ОАЭ"]][country_dict["Италия"]] = 0.2
countryMatr[country_dict["Италия"]][country_dict["Испания"]] = countryMatr[country_dict["Испания"]][country_dict["Италия"]] = 0.9

countryMatr[country_dict["США"]][country_dict["Германия"]] = countryMatr[country_dict["Германия"]][country_dict["США"]] = 0.5
countryMatr[country_dict["США"]][country_dict["ОАЭ"]] = countryMatr[country_dict["ОАЭ"]][country_dict["США"]] = 0.1
countryMatr[country_dict["США"]][country_dict["Испания"]] = countryMatr[country_dict["Испания"]][country_dict["США"]] = 0.3

countryMatr[country_dict["Германия"]][country_dict["ОАЭ"]] = countryMatr[country_dict["ОАЭ"]][country_dict["Германия"]] = 0.1
countryMatr[country_dict["Германия"]][country_dict["Испания"]] = countryMatr[country_dict["Испания"]][country_dict["Германия"]] = 0.4

countryMatr[country_dict["ОАЭ"]][country_dict["Испания"]] = countryMatr[country_dict["Испания"]][country_dict["ОАЭ"]] = 0.3

color_dict = {"Желтый": 0, "Синий": 1, "Оранжевый": 2, "Белый": 3, "Зеленый": 4, "Фиолетовый": 5, "Красный": 6}
colorMatr = np.zeros((len(color_dict), len(color_dict)), dtype=float)

for key in color_dict:
    colorMatr[color_dict[key]][color_dict[key]] = 0

colorMatr[color_dict["Желтый"]][color_dict["Синий"]] = colorMatr[color_dict["Синий"]][color_dict["Желтый"]] = 0.2
colorMatr[color_dict["Желтый"]][color_dict["Оранжевый"]] = colorMatr[color_dict["Оранжевый"]][color_dict["Желтый"]] = 0.8
colorMatr[color_dict["Желтый"]][color_dict["Белый"]] = colorMatr[color_dict["Белый"]][color_dict["Желтый"]] = 0.2
colorMatr[color_dict["Желтый"]][color_dict["Зеленый"]] = colorMatr[color_dict["Зеленый"]][color_dict["Желтый"]] = 0.3
colorMatr[color_dict["Желтый"]][color_dict["Фиолетовый"]] = colorMatr[color_dict["Фиолетовый"]][color_dict["Желтый"]] = 0.1
colorMatr[color_dict["Желтый"]][color_dict["Красный"]] = colorMatr[color_dict["Красный"]][color_dict["Желтый"]] = 0.7

colorMatr[color_dict["Синий"]][color_dict["Оранжевый"]] = colorMatr[color_dict["Оранжевый"]][color_dict["Синий"]] = 0.2
colorMatr[color_dict["Синий"]][color_dict["Белый"]] = colorMatr[color_dict["Белый"]][color_dict["Синий"]] = 0.1
colorMatr[color_dict["Синий"]][color_dict["Зеленый"]] = colorMatr[color_dict["Зеленый"]][color_dict["Синий"]] = 0.4
colorMatr[color_dict["Синий"]][color_dict["Фиолетовый"]] = colorMatr[color_dict["Фиолетовый"]][color_dict["Синий"]] = 0.8
colorMatr[color_dict["Синий"]][color_dict["Красный"]] = colorMatr[color_dict["Красный"]][color_dict["Синий"]] = 0.3

colorMatr[color_dict["Оранжевый"]][color_dict["Белый"]] = colorMatr[color_dict["Белый"]][color_dict["Оранжевый"]] = 0
colorMatr[color_dict["Оранжевый"]][color_dict["Зеленый"]] = colorMatr[color_dict["Зеленый"]][color_dict["Оранжевый"]] = 0.2
colorMatr[color_dict["Оранжевый"]][color_dict["Фиолетовый"]] = colorMatr[color_dict["Фиолетовый"]][color_dict["Оранжевый"]] = 0.2
colorMatr[color_dict["Оранжевый"]][color_dict["Красный"]] = colorMatr[color_dict["Красный"]][color_dict["Оранжевый"]] = 0.6

colorMatr[color_dict["Белый"]][color_dict["Зеленый"]] = colorMatr[color_dict["Зеленый"]][color_dict["Белый"]] = 0.1
colorMatr[color_dict["Белый"]][color_dict["Фиолетовый"]] = colorMatr[color_dict["Фиолетовый"]][color_dict["Белый"]] = 0
colorMatr[color_dict["Белый"]][color_dict["Красный"]] = colorMatr[color_dict["Красный"]][color_dict["Белый"]] = 0

colorMatr[color_dict["Зеленый"]][color_dict["Фиолетовый"]] = colorMatr[color_dict["Фиолетовый"]][color_dict["Зеленый"]] = 0.2
colorMatr[color_dict["Зеленый"]][color_dict["Красный"]] = colorMatr[color_dict["Красный"]][color_dict["Зеленый"]] = 0.1

colorMatr[color_dict["Фиолетовый"]][color_dict["Красный"]] = colorMatr[color_dict["Красный"]][color_dict["Фиолетовый"]] = 0.3

df["ручная работа"] = df["ручная работа"].map(lambda elem: 1 if elem == True else 0)
df["натуральные материалы"] = df["натуральные материалы"].map(lambda elem: 1 if elem == True else 0)

smell_tree = [
    {"семейство": "Цветочные", "категория": "нет", "запах": "Розы", "характеристика": "свежий, романтичный, мягкий"},
    {"семейство": "Цветочные", "категория": "нет", "запах": "Лаванда", "характеристика": "успокаивающий, травяной, сладкий"},
    {"семейство": "Цветочные", "категория": "нет", "запах": "Жасмин", "характеристика": "экзотический, сладкий"},

    {"семейство": "Фруктовые", "категория": "нет", "запах": "Яблоко", "характеристика": "сочный, сладкий, освежающий"},
    {"семейство": "Фруктовые", "категория": "Цитрусовые", "запах": "Лимон", "характеристика": "кислый, свежий, бодрящий"},
    {"семейство": "Фруктовые", "категория": "Цитрусовые", "запах": "Грейпфрут", "характеристика": "свежий, бодрящий"},

    {"семейство": "Древесные", "категория": "нет", "запах": "Дуб", "характеристика": "тёплый, землистый"},
    {"семейство": "Древесные", "категория": "Хвойные", "запах": "Кедр", "характеристика": "свежий, природный"},
    {"семейство": "Древесные", "категория": "Хвойные", "запах": "Сосна", "характеристика": "свежий, лесной, чистый"},

    {"семейство": "Пряные", "категория": "нет", "запах": "Имбирь", "характеристика": "острый, бодрящий, согревающий"},
    {"семейство": "Пряные", "категория": "нет", "запах": "Корица", "характеристика": "сладкий, уютный"},
    {"семейство": "Пряные", "категория": "нет", "запах": "Кардамон", "характеристика": "пряный, экзотический"},
    {"семейство": "Пряные", "категория": "Травяные", "запах": "Мята", "характеристика": "свежий, прохладный, бодрящий"},
    {"семейство": "Пряные", "категория": "Травяные", "запах": "Шалфей", "характеристика": "травяной, успокаивающий, землистый"},

    {"семейство": "Сладкие", "категория": "нет", "запах": "Ваниль", "характеристика": "bitter-sweet, rich, creamy"},
    {"семейство": "Сладкие", "категория": "нет", "запах": "Карамель", "характеристика": "creamy, sweet, nutty"},
    {"семейство": "Сладкие", "категория": "нет", "запах": "Мед", "характеристика": "sweet, creamy, chocolatey"}
]

smell_to_family = {item["запах"].lower(): item["семейство"].lower() for item in smell_tree}

df["запах"] = df['иерархия'].apply(lambda x: x[-1] if len(x) > 0 else None)
df["категория"] = df['иерархия'].apply(lambda x: x[1] if len(x) > 2 else x[0])

del df["иерархия"]

df['категория'] = df['категория'].str.strip()
smell_df['категория'] = smell_df['категория'].str.strip()

merge_df = pd.merge(df, smell_df, on="категория", how="left")

merge_df["Древесные"] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
merge_df["Пряные"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
merge_df["Сладкие"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0]
merge_df["Травяные"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
merge_df["Фруктовые"] = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
merge_df["Хвойные"] = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
merge_df["Цветочные"] = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
merge_df["Цитрусовые"] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

layer1 = {"Цветочные": 0, "Фруктовые": 1, "Древесные": 2, "Пряные": 3, "Сладкие": 4}
treeLayer1 = np.zeros((len(layer1), len(layer1)), dtype=float)

for key in layer1:
    treeLayer1[layer1[key]][layer1[key]] = 0

treeLayer1[layer1["Цветочные"]][layer1["Фруктовые"]] = treeLayer1[layer1["Фруктовые"]][layer1["Цветочные"]] = 0.5
treeLayer1[layer1["Цветочные"]][layer1["Древесные"]] = treeLayer1[layer1["Древесные"]][layer1["Цветочные"]] = 0.1
treeLayer1[layer1["Цветочные"]][layer1["Пряные"]] = treeLayer1[layer1["Пряные"]][layer1["Цветочные"]] = 0.3
treeLayer1[layer1["Цветочные"]][layer1["Сладкие"]] = treeLayer1[layer1["Сладкие"]][layer1["Цветочные"]] = 0.6

treeLayer1[layer1["Фруктовые"]][layer1["Древесные"]] = treeLayer1[layer1["Древесные"]][layer1["Фруктовые"]] = 0.1
treeLayer1[layer1["Фруктовые"]][layer1["Пряные"]] = treeLayer1[layer1["Пряные"]][layer1["Фруктовые"]] = 0.3
treeLayer1[layer1["Фруктовые"]][layer1["Сладкие"]] = treeLayer1[layer1["Сладкие"]][layer1["Фруктовые"]] = 0.8

treeLayer1[layer1["Древесные"]][layer1["Пряные"]] = treeLayer1[layer1["Пряные"]][layer1["Древесные"]] = 0.2
treeLayer1[layer1["Древесные"]][layer1["Сладкие"]] = treeLayer1[layer1["Сладкие"]][layer1["Древесные"]] = 0

treeLayer1[layer1["Пряные"]][layer1["Сладкие"]] = treeLayer1[layer1["Сладкие"]][layer1["Пряные"]] = 0.1

layer2 = {"Розы": 0, "Лаванда": 1, "Жасмин": 2, "Яблоко": 3, "Цитрусовые": 4,
          "Дуб": 5, "Хвойные": 6, "Имбирь": 7, "Корица": 8, "Кардамон": 9,
          "Травные": 10, "Ваниль": 11, "Карамель": 12, "Мед": 13}

treeLayer2 = np.zeros((len(layer2), len(layer2)), dtype=float)

for key in layer2:
    treeLayer2[layer2[key]][layer2[key]] = 0

treeLayer2[layer2["Розы"]][layer2["Лаванда"]] = treeLayer2[layer2["Лаванда"]][layer2["Розы"]] = 0.6
treeLayer2[layer2["Розы"]][layer2["Жасмин"]] = treeLayer2[layer2["Жасмин"]][layer2["Розы"]] = 0.6
treeLayer2[layer2["Розы"]][layer2["Яблоко"]] = treeLayer2[layer2["Яблоко"]][layer2["Розы"]] = 0.4
treeLayer2[layer2["Розы"]][layer2["Цитрусовые"]] = treeLayer2[layer2["Цитрусовые"]][layer2["Розы"]] = 0.2
treeLayer2[layer2["Розы"]][layer2["Дуб"]] = treeLayer2[layer2["Дуб"]][layer2["Розы"]] = 0.2
treeLayer2[layer2["Розы"]][layer2["Хвойные"]] = treeLayer2[layer2["Хвойные"]][layer2["Розы"]] = 0.3
treeLayer2[layer2["Розы"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Розы"]] = 0.5
treeLayer2[layer2["Розы"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Розы"]] = 0.4
treeLayer2[layer2["Розы"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Розы"]] = 0.4
treeLayer2[layer2["Розы"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Розы"]] = 0.5
treeLayer2[layer2["Розы"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Розы"]] = 0.5
treeLayer2[layer2["Розы"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Розы"]] = 0.4
treeLayer2[layer2["Розы"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Розы"]] = 0.5

treeLayer2[layer2["Лаванда"]][layer2["Жасмин"]] = treeLayer2[layer2["Жасмин"]][layer2["Лаванда"]] = 0.6
treeLayer2[layer2["Лаванда"]][layer2["Яблоко"]] = treeLayer2[layer2["Яблоко"]][layer2["Лаванда"]] = 0.4
treeLayer2[layer2["Лаванда"]][layer2["Цитрусовые"]] = treeLayer2[layer2["Цитрусовые"]][layer2["Лаванда"]] = 0.3
treeLayer2[layer2["Лаванда"]][layer2["Дуб"]] = treeLayer2[layer2["Дуб"]][layer2["Лаванда"]] = 0.3
treeLayer2[layer2["Лаванда"]][layer2["Хвойные"]] = treeLayer2[layer2["Хвойные"]][layer2["Лаванда"]] = 0.4
treeLayer2[layer2["Лаванда"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Лаванда"]] = 0.6
treeLayer2[layer2["Лаванда"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Лаванда"]] = 0.5
treeLayer2[layer2["Лаванда"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Лаванда"]] = 0.5
treeLayer2[layer2["Лаванда"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Лаванда"]] = 0.7
treeLayer2[layer2["Лаванда"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Лаванда"]] = 0.3
treeLayer2[layer2["Лаванда"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Лаванда"]] = 0.2
treeLayer2[layer2["Лаванда"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Лаванда"]] = 0.2

treeLayer2[layer2["Жасмин"]][layer2["Яблоко"]] = treeLayer2[layer2["Яблоко"]][layer2["Жасмин"]] = 0.5
treeLayer2[layer2["Жасмин"]][layer2["Цитрусовые"]] = treeLayer2[layer2["Цитрусовые"]][layer2["Жасмин"]] = 0.4
treeLayer2[layer2["Жасмин"]][layer2["Дуб"]] = treeLayer2[layer2["Дуб"]][layer2["Жасмин"]] = 0.3
treeLayer2[layer2["Жасмин"]][layer2["Хвойные"]] = treeLayer2[layer2["Хвойные"]][layer2["Жасмин"]] = 0.3
treeLayer2[layer2["Жасмин"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Жасмин"]] = 0.5
treeLayer2[layer2["Жасмин"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Жасмин"]] = 0.4
treeLayer2[layer2["Жасмин"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Жасмин"]] = 0.3
treeLayer2[layer2["Жасмин"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Жасмин"]] = 0.5
treeLayer2[layer2["Жасмин"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Жасмин"]] = 0.4
treeLayer2[layer2["Жасмин"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Жасмин"]] = 0.8
treeLayer2[layer2["Жасмин"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Жасмин"]] = 0.5

treeLayer2[layer2["Яблоко"]][layer2["Цитрусовые"]] = treeLayer2[layer2["Цитрусовые"]][layer2["Яблоко"]] = 0.5
treeLayer2[layer2["Яблоко"]][layer2["Дуб"]] = treeLayer2[layer2["Дуб"]][layer2["Яблоко"]] = 0.3
treeLayer2[layer2["Яблоко"]][layer2["Хвойные"]] = treeLayer2[layer2["Хвойные"]][layer2["Яблоко"]] = 0.3
treeLayer2[layer2["Яблоко"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Яблоко"]] = 0.5
treeLayer2[layer2["Яблоко"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Яблоко"]] = 0.6
treeLayer2[layer2["Яблоко"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Яблоко"]] = 0.4
treeLayer2[layer2["Яблоко"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Яблоко"]] = 0.6
treeLayer2[layer2["Яблоко"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Яблоко"]] = 0.4
treeLayer2[layer2["Яблоко"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Яблоко"]] = 0.7
treeLayer2[layer2["Яблоко"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Яблоко"]] = 0.4

treeLayer2[layer2["Цитрусовые"]][layer2["Дуб"]] = treeLayer2[layer2["Дуб"]][layer2["Цитрусовые"]] = 0.3
treeLayer2[layer2["Цитрусовые"]][layer2["Хвойные"]] = treeLayer2[layer2["Хвойные"]][layer2["Цитрусовые"]] = 0.4
treeLayer2[layer2["Цитрусовые"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Цитрусовые"]] = 0.6
treeLayer2[layer2["Цитрусовые"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Цитрусовые"]] = 0.5
treeLayer2[layer2["Цитрусовые"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Цитрусовые"]] = 0.3
treeLayer2[layer2["Цитрусовые"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Цитрусовые"]] = 0.4
treeLayer2[layer2["Цитрусовые"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Цитрусовые"]] = 0.2
treeLayer2[layer2["Цитрусовые"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Цитрусовые"]] = 0.3
treeLayer2[layer2["Цитрусовые"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Цитрусовые"]] = 0.4

treeLayer2[layer2["Дуб"]][layer2["Хвойные"]] = treeLayer2[layer2["Хвойные"]][layer2["Дуб"]] = 0.5
treeLayer2[layer2["Дуб"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Дуб"]] = 0.4
treeLayer2[layer2["Дуб"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Дуб"]] = 0.3
treeLayer2[layer2["Дуб"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Дуб"]] = 0.4
treeLayer2[layer2["Дуб"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Дуб"]] = 0.4
treeLayer2[layer2["Дуб"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Дуб"]] = 0.3
treeLayer2[layer2["Дуб"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Дуб"]] = 0.2
treeLayer2[layer2["Дуб"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Дуб"]] = 0.3

treeLayer2[layer2["Хвойные"]][layer2["Имбирь"]] = treeLayer2[layer2["Имбирь"]][layer2["Хвойные"]] = 0.5
treeLayer2[layer2["Хвойные"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Хвойные"]] = 0.5
treeLayer2[layer2["Хвойные"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Хвойные"]] = 0.4
treeLayer2[layer2["Хвойные"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Хвойные"]] = 0.4
treeLayer2[layer2["Хвойные"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Хвойные"]] = 0.3
treeLayer2[layer2["Хвойные"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Хвойные"]] = 0.2
treeLayer2[layer2["Хвойные"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Хвойные"]] = 0.3

treeLayer2[layer2["Имбирь"]][layer2["Корица"]] = treeLayer2[layer2["Корица"]][layer2["Имбирь"]] = 0.6
treeLayer2[layer2["Имбирь"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Имбирь"]] = 0.5
treeLayer2[layer2["Имбирь"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Имбирь"]] = 0.5
treeLayer2[layer2["Имбирь"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Имбирь"]] = 0.4
treeLayer2[layer2["Имбирь"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Имбирь"]] = 0.3
treeLayer2[layer2["Имбирь"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Имбирь"]] = 0.5

treeLayer2[layer2["Корица"]][layer2["Кардамон"]] = treeLayer2[layer2["Кардамон"]][layer2["Имбирь"]] = 0.6
treeLayer2[layer2["Корица"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Имбирь"]] = 0.5
treeLayer2[layer2["Корица"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Имбирь"]] = 0.4
treeLayer2[layer2["Корица"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Имбирь"]] = 0.3
treeLayer2[layer2["Корица"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Имбирь"]] = 0.5

treeLayer2[layer2["Кардамон"]][layer2["Травные"]] = treeLayer2[layer2["Травные"]][layer2["Кардамон"]] = 0.4
treeLayer2[layer2["Кардамон"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Кардамон"]] = 0.4
treeLayer2[layer2["Кардамон"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Кардамон"]] = 0.3
treeLayer2[layer2["Кардамон"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Кардамон"]] = 0.4

treeLayer2[layer2["Травные"]][layer2["Ваниль"]] = treeLayer2[layer2["Ваниль"]][layer2["Травные"]] = 0.3
treeLayer2[layer2["Травные"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Травные"]] = 0.2
treeLayer2[layer2["Травные"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Травные"]] = 0.3

treeLayer2[layer2["Ваниль"]][layer2["Карамель"]] = treeLayer2[layer2["Карамель"]][layer2["Ваниль"]] = 0.7
treeLayer2[layer2["Ваниль"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Ваниль"]] = 0.8

treeLayer2[layer2["Карамель"]][layer2["Мед"]] = treeLayer2[layer2["Мед"]][layer2["Карамель"]] = 0.9

layer3 = {"Лимон": 0, "Грейпфрут": 1, "Кедр": 2, "Сосна": 3, "Мята": 4, "Шалфей": 5}
treeLayer3 = np.zeros((len(layer3), len(layer3)), dtype=float)

for key in layer3:
    treeLayer3[layer3[key]][layer3[key]] = 0

treeLayer3[layer3["Лимон"]][layer3["Грейпфрут"]] = treeLayer3[layer3["Грейпфрут"]][layer3["Лимон"]] = 0.7
treeLayer3[layer3["Лимон"]][layer3["Кедр"]] = treeLayer3[layer3["Кедр"]][layer3["Лимон"]] = 0.4
treeLayer3[layer3["Лимон"]][layer3["Сосна"]] = treeLayer3[layer3["Сосна"]][layer3["Лимон"]] = 0.4
treeLayer3[layer3["Лимон"]][layer3["Мята"]] = treeLayer3[layer3["Мята"]][layer3["Лимон"]] = 0.5
treeLayer3[layer3["Лимон"]][layer3["Шалфей"]] = treeLayer3[layer3["Шалфей"]][layer3["Лимон"]] = 0.4

treeLayer3[layer3["Грейпфрут"]][layer3["Кедр"]] = treeLayer3[layer3["Кедр"]][layer3["Грейпфрут"]] = 0.3
treeLayer3[layer3["Грейпфрут"]][layer3["Сосна"]] = treeLayer3[layer3["Сосна"]][layer3["Грейпфрут"]] = 0.3
treeLayer3[layer3["Грейпфрут"]][layer3["Мята"]] = treeLayer3[layer3["Мята"]][layer3["Грейпфрут"]] = 0.4
treeLayer3[layer3["Грейпфрут"]][layer3["Шалфей"]] = treeLayer3[layer3["Шалфей"]][layer3["Грейпфрут"]] = 0.3

treeLayer3[layer3["Кедр"]][layer3["Сосна"]] = treeLayer3[layer3["Сосна"]][layer3["Кедр"]] = 0.8
treeLayer3[layer3["Кедр"]][layer3["Мята"]] = treeLayer3[layer3["Мята"]][layer3["Кедр"]] = 0.5
treeLayer3[layer3["Кедр"]][layer3["Шалфей"]] = treeLayer3[layer3["Шалфей"]][layer3["Кедр"]] = 0.5

treeLayer3[layer3["Сосна"]][layer3["Мята"]] = treeLayer3[layer3["Мята"]][layer3["Сосна"]] = 0.5
treeLayer3[layer3["Сосна"]][layer3["Шалфей"]] = treeLayer3[layer3["Шалфей"]][layer3["Сосна"]] = 0.6

treeLayer3[layer3["Мята"]][layer3["Шалфей"]] = treeLayer3[layer3["Шалфей"]][layer3["Мята"]] = 0.5

layer = [layer1, layer2, layer3]
tree = [treeLayer1, treeLayer2, treeLayer3]

def getDataFrameStat(df):
    dfNew = df.copy()
    for elem in ["цвет", "страна"]:
        del dfNew[elem]
    return dfNew

def getDistance(v1, v2, nPow):
    res = 0
    for i in range(len(v1)):
        try:
            val1 = float(v1[i])
            val2 = float(v2[i])
            if not isnan(v1[i]) or not isnan(v2[i]):
                res += pow(abs(v1[i] - v2[i]), nPow)
        except ValueError:
            continue
    return pow(res, 1 / nPow)

def getManhanttanDistance(v1, v2):
    return getDistance(v1, v2, 1)

def getEuclideanDistance(v1, v2):
    return getDistance(v1, v2, 2)

def getCosDistance(v1, v2):
    v1tmp = [x for x in v1 if isinstance(x, (int, float))]
    v2tmp = [x for x in v2 if isinstance(x, (int, float))]
    n = len(v1tmp)
    indArr = [i for i, (elem1, elem2) in enumerate(zip(v1tmp, v2tmp)) if isnan(elem1) or isnan(elem2)]
    v1tmp[:] = [elem for i, elem in enumerate(v1tmp) if i not in indArr]
    v2tmp[:] = [elem for i, elem in enumerate(v2tmp) if i not in indArr]

    return 1 - np.dot(v1tmp, v2tmp) / (norm(v1tmp) * norm(v2tmp))

def getTreeDistace(v1, v2):
    res = 0
    size = max(len(v1), len(v2))

    for i in range(size):
        try:
            res += tree[i][layer[i][v1[i]]][layer[i][v2[i]]]
        except:
            res += 0.5

    return res / size

def getCountyDistance(v1, v2):
    value = countryMatr[country_dict[v1]][country_dict[v2]]
    return value

def getColorDistance(v1, v2):
    value = colorMatr[color_dict[v1]][color_dict[v2]]
    return value

def getSimilarity(id, matr, nameArr):
    data = matr[id]
    res = pd.DataFrame(
        zip(data, nameArr),
        index = np.arange(len(matr)),
        columns = ["расстояние", "название"]
    )
    return res.sort_values("расстояние")

def calculateDistance(f, df):
    matrData = df.values.tolist()
    n = len(matrData)
    matrRes = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            matrRes[i][j] = matrRes[j][i] = f(matrData[i], matrData[j])

    return matrRes / matrRes.max()

def _getJacquard(v1, v2):
    v1_tmp = [x for x in v1 if isinstance(x, (int, float))]
    v2_tmp = [x for x in v2 if isinstance(x, (int, float))]
    intersection = sum(min(x, y) for x, y in zip(v1_tmp, v2_tmp))
    union = sum(max(x, y) for x, y in zip(v1_tmp, v2_tmp))

    if union == 0:
        return 0
    return intersection / union

def getJacquard(df):
    matrData = df.values.tolist()
    n = len(matrData)
    matrRes = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            matrRes[i][j] = matrRes[j][i] = _getJacquard(matrData[i], matrData[j])
    return matrRes

def calcDistanceCompined(df, dfTree):
    dfTree = dfTree["иерархия"]
    dfStatParams = getDataFrameStat(df)
    dfJac = dfStatParams.copy()

    matrTree = calculateDistance(getTreeDistace, dfTree)
    matrEucl = calculateDistance(getEuclideanDistance, dfStatParams)
    # matrMan = calcDistance(getManhattanDistance, dfStatParams)
    # matrCos = calcDistance(getCos, dfStatParams)
    matrBrand = calculateDistance(getColorDistance, df["цвет"])
    matrColor = calculateDistance(getCountyDistance, df["страна"])
    matrJac = getJacquard(dfJac)

    xTree = matrTree.max()
    xEuci = matrEucl.max()
    # xStat = matrMan.max()
    # xStat = matrCos.max()
    xJac = matrJac.max()
    xBrand = matrBrand.max()
    xColor = matrColor.max()

    kJac, kTree, kEuci, kBrand, kColor = 2, 2, 5, 1, 2

    return (kJac * matrJac + kTree * matrTree + kEuci * matrEucl + kBrand * matrBrand + kColor * matrColor) / \
        (kJac * xJac + kTree * xTree + kEuci * xEuci + kBrand * xBrand + kColor * xColor)

def draw(matrRes, nameArr, title, color='Inferno'):
    fig = px.imshow(matrRes, x=nameArr, y=nameArr, color_continuous_scale=color, title=title)
    fig.update_layout(width=1000, height=1200)
    fig.update_traces(text=nameArr)
    fig.update_xaxes(side="top")
    fig.show()

def drawManhattanDistance():
    matrRes = calculateDistance(getManhanttanDistance, getDataFrameStat(df))
    draw(matrRes, nameArr, "Манхэттенское расстояние")

def drawEuclideanDistance():
    matrRes = calculateDistance(getEuclideanDistance, getDataFrameStat(df))
    draw(matrRes, nameArr, "Евклидово расстояние")

def drawCosDistance():
    matrRes = calculateDistance(getCosDistance, getDataFrameStat(df))
    draw(matrRes, nameArr, "Косинусное подобие")

def drawCountryDistance():
    matrRes = calculateDistance(getCountyDistance, df["страна"])
    draw(matrRes, nameArr, "Расстояние по странам")

def drawColorDistance():
    matrRes = calculateDistance(getColorDistance, df["цвет"])
    draw(matrRes, nameArr, "Расстояние по цветам")

def drawJacquardDistance():
    matrRes = getJacquard(getDataFrameStat(df))
    np.fill_diagonal(matrRes, 0)
    draw(matrRes, nameArr, "Мера Жаккара")

def drawTreeDistance():
    matrRes = calculateDistance(getTreeDistace, dfTree["иерархия"])
    draw(matrRes, nameArr, "Расстояние по дереву")

def drawCompinedDistance():
    draw(calcDistanceCompined(df, dfTree), nameArr, "Комбинированная мера")

#lab3

#-----------------------------------------------------------------------------
#                                ЗАДАЧИ                                      #
#-----------------------------------------------------------------------------

matrSimilarity = calcDistanceCompined(df, dfTree)

def printRes(arr):
    print("\n%sРасстояние \t\t\t Название%s" % (Colors.GREEN, Colors.BASE))
    for elem in arr:
        for key, value in elem.items():
            print("{0}\t\t{1}".format(value, key))

# Задача 1
TASK_1_CONDITION = """
%sУсловие задачи%s

Вход: 1 объект (затравочный).
Выход: список рекомендаций, ранжированный по убыванию близости с затравкой.
    Примените Вашу обобщающую меру близости.
""" %(Colors.GREEN, Colors.BASE)

def _findSimilar(name):
    ind = df0[F_NAME].tolist().index(name)
    listSimilarity = getSimilarity(ind, matrSimilarity, nameArr)
    return listSimilarity

def findSimilarLike(name):
    listSimilarity = _findSimilar(name)
    return listSimilarity[listSimilarity[F_NAME] != name]

def task1():
    print(TASK_1_CONDITION)
    try:
        res = findSimilarLike(input("%sВведите затравочный объект:%s " %(Colors.GREEN, Colors.BASE)))
        #Ocean Mist
        #Vanilla Dream
    except:
        print("%s\nТакого объекта не существует%s" % (Colors.RED, Colors.BASE))
    else:
        print("\n", res)


# Задача 2
TASK_2_CONDITION = """
%sУсловие задачи%s

Вход: массив объектов (лайков).
Выход: сформированный ранжированный список рекомендаций.
""" %(Colors.GREEN, Colors.BASE)

def _findSimilarMany(nameArr):
    recList = []
    for name in nameArr:
        rec = _findSimilar(name)
        recList.append(rec.loc[rec[F_NAME].isin(nameArr) == False])

    dfRes = defaultdict(lambda: 1e2)
    for rec in recList:
        for i, row in rec.iterrows():
            curName = row[F_NAME]
            curDist = row[F_DIST]
            dfRes[curName] = min(dfRes[curName], curDist)

    return dfRes

def findSimilarMany(nameArr):
    resDict = _findSimilarMany(nameArr)
    return sorted(
        [{key: elem} for key, elem in resDict.items()],
        key=lambda elem: list(elem.values())[0]
    )

def task2():
    print(TASK_2_CONDITION)
    try:
        res = findSimilarMany(input("%sВведите лайкнутые объекты, разделенные запятой:%s " %(Colors.GREEN, Colors.BASE)).split(","))
        #Ocean Mist,Cinnamon Spice
        #Midnight Jasmine,Citrus Grove
    except:
        print("%s\nНедопустимых формат ввода, либо таких объектов не существует%s" %(Colors.RED, Colors.BASE))
    else:
        printRes(res)


# Задача 3

TASK_3_CONDITION = """
%sУсловие задачи%s

Вход: массив затравочных объектов и массив дизлайков.
Выход: сформированный ранжированный список рекомендаций.
""" % (Colors.GREEN, Colors.BASE)


def delOpposite(dict, nameArr):
    for name in nameArr:
        if name in dict.keys():
            del dict[name]

    return dict

def findSimilarLikeDislike(likesArr=[], dislikesArr=[]):
    likesRec = delOpposite(_findSimilarMany(likesArr), dislikesArr)
    dislikesRec = delOpposite(_findSimilarMany(dislikesArr), likesArr)
    dictRes = {}

    if len(likesArr) == 0:
        for key, elem in dislikesRec.items():
            dictRes[key] = 1 - elem
        return sorted([{key: elem} for key, elem in dictRes.items()], key=lambda elem: list(elem.values())[0])

    for key in likesRec.keys():
        if likesRec[key] <= dislikesRec[key]:
            dictRes[key] = likesRec[key]
    return sorted([{key: elem} for key, elem in dictRes.items()], key=lambda elem: list(elem.values())[0])

def task3():
    print(TASK_3_CONDITION)
    try:
        likesArr = input("%sВведите лайкнутые объекты, разделенные запятой:%s " %(Colors.GREEN, Colors.BASE)).split(",")
        #Ocean Mist,Cinnamon Spice
        dislikesArr=input("%sВведите дизлайкнутые объекты, разделенные запятой:%s " %(Colors.GREEN, Colors.BASE)).split(",")
        #Midnight Jasmine
        for arr in [likesArr, dislikesArr]:
            while "" in arr:
                arr.remove("")

        res = findSimilarLikeDislike(
            likesArr=likesArr,
            dislikesArr=dislikesArr,
        )

    except:
        print("%s\nНедопустимых формат ввода, либо таких объектов не существует%s" %(Colors.RED, Colors.BASE))
    else:
        printRes(res)
        
        
def ui_lab4():

    pn.extension()

    def getArrFromSeries(data):
        arr = []
        for elem in data:
            arr.append(elem)
        return arr

    def getDataFrameFromArr(data, reverse=0):
        resArr = []
        for elem in data:
            for key in elem.keys():
                resArr.append({"Название": key, "Величина схожести": 1 - elem[key] + reverse * (2 * elem[key] - 1)})

        return pd.DataFrame(resArr, index=range(1, len(resArr) + 1), columns=["Название", "Величина схожести"])

    namesUI = getArrFromSeries(nameArr)

    choiceLiked = pn.widgets.MultiChoice(
        name='👍👍👍 Нравится 👍👍👍',
        value=[],
        width=320,
        options=namesUI)

    choiceDisliked = pn.widgets.MultiChoice(
        name='👎👎👎 НЕ нравится 👎👎👎',
        value=[],
        width=320,
        options=namesUI)

    markdownError = pn.pane.Markdown('<h3 style="font-family: serif; text-align: center; color: red;">Ошибка ввода</h3>',
                                     width=800,
                                     visible=False)

    markdownDefault = pn.pane.Markdown("#### Выберете то, что: ", width=800, visible=True)
    markdownResultMustTitle = pn.pane.Markdown("#### Попробуйте следующие свечи: ", width=300, visible=False)
    markdownResultMaybeTitle = pn.pane.Markdown("#### Возможно Вам понравятся: ", width=300, visible=False)

    bokeh_formatters = {
        "Величина схожести": {'type': 'progress', 'max': 1}
    }

    tableRecMust = pn.widgets.Tabulator(visible=False, formatters=bokeh_formatters)
    tableRecMaybe = pn.widgets.Tabulator(visible=False, formatters=bokeh_formatters)

    def _initMustTable(recArr):
        tableRecMust.value = getDataFrameFromArr(recArr)

        markdownResultMustTitle.visible = True
        tableRecMust.visible = True

    def _initMaybeTable(recArr):
        tableRecMaybe.value = getDataFrameFromArr(recArr)

        markdownResultMaybeTitle.visible = True
        tableRecMaybe.visible = True

    def _changeStatusError(isError):
        if isError:
            markdownError.visible = True
            markdownDefault.visible = False
            markdownResultMustTitle.visible = False
            markdownResultMaybeTitle.visible = False

            tableRecMust.visible = False
            tableRecMaybe.visible = False
        else:
            markdownError.visible = False
            markdownDefault.visible = True

    def _splitMustMaybe(recArr):
        recMust, recMaybe = [], []
        for rec in recArr:
            for key in rec.keys():
                if rec[key] <= 0.5:
                    recMust.append(rec)
                else:
                    recMaybe.append(rec)
        return recMust, recMaybe

    def _splitMustMaybeDict(recDict):
        recMust, recMaybe = [], []
        for name, value in recDict.items():
            if value <= 0.3:
                recMust.append({name: value})
            else:
                recMaybe.append({name: value})
        return recMust, recMaybe

    def _isRightInput(arr1, arr2):
        inner = list(set(arr1) & set(arr2))
        return len(inner) == 0

    def _getDefaultResult(nameArr):
        resArr = []
        for name in nameArr:
            resArr.append({name: 1})
        return resArr

    def _getDefaultResultParams(nameArr):
        resArr = {}
        for name in nameArr:
            resArr[name] = 0
        return resArr

    def _getRecommendationArr(likesArr, dislikesArr):
        recArr = None

        if len(likesArr) and len(dislikesArr):
            recArr = findSimilarLikeDislike(likesArr, dislikesArr)
        elif len(likesArr) and len(dislikesArr) == 0:
            recArr = findSimilarMany(likesArr)
        elif len(likesArr) == 0 and len(dislikesArr):
            recArr = findSimilarLikeDislike(likesArr, dislikesArr)
        else:
            recArr = _getDefaultResult(namesUI)
        return recArr

    def _giveRecommendation(likesArr, dislikesArr):
        recArr = _getRecommendationArr(likesArr, dislikesArr)

        recMust, recMaybe = _splitMustMaybe(recArr)

        _initMustTable(recMust)
        _initMaybeTable(recMaybe)

    def run(a):
        likesArr = choiceLiked.value
        dislikesArr = choiceDisliked.value

        if not _isRightInput(likesArr, dislikesArr):
            _changeStatusError(isError=True)
            return

        _changeStatusError(isError=False)
        _giveRecommendation(likesArr, dislikesArr)

    button = pn.widgets.Button(
        name='Готово',
        button_type='success',
        width=50,
        height=40,
        margin=(24, 100, 10, 10))
    button.on_click(run)

    pLikes = pn.Column(
        markdownDefault,
        markdownError,
        pn.Row(
            pn.Column(choiceLiked, height=800),
            pn.Column(choiceDisliked, height=800),
            button,
            pn.Column(markdownResultMustTitle,
                      tableRecMust,
                      markdownResultMaybeTitle,
                      tableRecMaybe))
    )

    materialWidget = pn.widgets.CheckBoxGroup(
        name='Материал',
        options=['Парафиновый воск', 'Соевый воск', 'Пчелиный воск'],
        inline=False
    )

    materialElem = pn.Card(
        materialWidget,
        title = 'Материал',
        width = 400,
        margin=(10, 30, 10, 10)
    )

    countryArr = list(set(df0['страна'].tolist()))

    countryWidget = pn.widgets.MultiChoice(
        value=[],
        options=countryArr
    )

    countryElem = pn.Card(
        countryWidget,
        title='Страна-производитель',
        width=400,
        margin=(10, 30, 10, 10)
    )

    brandArr = list(set(df0['бренд'].tolist()))

    brandWidget = pn.widgets.MultiChoice(
        value=[],
        options=brandArr
    )

    brandElem = pn.Card(
        brandWidget,
        title='Бренд',
        width=400,
        margin=(10, 30, 10, 10)
    )

    wickArr = list(set(df0['тип фитиля'].tolist()))

    wickWidget = pn.widgets.MultiChoice(
        value=[],
        options=wickArr
    )

    wickElem = pn.Card(
        wickWidget,
        title='Тип фитиля',
        width=400,
        margin=(10, 30, 10, 10)
    )

    familyArrT = df0['иерархия'].map(lambda elem: elem.split(',')).tolist()
    unique_categories = set()
    for sublist in familyArrT:
        unique_categories.update(sublist)
    cleanedArr = [item.lstrip() for item in list(unique_categories)]
    familyArr = [item for item in cleanedArr if item in categories_and_sub]

    familyWidget = pn.widgets.MultiChoice(
        value=[],
        options=familyArr
    )

    familyElem = pn.Card(
        familyWidget,
        title='Семейства',
        width=400,
        margin=(10, 30, 10, 10))

    smellLikeList = smells.columns.values.tolist()

    smellLikeList.remove("категория")

    smellArr = list(set(smellLikeList) | set(smells))
    smellArr.sort()

    smellWidget = pn.widgets.MultiSelect(
        value=[],
        size=10,
        options=smells_base
    )

    smellElem = pn.Card(
        smellWidget,
        title='Запахи',
        width=400,
        margin=(10, 60, 10, 10))

    markdownResultMustTitle2 = pn.pane.Markdown("#### Попробуйте следующие ароматы: ", width=300, visible=False)
    markdownResultMaybeTitle2 = pn.pane.Markdown("#### Возможно Вам понравятся: ", width=300, visible=False)

    tableRecMust2 = pn.widgets.Tabulator(visible=False, formatters=bokeh_formatters)
    tableRecMaybe2 = pn.widgets.Tabulator(visible=False, formatters=bokeh_formatters)

    def _initMustTable2(recArr):
        tableRecMust2.value = getDataFrameFromArr(recArr, 1)

        markdownResultMustTitle2.visible = True
        tableRecMust2.visible = True

    def _initMaybeTable2(recArr):
        tableRecMaybe2.value = getDataFrameFromArr(recArr, 1)

        markdownResultMaybeTitle2.visible = True
        tableRecMaybe2.visible = True

    # def _updateMaterial(materialArr):
    #     res = []
    #     for material in materialArr:
    #         res.append(material_dict[material])
    #     return res

    # def _updateWick(wickArr):
    #     res = []
    #     for wick in wickArr:
    #         res.append(wick_dict[wick])
    #     return res

    def sortDict(resDict):
        sorted_tuples = sorted(resDict.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        return sorted_dict

    def _updateResult(dataDict, nameArr, n):
        resDict = {}
        for key, value in dataDict.items():
            if value != 0:
                resDict[nameArr[key]] = 1 - value / n

        return sortDict(resDict)

    def _fromArrDictToDict(arrDict):
        resDict = {}
        for elem in arrDict:
            resDict.update(elem)
        return resDict

    def _getRecommendationParams(materialSelected, countrySelected, brandSelected,
                                 wickSelected, familySelected, smellSelected, colorSelected, merge_df):
        dfColumnsArr = merge_df.columns.values.tolist()
        indexDict = {}

        indexDict[dfColumnsArr.index('материал')] = materialSelected
        indexDict[dfColumnsArr.index('страна')] = countrySelected
        indexDict[dfColumnsArr.index('бренд')] = brandSelected
        indexDict[dfColumnsArr.index('тип фитиля')] = wickSelected
        indexDict[dfColumnsArr.index('цвет')] = colorSelected

        for family in familySelected:
            indexDict[dfColumnsArr.index(family)] = [1]
        for smell in smellSelected:
            smell = smell.lower()
            indexDict[dfColumnsArr.index(smell)] = [1]

        matrData = merge_df.values.tolist()
        sDict = {}
        for i in range(len(matrData)):
            s = 0
            for ind in indexDict.keys():
                if matrData[i][ind] in indexDict[ind]:
                    s += 1
            sDict[i] = s

        return sDict

    def getRecommendationParams(materialSelected, countrySelected, brandSelected,
                                wickSelected, familySelected, smellSelected, colorSelected, merge_df):
        nAll = 0
        if len(materialSelected):
            nAll += 1
        if len(countrySelected):
            nAll += 1
        if len(brandSelected):
            nAll += 1
        if len(wickSelected):
            nAll += 1
        if len(colorSelected):
            nAll += 1

        nAll += len(familySelected) + len(smellSelected)
        if nAll == 0:
            recDict = _getDefaultResultParams(namesUI)
        else:
            recDict = _getRecommendationParams(materialSelected, countrySelected, brandSelected, wickSelected, familySelected,
                                               smellSelected, colorSelected, merge_df)

        return _updateResult(recDict, nameArr, nAll)

    def _compareLikesParams(likesDict, paramsDict, familySelected, smellSelected, dislikesSelected):
        resDict = {}
        likesDictRes = {}

        if len(familySelected) != 0:
            for family in familySelected:
                for like in likesDict.keys():
                    # print(merge_df)
                    brand_data = merge_df[merge_df['название'] == like]
                    if family in brand_data['категория'].values:
                        likesDictRes[like] = likesDict[like]

        if len(smellSelected) != 0:
            for smell in smellSelected:
                smell = smell.lower()
                for like in likesDict.keys():
                    brand_data = merge_df[merge_df['название'] == like]
                    if smell in brand_data['запах'].values:
                        likesDictRes[like] = likesDict[like]
                    elif smell_to_family[smell] in brand_data['категория'].values:
                        likesDictRes[like] = likesDict[like]

        for key in dislikesSelected:
            if key in paramsDict.keys():
                del paramsDict[key]

        for key, value in likesDict.items():
            if key in paramsDict.keys():
                resDict[key] = (value + paramsDict[key]) * 0.5
                del paramsDict[key]
            else:
                resDict[key] = value * 0.5

        if len(paramsDict.keys()):
            for key, value in paramsDict.items():
                resDict[key] = 0.5 * value
        return resDict

    def giveRecommendationFull(materialSelected, countrySelected, brandSelected,
                               wickSelected, familySelected, smellSelected, likesSelected, dislikesSelected, colorSelected, merge_df):
        recDict = getRecommendationParams(materialSelected = materialSelected, countrySelected = countrySelected, brandSelected = brandSelected, wickSelected = wickSelected,
                                          familySelected = familySelected, smellSelected = smellSelected, colorSelected = colorSelected, merge_df = merge_df)
        if len(likesSelected) or len(dislikesSelected):
            recLikesArr = _getRecommendationArr(likesSelected, dislikesSelected)
            recLikesDict = _fromArrDictToDict(recLikesArr)
            recDict = _compareLikesParams(recLikesDict, recDict, familySelected, smellSelected, dislikesSelected)

        return _splitMustMaybeDict(sortDict(recDict))

    def runFull(a):
        materialSelected = materialWidget.value
        countrySelected = countryWidget.value
        brandSelected = brandWidget.value
        wickSelected = wickWidget.value
        familySelected = familyWidget.value
        smellSelected = smellWidget.value

        likesSelected = choiceLiked.value
        dislikesSelected = choiceDisliked.value

        if not _isRightInput(likesSelected, dislikesSelected):
            _changeStatusError(isError=True)
            return

        _changeStatusError(isError=False)

        # materialSelected = _updateMaterial(materialSelected)
        # wickSelected = _updateWick(wickSelected)

        giveRecommendationFull(materialSelected, countrySelected, brandSelected, wickSelected, familySelected, smellSelected,
                               likesSelected, dislikesSelected, merge_df)

    buttonFull = pn.widgets.Button(
        name='Готово',
        button_type='success',
        width=400,
        height=40,
        margin=(24, 100, 10, 10))
    buttonFull.on_click(runFull)

    elemArr = pn.Column(
        materialElem,
        countryElem,
        brandElem,
        wickElem,
        familyElem,
        smellElem,
        buttonFull
    )

    elemSet = pn.Row(
        elemArr,
        pn.Column(
            markdownResultMustTitle2,
            tableRecMust2,
            markdownResultMaybeTitle2,
            tableRecMaybe2
        )
    )

    tabs = pn.Tabs(("👍/👎", pLikes), ("⚙️", elemSet))
     tabs.show()
