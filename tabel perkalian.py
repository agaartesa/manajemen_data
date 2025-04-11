bilangan = int(input("Masukkan Bilangan :"))

#menampilkan tabel perkalian
print ("Tabel Perkalian Untuk Bilangan ", bilangan)
for i in range(1,11):
    hasil = bilangan * i
    print(f"{bilangan} x {i} = {hasil}")