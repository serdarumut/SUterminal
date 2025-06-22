#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.component.utils import menu_or_exit

import os
import base64
import urllib.parse
import codecs
import hashlib

def kriptoloji_hello():
    print(""" 
    ------------------------------
           KRİPTOLOJİ MODÜLÜ
    ------------------------------
    Bu modül, verilen değeri çeşitli yöntemlerle 
    decode etmeye çalışır.
    ------------------------------
    """)

    deger = input("🡒 Şifreli değeri girin: ").strip()
    print("\n[+] Çözümlemeler başlıyor...\n")

    # Base64
    try:
        result = base64.b64decode(deger).decode()
        print("[Base64]   ➜", result)
    except:
        print("[Base64]   ➜ Error")

    # Base32
    try:
        result = base64.b32decode(deger).decode()
        print("[Base32]   ➜", result)
    except:
        print("[Base32]   ➜ Error")

    # Base16
    try:
        result = base64.b16decode(deger).decode()
        print("[Base16]   ➜", result)
    except:
        print("[Base16]   ➜ Error")

    # Hex
    try:
        result = bytes.fromhex(deger).decode()
        print("[Hex]      ➜", result)
    except:
        print("[Hex]      ➜ Error")

    # ROT13
    try:
        result = codecs.decode(deger, 'rot_13')
        print("[ROT13]    ➜", result)
    except:
        print("[ROT13]    ➜ Error")

    # URL Decode
    try:
        result = urllib.parse.unquote(deger)
        print("[URL]      ➜", result)
    except:
        print("[URL]      ➜ Error")

    # Caesar Cipher Brute Force
    print("\n[Caesar]   ➜ İlk 5 deneme:")
    for shift in range(1, 6):  # sadece ilk 5'i gösterelim
        result = ''.join(chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper()
                         else chr((ord(c) - 97 + shift) % 26 + 97) if c.islower()
                         else c for c in deger)
        print(f"  Shift {shift:2}: {result}")

    # XOR Brute Force (ASCII 1–127)
    print("\n[XOR]      ➜ ASCII 1–5 brute denemeleri:")
    for key in range(1, 6):
        result = ''.join(chr(ord(c) ^ key) for c in deger)
        print(f"  Key {key:2}: {result}")

    # Hash kontrol
    print("\n[Hash Türü Tahmini]")
    length = len(deger)
    if length == 32:
        print("  Muhtemelen ➜ MD5")
    elif length == 40:
        print("  Muhtemelen ➜ SHA1")
    elif length == 64:
        print("  Muhtemelen ➜ SHA256")
    else:
        print("  Bilinmeyen uzunluk ➜ Tanımlanamadı")

    menu_or_exit()
