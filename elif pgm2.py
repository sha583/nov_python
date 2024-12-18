age=int(input('enter the age:'))
r1=5,r2=30
rupees1=r1*80
rupees2=r2*80
if age>50:
    print('ticket is free')
elif age in range(18,31):
    print('ticket is',rupees1)
elif age in range(30,51):
    print('ticket is',rupees2)
else:
    print("invalid age")    
