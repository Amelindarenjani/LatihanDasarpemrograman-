# Deskriptif
# membuat variabel nama  barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

while(True):

    nama_barang = input("Masukan nama barang : ")
    harga_barang1 = int(input("Masukan harga barang : "))
    persen = input("masukan persen barang : ")
    harga_keuntungan = int(harga_barang1)*int(persen)/100
    harga_jual = int(harga_barang1) + harga_keuntungan
    print(nama_barang, 'dijual dengan harga :', harga_jual)

    ApakahLanjut = input("apakah ingin input barang lain? Y lanjut : ")
    if(ApakahLanjut != 'Y'):
        break
