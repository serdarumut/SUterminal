#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Modülleri içeri al
import src.component.nmap as nmap
import src.component.gobuster as gobuster
import src.component.hydra as hydra
import src.component.file as files
import src.component.kriptoloji as kripto
import src.component.macchanger as macch
import src.component.firewall as firewall

def figlet():
    os.system("clear")
    if os.system("which figlet > /dev/null") != 0:
        print("[!] Figlet yüklü değil. Kuruluyor...")
        os.system("sudo apt install figlet -y")
    os.system("figlet Hosgeldin Serdar Knkssss")

def anaekran():
    print("""
    -----------------------------
              ARAÇ MENÜSÜ
    -----------------------------
    1 - NMAP               (Ağ tarama)
    2 - Gobuster           (Dizin keşfi)
    3 - Hydra              (Şifre brute-force)
    4 - Binwalk            (Dosya analizi)
    5 - Kriptoloji         (Decode analiz)
    6 - MAC Changer        (MAC değiştirme)
    7 - Firewall Tespiti   (WAF kontrol)
    q - Çıkış
    """)

def main():
    figlet()
    while True:
        anaekran()
        islemno = input("🡒 İşlem numarası seçin: ").strip()
        if islemno == "1":
            nmap.nmap_hello()
        elif islemno == "2":
            gobuster.gobuster_hello()
        elif islemno == "3":
            hydra.hydra_hello()
        elif islemno == "4":
            files.file_information()
        elif islemno == "5":
            kripto.kriptoloji_hello()
        elif islemno == "6":
            macch.mac_degis()
        elif islemno == "7":
            firewall.firewall_hello()
        elif islemno.lower() == "q":
            print("Çıkış yapılıyor...")
            break
        else:
            print("[-] Geçersiz seçim. Lütfen 1–7 arası bir sayı ya da 'q' girin.")
        input("\n⏎ Devam etmek için ENTER'a basın...")

if __name__ == "__main__":
    main()
