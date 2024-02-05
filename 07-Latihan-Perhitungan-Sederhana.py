# Latihan konversi satuan temperatur

# Konversi celcius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATUR \n")

celcius = float(input("Masukkan suhu dalam celcius: "))
print(f"Suhu adalah {celcius} Celcius")

# Reamur
reamur = (4 / 5) * celcius
print(f"Suhu dalam Reamur adalah {reamur} Reamur")

# Fahreinheit
fahrenheit = ((9 / 5) * celcius) + 32
print(f"Suhu dalam Fahreinheit adalah {fahrenheit} Fahreneit")

# Kelvin
kelvin = celcius + 273
print(f"Suhu dalam Kelvin adalah {kelvin} Kelvin")
