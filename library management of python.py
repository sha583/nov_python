books=['the mind','history','power of money']
lended_books={}
class lib:
    def request_book(self):
        for x in books:
            print(x)
        req=input('enter the book name')
        return req
    def lending_book(self,catcher):
        if catcher in books:
            print('book is available')
        else:
            print('books not available')
   

l1=lib()
catcher=l1.request_book()
print(catcher)
l1.lending_book(catcher)

