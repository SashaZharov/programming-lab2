from random import randint
import numpy as np

def rand():
    n = randint(1, 30)
    return n

def aprok(s, f, arr):
    k = 0
    b = 0
    if f == len(arr):
        f -= 1
    if arr[f] == None:
        k = arr[s - 1] - arr[s - 2]
        b = arr[s - 1] - k * (s - 1)
        
    else:
        if s == 0:
           b = arr[f]
        else:
            k = (arr[f] - arr[s - 1])/(f - s + 1)
            b = arr[s - 1] - k * (s - 1)
    for i in range(s, f):
        arr[i] = int(k*i + b)
    if arr[f] == None:
        arr[f] = int(k*f + b)


n = int(input("Введите размерность таблицы "))
table = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        table[i][j] = randint(1, 30)

# Удаление элементов
count = 0
while count != 10:
    i = randint(0, n-1)
    j = randint(0, n-1)
    if table[i][j] != None:
        table[i][j] = None
        count += 1

# Перобразование таблицы в массив
lst = []
for i in table:
    lst += i
print(lst)


# Метод апроксимации
i = 0
s = 0
f = 0
while i < n**2:
    while i < n**2 and lst[i] == None:
        i += 1 
        f = i 
    if s != f:
        aprok(s, f, lst)


    i += 1
    s = i
    f = i
print(lst)




            


            
