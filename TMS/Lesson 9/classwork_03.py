"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""


class Cat:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run{self.name}")

    def meow(self):
        print(f"bark{self.name}")


if __name__ == "__main__":
    cat = Cat(100, 100, "Sofi", 10)
    cat.jump()
    cat.run()
    cat.meow()
    print(cat.name)
    print(cat.height)
    print(cat.age)
    print(cat.weight)
