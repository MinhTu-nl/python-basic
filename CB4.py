'''
    Nếu không sử dụng (if __name__ == '__main__':) thì khi import, 
    1 file khác thì sẽ chạy toàn bộ lệnh có trong hàm main()
'''
def emailProcess(email):
    #youtube@minhtu.dev
    email_username = email[0:email.index("@")]
    #print(f'username is {email_username}')
    email_domain = email[email.index("@")+1 : ]
    return [email_username , email_domain]

def printmsg(email_username , email_domain):
    print(f'Username is {email_username}')
    print(f'Domain is {email_domain}')

def main():
    email = input("Please enter your email address: ").strip()
    email_username , email_domain = emailProcess(email)
    printmsg(email_username , email_domain)

if __name__ == '__main__':
    main()