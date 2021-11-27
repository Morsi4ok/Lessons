"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский, где слово - это входной параметр,
вторая функция - с русского на английский.
"""


def translate_en_to_ru(d, word):
    return d[word]


def translate_ru_to_en(d, word):
    for en, ru in d.items():
        if word == ru:
            return en


if __name__ == "__main__":
    dictionary = {"sun": "Солнце", "moon": "Луна"}

    print(translate_en_to_ru(dictionary, "sun"))
    print(translate_ru_to_en(dictionary, "Луна"))
