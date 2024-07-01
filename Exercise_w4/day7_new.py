import numpy as np


def getMaxPooling(a, step=2):
    print(a)
    rows_a = len(a)
    cols_a = len(a[0])
    result_height = rows_a - step
    result_width = cols_a - step
    result = np.zeros((result_height, result_width))
    for i in range(result_height):
        for j in range(result_width):
            row = i*step  # get row of a
            col = j*step  # get col of a#
            sublist = a[row:row+step, col:col+step]
            amax = np.max(sublist)
            result[i][j] = amax

    return result


def getAveragePooling(a, step=2):
    rows_a = len(a)
    cols_a = len(a[0])
    result_height = rows_a - step
    result_width = cols_a - step
    result = np.zeros((result_height, result_width))
    for i in range(result_height):
        for j in range(result_width):
            row = i*step  # get row of a
            col = j*step  # get col of a
            sublist = a[row:row+step, col:col+step]
            avg = np.mean(sublist)
            result[i][j] = avg

    return result


mat_a = np.array([[0, 0, 0, 4], [0, 4, 0, 2], [0, 1, 0, 2], [0, 3, 0, 2]])
# cau 1
x = getMaxPooling(mat_a, 2)
print(f'Maxpooling: {x}')
# cau 2
x = getAveragePooling(mat_a, 2)
print(f'Avergate pooling: {x}')
