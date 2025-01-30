# class Car:
#     def __init__(self):
#         self.name='tata'
#         print(self.name)
#         self.cost=2
#         print(self.cost)
#         print("program running")
# tata=Car()
# tata

# class Insta:
#     def __init__(self):
#         self.name='ram'
#         self.id=1234
#         print(self.name,self.id)
# im=Insta()


# class maths:
#     def __init__(self):
#         self.sub_name='maths'
#     def add(self):
#         a,b=10,20
#         print(a+b)
# m1=maths()
# m1.add()

class Instagram:
    def __init__(self):
        self.instagram_version='version11'
        self.instagram_developer='kiran'
    def autentication(self):
        username=input('enter username')
        password=int(input('enter the pass'))
        if username=='prince123' and password==123:
            print('username and pass matched')
        else:
            print('invalid ')
m1=Instagram()
m1.autentication()
