#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def firewall_hello():
    print("""
    -----------------------------
             FIREWALL
    -----------------------------
    Bu modül, hedef web sunucusunda bir WAF
    (Web Application Firewall) olup olmadığını
    kontrol eder. Araç: wafw00f
    """)

    ip = input("🡒 Hedef IP veya domain (http dahil olabilir): ").strip()

    print(f"\n[+] Taranıyor: {ip}\n")
    os.system(f"wafw00f {ip}")
