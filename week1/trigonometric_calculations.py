import math


def approx_sin(x, n):
    result = 0
    for i in range(n + 1):
        result += ((-1) ** i) / math.factorial(2 * i + 1) * (x ** (2 * i + 1))
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n + 1):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n + 1):
        result += x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n + 1):
        result += x ** (2 * i) / math.factorial(2 * i)
    return result


# test
print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))
