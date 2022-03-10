import copy
import numpy as np

# Возведение в квадрат
def sqrMatrix(matrix):
    answ = [[0]*len(matrix) for i in range(len(matrix[0]))]
    if len(matrix) == len(matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                for k in range(len(matrix)):
                    answ[i][j] += matrix[i][k] * matrix[k][j]
    else:
        print("Невозможно возвести в квадрат матрицу, т.к она не квадратная")
    print(answ)


# Транспонирование матрицы
def transMatix(matrix):
    answ = [[0]*len(matrix) for i in range(len(matrix[0]))]
    if len(matrix) == len(matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                answ[i][j] = matrix[j][i]
        print(answ)
    else:
        print("Невозможно транспонировать матрицу, т.к она не квадратная")


# поиск определителя
def detMatrix(matrix):
    def minor(matrix, i, j):
        M = copy.deepcopy(matrix)
        del M[i]
        for i in range(len(matrix[0]) - 1):
            del M[i][j]
        return M

    def detM(matrix):
        m = len(matrix)
        n = len(matrix[0])
        if m != n:
            return None
        if n == 1:
            return matrix[0][0]
        k = 1
        det = 0

        for j in range(n):
            det += matrix[0][j]*k*detM(minor(matrix, 0, j))
            k *= -1
        return det

    if detM(matrix) == None:
        print("Матрица не квадратная")
    else:
        print(detM(matrix))


# Numpy

def sqrMatrixNum(m):
    A = np.array(m)
    print(np.linalg.matrix_power(A, 2))

def detMatrixNum(m):
    A = np.array(m)
    print(np.linalg.det(A))

def transMatixNum(m):
    A = np.array(m) 
    print(A.transpose())
