import math

def approx_sinh(x, n):
    result = 0
    for i in range(n + 1):
        result += x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return result

print(round(approx_sinh(3.14,10),2))
#11.53 - q11 - a