class Refrigerator(object):

    def __init__(self):
        self.__price = 0
        self.__volume = 0
        self.__color = None
        self.__energyce = 0

    def get_price(self):
        return self.__price
    def set_price(self,value):
        self.__price = value
    
    def get_volume(self):
        return self.__volume
    def set_volume(self,value):
        self.__volume = value
    
    def get_color(self):
        return self.__color
    def set_color(self,value):
        self.__color = value
    
    def get_energyce(self):
        return self.__energyce
    def set_energyce(self,value):

        self.__energyce = value

def main():
    refrigerator = Refrigerator()
    refrigerator.set_price(1100000)
    refrigerator.set_volume(832)
    refrigerator.set_color("white")
    refrigerator.set_energyce(2)
    print("가격 :", refrigerator.get_price() ,"원 입니다.", "들어가는 용량 :",refrigerator.get_volume(),"L 입니다.", "색깔 :",refrigerator.get_color() ,"입니다.","에너지 효율등급 :",refrigerator.get_energyce(),"입니다.")

    
if __name__ == "__main__":
    main()
    input()
