print("20211127 이건호")

class Car(object):
    def __init__(self, speed, price):
        self.__speed = speed
        self.__price = price
    def get_speed(self):
        return self.__speed
    def set_speed(self,value):
        if value >= 0:
            self.__speed = self.__speed+value
            print(f"자동차를 {value}가속함")
        else:
            print(" 0 보다 커야함. 입력실패.")
    def get_price(self):
        return self.__price
    def set_price(self,value):
        self.__price = value

def main():
    car = Car(0,10000)
    print("원래 속도, 가격", car.get_speed(),car.get_price())
    car.set_speed(100)
    car.set_price(20000)
    print("변경속도,가격", car.get_speed(),car.get_price())
if __name__ == "__main__":
    main()
    input()