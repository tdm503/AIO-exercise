def my_function(n):
    max_value = -1e9
    for value in n:
        max_value = max(value, max_value)
    return max_value


my_list = [1, 9, 9, 0]
print(my_function(my_list))
