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



while True:
    clear_screen()
    sys_type = os.name
    sys_version = os.sys.version
    sys_platform = os.sys.platform
    am_pm_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    print(f'[{red}+{reset}] System Monitor {white}[{red} v1.1 {reset}-{red} By Hash {white}]{reset}\n')
    print(f'[{red} DEBUG {reset}] Time   {white}[{red}{am_pm_time}{white}]{reset}')
    print(f'[{red} DEBUG {reset}] Date   {white}[{red}{datetime.datetime.now().strftime("%d/%m/%Y")}{white}]{reset}')
    print(f'[{red} DEBUG {reset}] sys    {white}[{red}{sys_platform}{white}]{reset}')
    print(f'[{red} DEBUG {reset}] CPU    {white}[{red}{psutil.cpu_percent()}%{white}]{reset}')
    print(f'[{red} DEBUG {reset}] Memory {white}[{red}{psutil.virtual_memory().percent}%{white}]{reset}')
    print(f'[{red} DEBUG {reset}] Disk   {white}[{red}{psutil.disk_usage("/").percent}%{white}]{reset}')
    print(f'[{red} DEBUG {reset}] Uptime {white}[{red}{get_running_time()}{white}]{reset}')
    print()
    time.sleep(1)
