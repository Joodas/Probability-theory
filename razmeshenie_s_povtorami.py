from __future__ import print_function
import decimal
import math

def Razmeshenie_s_povtorami(n, m):
	return pow(n, m)

print ("Введите значения n и m")
print ("n = ", end = '')
n = int(input(""))
print ("m = ", end = '')
m = int(input(""))

A = Razmeshenie_s_povtorami(n, m)
print ("A =", A)
