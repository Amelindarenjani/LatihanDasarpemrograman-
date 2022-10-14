# Deskriptif
# membuat variabel nama  barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

nama_barang = input("Masukan nama barang : ")
harga_barang1 = int(input("Masukan harga barang :"))
persen = 10
harga_keuntungan = int(harga_barang1)*persen/100
harga_jual = int(harga_barang1) + harga_keuntungan
print(nama_barang, 'dijual dengan harga :', harga_jual)

nama_barang = input("Masukan nama barang : ")
harga_barang2 = int(input("Masukan harga barang : "))
persen = 10
harga_keuntungan = int(harga_barang2)*persen/100
harga_jual = int(harga_barang2) + harga_keuntungan
print(nama_barang, 'dijual dengan harga :', harga_jual)

nama_barang = input("Masukan nama barang : ")
harga_barang3 = int(input("Masukan harga barang: ")) 
persen = 10
harga_keuntungan = int(harga_barang3)*persen/100
harga_jual = int(harga_barang3) + harga_keuntungan
print(nama_barang, 'dijual dengan harga :', harga_jual)


total = harga_barang1+harga_barang2+harga_barang3
hargapersen = int(total*10 /100)
print("\n\nKeuntungan semua barang : ", hargapersen)
print("\nTotal Harga semua barang : ", total + hargapersen)