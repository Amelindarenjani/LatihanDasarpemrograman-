# Deskriptif
# membuat variabel nama  barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0
while(True):

    nama_barang = input("Masukan nama barang : ")
    harga_barang = int(input("Masukan harga barang : "))
    persen = int(input("masukan persen barang : "))
    barang_terjual = int(input("masukan jumlah barang : "))

    keuntungan_persen = harga_barang * persen/100
    harga_jual = harga_barang + keuntungan_persen

    # menghitung modal
    modal = harga_barang *  barang_terjual
    # menghitung modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    # menghitung laba
    laba = keuntungan_persen * barang_terjual
    # menghitung laba keseluruhan 
    laba_keseluruhan = laba_keseluruhan + laba

    print("\n\nbarang", nama_barang)
    print("harga barang                 :", harga_barang)
    print("keuntungan per barang        :", keuntungan_persen)
    print("dijual dengan harga          :", harga_jual)
    print("terjual                      :", barang_terjual)
    print("modal                        :", modal)
    print("laba                         :", laba)
    

    ApakahLanjut = input("apakah ingin input barang lain? Y lanjut : ")
    if(ApakahLanjut != 'Y'):
        break

print("\n\n========STRUK========")
print("Modal keseluruhan    : Rp. ", modal_keseluruhan)
print("Laba keseluruhan     : Rp. ", laba_keseluruhan)