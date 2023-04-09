import time, os, datetime, psutil, sys
from colorama import Fore, Back, Style

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
white = Fore.WHITE
reset = Fore.RESET

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def get_running_time():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    return str(uptime).split('.')[0]

def get_weather():
    link = 'https://wttr.in/?format=1'
    weather = os.popen(f'curl -s {link}').read()
    return weather
while True:
    clear_screen()
    sys_type = os.name
    sys_version = os.sys.version
    sys_platform = os.sys.platform
    lc = '┌'
    rc = '┐'
    mid = '─'
    blc = '└'
    brc = '┘'
    line = '│'
    line2 = '├'
    line2flip = '┤'
    am_pm_time = datetime.datetime.now().strftime("%I:%M:%S %p")

    print(f'{lc}{mid*10} System Info {mid*11}{rc}')
    print(f'{line} {green}System Type: {reset}{sys_type} {" "*13} │')
    print(f'{line} {green}System Platform: {reset}{sys_platform}{" "*10} │')
    print(f'{line} {green}Running Time: {reset}{get_running_time()}{" "*11} │')
    print(f'{line} {green}Python Version: {reset}{sys_version[:7]}{" "*9} │')
    print(f'{line}                                  {line}')
    print(f'{line2}{mid*10} System Stats {mid*10}{line2flip}')
    print(f'{line} {green}CPU Usage: {reset}{psutil.cpu_percent()}%{" "*17}│')
    max_mem = psutil.virtual_memory().total / 1024 ** 3
    available_mem = psutil.virtual_memory().available / 1024 ** 3
    used_mem = max_mem - available_mem
    print(f'{line} {green}Memory Usage: {reset}{used_mem:.2f}GB/{max_mem:.2f}GB{" "*5}│')
    #print(f'{line} {green}Memory Usage: {reset}{psutil.virtual_memory().percent}%{" "*14}│')
    max_disk = psutil.disk_usage("/").total / 1024 ** 3
    used_disk = psutil.disk_usage("/").used / 1024 ** 3
    print(f'{line} {green}Disk Usage: {reset}{used_disk:.2f}GB/{max_disk:.2f}GB{" "*5}│')
    max_ram = psutil.virtual_memory().total / 1024 ** 3
    available_ram = psutil.virtual_memory().available / 1024 ** 3
    used_ram = max_ram - available_ram
    print(f'{line} {green}RAM Usage: {reset}{used_ram:.2f}GB/{max_ram:.2f}GB{" "*8}│')

    print(f'{line}                                  {line}')
    print(f'{line2}{mid*11} Local Info {mid*11}{line2flip}')
    print(f'{line} {green}Local Time: {reset}{am_pm_time}{" "*10}│')
    print(f'{line} {green}Local Date: {reset}{datetime.datetime.now().strftime("%m/%d/%Y")}{" "*10} │')

    # Credits Section
    print(f'{line}                                  {line}')
    print(f'{line2}{mid*11} Credits {mid*14}{line2flip}')
    Author = 'Author: Hash'
    instagram = '0xnvm'
    discord = 'hash#1234'
    github = '0xlash'
    print(f'{line} {green}Author: {reset} Hash{" "*19} │')
    print(f'{line} {green}Instagram: {reset}{instagram}{" "*17}│')
    print(f'{line} {green}Discord: {reset}{discord}{" "*15}│')
    print(f'{line} {green}Github: {reset}{github}{" "*19}│')
    #Close Section
    print(f'{blc}{mid*18}{mid*16}{brc}')
    print()

    
    time.sleep(.5)
