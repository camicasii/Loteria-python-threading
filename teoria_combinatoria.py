import math
"""Permutacion P = n!"""
def permutacion(n):
    n_perm = math.factorial(n)
    return n_perm
"""
Variacion rVn =n.(n-1).(n-2)...(n-r+1)
"""
def variacion(n, r):
    n_abs = abs(n)
    r_abs = abs(r)
    num = 1
    for i in range(r_abs):
        if i == 0:
            num = n_abs
            continue
        else:
            valor = n_abs - i
            num *= valor
    return num

"""
    rCn = n!/r!(n-r)!
"""

def combinacion(n, r):
    n_fact = math.factorial(n)
    r_fact = math.factorial(r)
    rn = n - r
    rn_fact = math.factorial(rn)
    res = n_fact / (r_fact * rn_fact)
    return res

print(combinacion(24,15))