import math

def combinations_without_repetition(n, m):                                  # отдельная функция для подсчёта сочетаний без повторений
    return (math.factorial(n)/(math.factorial(m)*math.factorial(n-m)))      # формула сочетаний без повторений

print("Введите значения n и m")                                             #
print("n = ", end = '')                                                     #
n = int(input(""))                                                          # просим ввести значения
print("m = ", end = '')                                                     #
m = int(input(""))                                                          #

if m > n:                                                                   # проверяем  m > n или нет
                                                                            
    print("m должно быть меньше или равно n ")                              
    print("Введите значения n и m")                                         #
    print("n = ", end = '')                                                 # повторныый ввод, если значчения не удволетворяют условию
    n = int(input(""))                                                      #
    print("m = ", end = '')                                                 #
    m = int(input(""))                                                      #
    
print ("c = ", int(combinations_without_repetition(n, m)))                  # вывод результата
