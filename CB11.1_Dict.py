'''
TOPIC - DICTIONARY: một tập hợp các key_value không có thứ tự, có thể thay đổi và lập chỉ mục
Dictionary được khởi tạo với các dấu ngoặc nhọn {} và chúng có các khoá và giá trị 

Mỗi cặp key - value là 1 item
'''
'''
1. Create a new Dictionary
'''
#Cách 1:
my_dict1 = {"name": 'Nguyen Le Minh Tu',
            'age' : 20,
            'MSSV': 221359}

#Cách 2:
my_dict2 = dict(name='MinhTu', age = 20, Mssv = 221359)

#2. ACCESS ITEM
#2.1Check for key
#Cách 1:
name_in_dict2 = my_dict2['age']
print(name_in_dict2)

#Cách 2:
if 'name' in my_dict2:
    print(my_dict2['name'])
else:
    print('No key found')

#Cách 3: use try-except
try:
    print(my_dict2['ma'])
except KeyError:
    print('No Key Found')

#2.2 Add and change item
#add a new key
my_dict2['Email'] = 'tu221359@student.vn'
print(my_dict2)

#Thay đổi giá trị
my_dict2['age'] = 19
print(my_dict2)

#2.3 Delete key - value
#Sử dụng hàm del
del my_dict1['age']
print('2.3 Delete age: ', my_dict1)

#Sử dụng hàm pop()
# print('2.3 popped value: ', my_dict2.pop('age'))

#2.4 Looping through Dictionary
for key in my_dict2:
    print('2.4 ',key, my_dict2[key])