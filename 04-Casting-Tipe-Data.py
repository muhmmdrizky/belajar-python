"""
Belajar Casting Tipe Data
- Mengubah dari satu tipe data ke tipe data lain
- Tipe data: Int, Float, Str, Bool
"""

# INTEGER
print("====INTEGER====")
data_int = 9
print("Data: ", data_int, "Tipe:", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # Akan false jika nilai INT = 0
print("Data: ", data_float, "Tipe: ", type(data_float))
print("Data: ", data_str, "Tipe: ", type(data_str))
print("Data: ", data_bool, "Tipe: ", type(data_bool))

# FLOAT
print("====FLOAT====")
data_float = 9.9
print("Data: ", data_float, "Tipe:", type(data_float))

data_int = int(data_float)  # Akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # Akan false jika nilai Float = 0
print("Data: ", data_int, "Tipe: ", type(data_int))
print("Data: ", data_str, "Tipe: ", type(data_str))
print("Data: ", data_bool, "Tipe: ", type(data_bool))

# BOOLEAN
print("====BOOLEAN====")
data_bool = False
print("Data: ", data_bool, "Tipe:", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Data: ", data_int, "Tipe: ", type(data_int))
print("Data: ", data_str, "Tipe: ", type(data_str))
print("Data: ", data_float, "Tipe: ", type(data_float))

# STRING
print("====STRING====")
data_str = "5"
print("Data: ", data_str, "Tipe:", type(data_str))

data_int = int(data_str)  # String harus angka
data_bool = bool(data_str)  # String harus angka
data_float = float(data_str)  # False jika string kosong
print("Data: ", data_int, "Tipe: ", type(data_int))
print("Data: ", data_bool, "Tipe: ", type(data_bool))
print("Data: ", data_float, "Tipe: ", type(data_float))
