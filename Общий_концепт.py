from __future__ import print_function
import math

def Razmeshenie_s_povtorami(n, m):
	return pow(n, m)

def combinations_without_repetition(n, m):                                 
	return (math.factorial(n)/(math.factorial(m)*math.factorial(n - m)))    

def sochetania_s_povtoreniami(n, m):
        return math.factorial(n + m - 1)/(math.factorial(m)*math.factorial(n - 1))

print ("Какую формулу вы хотите использовать?\n Введите 1 - размещение с повторами,\n 2 - число сочетаний без повтора,\n 3 - число сочетаний с повторениями")
print ("Formula = ", end = '')
Formula = int(input(""))

if (Formula == 1):
	print ("Вы выбрали формулу: размещение с повторами")
	print ("A = n^m")
	print ("Введите значения n и m")
	print ("n и m изменяются в пределах от (0, бесконечность)")
	print ("n = ", end = '')
	n = int(input(""))
	print ("m = ", end = '')
	m = int(input(""))
	A = Razmeshenie_s_povtorami(n, m)
	print ("A =", A)
elif (Formula == 2):
	print ("Вы выбрали формулу: число сочетаний без повтора")
	print ("C[n, m] = n! / (m! * (n-m)!)")
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

	print ("C =", int(combinations_without_repetition(n, m)))
elif (Formula == 3): #Здесь должна быть часть кода Никитоса
	print ("Вы выбрали формулу: число сочетаний с повторениями")
	print ("С[n, m] = (n + m - 1)! / (m! * (n - 1)!)")
	print ("Введите значения n и m")
        print ("n = ", end = '')
        n = int(input(""))
        print ("m = ", end = '')
        m = int(input(""))
        C = sochetania_s_povtoreniami(n, m)
        print ("С =", int(C))
