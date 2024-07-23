# Data yang dimasukkan pasti String
dataPertama = input("Masukkan Angka Pertama: ")
print(dataPertama, type(dataPertama))

# Gimana kalau mau ambil data INT atau Float?
dataKedua = int(input("Masukkan Integer: "))
print(dataKedua, type(dataKedua))

dataKetiga = float(input("Masukkan float: "))
print(dataKetiga, type(dataKetiga))


# Gimana kalau boolean?
dataKeempat = bool(int(input("Masukkan Boolean: ")))
print(dataKeempat, type(dataKeempat))

nama = input("Masukkan nama anda: ")
print(nama)

angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))
hasil = angka_pertama * angka_kedua
print(f"Hasil dari {angka_pertama} * {angka_kedua} = {hasil}")