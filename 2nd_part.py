from __future__ import print_function
from Razmeshenie import Razmeshenie_s_povtorami, Razmeshenie_bez_povtorov

print ("Дана задача: \n В отделении связи поступило m телеграмм, которые случайным образом \n распределяются по n каналам связи(n > m). Найти вероятность события A - на \n каждый канал придётся не больше одной телеграммы.")

print ("Для решения данной задачи воспользуемся следующей формулой: \n P(A) = A[n, m]/A(повторы)[n, m]")

print ("Введите значения n и m")
print ("n = ", end = '')
n = int(input(""))
print ("m = ", end = '')
m = int(input(""))

A1 = Razmeshenie_s_povtorami(n, m)
A = Razmeshenie_bez_povtorov(n, m)

P = A/A1

print ("P(A) =", "%.20f" % P)
