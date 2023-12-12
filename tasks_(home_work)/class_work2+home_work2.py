'''
1.Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран,
сообщая об ошибке в случае деления на ноль.
'''

a = float(input("a ="))
b = float(input("b ="))
try:
    print(a/b)
except ZeroDivisionError:
    print("Деление на ноль")


'''
2.Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю,
если сумма покупки превышает 20 у.е. Сумму покупки ввести с клавиатуры,
а результаты округлить до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки.
'''

sum = float(input('Сумма покупки без скидки:'"$"))
if sum>20:
    sum1 = sum / 100 * 65
    print(round(sum1 ,2))
else:
    print(sum)

'''
3. Напишите скрипт, который по введенному пользователем числу от 1 до 12,
будет выводить на экран сообщение в виде названия месяца и времени года.
Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.
'''
month = int(input("Введите месяц от 1 до 12:"))
if month == 12 :
    print("december,"+"winter")
elif month ==1:
    print("january,"+"winter")
elif month ==2:
    print("february,"+"winter")
else:
    if month == 3 :
        print("march,"+"spring")
    elif month ==4:
        print("april,"+"spring")
    elif month ==5:
        print("may,"+"spring")
    else:
        if month == 6 :
            print("june,"+"summer")
        elif month ==7:
            print("july,"+"summer")
        elif month ==8:
            print("august,"+"summer")
        else:
            if month == 9 :
                print("september,"+"autumn")
            elif month ==10:
                print("october,"+"autumn")
            elif month ==11:
                print("november,"+"autumn")
            else:
                print("Измените диапозон месяцев от 1 до 12")

'''
                                                                                        класс ворк:
1.Написать программу, которая считает дискриминант, выводит корни и их количество.
'''
import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

discr = b**2 - 4*a*c
print(discr)
if discr > 0 and a !=0:
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b - math.sqrt(discr)) / (2*a)
    print("Решение имеет два корня:",x1 , x2)
elif discr == 0:
    x = -b / (2*a)
    print("Решение имеет один корень: ", x)
else:
    print("решение не имеет корней")

'''
5.Написать программу через цикл, которая будет склонять слово "коробка" и выводить в столбец от первого до n-го введённого номера.
'''
n = int(input("Введите число: "))

for i in range(1, n+1):
    if i % 10 == 1 and i % 100 != 11:
        print(f"{i} коробка")
    elif i % 10 in [2, 3, 4] and i % 100 not in [12, 13, 14]:
        print(f"{i} коробки")
    else:
        print(f"{i} коробок")






