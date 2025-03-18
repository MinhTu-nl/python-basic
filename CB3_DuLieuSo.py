a = 5e9 #5*10 mũ 9
print(a)

b = 10 // 3 #10 chia 3 lấy phần nguyên
print(b)

'''
Biểu thức so sánh
ví dụ 
    a = 10
    b = 11

    c = a < b : so sánh a nhỏ hơn b
    c = a > b : so sánh a lớn hơn b
    c = a <= b : so sánh a nhỏ hơn hoặc bằng b
    c = a >= b : so sánh a lớn hơn hoặc bằng b

    c = a == b : so sánh a bằng b
    c = a != b : so sánh a khác b 
'''
'''
and, or, not
and : True khi cả hai đều đúng
or : True khi 1 trong 2 là đúng
not : ngược lại
'''
number1 = 12
number2 = 15
number3 = 17
ss1 = number3 > number1 and number1 > number2
print(ss1)
ss2 = number2 > number1 or number1 > number3
print(not(ss2))
print(ss2)

