def ex1(num_list, k):
    result = []
    if (len(num_list) >= k):
        for i in range(len(num_list)-k+1):
            sub_list = num_list[i:i+k]
            result.append(max(sub_list))
    return result

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
# Output: [5, 5, 5, 5, 10, 12, 33, 33]
result = ex1(num_list, 3)
print(result)