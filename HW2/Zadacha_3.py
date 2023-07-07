# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму
# и произведение дробей.Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

# Ввод данных
input_str1 = input("Введите числитель: ")
input_str2 = input("Введите знаменатель: ")

# Преобразование строкового вида в объекты Fraction
fraction1 = Fraction(input_str1)
fraction2 = Fraction(input_str2)

# Сумма дробей
sum_fraction = fraction1 + fraction2

# Произведение дробей
product_fraction = fraction1 * fraction2

# Вывод результата
print("Сумма числителя и знаменателя:", sum_fraction)
print("Произведение числителя и знаменателя:", product_fraction)
