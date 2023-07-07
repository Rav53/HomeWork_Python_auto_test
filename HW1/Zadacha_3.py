# Напишите код, который запрашивает число и сообщает является ли оно
#  простым или составным. Используйте правило для проверки: 
#  “Число является простым,
#   если делится нацело только на единицу и на себя”.
#  Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


import math

number = int(input("Введите число: "))

if number < 0 or number > 100000:
    print("Введенное число не удовлетворяет ограничениям.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Число является простым.")
    else:
        print("Число является составным.")    