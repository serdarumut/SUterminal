#!/usr/bin/env python
#  -*- coding utf-8 -*-

import os

def nmap_hello():
	print("""
	
	--------------------------
	NMAP
	--------------------------
	
	echo "1) -sP       # Aktif IP taraması (ping)"
	echo "2) -p 1-65535 -sS -T4   # Tüm portlara hızlı SYN tarama"
	echo "3) -sV -sS -A -T4       # Servis + detaylı bilgi (hızlı)"
	echo "4) -sV -sS -A -T5       # Servis + detaylı bilgi (çok hızlı)"
	echo "5) -sV -O -sS -T5       # Servis + OS bilgisi (çok hızlı)"
	echo "6) -Pn -sS -sV          # Ping atlama + SYN + servis bilgisi"
	
	
	
	""")
	
	ip = input("Ip Adresi Giriniz : ")
	islemno = input("Islem No Giriniz : ")
	
	if(islemno=="0"):
		os.system("nmap "+ip)
	if(islemno=="1"):
		os.system("nmap -sC -sV "+ip)
	if(islemno=="2"):
		os.system("nmap "+ip)
	if(islemno=="3"):
		os.system("nmap -sC -sV "+ip)
	if(islemno=="4"):
		os.system("nmap "+ip)
	if(islemno=="5"):
		os.system("nmap -sC -sV "+ip)	
		
		
		
nmap_hello()




