print("20211127 이건호")

class AnimalY(object):
   def __init__(self):
      print(f"Animal.__init__()")

class Donkey(AnimalY):
   def __init__(self):
      print(f"Donkey.__init__()")
      super().__init__()

class Horse(AnimalY):
   def __init__(self):
      print(f"Horse.__init__()")
      super().__init__()

class Mule(Donkey,Horse):
   def __init__(self):
      print(f"Mule.__init__()")
      super().__init__()

def main():
   mule = Mule()

if __name__ =="__main__": 
   main()
   print(Mule.__mro__)
   print(Mule.mro())
   input()

