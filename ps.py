from socket import *
from colorama import Fore
import os

try:
    # host adderss
    os.system("cls")
    print(Fore.LIGHTGREEN_EX+"""

                  _
 _ __   ___  _ __| |_     ___  ___ __ _ _ __  _ __   ___ _ __
| '_ \ / _ \| '__| __|   / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| |_) | (_) | |  | |_    \__ \ (_| (_| | | | | | | |  __/ |
| .__/ \___/|_|   \__|   |___/\___\__,_|_| |_|_| |_|\___|_|
|_|

    """)
    host = input(Fore.WHITE+"Enter Your target: ")
    # range [1,2]
    range_aval = input("Enter your range (1): ")
    range_dovom = input("Enter your range (2): ")
    for i in range(int(range_aval), int(range_dovom)):
        sock_POBT = socket(AF_INET,SOCK_STREAM)
        con = sock_POBT.connect_ex((host,i))
        print()
        if con == 0:
            servisname = getservbyport(i)
            print(Fore.LIGHTGREEN_EX+"[<=>] port " , i , servisname , " open ")
        else:
            print(Fore.LIGHTRED_EX+"[-] port ", i , " close ")
except :
    print("Plz check Host or internet ")
    