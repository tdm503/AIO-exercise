def my_function(x):
    res = ''
    for i in range(len(x) - 1, -1, -1):
        res += x[i]
    return res


x = 'apricot'
print(my_function(x))
