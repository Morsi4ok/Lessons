"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы,
которая считывает название города и выводит на печать страну.
"""


def check_city(city):
    country_cities = {"Belarus": ("Minsk", "Brest", "Vitebsk"), "Russia": ("Moscow", "SPB", "Sochi", "Krasnoyarsk")}
    for key, value in country_cities.items():
        if city in value:
            return key


if __name__ == "__main__":
    city = input("Название города: ")
    print(check_city(city))
