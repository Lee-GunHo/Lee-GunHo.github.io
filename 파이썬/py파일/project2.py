class Refrigerator(object):

    def __init__(self, price, volume, color, energyce):
        self.__price = price
        self.__volume = volume
        self.__color = color
        self.__energyce = energyce

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def energyce(self):
        return self.__energyce

    @energyce.setter
    def energyce(self, value):
        self.__energyce = value

def main():
    refrigerator = Refrigerator(1100000, 832, "white", 2)
    print(refrigerator.price, refrigerator.volume, refrigerator.color, refrigerator.energyce)

if __name__ == "__main__":
    main()
    input()
