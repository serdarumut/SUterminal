#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def hydra_hello():
    print("""  
    -----------------------------
              HYDRA
    -----------------------------
    Brute-force saldırı aracı.
    Kullanıcı adı ve parola denemeleri yapar.
    
    ID  | Tür         | Wordlist
    -----------------------------
    0   | Genel       | rockyou.txt
    1   | Directory   | common.txt
    2   | Username    | names.txt
    3   | Directory   | apache-user-enum-1.0.txt
    4   | Directory   | apache-user-enum-2.0.txt
    5   | Directory   | directory-list-1.0.txt
    6   | Directory   | directory-list-2.3-medium.txt
    7   | Directory   | directory-list-2.3-small.txt
    8   | Directory   | lowercase-2.3-medium.txt
    9   | Directory   | lowercase-2.3-small.txt
    10  | Directory   | medium.txt
    11  | Password    | fasttrack.txt
    12  | Password    | best110.txt
    """)

    ip = input("🡒 Hedef IP / Domain : ").strip()
    servis = input("🡒 Servis (örnek: ssh, ftp, http-get): ").strip()
    username = input("🡒 Kullanıcı adı : ").strip()
    islemno = input("🡒 Wordlist ID : ").strip()

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
        cmd = f"hydra -l {username} -P {path} {ip} {servis}"
        print(f"\n[+] Komut çalıştırılıyor: {cmd}\n")
        os.system(cmd)
    else:
        print("[-] Geçersiz wordlist ID girdiniz!")
