# Напишите функцию для транспонирования матрицы


matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix :
    print(row)
transpon_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("\n")
for row in transpon_matrix:
    print(row)    