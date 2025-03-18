'''
1.Viết một chương trình tráo đổi phần tử đầu với phần tử cuối trong danh sách, phần tử thứ 2 với phần tử thứ n - 1 trong danh sách (giả sử danh sách có n phần tử)...
Ví dụ 
danh sách ban đầu [4, 2, 6, 7, 9, 8], 
danh sách sau khi tráo đổi là [8, 9, 7, 6, 2, 4]
'''
my_list = [4, 2, 6, 7, 9, 8]
long_list = len(my_list)

for i in range(long_list // 2):
    tmp = my_list[i]
    my_list[i] = my_list[long_list- 1-i]
    my_list[long_list - 1 - i] = tmp

print(my_list)