class database:
    def __init__(self):
        self.__storage={}
    def write(self,key,value):
        self.__storage[key]=value
    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print('db not available')
chandan=database()
chandan.write('sub',100)
chandan.read('sub')
print(chandan.__storage)