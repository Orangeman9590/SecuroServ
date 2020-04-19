# BULLETSCRIPT
# CODED BY: Orangeman
# USE AT YOUR OWN RISK

import os
import time
import termcolor
from termcolor import colored
import secrets
import string
import random
import re
import shodan

colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
colour = random.choice(colours)
sho = '''
 _____ _   _ ___________  ___   _   _ 
/  ___| | | |  _  |  _  \/ _ \ | \ | |
\ `--.| |_| | | | | | | / /_\ \|  \| |
 `--. \  _  | | | | | | |  _  || . ` |
/\__/ / | | \ \_/ / |/ /| | | || |\  |
\____/\_| |_/\___/|___/ \_| |_/\_| \_/
'''



os.system('clear')
# MAIN MENU
while True :
    os.system('clear')
    print(colored('         █╗    █╗        All-in one tool', colour))
    print(colored('         █║ █╗ █║    For Penetration Testing', colour))
    print(colored('         █║ █║ █║ ', colour))
    print(colored('██████╗ ████████╗██╗     ██╗     ███████╗████████╗', colour))
    print(colored('██╔══██╗██║   ██║██║     ██║     ██╔════╝╚══██╔══╝', colour))
    print(colored('██████╔╝██    ██║██║     ██║     █████╗     ██║   ', colour))
    print(colored('██╔══██╗████████║██║     ██║     ██╔══╝     ██║   ', colour))
    print(colored('██████╔╝╚██████╔╝███████╗███████╗███████╗   ██║   ', colour))
    print(colored('╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ', colour))
    print(colored('----------| Coded by: Orangeman |----------', 'red'))
    print(colored('--------------| MAIN MENU |----------------', 'cyan'))
    print(colored('[1] Enter AirDos (Wireless attacks)', 'red'))
    print(colored('[2] Password Attacks', 'red'))
    print(colored('[3] BeaverCrypt (AES-256 Bit Encryptor of files)', 'red'))
    print(colored('[4] Information Gathering', 'red'))
    print(colored("[5] Sniffing and Spoofing", 'red'))
    print(colored('[6] Exploitation', 'red'))
    print(colored("[99] Quit Script", 'red'))
    print('')

    # MAIN INPUT
    q = input('bullet> ')

    # AIRDOS
    if q == '99' :
        print('Thank You for using my script...')
        os.system('clear')
        quit()

    if q == '1' :
        os.system('clear')
        print(colored("DO YOU HAVE AIRDOS?[Y/N]", 'red'))
        k = input('bullet> ')
        if k == 'Y' :
            os.system('python3 airdos/dos.py')
        elif k == 'N' :
            os.system('clear')
            os.system('git clone https://github.com/Orangeman9590/airdos')
            os.system('python3 airdos/dos.py')

    # PASSWORD
    elif q == '2' :
        os.system('clear')
        print(colored('______  ___    _____ _____  _    _  _________________  ', 'cyan'))
        print(colored('| ___ \/ _ \  /  ___/  ___|| |  | ||  _  | ___ \  _  \ ', 'cyan'))
        print(colored('| |_/ / /_\ \ \ `--.\ `--. | |  | || | | | |_/ / | | | ', 'cyan'))
        print(colored('|  __/|  _  |  `--. \`--. \| |/\| || | | |    /| | | | ', 'cyan'))
        print(colored('| |   | | | | / \__/ /\__/ /\  /\  /\ \_/ / |\ \| |/ /  ', 'cyan'))
        print(colored('\_|   \_| |_/ \____/\____/  \/  \/  \___/\_| \_|___/   ', 'cyan'))
        print(colored('--------------------------------------------------------', 'red'))
        print(colored('[1] HashCat', 'red'))
        print(colored('[2] Generate Random Password', 'red'))
        print(colored('[3] Hydra', 'red'))
        print(colored('[ENTER] Go Back', 'red'))

        # SECOND INPUT
        w = input('bullet> ')

        # HASHCAT
        if w == '99' :
            os.system('clear')
        if w == '1' :
            print(colored('ENTER HASH OF PASSWORD: ', 'cyan'))
            e = input('bullet> ')
            print("SELECT ATTACK MODE...")
            print("0 = Straight")
            print("1 = Combination")
            print("2 = Toggle-Case")
            print("3 = Brute-force")
            print("4 = Permutation")
            print("5 = Table-lookup")
            i = input("Choose: ")
            if i == 0 :
                os.system(
                    'hashcat -m 0 -a 0 -o cracked.txt --force ' + e + ' /root/wordlists/rockyou.txt -r /usr/share/hashcat/rules/combinator.rule')
            elif i == 1 :
                os.system(
                    'hashcat -m 0 -a 1 -o cracked.txt --force ' + e + ' /root/wordlists/rockyou.txt -r /usr/share/hashcat/rules/combinator.rule')
            elif i == 2 :
                os.system(
                    'hashcat -m 0 -a 2 -o cracked.txt --force ' + e + ' /root/wordlists/rockyou.txt -r /usr/share/hashcat/rules/combinator.rule')
            elif i == 3 :
                os.system('hashcat -m 0 -a 3 -o cracked.txt --force ' + e + ' /root/wordlists/rockyou.txt')
            elif i == 4 :
                os.system(
                    'hashcat -m 0 -a 4 -o cracked.txt --force ' + e + ' /root/wordlists/rockyou.txt -r /usr/share/hashcat/rules/combinator.rule')
            elif i == 5 :
                os.system(
                    'hashcat -m 0 -a 5 -o cracked.txt --force ' + e + ' /root/wordlists/rockyou.txt -r /usr/share/hashcat/rules/combinator.rule')

        elif w == '2' :
            # RANDOM PASSWORD
            os.system('clear')
            rando = string.ascii_letters + string.digits + string.punctuation
            pwd = secrets.choice(string.ascii_lowercase)
            pwd += secrets.choice(string.digits)
            pwd += secrets.choice(string.ascii_uppercase)
            pwd += secrets.choice(string.punctuation)

            for i in range(21) :
                pwd += secrets.choice(rando)
            char_list = list(pwd)
            secrets.SystemRandom().shuffle(char_list)
            pwd = ''.join(char_list)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                      x")
            print("x          YOUR PASSWORD IS            x")
            print("x      " + pwd + "       x")
            print("x                                      x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(" ")
            print(colored('PRESS {99} TO GO BACK'))
            input = input('bullet> ')
            if input == '99' :
                continue
        elif w == '3' :
            # HYDRA
            os.system('hydra --help')
            time.sleep(1)
    elif q == '3' :
        # BEAVERCRYPT
        os.system('clear')
        print('DO YOU HAVE BEAVERCRYPT?[Y/N]')
        bee = input('bullet> ')
        if bee == 'Y' :
            os.system('clear')
            os.system('python3 /BeaverCrypt/beaver.py')
        elif bee == 'N' :
            os.system('clear')
            os.system('git clone https://github.com/Orangeman9590/BeaverCrypt')
            os.system('python3 BeaverCrypt/beaver.py')

    elif q == '4' :
        # INFO
        os.system('clear')
        print(colored(" _____   _   _  ______   _____ ", 'cyan'))
        print(colored("|_   _| | \ | | |  ___| |  _  |", 'cyan'))
        print(colored("  | |   |  \| | | |_    | | | |", 'cyan'))
        print(colored("  | |   | . ` | |  _|   | | | |", 'cyan'))
        print(colored(" _| |_  | |\  | | |     \ \_/ /", 'cyan'))
        print(colored(" \___/  \_| \_/ \_|      \___/ ", 'cyan'))
        print(colored("<------------------------------->", 'cyan'))
        print(colored("[1] Nmap", 'magenta'))
        print(colored("[2] Shodan", 'magenta'))
        print(colored("[3] Setoolkit", 'magenta'))
        print(colored("[4] Autopsy", 'magenta'))
        print(colored("[5] Validate E-mail", 'magenta'))
        print(colored("[6] Netdiscover", 'magenta'))
        print(colored("[ENTER] Go Back", 'magenta'))

        t = input("bullet> ")
        if t == '1' :
            # NMAP
            os.system('clear')
            print(colored("ENTER THE IP YOU WANT TO SCAN: ", 'red'))
            y = input("bullet> ")
            print(colored(" _   _ ___  ___  ___  ______ ", 'cyan'))
            print(colored("| \ | ||  \/  | / _ \ | ___ \ ", 'cyan'))
            print(colored("|  \| || .  . |/ /_\ \| |_/ /", 'cyan'))
            print(colored("| . ` || |\/| ||  _  ||  __/ ", 'cyan'))
            print(colored("| |\  || |  | || | | || |    ", 'cyan'))
            print(colored("\_| \_/\_|  |_/\_| |_/\_|    ", 'cyan'))
            print(colored("<----------------------------->", 'red'))
            print(colored("[1] Fast Scan (-f)", 'red'))
            print(colored("[2] Aggressive Scan (-A)", 'red'))
            print(colored("[3] Syn ACK Scan (-Ss)", 'red'))
            print(colored("[4] UDP Scan (-sU)", 'red'))
            print(colored("[ENTER] Go Back", 'red'))

            u = input("bullet> ")
            if u == '1' :
                os.system('clear')
                print(colored("STARTING FAST SCAN...", 'red'))
                time.sleep(1)
                os.system('nmap -v -f ' + y)
                print('PRESS [ENTER] TO GO BACK')
                ba = input()
                if ba == '99':
                    continue
            elif u == '2' :
                os.system('clear')
                print(colored("STARTING AGGRESIVE SCAN...", 'red'))
                time.sleep(1)
                os.system('nmap -v -A ' + y)
                print('PRESS [ENTER] TO GO BACK')
                bac = input()
                if bac == '99':
                    continue
            elif u == '3' :
                os.system('clear')
                print(colored("STARTING SYN ACK SCAN", 'red'))
                time.sleep(1)
                os.system('nmap -v -Ss' + y)
                print('PRESS [ENTER] TO GO BACK')
                back = input()
                if back == '99':
                    continue
            elif u == '4' :
                os.system('clear')
                print(colored("STARTING UDP SCAN", 'red'))
                time.sleep(1)
                os.system('nmap -v -sU' + y)
                print('PRESS [ENTER] TO GO BACK')
                backs = input()
                if backs == '99':
                    continue

        elif t == '2' :
            # SHODAN
            os.system('clear')
            print(colored(sho, 'magenta'))
            print(colored('PLEASE ENTER IN YOUR SHODAN API KEY', 'red'))
            SHODAN_API_KEY = input('bullet> ')
            api = shodan.Shodan(SHODAN_API_KEY)
            os.system('clear')
            print(colored('WHAT DO YOU WANT TO SEARCH ON SHODAN', 'red'))
            search = input('bullet> ')
            try:
                results = api.search(search)
                print(colored('RESULTS FOUND: %s' % results['total'], 'cyan'))
                for result in results['matches']:
                    print('IP: %s' % result['ip_str'])
                    print(result['data'])
                    print('')
                print('PRESS {ENTER} TO GO BACK')
                back = input('bullet> ')
            except shodan.APIError:
                print('ERROR')

        elif t == '3' :
            # SETOOLKIT
            os.system('clear')
            os.system('sudo setoolkit')
        elif t == '4' :
            os.system('clear')
            os.system('autopsy')
        elif t == '5' :
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


            def check(email) :
                if (re.search(regex, email)) :
                    print("Valid Email")
                else :
                    print("Invalid Email")


            os.system('clear')
            print(colored("ENTER EMAIL YOU WANT TO CHECK", 'red'))
            print('')
            email = input('bullet> ')
            os.system('clear')
            check(email)
            print('ENTER {99} TO GO BACK')
            nine = input('bullet> ')
            if nine == '99' :
                continue
        elif t == '6' :
            os.system('clear')
            os.system('netdiscover')





    elif q == '5' :
        # SNIFF&SPOOF
        os.system('clear')
        print(colored(" _____ _   _ _________________            ___________ _____  ___________  ", 'red'))
        print(colored("/  ___| \ | |_   _|  ___|  ___|   ___    /  ___| ___ \  _  ||  _  |  ___| ", 'red'))
        print(colored("\ `--.|  \| | | | | |_  | |_     ( _ )   \ `--.| |_/ / | | || | | | |_   ", 'red'))
        print(colored(" `--. \ . ` | | | |  _| |  _|    / _ \/\  `--. \  __/| | | || | | |  _|   ", 'red'))
        print(colored("/\__/ / |\  |_| |_| |   | |     | (_>  < /\__/ / |   \ \_/ /\ \_/ / |    ", 'red'))
        print(colored("\____/\_| \_/\___/\_|   \_|      \___/\/ \____/\_|    \___/  \___/\_|     ", 'red'))
        print(colored("<------------------------------------------------------------------------->", 'cyan'))
        print(colored("[1] ARPspoof", 'red'))
        print(colored("[2] Setoolkit", 'red'))
        print(colored("[3] ShellPhish", 'red'))
        print(colored("[4] URLSnarf (Works in conjunction with ARPspoof)", 'red'))
        print(colored("[5] Dsniff (Works in conjunction with ARPspoof)", 'red'))
        print(colored("[ENTER] Go Back", 'red'))
        f = input('bullet> ')
        if f == '1' :
            # ARPSPOOF
            os.system('clear')
            print(colored('ENTER CLIENTS IP: ', 'red'))
            g = input('bullet> ')
            os.system('clear')
            os.system('ip r')
            print(colored("ENTER GATEWAY IP: ", 'red'))
            h = input('bullet> ')
            os.system('clear')
            os.system('ifconfig')
            print(colored('{+}---------------------------------------------{+}'))
            print(colored("ENTER YOUR INTERFACE:", 'red'))
            j = input('bullet> ')
            os.system('clear')
            os.system('gnome-terminal --command="arpspoof -i "' + j + '" -t "' + g + "' '" + h)
            os.system('clear')
            os.system('gnome-terminal --command="arpspoof -i "' + j + '" -t "' + h + "' '" + g)
            os.system('clear')
            continue
        elif f == '2' :
            os.system('clear')
            os.system('sudo setoolkit')
        elif f == '3' :
            # SHELLPHISH
            os.system("clear")
            print(colored("DO YOU HAVE SHELLPHISH?[Y/N]", 'red'))
            v = input('bullet> ')
            if v == 'Y' :
                os.system('clear')
                os.system('./shellphish/shellphish.sh')
            elif v == 'N' :
                print(colored("DO YOU WANT TO INSTALL IT[Y/N]", 'red'))
                m = input('bullet> ')
                if m == 'Y' :
                    os.system('clear')
                    os.system('git clone https://github.com/thelinuxchoice/shellphish')
                    os.system('./shellphish/shellphish.sh')
                if m == 'N' :
                    print("THEN WHY DID YOU COME HERE lol")
                    continue
        elif f == '4' :
            os.system('clear')
            os.system('ifconfig')
            print(colored("|------------------------------------------------|", 'red'))
            print("WHAT IS YOUR WIRELESS INTERFACE?")
            z = input('bullet> ')
            os.system('clear')
            os.system('urlsnarf ' + z)
        elif f == '5' :
            os.system('clear')
            os.system('dsniff')


    elif q == '6' :
        os.system('clear')
        print(colored(" _______   ________ _     _____ _____ _____ ", 'magenta'))
        print(colored("|  ___\ \ / /| ___ \ |   |  _  |_   _|_   _|", 'magenta'))
        print(colored("| |__  \ V / | |_/ / |   | | | | | |   | |  ", 'magenta'))
        print(colored("|  __| /   \ |  __/| |   | | | | | |   | |  ", 'magenta'))
        print(colored("| |___/ /^\ \| |   | |___\ \_/ /_| |_  | | ", 'magenta'))
        print(colored("\____/\/   \/\_|   \_____/\___/ \___/  \_/  ", 'magenta'))
        print(colored("<-------------------------------------------->", 'cyan'))
        print(colored("[1] Metasploit Framework", 'white'))
        print(colored("[2] BEEF-XSS Framework", 'white'))
        print(colored("[3] Shodan", 'white'))
        print(colored("[4] Router Sploit", 'white'))
        print(colored("[5] The Fat Rat(BackDoor Factory)", 'white'))
        print(colored("[ENTER] Go Back", 'red'))
        l = input("bullet>")
        if l == '1' :
            os.system('clear')
            os.system('sudo service postgresql start')
            os.system('msfconsole')
        elif l == '2' :
            os.system('clear')
            os.system('sudo beef-xss')
        elif l == '3' :
            os.system('clear')
            os.system('firefox shodan.io')
        elif l == '4' :
            os.system("clear")
            print('DO YOU HAVE ROUTERSPLOIT?[Y/N]')
            x = input('bullet> ')
            if x == 'Y' :
                os.system('clear')
                os.system('python3 routersploit/rsf.py')
            elif x == 'N' :
                os.system('clear')
                os.system('git clone https://github.com/threat9/routersploit')
                os.system('python3 routersploit/rsf.py')
        elif l == '5' :
            os.system('clear')
            print('DO YOU HAVE THE FAT RAT?[Y/N]')
            a = input('bullet> ')
            if a == 'Y' :
                os.system('clear')
                os.system('./TheFatRat/fatrat')
            elif a == 'N' :
                os.system('clear')
                os.system('git clone https://github.com/Screetsec/TheFatRat')
                os.system('./TheFatRat/fatrat')
            x = input('bullet> ')
            if x == 'Y' :
                os.system('clear')
                os.system('python3 routersploit/rsf.py')
            elif x == 'N' :
                os.system('clear')
                os.system('git clone https://github.com/threat9/routersploit')
                os.system('python3 routersploit/rsf.py')
        elif l == '5' :
            os.system('clear')
            print('DO YOU HAVE THE FAT RAT?[Y/N]')
            a = input('bullet> ')
            if a == 'Y' :
                os.system('clear')
                os.system('./TheFatRat/fatrat')
            elif a == 'N' :
                os.system('clear')
                os.system('git clone https://github.com/Screetsec/TheFatRat')
                os.system('./TheFatRat/fatrat')
