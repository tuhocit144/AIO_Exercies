# phương pháp nội suy Nearest Neighbor
def NearestNeighbor(data, x):
    while (data.count(x) > 0):
        index = data.index(x)
        tmp = min(data[index-1], data[index+1])
        data[index] = tmp
    return data


lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
# áp dụng phương pháp nội suy Nearest Neighbor để gắn giá trị None có trong lst_data
print(NearestNeighbor(lst_data, None))
