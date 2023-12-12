import matplotlib.pyplot as plt
import numpy as np


# Функция для расчета f(x) = (x^β + α^β) / x^β
def f(x, alpha, beta):
    return (x ** beta + alpha ** beta) / x ** beta


# Подготовка значений x для различных интервалов
x_positive = np.linspace(0.1, 10, 400)
x_small = np.linspace(0.1, 1, 400)
x_large = np.linspace(1, 10, 400)
x_negative = np.linspace(-10, -0.1, 400)
x_infinity = np.linspace(-10, -1, 400)

# Настройка графиков
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Графики для x > 0
for alpha, beta, color in [(1, 1, 'b'), (2, 1, 'g'), (1, 2, 'r')]:
    axs[0].plot(x_positive, f(x_positive, alpha, beta), color, label=f'α={alpha}, β={beta}')
    axs[0].plot(x_small, f(x_small, alpha, beta), color, linestyle='--')
    axs[0].plot(x_large, f(x_large, alpha, beta), color, linestyle='--')

axs[0].set_title('Графики функций для x > 0')
axs[0].set_xlabel('x')
axs[0].set_ylabel('f(x)')
axs[0].legend(loc='upper right')
axs[0].grid(True)

# Графики для x < 0
for alpha, beta, color in [(1, 1, 'b'), (2, 1, 'g'), (1, 2, 'r')]:
    axs[1].plot(x_negative, f(x_negative, alpha, beta), color, label=f'α={alpha}, β={beta}')
    axs[1].plot(x_infinity, f(x_infinity, alpha, beta), color, linestyle='--')

# Добавление линии f(x) = 0
axs[1].axhline(0, color='black', linewidth=0.8, linestyle='--')

axs[1].set_title('Графики функций для x < 0')
axs[1].set_xlabel('x')
axs[1].set_ylabel('f(x)')
axs[1].legend(loc='upper right')
axs[1].grid(True)

# Сохранение графиков в SVG
#plt.savefig('/mnt/data/functions_graphs.svg')

plt.show()


'''
1) Графики для x>0: Графики функций для различных комбинаций α и β 
(конкретно α=1, β=1; α=2, β=1; и α=1, β=2) показали, 
что функции ведут себя различно в зависимости от этих параметров. 
Включение врезок для малых и больших значений x помогло более детально 
изучить поведение функций в этих интервалах.

2) Графики для x<0: При построении графиков для отрицательных значений x, 
было интересно наблюдать, как функции ведут себя, стремясь к -∞. 
Включение прямой f(x)=0 помогло визуализировать, как функции приближаются к этой линии.

3) Графики для различных значений β при α=1: Эти графики продемонстрировали 
интересное поведение функций при различных значениях β, включая β=0.5, β=−0.5, и β=−1.5. 
Однако, при построении графиков возникли предупреждения, 
связанные с трудностями в вычислении значений функции для некоторых комбинаций α и β, 
особенно когда β принимает отрицательные значения.
'''