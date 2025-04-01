import winreg as reg
import pyuac, Win32Security
import colorama
from colorama import Back, Fore, Style
import os
from time import sleep

splash = r'''
 _   _        ______                            _____       ______  _____  ___________ 
| \ | |       | ___ \                          |_   _|      | ___ \/  ___||  _  |  _  \
|  \| | ___   | |_/ / __ ___  _ __ ___   ___     | | _ __   | |_/ /\ `--. | | | | | | |
| . ` |/ _ \  |  __/ '__/ _ \| '_ ` _ \ / _ \    | || '_ \  | ___ \ `--. \| | | | | | |
| |\  | (_) | | |  | | | (_) | | | | | | (_) |  _| || | | | | |_/ //\__/ /\ \_/ / |/ / 
\_| \_/\___/  \_|  |_|  \___/|_| |_| |_|\___/   \___/_| |_| \____/ \____/  \___/|___/  
                                                                                       
Created by not.yoshi
My RU TG channels - https://t.me/drop_yoshi



'''

colorama.init(autoreset=True)

def DisablePromo():
    with r"SYSTEM\CurrentControlSet\Control\CrashControl" as reg_path:
        key = reg.OpenKeyEx("HKEY_LOCAL_MACHINE", reg_path, 0, reg.KEY_WRITE)

        reg.SetValueEx(key, "DisplayParameters", 0, reg.REG_DWORD, 4)
        print(rf"Added DisplayParameters value to HKLM\{reg_path}")
        reg.SetValueEx(key, "DisablePromo", 0, reg.REG_DWORD, 1)
        print(rf"Added DisablePromo value to HKLM\{reg_path}")
    restartVar = str.lower(input("You need to restart to apply changes, do it now?(Y/N): "))
    if restartVar == "y":
        os.system("shutdown /r /t 0")
    elif restartVar == "n":
        print("\nYou need to restart manually later. Now you can safely close this app.")
    else:
        print("Got other input, taking it as NO")
        print("\nYou need to restart manually later. Now you can safely close this app.")

def EnablePromo():
    with r"SYSTEM\CurrentControlSet\Control\CrashControl" as reg_path:
        key = reg.OpenKeyEx("HKEY_LOCAL_MACHINE", reg_path, 0, reg.KEY_WRITE)

        reg.DeleteValue(key, "DisplayParameters")
        print(rf"Removed DisplayParameters value from HKLM\{reg_path}")
        reg.DeleteValue(key, "DisablePromo")
        print(rf"Removed DisablePromo value from HKLM\{reg_path}")
    restartVar = str.lower(input("You need to restart to apply changes, do it now?(Y/N): "))
    if restartVar == "y":
        os.system("shutdown /r /t 0")
    elif restartVar == "n":
        print("\nYou need to restart manually later. Now you can safely close this app.")
    else:
        print("Got other input, taking it as NO")
        print("\nYou need to restart manually later. Now you can safely close this app.")

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()

print(splash)

print(Back.RED + "THIS IS NOT SUPPOSED TO HARM DEVICE, HOWEVER, YOU ARE RESPONSIBLE FOR ALL ACTIONS AND ACT ON YOUR OWN RISK")
continueVar = input(Back.WHITE + Fore.BLACK + "Press ENTER to continue" + Style.RESET_ALL)

os.system("cls")

print(splash)
print("Disable/Enable promo ads in new Windows 11 Crash Screen!\n")

print("1. Disable promo in crash screen")
print("2. Enable promo in crash screen\n")
while True:
    try:
        actionChoose = int(input("Choose next action to do:"))
        if actionChoose in [1, 2]:
            break
        else:
            print("\nGot wrong number, please type correct one instead.")
    except ValueError:
        print("\nGot wrong input, please type correct one instead.")

if actionChoose == 1:
    DisablePromo()
elif actionChoose == 2:
    EnablePromo()