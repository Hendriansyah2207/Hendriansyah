Teori = 78
Praktek = 78
KKM = 70
if Teori==Praktek > KKM:
    print("Selamat, anda lulus")
if Teori > KKM > Praktek:  
    print("Anda Harus Mengulang Ujian Praktek")
if Praktek > KKM > Teori:
    print("Anda Harus Mengulang Ujian Teori")
if Teori==Praktek < KKM:
    print("Anda Harus mengulang ujian Teori dan Praktek")