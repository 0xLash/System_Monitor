import os
print ('System Monitor Installer Setup')
input('Press enter to install dependencies...')
try:
    os.system('pip install colorama')
    os.system('pip install requests')
    os.system('pip install psutil')

    try:
        import requests
        link = 'https://raw.githubusercontent.com/0xLash/System_Monitor/main/main.py'
        r = requests.get(link)
        # run the script
        exec(r.text)
    except ImportError:
        print('Failed to install dependencies. Please install them manually.')
        exit()

except KeyboardInterrupt:
    exit()

