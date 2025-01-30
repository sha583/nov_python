class flipkart:
    def __init__(self):
        self.brand_name='wipro'
        print(self.brand_name)
    def show(self):
        global price
        price=1000
        print(price)
    def add(self):
        print(price)
f1=flipkart()
f1.show()
f1.add()