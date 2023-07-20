# Создайте функцию генератор чисел Фибоначчи

n = int(input("Сколько показать чисел фиббоначи? "))
fib1 = fib2 = 1
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
    