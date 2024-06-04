import math

def approx_sin(x, n):
    result = 0
    for i in range(n + 1):
        result += ((-1) ** i) / math.factorial(2 * i + 1) * (x ** (2 * i + 1))
    return result

print(round(approx_sin(3.14,10),4))
#0.0016 - q10 - a