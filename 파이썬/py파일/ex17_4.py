print("20211127 이건호")

class Animal4(object):
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    def print_info(self):
        print(f"Animal 클래스 사용, 이름 : {self.name}")

class Cat4(Animal4):
    def __init__(self, name, color):
        Animal4.__init__(self, name)
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
    def print_info(self):
        print(f"서브 클래스 메소드 추가, 컬러 : {self.color}")

def main():
    animal = Animal4("일반동물")
    cat = Cat4("고양이", "회색")
    animal_list = [animal, cat]
    for item in animal_list:
        item.print_info()

if __name__ == "__main__":
    main()
    input()