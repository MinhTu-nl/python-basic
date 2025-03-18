'''
Topic: List trong python - một dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau
chúng có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử trong list

Ngôn ngữ khác: C/C++ , Java, List trong python = Mảng arry
'''
'''
1. Creating a list
'''
List_1 = ['banana', 'apple', 'orange', 'cherry']
List_2 = [5, 6.5, 'minhtu', True, None]
List_3 = list() #list rỗng
print('1. ',List_1)
print('1. ',List_2)

'''
2. Access element: Truy cập đến các giá trị trong list
'''
List_4 = [1, 2, 2, 3, 2, 'apple', 'orangre']
#len() - Hàm truy xuất độ dài của list
print('2. Sử dụng hàm len() : ', len(List_4))

#index() - tìm vị trí của phần tử
print('2. Sử dụng hàm index() :',List_4.index('apple'))

#count() - Đếm số phần tử
print('2. Sử dụng hàm count() :',List_4.count(2))

#enumerate(<list_name>, start= ) - vị trí của phần tử
print('2. Sử dụng hàm enumerate() : \n')
for index, item in enumerate(List_4, start=1):
    print(f'List_4 #{index} : {item}')

'''
Slicing
: is called slicing and has the format [start : end : step]

NOTE:
    LIST_NAME[:9] - từ 0 đến phần tử thứ 9
    LIST_NAME[0:] - từ 0 đến phần tử cuối cùng
    LIST_NAME[::2] - từ đầu đến cuối, bước nhảy 2
    LIST_NAME[2:9] - từ 2 đến 9
    LIST_NAME[2:9:3] - từ 2 đến 9, bước nhảy 3
'''
print(List_4[5 : ])

'''
3. List Operations & Useful Methods
    3.1 Add to list
    3.2 Remove from list
    3.3 Sort 
    3.4 Useful operation
'''
'''
3.1 Add to list
'''
my_list = ['hi', 3.5, 10, 'minhtu']

#1
my_list_1 = my_list + [221359, 'DNC'] #có thể thêm phần tử thêm cách này
print(my_list_1)

#2
my_list_2 = my_list.append(6) #append() - thêm phần tử vào vị trí cuối của list
print(my_list)

#3
my_list_3 = my_list.extend(['ham', 'extend']) #thêm nhiều phần tử vào đuôi list
print(my_list)

#4
my_list_4 = my_list.insert(2, 3.6)
print(my_list)

'''
3.2 Remove from list
'''
myList = [1, 2, 3, 3]
print(myList)
# pop() - xoá phần tử được chỉ định, nếu trống chỉ định thì sẽ xoá phần tử cuối
#       - return về giá trị xoá
# print(f'phần tử được xoá là: {myList.pop(1)}')
# print(myList)

myList.remove(3) #remove() - xoá phần tử đầu tiên khi nó tìm thấy
print(myList)

'''
3.3 Sort
'''
mList = [1, 2, 5, 3, 9, 4, 6, 8, 7]
print('3.3 \n',mList)
mList.sort()
print('3.3 List sắp xếp tăng: ', mList)
mList.sort(reverse=True)
print('3.3 List sắp xếp giảm dần: ', mList)

#sorted() - sắp xếp tăng thành 1 list mới, giữ list ban đầu
print(f'3.3 sắp xếp tăng theo sorted(): {sorted(mList)} \n và gọi lại list ban đầu {mList}')

'''
3.4 Useful operations
'''
Mlist = [100, 200, 500, 501, 201]
print('3.4 \n', Mlist)
print(f'3.4 MAX = {max(Mlist)}')
print(f'3.4 MIN = {min(Mlist)}')
print(f'3.4 SUM = {sum(Mlist)}')
