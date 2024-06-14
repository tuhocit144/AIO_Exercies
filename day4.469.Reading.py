mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
kernal = [[2, 4], [1, 3]]


def getConvolutional(a, kernel):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_k = len(kernel)
    cols_k = len(kernel[0])
    result_height = rows_a - rows_k + 1
    result_width = cols_a - rows_k + 1
    result = [[0 for _ in range(result_width)] for _ in range(result_height)]
    for i in range(result_height):
        for j in range(result_width):
            sum = 0
            for ki in range(rows_k):
                for kj in range(cols_k):
                    sum += a[i + ki][j + kj] * kernel[ki][kj]
            result[i][j] = sum
    return result


# cau 1
x = getConvolutional(mat_a, kernal)
print(x)
# cau 2
kernal_c = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
x = getConvolutional(mat_a, kernal_c)
print(x)
