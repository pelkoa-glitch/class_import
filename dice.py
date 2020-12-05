from random import randint


class Die:
    """Модель кубика, который можно подбросить."""
    def __init__(self, sides=6):
        """Инициализация кубика"""
        self.sides = sides

    def roll_die(self):
        """Бросок кубика"""
        return randint(1, self.sides)


# Создание шестигранного кубика и вывод результата 10 его бросков.
die_6 = Die()

results = []
"""Бросок кубика"""
for roll_number in range(10):
    result = die_6.roll_die()
    results.append(result)
print("Результат десяти бросков шестигранного кубика:")
print(results)

# Создание кубика с 10 сторонами и вывод результата 10 бросков.
die_10 = Die(sides=10)

results = []
"""Бросок кубика"""
for roll_number in range(10):
    result = die_10.roll_die()
    results.append(result)
print("\nРезультат десяти бросков десятигранного кубика:")
print(results)

# Создание кубика с 12 сторонами и вывод результата 10 бросков.
die_20 = Die(sides=20)

results = []
"""Бросок кубика"""
for roll_number in range(10):
    result = die_20.roll_die()
    results.append(result)
print("\nРезультат десяти бросков двадцатигранного кубика:")
print(results)
