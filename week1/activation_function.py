import math
ALPHA = 0.01


def is_number(n):
    return isinstance(n, (int, float))


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def elu(x):
    if x <= 0:
        return ALPHA * (math.exp(x) - 1)
    else:
        return x


def calc_activation_func(x, act_name):
    if not is_number(x):
        print("x must be a number")
        return
    if act_name != "sigmoid" and act_name != "relu" and act_name != "elu":
        print("ten_function_user is not supported")
        return
    if act_name == "sigmoid":
        print(f"sigmoid: f({x})={sigmoid(x)}")
    elif act_name == "relu":
        print(f"relu: f({x})={relu(x)}")
    elif act_name == "elu":
        print(f"elu: f({x})={elu(x)}")


calc_activation_func(-4, "elu")
calc_activation_func(3, "relu")
calc_activation_func(-4, "sigmoid")
