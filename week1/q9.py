import math
def approx_cos(x,n):
    result = 0
    for i in range(n + 1):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i) 
    return result
print(round(approx_cos(3.14,10),2))
# -1.0 - q9- c
