class Human:
    default_name = "tom"
    default_age = 26

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"{self.name} , {self.age}  , {self.__money} , {self.__house}")

    @staticmethod
    def default_info():
        print(f"{Human.default_name} , {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, rebate):
        if self.__money >= house.final_price(rebate):
            self.__make_deal(house, house.final_price(rebate))
            print("House purchase successful!")
        else:
            print("Not enough money")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, rebate):
        return self._price - rebate


class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=100000)


Human.default_info()
person = Human()
person.info()

house = SmallHouse()

person.buy_house(house, 0.1)
person.earn_money(120000)

person.buy_house(house, 0.1)
person.info()