import os
import subprocess
import time
import psutil
from colorama import Fore, Style

def wait_for_minecraft():
    print(Fore.YELLOW + "\n[!] Waiting for Minecraft to open..." + Style.RESET_ALL)
    
    while True:
        for process in psutil.process_iter(attrs=['name']):
            if 'Minecraft' in process.info['name']:
                print(Fore.GREEN + "[+] Minecraft detected! Starting import..." + Style.RESET_ALL)
                return
        time.sleep(3)

def mcpack_importer():
    print(Fore.CYAN + "\nMCPACK Quick Importer - StevePVPs" + Style.RESET_ALL)
    
    folder_path = input("Enter path for quick import: ").strip().replace("\"", "")
    
    if not os.path.isdir(folder_path):
        print(Fore.RED + "[!] Invalid directory. Please check the path and try again." + Style.RESET_ALL)
        return
    
    mcpack_files = [f for f in os.listdir(folder_path) if f.endswith(".mcpack")]
    
    if not mcpack_files:
        print(Fore.YELLOW + "[!] No .mcpack files found in the given directory." + Style.RESET_ALL)
        return
    
    wait_for_minecraft()
    
    print(Fore.MAGENTA + f"\n[+] Found {len(mcpack_files)} .mcpack files. Importing...\n" + Style.RESET_ALL)
    
    for pack in mcpack_files:
        pack_path = os.path.join(folder_path, pack)
        try:
            subprocess.Popen([pack_path], shell=True)
            print(Fore.GREEN + f"[+] {pack}" + Style.RESET_ALL)
            time.sleep(2)
        except Exception as e:
            print(Fore.RED + f"[!] Failed to open {pack}: {e}" + Style.RESET_ALL)
    
    print(Fore.CYAN + "\n[✔] All packs have been imported successfully!" + Style.RESET_ALL)

if __name__ == "__main__":
    mcpack_importer()
