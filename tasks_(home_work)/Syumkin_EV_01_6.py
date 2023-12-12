#1Дан двумерный массив размером 3x3.
#  Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива.
#  Вывести полученные значения.
'''from random import randint

n = 3

matrix = [[randint(-100, 101) for j in range(n)]for i in range (n)]
for i in range(n):
  for j in range(n):
    print(matrix[i][j], end = ' ')
  print()
max_third = max(matrix[0][2], matrix[1][2], matrix[2][2])
max_second = max(matrix[1][0], matrix[1][1], matrix[1][2])
print('Максимальное значение в третьем столбце:', max_third)
print('Максимальное значение во второй строке:', max_second)
'''

#2Дан двумерный массив размером mxn.
#Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями.
#Вывести оба массива.
'''
from random import randint

m = int(input('введите количество строк массива:'))
n = int(input('введите колчество столбцов массива:'))

for i in range(m):
    for j in range(n):
        matrix = [[randint(-100, 101) for j in range(n)]for i in range(m)]
print(matrix)
for i in range(m):
  for j in range(n):
    if matrix[i][j] > 0:
      matrix[i][j] = 1
    else:
      matrix[i][j] = 0
print(matrix)
'''


#3 Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом,
#т.е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
'''
from random import randint


n = int(input('введите размерность матрицы:'))

for i in range(n):
    for j in range(n):
        matrix = [[randint(1,2) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()

sum_matrix = sum(matrix[0])
magic_square = True
col_sum = sum(matrix[j])

for i in range(n):
    if sum(matrix[i]) != sum_matrix:
        magic_square = False
        break

for j in range(n):
    if col_sum != sum_matrix:
        magic_square = False
        break

if magic_square:
    print("магический квадрат")
else:
    print("не магический квадрат")
'''



#Определить, является ли заданная целая квадратная матрица n-го порядка симметричной
#(относительно главной диагонали).
from random import randint


n = int(input('введите размерность матрицы:'))

for i in range(n):
    for j in range(n):
        matrix = [[randint(1,2) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()
symmetric = True
for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("матрица симметрична относительно главной диагонали")
else:
    print("матрица не симметрична относительно главной диагонали")