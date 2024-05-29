print("20211127 이건호")

class Beverage(object):
    def __init__(self, product, price, quantity):
        self.__product = product
        self.__price = price
        self.__quantity = quantity
    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product):
        self.__product = product
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    def get_total(self):
        return self.__price * self.__quantity
    def print_title(self):
        print("제품명\t단가\t수량\t금액")
    def print_data(self):
        print(
            self.__product + '\t' + str(self.__price)
            + '\t' + str(self.__quantity) + '\t' +
            str(self.get_total())
        )

def main():
    coke = Beverage("콜라", 2000, 15)
    coke.print_title()
    coke.print_data()
    cider = Beverage("사이다", 3000, 20)
    cider.print_data()
    sum = coke.get_total() + cider.get_total()
    print(f"전체 합계 = {sum}")

if __name__ == "__main__":
    main()
    input()