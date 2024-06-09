def max_kernel(list,k):
    output_list = []
    n = len(list)
    for i in range(n - k + 1):
        max_value = -1e9
        for j in range(i,i+k):
            if list[j] >= max_value:
                max_value = list[j]
        output_list.append(max_value)
    return output_list

assert max_kernel([3,4,5,1,-44],3) == [5,5,5]
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
print(max_kernel(num_list,k))
