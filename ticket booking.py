tkts=[1,2,3,4,5]
print('available tkts')
user_input=int(input('how many tkts u want to buy'))
for x in range(user_input):
    tkt_num=int(input('enter tkt number'))
    tkts.remove(tkt_num)
print('available tkts',tkts)