# bai 1: slicing window
def max_kernel(data, k):
    result = []
    length = len(data)-k
    for counter in range(length+1):
        result.append(max(data[counter:counter+k]))
    return result


# ham main
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(f'input: num_list = {num_list}, k={k}')
print(f'output: {max_kernel(num_list, k)}')
