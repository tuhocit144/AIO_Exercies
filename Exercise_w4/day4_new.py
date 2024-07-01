import numpy as np
mat_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernal = np.array([[2, 4], [1, 3]])


def getConvolutional(a, kernel):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_k = len(kernel)
    cols_k = len(kernel[0])
    result_height = rows_a - rows_k + 1
    result_width = cols_a - rows_k + 1
    result = np.zeros((result_height, result_width))
    for i in range(result_height):
        for j in range(result_width):
            Slider = a[i:i+rows_k, j:j+cols_k]

            result[i][j] = np.sum(Slider*kernel)

    return result


print(getConvolutional(mat_a, kernal))
c = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
print(getConvolutional(mat_a, c))
