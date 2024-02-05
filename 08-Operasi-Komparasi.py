"""
Operator komparasi menghasilkan nilai boolean (True or False)
"""

angkaPertama = int(input("Masukkan angka pertama: "))
angkaKedua = int(input("Masukkan angka kedua: "))

# Lebih besar dari
lebihBesarDari = angkaPertama > angkaKedua
print(f"{angkaPertama} lebih besar dari {angkaKedua} adalah {lebihBesarDari}")

# Kurang dari
kurangDari = angkaPertama < angkaKedua
print(f"{angkaPertama} kurang dari {angkaKedua} adalah {kurangDari}")

# Sama dengan
samaDengan = angkaPertama == angkaKedua
print(f"{angkaPertama} sama dengan {angkaKedua} adalah {samaDengan}")

# Tidak sama dengan
tidakSamaDengan = angkaPertama != angkaKedua
print(f"{angkaPertama} tidak sama dengan {angkaKedua} adalah {tidakSamaDengan}")

# Lebih dari sama dengan
lebihDariSamaDengan = angkaPertama >= angkaKedua
print(
    f"{angkaPertama} lebih dari sama dengan {angkaKedua} adalah {lebihDariSamaDengan}"
)

# Kurang dari sama dengan
kurangDariSamaDengan = angkaPertama <= angkaKedua
print(
    f"{angkaPertama} kurang dari sama dengan {angkaKedua} adalah {kurangDariSamaDengan}"
)

# Object Identity
"""
Buat ngebandingin yang bukan angka, sebaiknya gunakan is atau is not
"""
x = 5
y = 6
hasil = x is not y
print(hasil)
