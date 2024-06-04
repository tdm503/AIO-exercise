import math

def approx_cosh(x, n):
    result = 0
    for i in range(n + 1):
        result += x ** (2 * i) / math.factorial(2 * i)
    return result

print(round(approx_cosh(3.14,10),2))
#11.57 -q12 - a