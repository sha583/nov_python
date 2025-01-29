class mobile():
    def __init__(self,brand,gb,camera):
        self.brand=brand
        self.gb=gb
        self.camera=camera
    def work(self):
        print(f'{self.brand} is top brand ')
        print(f'{self.gb} is top storage ')
        print(f'{self.camera} is top quality ')
sharan=mobile('samsung',4,220)
kiran=mobile('oppo',8,1010)
sharan.work()
kiran.work()