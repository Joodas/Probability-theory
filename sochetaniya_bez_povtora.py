import math

def combinations_without_repetition(n, m):                                  # отдельная функция для подсчёта сочетаний без повторений
    return (math.factorial(n)/(math.factorial(m)*math.factorial(n-m)))      # формула сочетаний без повторений
