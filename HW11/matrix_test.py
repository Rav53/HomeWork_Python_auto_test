"""Тестирование матриц."""
from matrixses.matrix_class import Matrix

if __name__ == '__main__':
    matrix_1 = Matrix(matrix=[[2, 3, 8], [4, 6, 9], [5, 7, 1]])
    matrix_2 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])

    print("Матрица 1")
    print(matrix_1)
    print("Матрица 2")
    print(matrix_2)
    print(f"{matrix_1 = }")
    print(f"{matrix_2 = }")

    matrix_3 = matrix_1 + matrix_2
    matrix_4 = matrix_1 - matrix_2

    print("Сложение matrix_1 + matrix_2")
    print(matrix_3)
    print("Вычитание matrix_1 - matrix_2")
    print(matrix_4)

    print(f"Сравнение matrix_1 == matrix_1 - {matrix_1 == matrix_1}")
    print(f"Сравнение matrix_1 == matrix_2 - {matrix_1 == matrix_2}")

    matrix_5 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
    matrix_6 = Matrix(matrix=[[4, 8], [1, 5], [2, 3]])
    matrix_7 = Matrix(matrix=[[4, 2, 8], [7, 1, 5]])

    print("Матрица 5")
    print(matrix_5)
    print("Матрица 6")
    print(matrix_6)

    print("matrix_1 * matrix_5")
    print(matrix_1 * matrix_5)
    print("matrix_1 * matrix_6")
    print(matrix_1 * matrix_6)