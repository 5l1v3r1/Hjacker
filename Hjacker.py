from colorama import Fore, Style, init
import platform as pf
import pyautogui as pg
import sys, time, threading, itertools, random, base64, getpass, os, requests, random
init()
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\r{Fore.GREEN}Loading Hjacker ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rHjacker Sucefully loaded')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
done = True
os.system('cls')
print(f"""{Fore.MAGENTA}
 ▄▄   ▄▄     ▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█  █ █  █   █   █      █       █   █ █ █       █   ▄  █  
█  █▄█  █   █   █  ▄   █       █   █▄█ █    ▄▄▄█  █ █ █  
█       █▄  █   █ █▄█  █     ▄▄█      ▄█   █▄▄▄█   █▄▄█▄ 
█   ▄   █ █▄█   █      █    █  █     █▄█    ▄▄▄█    ▄▄  █
█  █ █  █       █  ▄   █    █▄▄█    ▄  █   █▄▄▄█   █  █ █
█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█  
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
        print('getip - Get your current ip adress\nclear - clear screen\nexit - Exit\nscreenshot - Make screenshot\nflood - SMS & Call flood\nbase64encode - Encode string (base64 algorithm)\nbase64decode - Decode string (base64 algorithm)\nutillist - Show utility list')
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
            attackthreads = input('Enter threads count: ')
            attacktime = input('Enter attack time: ')
            os.system('python Impulse/impulse.py --method SMS --time ' + attacktime + ' --threads ' + attackthreads + ' --target +' + number)
    elif command == 'base64encode':
        sample_string = input('Enter string to encode: ')
        sample_string_bytes = sample_string.encode("ascii")
  
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        print(f"Encoded string: {base64_string}")
    elif command == 'base64decode':
        encodedstring = input('Enter encoded string: ')
        encodedresult = base64.b64decode(encodedstring)
        print(Fore.GREEN + 'Decoded string: ' + f'{encodedresult}')
    elif command == 'utillist':
        os.system('cls')
        print(f'{Fore.MAGENTA}Tool list:\nImpulse by LimerBoy (https://github.com/LimerBoy/Impulse)')
    else:
        print(' ')
        print(Fore.RED + 'Unknown command')
        print(' ')