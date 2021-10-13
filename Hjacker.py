from colorama import Fore, Style
from colorama import init
import platform as pf
import requests
import os
import getpass
import pyautogui as pg
import base64

os.system('cls')
print(f"""{Fore.MAGENTA}
 ██░ ██ ▄▄▄██▀▀▀▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██░ ██▒  ▒██  ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░  ░██  ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█ ░██▓██▄██▓ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓▓███▒   ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒▒▓▒▒░   ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░▒ ░▒░    ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░░ ░ ░    ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░  ░  ░░   ░        ░  ░░ ░      ░  ░      ░  ░   ░     
                                    Coded by ToxidWorm
                                    Type 'help' for help{Fore.RESET}""")
print(Fore.MAGENTA + 'Computer name: ' + f'{pf.node()}')
print(Style.RESET_ALL)

while True:
    os.system('title Hjacker')
    command = input(Fore.CYAN + 'hjacker@' + getpass.getuser() + ': ')
    if command == 'getip':
        response = requests.get("http://jsonip.com/").json()
        print(f"IP Adress: {response['ip']}")
    elif command == 'help':
        print(' ')
        print('getip - Get your current ip adress\nclear - clear screen\nexit - Exit\nscreenshot - Make screenshot\nflood - SMS & Call flood\nbase64 - Encode string (base64 algorithm)')
        print(' ')
    elif command == 'exit':
        exit()
    elif command == 'clear':
        os.system('cls')
    elif command == 'screenshot':
        pg.screenshot('screenshot.png')
    elif command == 'flood':
        print(Fore.GREEN + 'Impulse toolkit created by LimerBoy, not by ToxidWorm\nBut Impulse very nice\nIf you want to cancel attack type "cancel"')
        print('')
        number = input('Enter phone number to flood (without +): ')
        if number == 'cancel':
            print(' ')
            print(Fore.RED + 'You canceled attack')
            print(' ')
        else:
            os.system('python Impulse/impulse.py --method SMS --time 20 --threads 15 --target +' + number)
    elif command == 'base64':
        sample_string = input('Enter string to encode: ')
        sample_string_bytes = sample_string.encode("ascii")
  
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        print(f"Encoded string: {base64_string}")
    else:
        print(' ')
        print(Fore.RED + 'Unknown command')
        print(' ')