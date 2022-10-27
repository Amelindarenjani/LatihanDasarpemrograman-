# program  penilaian (kondisi percabangan) by Amelinda Renjani

while(True):

    print("======Program Grade Nilai======")
    mapel = input("Masukkan mata pelajaran : ")
    skor = input("Masukkan skor : ")

    if (skor.isnumeric() == True):
        skor_int = int(skor)
        if skor_int >= 101:
            nilai = "Nilai berlebihan, harap hitung kembali!"
            predikat = "Tidak dapat memberikan predikat"
        elif skor_int >= 90:
            nilai = "A"
            predikat = "Dengan Pujian"
        elif skor_int >= 80:
            nilai =  "B"
            predikat =  "Sangat memuaskan"
        elif skor_int >= 70:
            nilai = "C"
            predikat = "Memuaskan"
        elif skor_int >= 60:
            nilai = "D"
            predikat = "Tidak memuaskan"
        elif skor_int >= 0:
            nilai = "E"
            predikat = "Tidak Lulus"

        print("===========================")
        print("Mata Pelajaran   : ", mapel)
        print("Nilai            : ", nilai)
        print("Predikat         : ", predikat)

    else:
        print("format yang dimasukkan salah!")

    apakahLanjut = input("\nApakah anda ingin mendata kembali? Y or N : ")
    if(apakahLanjut != "Y" ):
        break


