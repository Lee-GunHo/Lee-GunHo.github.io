print("20211127 이건호")

class Circle(object):
    __PI = 3.141592
    def __init__(self, radius):
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def get_area(self):
        return Circle.__PI * (self.get_radius() ** 2)
    @classmethod
    def get_areac(cls, radius):
        return cls.__PI * (radius ** 2)
    @staticmethod
    def get_circumference(pi, radius):
        return 2 * pi * radius

def main():
    circle = Circle(10)
    print("객체 메소드", circle.get_area())

    print("클래스 메소드", Circle.get_areac(20))
    print("스태틱 메소드", Circle.get_circumference(3.14, 30))

if __name__ == "__main__":
    main()
    input()