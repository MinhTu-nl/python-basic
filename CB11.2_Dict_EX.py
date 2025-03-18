'''
Hãy nhập vào 1 danh sách sinh viên gồm: Mã, Tên SV, lớp. 
Sau đó in danh sách sinh viên ra màn hình, 
    thông tin của mỗi sinh viên trên một dòng
'''
n = int(input('- Nhập số lượng sinh viên: '))
dict_SinhVien = []
for i in range(n):
    SinhVien = {'MSSV' : '', 'TÊN' : '', 'LOP' : ''}
    for j in SinhVien:
        print('+ Nhập ', j, ':', end='')
        value = input()
        SinhVien[j] = value

    dict_SinhVien.append(SinhVien)

for i in range(n):
    print('THÔNG TIN SINH VIÊN', i+1)
    print(f'MSSV: {dict_SinhVien[i]['MSSV']}; TÊN: {dict_SinhVien[i]['TÊN']}; LOP: {dict_SinhVien[i]['LOP']}')

