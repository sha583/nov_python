# print([x for x in [1,3,4,5,6,7] if x%2==1])

# val=[1,2,3]
# print([f'even value{x}'if x%2==0 else  f'{x} odd value'for x  in val])

#remove
# tkts=[1,2,3,4,5]
# print('available tkts',tkts)
# user_input=int(input('enter how many tkts u wanna buy '))
# for x in range(user_input):
#     ticket_num=int(input('enter tckt number'))
#     tkts.remove(ticket_num)
# print('availabletkts',tkts)

#sets
# lst=[1,2,3,4,1,2]
# emp_lst=[]
# for x in lst:
#     if x not in emp_lst:
#         emp_lst.append(x)
# print(emp_lst)


# lst=[1,2,3,4,1,2]
# emp_lst=[]
# dupl_lst=[]
# for x in lst:
#     if x in emp_lst:
#         dupl_lst.append(x)
#     else:
#         emp_lst.append(x)
# print(dupl_lst)
    
# sales_items=[]
# print(type(sales_items))
# val={}
# print(type(val))

sql={1,2,3}
python={3,4,5}
print(sql.intersection(python))
print(sql.difference(python))
print(sql.intersection(python))

sql={1,2,3,4,5}
python={1,6,7,8}
aws={1,4,5,6,99}
print(sql.intersection(python,aws))
print(sql)

