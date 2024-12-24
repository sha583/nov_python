cor_ans=0
wrong_ans=0
print('1.what is the capital of india')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='delhi':
    cor_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
print('percentage',((cor_ans/(cor_ans+wrong_ans))*100))  
print('1.what is the capital of karnataka')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='bangalore':
    cor_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
print('percentage',((cor_ans/(cor_ans+wrong_ans))*100))       
print('1.what is the national animal')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='tiger':
    cor_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
print('percentage',((cor_ans/(cor_ans+wrong_ans))*100)) 
print('1.what is the national bird')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='peacock':
    cor_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
print('percentage',((cor_ans/(cor_ans+wrong_ans))*100))

