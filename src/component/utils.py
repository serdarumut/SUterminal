def menu_or_exit():
    while True:
        secim = input("\n[m] Ana menüye dön  |  [q] Çıkış yap\n🡒 Seçim: ").strip().lower()
        if secim == "m":
            return
        elif secim == "q":
            print("Çıkış yapılıyor...")
            exit()
        else:
            print("[-] Geçersiz seçim, sadece 'm' ya da 'q' girin.")
