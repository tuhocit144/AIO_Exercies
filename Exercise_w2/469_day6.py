# get zero padding
def getZeroPadding(a):
    row_a = len(a)
    col_a = len(a[0])
    a_new = [[0]*(row_a+2) for x in range(col_a+2)]
    # input data of a in a_new
    for idr in range(1, row_a+1):
        for idc in range(1, col_a+1):
            a_new[idr][idc] = a[idr-1][idc-1]
    return a_new
# tinh tich chap


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


# main
# cau 1:
mat_a = [[0, 0, 0], [0, 4, 0], [0, 1, 0]]
mat_b = [[1, 1], [1, 1]]
mat_azero = getZeroPadding(mat_a)
# print(mat_azero)
mat_convolution = getConvolutional(mat_azero, mat_b)
print(f'Cau 1: {mat_convolution}')
# cau 2:
mat_c = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
mat_convolution = getConvolutional(mat_azero, mat_c)
print(f'Cau 2: {mat_convolution}')
