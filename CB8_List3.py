'''
Advanced functions
'''
#zip(): looping through two list simultaneously
nameEN = ['DOG', 'CAT', 'PIG']
nameVN = ['Chó', 'Cá', 'Heo']

for index, (naEN, naVN) in enumerate(zip(nameEN, nameVN), start=1):
    print(f'{index} | {naEN} is {naVN}')

#sorted()
sorted_by_second = sorted(['hi', 'hello', 'you', 'minhtu'], key=lambda el: el[1])
print(sorted_by_second)

'''
VD: hàm sắp xếp list theo name đã cho
'''
key_list = [{'name':'MinhTú' , 'age' : 20}, 
            {'name':'AnhTuấn' , 'age' : 21}, 
            {'name':'Hoàng', 'age' : 22}]

sorted_by_name = sorted(key_list, key=lambda el: el['name'])
print(sorted_by_name)
