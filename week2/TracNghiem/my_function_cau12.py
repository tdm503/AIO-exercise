def my_function(data):
    var = []
    for i in data :
        if i % 3 == 0:
            var.append(i)
    return var

print(my_function([1,2,3,5,6]))