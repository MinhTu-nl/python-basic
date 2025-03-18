#XU LÝ CHUỖI P2

s = 'nguyen le minh tu'
print('CHUỖI: ',s)

# capitalize() - Viết hoa chữ cái đầu tiên 
print('- Viết hoa chữ cái đầu: ', s.capitalize())

# upper() - Chuyển chuỗi sang in hoa
print('- Viết hoa tất cả cái ký tự: ', s.upper())

# lower() - Chuyển chuỗi sang chữ thường
print('- In hoa chữ đầu: ', s.lower())

# title() - Chuyển ký tự đầu mỗi từ thanh in hoa
print('- chuyển ký tự đầu sang in hoa: ', s.title())

# strip() - Xoá ký tự được chỉ định ở đầu và cuối chuỗi
# lstrip() - Xoá ký tự được chỉ định bên trái chuỗi
# split(<kí tự>, <số lần tách>) - Tách các ký tự trong chuỗi
print('- Tách chuỗi thành các từ được tách bởi dấu cách: ',s.split(' ', -1))

# count() - đếm lần xuất hiện
# <ten_chuoi>.count(<kí tự>, <bắt đàu>, <kết thúc>)
print('- Đếm chữ n trong chuỗi: ', s.count('n'))

# find() - Tim chuoi con đầu tiên trả về vị trí xuất hiện, Nếu không tìm được thì return về -1
# <ten_chuoi>.find(<kí tự>, <start>, <end>)
print('- Tìm n trong chuỗi: ',s.find('n'))

# join() - nối tham số thành 1 chuỗi
s1 = ['Minh', 'Tú']
s2 = " ".join(s1)
print('- nối Minh và Tú của 1 mảng thành 1 chuỗi: ', s2)

# replace() - Thay thế chuỗi con trong chuỗi gốc
print('- Thay thế chữ lê thành minh: ',s.replace('le', 'minh'))