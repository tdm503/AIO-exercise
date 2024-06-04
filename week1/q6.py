import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def relu(x):
    return max(0, x)
ALPHA = 0.01
def elu(x):
    if x <= 0 :
        return ALPHA * (math.exp(x) - 1)
    else:
        return x

def calc_activation_func(x,act_name):
    if act_name == "sigmoid":
        return sigmoid(x)
    elif act_name == "relu":
        return relu(x)
    elif act_name == "elu":
        return elu(x)

assert calc_activation_func(1,"relu") == 1
print(round(calc_activation_func(3,"sigmoid"),2))
#0.95 - q6 - A