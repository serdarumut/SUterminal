#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.component.utils import menu_or_exit

import os

def mac_degis():
    print("""
    -----------------------------
            MAC CHANGER
    -----------------------------
    0 - Otomatik rastgele MAC adresi ata
    1 - Manuel olarak MAC adresi belirle
    2 - Orijinal MAC adresine dön
    """)

    islemno = input("🡒 İşlem No giriniz (0–2): ").strip()
    interface = input("🡒 Ağ arayüzü (örnek: eth0, wlan0): ").strip()

    if islemno == "0":
        os.system(f"ifconfig {interface} down")
        os.system(f"sudo macchanger -r {interface}")
        os.system(f"ifconfig {interface} up")
        print("[+] MAC adresi rastgele olarak değiştirildi.")

    elif islemno == "1":
        yeni_mac = input("🡒 Yeni MAC adresini girin: ").strip()
        os.system(f"ifconfig {interface} down")
        os.system(f"sudo macchanger --mac {yeni_mac} {interface}")
        os.system(f"ifconfig {interface} up")
        print(f"[+] MAC adresi manuel olarak {yeni_mac} olarak ayarlandı.")

    elif islemno == "2":
        os.system(f"ifconfig {interface} down")
        os.system(f"sudo macchanger -p {interface}")
        os.system(f"ifconfig {interface} up")
        print("[+] Orijinal MAC adresine dönüldü.")

    else:
        print("[-] Geçersiz işlem numarası!")

    menu_or_exit()
