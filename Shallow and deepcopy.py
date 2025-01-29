#shallow copy
# import copy
# lst1=[[10,20],[20,30]]
# lst2=copy.copy(lst1)
# lst1[1][0]=300
# print(lst1)
# print(lst2)

#deepcopy
# import copy
# lst1=[[10,20],[20,30]]
# lst2=copy.deepcopy(lst1)
# lst1[1][0]=300
# print(lst1)
# print(lst2)

import copy
animals=[1,2]
numbers=copy.copy(animals)
animals[0]=5
print(animals)
print(numbers)
















