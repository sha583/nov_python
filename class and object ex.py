class Rohit:
    def __init__(self, fullname,handed,place):#constructor
        self.fullname=fullname#attributes
        self.handed=handed
        self.place=place
    def shots(self):#methods or functions
        print(f"{self.fullname} is indian captain")
    def food(self):
        print(f"{self.place} he eats vada pav")


mi=Rohit("rohit sharma","right","mumbai")#objects # object name = class name,mi is reference variable
mi2=Rohit("sky","right","delhi")
mi.shots()
mi.food()