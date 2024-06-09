def my_function(n):
    min_value = 1e9
    for value in n:
        min_value = min(min_value,value)
    return min_value

my_list = [1,22,93,-100]
assert my_function(my_list) == -100

my_list = [1,2,3,-1]
print(my_function(my_list))