from random import randint


n = int(input("Введите размерность таблицы "))
table = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        table[i][j] = randint(1, 30)

for i in range(n):
    M = 0
    D = 0
    N = 0
    for j in range(n):
        M += (1/30)*table[i][j]
        N += table[i][j]
    avrg = N/n
    for j in range(n):
        D += (avrg - table[i][j])**2

    print(table[i], M, D)

