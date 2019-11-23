import socket
import subprocess
import sys
from datetime import datetime
from colorama import Fore, Style, init


init()
print(Fore.GREEN + Fore.LIGHTGREEN_EX +""" 


 ██▓███ ▓██   ██▓ ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████  ▄████▄   ▄▄▄       ███▄    █ 
▓██░  ██▒▒██  ██▒▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
▓██░ ██▓▒ ▒██ ██░▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
▒██▄█▓▒ ▒ ░ ▐██▓░▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ░ ██▒▓░▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
▒▓▒░ ░  ░  ██▒▒▒ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░▒ ░     ▓██ ░▒░ ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
░░       ▒ ▒ ░░  ░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
         ░ ░                  ░ ░     ░                    ░  ░ ░            ░  ░         ░ 
         ░ ░                                                  ░                             

Coded By Xelj

	""")
Server  = input("Introduce una web: ")
ServerIP  = socket.gethostbyname(Server)

print("-" * 60)
print("Porfavor espera, escaneando el host", ServerIP)
print("-" * 60)

t1 = datetime.now()


try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ServerIP, port))
        if result == 0:
            print("Puerto {}:       Open".format(port))
            sock.close()

except KeyboardInterrupt:
    print("Has presionado Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("El host no se ha resuelto, saliendo..")
    sys.exit()

except socket.error:
    print("No se pudo conectar")
    sys.exit()

t2 = datetime.now()

total =t2 - t1

print("Escaneo completo: ", total)
