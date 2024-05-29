print("20211127 이건호")

class Animal2(object):
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    def prinf_info(self):
        print(f"슈퍼 클래스 사용, 이름 : {self.name}")

class Cat2(Animal2):
    def __init__(self, name, color):
        Animal2.__init__(self, name)
        #super().__init__(name) #self 없음
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

def main():
    my_cat = Cat2("고양이", "Red")
    my_cat.prinf_info()
    print(f"서브 클래스 color 변수 추가 : {my_cat.color}")

if __name__ == "__main__":
    main()
    input()