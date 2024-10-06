def check_the_number(n):
    list_of_number = []
    result = ""
    for i in range(1, 5):
        list_of_number.append(i)
    if n in list_of_number:
        result = "True"
    if n not in list_of_number:
        result = "False"
    return result


n = 7
assert check_the_number(n) == "False"

n = 2
result = check_the_number(n)
print(result)
