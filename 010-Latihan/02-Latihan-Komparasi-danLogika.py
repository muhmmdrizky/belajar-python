# Membuat gabungan area rentang dari angka
# Combination

inputUser = float(input("Input number less than 3 or more than 10: "))

# Checking number less than 3
isLessThan = inputUser < 3
print(f"Less than 3 = {isLessThan}")

# Checking number more than 10
isMoreThan = inputUser > 10
print(f"More than 10 = {isMoreThan}")

# Checking the number inputted is less than 3 or more than 10
isCorrect = isLessThan or isMoreThan
print(f"The number you inputted: {isCorrect}")

# ==========================================================

# Intersections
inputUser = float(input("Input number more than 3 and less than 10: "))

# Checking number more than 3
isMoreThan = inputUser > 3
print(f"More than 3 = {isMoreThan}")

# Checking number less than 10
isLessThan = inputUser < 10
print(f"Less than 10 = {isLessThan}")

# Checking the number inputted is more than and less than 10
isCorrect = isMoreThan and isLessThan
print(f"The number you inputted: {isCorrect}")
