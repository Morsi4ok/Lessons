"""
Оформить предыдущую задачу в виде программы, вынести функцию в отдельный файл, добавить комментарии с описанием.
"""
from my_func import filter_cars
# указывается год и выводит словари, где года машин старше


def main():
    car_list = [
        {
            "serial": 123456,
            "color": "red",
            "year": 1999,
        },
        {
            "serial": 234567,
            "color": "red",
            "year": 2020,
        },
        {
            "serial": 345678,
            "color": "red",
            "year": 2012,
        }
    ]
    year = int(input("Year: "))
    print(filter_cars(car_list, year))


if __name__ == "__main__":
    main()
