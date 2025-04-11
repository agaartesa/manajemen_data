#Inputan
nm = input("Masukkan Nama: ")
nt = float(input("Masukkan Nilai Tugas: "))
nu = float(input("Masukkan Nilai Ujian: "))

#proses hitung nilai
na = 40/100 * nt + 60/100 * nu

#output
print("Halo nama saya", nm, " Nilai Akhir saya adalah: ", na)