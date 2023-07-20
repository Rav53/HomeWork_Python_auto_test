# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.



file_1 = "d:\\HomeWork\\Zadacha_1\\file_1.py"
file_2 = "d:\\HomeWork\\Zadacha_2\\file_2.js"
file_3 = "d:\\HomeWork\\Zadacha_3\\file_3.txt"


def split_path(path: str) -> tuple[str, str, str]:
# Парсинг абсолютного пути на каталог, имя и расширение файла
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext

print(split_path(file_1))
print(split_path(file_2))
print(split_path(file_3))

