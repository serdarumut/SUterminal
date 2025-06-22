#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def gobuster_hello():
    print("""  
    -----------------------------
              GOBUSTER
    -----------------------------
    0  -  Genel         rockyou.txt
         # En yaygın şifre listesi (brute-force için)

    1  -  Directory     common.txt
         # Küçük & hızlı dizin taraması (CTF’ler için ideal)

    2  -  Username      names.txt
         # Kullanıcı adı denemeleri için (FTP, SSH, web login)

    3  -  Directory     apache-user-enum-1.0.txt
    4  -  Directory     apache-user-enum-2.0.txt
         # Apache kullanıcı dizinleri keşfi (web shell vs.)

    5  -  Directory     directory-list-1.0.txt
         # Hızlı ve basit dizin listesi (eski siteler)

    6  -  Directory     directory-list-2.3-medium.txt
         # Gerçek hedeflerde detaylı tarama için önerilir

    7  -  Directory     directory-list-2.3-small.txt
         # Daha hızlı ama az kapsamlı – başlangıç için ideal

    8  -  Directory     directory-list-lowercase-2.3-medium.txt
    9  -  Directory     directory-list-lowercase-2.3-small.txt
         # Küçük harf zorunlu URL’ler için (case sensitive)

    10 -  Directory     medium.txt
         # Genel amaçlı dizin taraması için

    11 -  Password      fasttrack.txt
         # Az ama etkili şifreler – hızlı brute-force

    12 -  Password      best110.txt
         # En çok tutan 110 şifre – çok hızlı testler
    """)

    ip = input("🡒 IP adresi veya Web adresi: ").strip()
    islemno = input("🡒 Wordlist ID giriniz (0-12): ").strip()

    wordlists = {
        "0": "rockyou.txt",
        "1": "common.txt",
        "2": "names.txt",
        "3": "apache-user-enum-1.0.txt",
        "4": "apache-user-enum-2.0.txt",
        "5": "directory-list-1.0.txt",
        "6": "directory-list-2.3-medium.txt",
        "7": "directory-list-2.3-small.txt",
        "8": "directory-list-lowercase-2.3-medium.txt",
        "9": "directory-list-lowercase-2.3-small.txt",
        "10": "medium.txt",
        "11": "fasttrack.txt",
        "12": "best110.txt"
    }

    if islemno in wordlists:
        dosya = wordlists[islemno]
        path = f"./src/wordlist/{dosya}"
        print(f"\n[+] Komut çalıştırılıyor: gobuster dir -u {ip} -w {path}\n")
        os.system(f"gobuster dir -u {ip} -w {path}")
    else:
        print("[-] Hatalı seçim! Geçerli bir ID giriniz (0-12).")
        
        
        
        
