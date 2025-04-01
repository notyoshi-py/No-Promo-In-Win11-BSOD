import winreg as reg
import pyuac
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
    try:
        reg_path = r"SYSTEM\CurrentControlSet\Control\CrashControl"
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_path, 0, reg.KEY_SET_VALUE)

        reg.SetValueEx(key, "DisplayParameters", 0, reg.REG_DWORD, 4)
        print(rf"Added DisplayParameters value to HKLM\{reg_path}")
        reg.SetValueEx(key, "DisablePromo", 0, reg.REG_DWORD, 1)
        print(rf"Added DisablePromo value to HKLM\{reg_path}")

        reg.CloseKey(key)

        restart_prompt()

    except Exception as e:
        print(f"Error: {e}")

def EnablePromo():
    try:
        reg_path = r"SYSTEM\CurrentControlSet\Control\CrashControl"
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_path, 0, reg.KEY_SET_VALUE)

        try:
            reg.DeleteValue(key, "DisplayParameters")
            print(rf"Removed DisplayParameters value from HKLM\{reg_path}")
        except FileNotFoundError:
            print("DisplayParameters value not found, skipping...")

        try:
            reg.DeleteValue(key, "DisablePromo")
            print(rf"Removed DisablePromo value from HKLM\{reg_path}")
        except FileNotFoundError:
            print("DisablePromo value not found, skipping...")

        reg.CloseKey(key)

        restart_prompt()

    except Exception as e:
        print(f"Error: {e}")

def restart_prompt():
    restart_var = input("You need to restart to apply changes, do it now? (Y/N): ").strip().lower()
    if restart_var == "y":
        os.system("shutdown /r /t 0")
    else:
        print("Restart manually later. You can safely close this app.")

# Ensure script is running as Administrator
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
    exit()

print(splash)
print(Back.RED + "WARNING: This modifies system registry. You proceed at your own risk.")
input(Back.WHITE + Fore.BLACK + "Press ENTER to continue" + Style.RESET_ALL)

os.system("cls")

print(splash)
print("Disable/Enable promo ads in new Windows 11 Crash Screen!\n")

print("1. Disable promo in crash screen")
print("2. Enable promo in crash screen\n")

while True:
    try:
        action_choose = int(input("Choose an action: "))
        if action_choose in [1, 2]:
            break
        print("Invalid number, try again.")
    except ValueError:
        print("Invalid input, try again.")

if action_choose == 1:
    DisablePromo()
else:
    EnablePromo()
