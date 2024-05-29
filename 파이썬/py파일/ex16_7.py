print("20211127 이건호")

class Animal(object):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def identify(self):
        return "동물"
    
def main():
    anim = Animal("야옹이")
    print("생성 동물 이름", anim.get_name())
    anim.set_name("여웅이")
    print("변경 동물 이름", anim.get_name())
    print(anim.identify())

if __name__ == "__main__":
    main()
    input()