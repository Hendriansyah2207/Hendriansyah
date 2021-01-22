def masuk():
    print("Selamat Datang!")

def menu():
    print("Menu")
    print("1.Daftar Kontak")
    print("2.Tambah Kontak")
    print("3.Keluar")

def satu():
    print("Daftar Kontak")
    print("Nama : Hendri")
    print("No.Telfon : 08119469699")
    print("Nama : Nafisha")
    print("No.Telfon : 08111993405")
    
def dua():
    print("Nama : ")
    print("No Telepon : ")

def ditambahkan():
    print("Kontak Berhasil Ditambahkan")

def tiga():
    print("Program Selesai, Sampai Jumpa Kembali!")

def tidak():
    print("Menu tidak tersedia")


print("Selamat Datang !")
masukan = input("Pilih Menu : ")
if masukan =="Minta Menu":
    menu()
elif masukan == "1":
    satu()
elif masukan == "2":
    dua()
elif masukan == "Sudah Ditambahkan":
    ditambahkan()
elif masukan == "3":
    tiga()
elif masukan > "3":
    tidak()