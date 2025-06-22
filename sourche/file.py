#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def file_information():
    print("""
    -----------------------------
          BINWALK DOSYA ANALİZİ
    -----------------------------
    Bu araç, dosya içindeki gömülü verileri ve
    gizli dosyaları analiz eder.

    NOT: Dosya masaüstünde olmalı!
    -----------------------------

    0 - Binwalk -e (extract mode)
    1 - Binwalk -B (entropy göster)
    2 - Binwalk -E (dosya uzantısı tahmini)
    3 - Binwalk -D (yalnızca imaj çıkarımı)
    """)

    islemno = input("🡒 İşlem No giriniz (0–3): ").strip()
    dosyaadi = input("🡒 Dosya adını giriniz (örn: ornek.jpg): ").strip()
    path = f"/home/kali/Desktop/{dosyaadi}"

    if not os.path.exists(path):
        print("[-] Dosya bulunamadı! Masaüstünde olduğundan emin olun.")
        return

    if islemno == "0":
        os.system(f"binwalk -e '{path}'")
    elif islemno == "1":
        os.system(f"binwalk -B '{path}'")
    elif islemno == "2":
        os.system(f"binwalk -E '{path}'")
    elif islemno == "3":
        os.system(f"binwalk -D='jpg' '{path}'")
    else:
        print("[-] Geçersiz işlem numarası!")
