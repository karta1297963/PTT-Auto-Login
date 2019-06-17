#coding=utf-8
import csv, sys, os
import telnetlib
import time

host = 'ptt.cc'

file_name = 'login-data.txt'
login_data = []
telnet = telnetlib.Telnet(host)


def get_account_info(file_name):
    lst = []
    path = os.path.join(sys.path[0], file_name)
    
    with open(path, newline = '') as inputfile:
        rows = csv.reader(inputfile)

        for row in rows:
            lst.append(row)

    return lst



def key_in(str_content, rtn):
    if rtn:
        telnet.write((str_content + "\r\n").encode("ascii"))
    else:
        telnet.write((str_content).encode("ascii"))


def login(user, password):

    time.sleep(1)
    content = telnet.read_very_eager().decode('big5','ignore')
    print(content)


    if u"請輸入代號" in content:
        print("輸入帳號中...")
        key_in(user, True)
        time.sleep(1)

        content = telnet.read_very_eager().decode('big5','ignore')

        print(content)

        if u"請輸入您的密碼" in content:
            print("輸入帳號中...")
            key_in(password, True)
            time.sleep(1)

            content = telnet.read_very_eager().decode('big5','ignore')

            print(content)

        if u"任意鍵" in content:
                print("資訊頁面，按任意鍵繼續...")
                key_in("", True)
                time.sleep(3)
                content = telnet.read_very_eager().decode('big5','ignore')
                print(content)



def logout():
    content = display_cur()

    key_in("g", True)
    content = display_cur()
    time.sleep(1)
    key_in('y', True)

    content = display_cur()
    if u"按任意鍵繼續" in content:
        key_in("", True)


def display_cur():
    time.sleep(1)
    content = telnet.read_very_eager().decode('big5','ignore')
    print(content)
    return content


def get_board(name):
    key_in("s", False)
    key_in(name, True)
    time.sleep(1)
    key_in("", True)
    time.sleep(2)
    content = telnet.read_very_eager().decode('big5','ignore')
    print(content)




login_data = get_account_info(file_name)

for account in login_data:
    telnet = telnetlib.Telnet(host)
    login(account[0], account[1])
    logout()
    