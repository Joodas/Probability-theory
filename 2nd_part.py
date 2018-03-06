from __future__ import print_function 
from razmeshenie_s_povtorami import Razmeshenie_s_povtorami
from sochetaniya_bez_povtora import combinations_without_repetition

print ("Дана задача: \n В отделении связи поступило m телеграмм, которые случайным образом \n распределяются по каналам связи (n > m). Найти вероятность события A - на \n каждый канал придётся не больше одной телеграммы.")

print ("Для решения данной задачи воспользуемся следующей формулой: \n P(A) = C[1, n]*C[l, n - 1]*C[l, n - 2]*...*C[1, n - r + 1]*C[0, n - r]/A[n, m]")

print ("Введите значения n и m")
print ("n = ", end = '')
n = int(input(""))
print ("m = ", end = '')
m = int(input(""))

if (m > n):
    print ("m должно быть меньше или равно n")
    print ("Введите значения n и m")
    print ("n = ", end = '')
    n = int(input(""))
    print ("m = ", end = '')
    m = int(input(""))
C_n = 1
while (n >= 2):
    C = int(combinations_without_repetition(n, m - 3))
    C_n = C * C_n
    n = n - 1
P = C_n/Razmeshenie_s_povtorami(n, m)
print ("P(A) = ", P)
