print(8*"="+ "Program Aplikasi Sederhana" +8*'=')

while (True):
    print('Menu')
    print('1. Hitung luas segitiga')
    print('2. Hitung luas persegi panjang')
    print('3. Menentukan angka ganjil genap')
    print('Quit')
    
    listMenu = input('Masukan pilihan : ')

    if listMenu == "1":
        print("Menu--Hitung luas segitiga")
        alas = int(input("\nMasukan panjang alas : "))
        tinggi = int(input("Masukan tinggi : "))

        rumus_segitiga = 1/2 * alas * tinggi
        print("Luas segitiga : ", rumus_segitiga)

    elif listMenu == "2":
        print("Menu -- Hitung luas persegi panjang")
        panjang = int(input("\nMasukan panjang : "))
        lebar = int(input("Masukan lebar : "))

        rumus_PersegiPanjang =  panjang * lebar
        print("Luas persegi panjang : ", rumus_PersegiPanjang)

    elif listMenu == "3":
        print("Menu -- Menentukan angka ganjil genap")
        angka = int(input("\nMasukan angka : "))

        if (angka % 2 == 0):
            print("angka", angka, "merupakan angka genap")
        else :
            print("angka", angka, "merupakan bilangan ganjil")

    else:
        menu = input("Terimakasih")
        print("--- --- ---")
        break
