from src.component.utils import menu_or_exit
import os
def nmap_hello():
    print("""
    --------------------------
            NMAP
    --------------------------
    1) -sP       # Aktif IP taraması (ping)
    2) -p 1-65535 -sS -T4   # Tüm portlara hızlı SYN tarama
    3) -sV -sS -A -T4       # Servis + detaylı bilgi (hızlı)
    4) -sV -sS -A -T5       # Servis + detaylı bilgi (çok hızlı)
    5) -sV -O -sS -T5       # Servis + OS bilgisi (çok hızlı)
    6) -Pn -sS -sV          # Ping atlama + SYN + servis bilgisi
    """)

    ip = input("IP Adresi Giriniz : ")
    scan_id = input("İşlem No Giriniz (1–6): ")

    options = {
        "1": "-sP",
        "2": "-p 1-65535 -sS -T4",
        "3": "-sV -sS -A -T4",
        "4": "-sV -sS -A -T5",
        "5": "-sV -O -sS -T5",
        "6": "-Pn -sS -sV"
    }

    if scan_id in options:
        print(f"[+] Komut çalıştırılıyor: nmap {options[scan_id]} {ip}")
        os.system(f"nmap {options[scan_id]} {ip}")
    else:
        print("[-] Geçersiz seçim!")
    menu_or_exit()
