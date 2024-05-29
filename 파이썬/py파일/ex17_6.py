print("20211127 이건호")

class AnimalX(object):
    def __init__(self):
        print(f"Animal__init__()")

class Donkey(AnimalX):
    def __init__(self):
        AnimalX.__init__(self)
        print(f"Donkey__init__()")

class Horse(AnimalX):
    def __init_(self):
        AnimalX.__init__(self)
        print(f"Horse__init__()")

class Mule(Donkey, Horse):
    def __init__(self):
        Donkey.__init__(self)
        Horse.__init__(self)
        print(f"Mule__init__()")

def main():
    mule = Mule()

if __name__ == "__main__":
    main()
    print(Mule.__mro__)
    print(Mule.mro())
    input()