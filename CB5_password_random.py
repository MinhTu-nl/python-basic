'''
project: Ramdom password generator
password: abcxyz_dajkk;
'''
import string as str
import random as rd

# Dãy chữ cái ascii từ in thường đến in hoa
Letters = str.ascii_letters
# Dãy số từ 0 -> 9
Numbers = str.digits
# Kí tự dấu / + 
Punctuation = str.punctuation

# print(Letters)
# print(Numbers)
# print(Punctuation)
def password_generator(length = 10):
    printable = f'{Letters}{Numbers}{Punctuation}'
    printable = list(printable)

    rd.shuffle(printable)
    random_password = rd.choices(printable, k = length)
    random_password = ''.join(random_password)
    return random_password

def get_password_length():
    password_length = input("How long do you want your password: ")
    return int(password_length)
def main():
    password_length = get_password_length()
    password = password_generator(password_length)
    print(password)

if __name__ == '__main__':
    main()