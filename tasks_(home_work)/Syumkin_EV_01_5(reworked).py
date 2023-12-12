# 1
def dl(x1, y1):
    return (x1**2+y1**2)**0.5

total = 0
x, y, a, b = int(input()), int(input()), int(input()), int(input())
r = ((x-a)**2+(y-b)**2)**0.5
for i in range(3):
    x1, y1 = int(input()), int(input())
    if dl(x1, y1) < r:
      total += 1
print('Количество точек, которые находятся внутри окружности', total)

# 2

from random import randint

def s(x):
    return sum(x)

a2 = [randint(-10**6, 10**6) for k in range(randint(1, 15))]
b2 = [randint(-10**6, 10**6) for k in range(randint(1, 15))]
c2 = [randint(-10**6, 10**6) for k in range(randint(1, 15))]

print('Сумма чисел ', s(a2), 'Среднее значение ', s(a2)/len(a2))
print('Сумма чисел ', s(b2), 'Среднее значение ', s(b2)/len(b2))
print('Сумма чисел ',  s(c2), 'Среднее значение ', s(c2)/len(c2))

# 3

def ans(a_3, b_3):
    return (a_3**2+b_3**2)**0.5

a3 = randint(1, 100)
b3 = randint(1, 100)
print(a3, 'и',  b3, 'катеты 1 треугольника')
print(ans(a3, b3), 'гипотенуза 1 треугольника')
a31 = randint(1, 100)
b31 = randint(1, 100)
print(a31, 'и',  b31, 'катеты 2 треугольника')
print(ans(a31, b31), 'гипотенуза 2 треугольника')
if ans(a3, b3) > ans(a31, b31):
    print(ans(a3, b3))
else:
    ans(a31, b31)

# 4

def f(q):
    total = 0
    for j in range(len(q)):
        total += int(q[j])**len(q)
    if total == int(a4):
        return int(a4)

k = int(input())
for kl in range(1, k+1):
    a4 = str(kl)
    s = []
    for _ in range(len(a4)):
        s.append(a4[_])
    print(f(a4))

# 5

import math

def t(w1, w2):
    tan = w1/w2
    return math.atan(tan)

x1, x2, y1, y2, z1, z2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
ans = 0
if t(x1, x2) < t(y1, y2):
    if t(z1, z2) < t(x1, x2):
        ans = t(z1, z2)
    else:
        ans = t(x1, x2)
if t(y1, y2) < t(x1, x2):
    if t(z1, z2) < t(y1, y2):
        ans = t(z1, z2)
    else:
        ans = t(y1, y2)
if t(z1, z2) < t(y1, y2):
    if t(x1, x2) < t(z1, z2):
        ans = t(x1, x2)
    else:
        ans = t(z1, z2)
if t(y1, y2) < t(z1, z2):
    if t(x1, x2) < t(y1, y2):
        ans = t(x1, x2)
    else:
        ans = t(y1, y2)
print(ans)

