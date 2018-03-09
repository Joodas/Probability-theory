import math

def Razmeshenie_s_povtorami(n, m):
	return pow(n, m)

def Razmeshenie_bez_povtorov(n, m):
        return math.factorial(n)/math.factorial(n-m)
