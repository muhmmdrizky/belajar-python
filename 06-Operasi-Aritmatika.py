a = 6
b = 5

# Operasi penjumlahan
hasil = a + b
print(f"{a} + {b} = {hasil}")

# Operasi pengurangan
hasil = a - b
print(f"{a} - {b} = {hasil}")

# Operasi perkalian
hasil = a * b
print(f"{a} * {b} = {hasil}")

# Operasi pembagian
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi modulus
hasil = a % b
print(f"{a} % {b} = {hasil}")

# Operasi eksponen (pangkat)
hasil = a**b
print(f"{a} ** {b} = {hasil}")

# Operasi floor division
hasil = a // b
print(f"{a} // {b} = {hasil}")

"""
PRIORITAS OPERASI:
- ()
- Eksponen
- Perkalian dan teman-temannya * / ** % //
- Penjumlahan dan Pengurangan
"""

x = 3
y = 2
z = 4

hasil = x**y * (z + x) / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z

print(x, "+", y, "*", z, "=", hasil)  # kurung akan mengambil langkah paling pertama
hasil = (x + y) * z

print("(", x, "+", y, ") *", z, "=", hasil)
