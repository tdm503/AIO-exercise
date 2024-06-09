def sliding_window(list,k,n):
    output_list = []
    for i in range(n - k + 1):
        max_value = -1e9
        for j in range(i,i+k):
            if list[j] >= max_value:
                max_value = list[j]
        output_list.append(max_value)
    return output_list

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
output = sliding_window(num_list,k,len(num_list))
print(output)

