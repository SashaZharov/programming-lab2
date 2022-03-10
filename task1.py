import module
import time
from random import randint


# Создаем путсую матрицу
m, n = map(int, input("Введите кол-во строк и столбцов матрицы: ").split())
print(n, m)
matrix = [[0]*n for i in range(m)]
print(matrix)

# заполнение матрицы
for i in range(m):
    for j in range(n):
        matrix[i][j] = randint(1, 100)
print(matrix)

action = int(input("Введите действие (квадрат - 1, детерминант - 2, транспонировать - 3) "))
start_time = time.time()
if action == 1:
    module.sqrMatrix(matrix)
    res = time.time() - start_time
    print(float(res), " наша функия")
    module.sqrMatrixNum(matrix)
    print(float(time.time() - start_time - res))
elif action == 2:
    module.detMatrix(matrix)
    res = time.time() - start_time
    print(float(res), " наша функция")
    module.detMatrixNum(matrix)
    print(float(time.time() - start_time - res), " numpy")
elif action == 3:
    module.transMatix(matrix)
    res = float(time.time() - start_time)
    print(float(res), " 1")
    module.transMatixNum(matrix)
    print(float(time.time() - start_time - res))

else:
    print("Введено неизвестное действие")
