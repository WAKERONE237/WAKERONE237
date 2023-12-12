'''
Задание 1.Создать объект pandas Series из листа, объекта NumPy, и словаря
'''
import numpy as np
import pandas as pd

list = list(['Mariia', 'Ivan', 'Anna'])
arr = np.arange(1,4)
dict = dict(zip(list, arr))
 
a = pd.Series(dict)

print('Имя и порядковый номер:') 
print(a)


'''
Задание 2. Получить не пересекающиеся элементы в двух объектах Series
'''
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([3, 4, 5, 6, 7])

a_not_inter = a[~a.isin(b)]
b_not_inter = b[~b.isin(a)]

result = pd.concat([a_not_inter, b_not_inter])

print('Series #1:', a)
print('Series #2:', b)
print('Не пересекающиеся элементы Series #1 и Series #2:', result)


'''
Задание 3. Узнать частоту уникальных элементов объекта Series (гистограмма)
'''
import pandas as pd
import matplotlib.pyplot as plt

elements = pd.Series([1, 2, 2, 3, 3, 3, 3, 4, 4, 5])
value_counts = elements.value_counts()

plt.bar(value_counts.index, value_counts, color = 'slateblue')
plt.title('Гистограмма уникальных элементов')
plt.xlabel('Уникальные элементы')
plt.ylabel('Частота') 
plt.show()


'''
Задание 4. Объединить два объекта Series вертикально и горизонтально
'''
import pandas as pd
a = pd.Series([1, 2, 3])
b = pd.Series([4, 5, 6])

print('Series #1:', a)
print('Series #2:', b)

vertical = pd.concat([a, b], axis=0)
print("Вертикальное объединение:")
print(vertical)

horizontal = pd.concat([a, b], axis=1)
print("Горизонтальное объединение:")
print(horizontal)


'''
Задание 5. Найти разность между объектом Series и смещением объекта Series на n
'''
import pandas as pd
s = pd.Series([1, 3, 5, 9, 13])
print('Series:')
print(s)

n = int(input('Укажите количество позиций смещения объекта Series:'))
result = s.diff(periods=n)

print('Разность между объектом Series и смещением объекта Series на', n, ':')
print(result)
