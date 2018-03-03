import decimal #библиотека длинной арифметики
import math

def soch_bez_povtora(n, m): #отдельная функция для подсчёта сочетаний без повторений
    c = math.factorial(n)/(math.factorial(m)*math.factorial(n-m)) #формула сочетаний без повторений
    return (c)

print("Введите значения n и m")
print("n = ")
n = int(input(""))
print("m = ")
m = int(input(""))   

#проверяем  m > n или нет
if m > n:
    print("m должно быть больше или равно n ")
    print("Введите значения n и m")
    print("n = ")
    n = int(input(""))
    print("m = ")
    m = int(input(""))
    soch_bez_povtora(n, m)
else:
    soch_bez_povtora(n, m)
print(n, m)
print ("c = ", int(soch_bez_povtora(n, m))) #вывод результата
