print("20211127 이건호")

class Car(object):
    def __init__(self):
        self.__speed = 0
    def set_speed(self,value):
        self.__speed = self.__speed+value
        print(f"자동차를 {self.__speed}로 가속함")
def main():
    car = Car()
    car.set_speed(30)
if __name__ == "__main__":
    main()
    input()