'''
4. List Comprehensions

List comprehensions giúp bạn viết code ngắn gọn (đặc biệt khi đang ở trong 1 vòng lặp đã có)
và dễ đọc, nhìn code rõ
'''
#new_list[<action> for <item> in <iterator> if <some condition>]
word = 'hello world'
print(f'4. \n {word}')
print([char for char in word]) #thành dạng list

even_numbers = [i for i in range(0, 10) if i % 2 == 0]
print('in ra dãy số chia hết chia 2: ',even_numbers)

'''
VD: Tổng bill cộng thêm VAT. với TAX_RATE là 8%, SERVICE_CHARGE là 7%
'''
transactions = [1000, 2000, 300, 8000]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07

def get_price_tax_service(bill):
    return bill*(1 + TAX_RATE + SERVICE_CHARGE)

final_prices = [get_price_tax_service(bill) for bill in transactions]
print(final_prices)