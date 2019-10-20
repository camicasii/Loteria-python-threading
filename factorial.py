def fact(n):
    maestro = abs(n)
    num = 1
    if maestro > 0:
        for i in range(1, maestro + 1):
            num *= i
        return num
    else:
        return num
