# Konversi Fahrenheit ke Kelvin
inputFahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
kelvin = (inputFahrenheit - 32) * 5 / 9 + 273.15
print(
    f"Hasil dari konversi {inputFahrenheit} Fahrenheit ke Kelvin adalah {kelvin} Kelvin"
)

# Konversi Kelvin ke Fahrenheit
inputKelvin = float(input("Masukkan suhu dalam Kelvin: "))
fahrenheit = (inputKelvin - 273.15) * 9 / 5 + 32
print(
    f"Hasil dari konversi {inputKelvin} Kelvin ke Fahrenheit adalah {fahrenheit} Fahrenheit"
)
