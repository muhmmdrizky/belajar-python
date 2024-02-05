# Latihan komparasi dan logika

inputNumber = int(input("Masukkan angka: "))

"""
akan true jika Lebih dari 0 dan kurang dari 5 
atau lebih dari 8 dan kurang dari 11
"""
result = (inputNumber > 0 and inputNumber < 5) or (inputNumber > 8 and inputNumber < 11)
print(f"Hasil soal pertama: {result}")

"""
Pernyataan benar jika nilai inputNumber kurang dari 0, 
atau jika nilai inputNumber lebih besar dari 5 dan kurang dari 8, 
atau jika nilai inputNumber lebih besar dari 11.
"""
result = (inputNumber < 0) or (5 < inputNumber < 8) or (inputNumber > 11)
print(f"Hasil soal kedua: {result}")
