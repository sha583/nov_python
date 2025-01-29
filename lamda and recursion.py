# def add(*num):
#     return sum(num)
# print(add(1,2,3,4))

# lambda fuction is a anonymous function which can take many arguements but it has only one expression

# add=lambda a,b:a+b
# print(add(1,2))

# double=lambda x:2*x
# print(double(200))

lst=[{'name':'sharan','marks':95},
     {'name':'kiran','marks':90},
    {'name':'ss','marks':55 }]
lst.sort(key=lambda x:x['marks'],reverse=True )
print(lst)
