'''
2. Tính giá trị của đa thức sau
P = a0 + a1 x + a2 x2 + ... + anxn
'''
my_list = []
n = int(input("- Nhập n = "))

for i in range(n):
    print('- Nhập vào phần tử thứ', i+1, ':', end= '')
    x = int(input())
    my_list.append(x)

x = int(input('x = '))
tong = 0

for i in range(n):
    tong += my_list[i] * (x ** i)

print('Tổng = ', tong)