import math
ALPHA = 0.01
def calc_elu(x):
    if x <= 0 :
        return ALPHA * (math.exp(x) - 1)
    else:
        return x
assert round(calc_elu(1)) == 1
print(round(calc_elu(-1),2))
#-0.01 - q5 - B