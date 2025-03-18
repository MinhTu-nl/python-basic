from CB4 import emailProcess, printmsg
def main():
    emails = [
        'youtube@nguyenleminhtu.dev',
        'minhtu@developer.dev',
        'tunguyen@mssv221359.vn'
    ]
    for email in emails:
        username , domain = emailProcess(email)
        printmsg(username , domain)

if __name__ == '__main__':
    main()