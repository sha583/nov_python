# def marriage(boy,girl):#parameters
#     print(f'{boy} married {girl}')

# marriage('chandan','chandana')#positional arguements
# marriage(boy='sky', girl='dew')#keyward  arguements

# def tables(num):
    # for i in range(1,11):
        # print(f"{num}x{i}={num*i}")
# tables(2)
# tables(3)

#returning value from function
# def func(num):
#     return int(str(num)*5)
# a=20
# b=a+func(5)
# print(b)

#local and global variables

def func():
    x='chandan'
    print(x) #local variable
    print(y)

y='kkkkk'#global variable    
func()