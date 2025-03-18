'''
3. Một hãng thời trang có n cửa hàng trên toàn quốc, 
hãy xây dựng một chương trình cho phép nhập doanh số bán hàng của các cửa hàng đó sau đó:
- Sắp xếp doanh số bàn hàng từ bé đến lớn
- Tính trung bình doanh số của n cửa hàng
- Hiển thị doanh số bán hàng lớn nhất, nhỏ nhất
'''
DoanhSo = []
n = int(input('Nhập số lượng cửa hàng: '))

for i in range(n):
    print('- Nhập doanh số của cửa hàng thứ', i+1,':', end= '')
    x = int(input())
    DoanhSo.append(x)

#sắp xếp
Sort_Tang_DoanhSo = sorted(DoanhSo)
print('Sắp xếp doanh số theo tăng dần: ', Sort_Tang_DoanhSo)


Tong_DoanhSo = sum(DoanhSo)
TB_DoanhSo = round(Tong_DoanhSo / n, 0)

#Trung bình
print(f'Trung bình doanh thu: {TB_DoanhSo}')

# MAX & MIN
print(f'Doanh số cao nhất: {max(DoanhSo)}')
print(f'Doanh số thấp nhất: {min(DoanhSo)}')