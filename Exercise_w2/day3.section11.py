# tính tổng 2 ma trận
def Tong2MaTran(a, b):
    result = []
    rows = len(a)
    cols = len(a[0])
    for idr in range(rows):
        row_tmp = []
        for idc in range(cols):
            t = a[idr][idc]+b[idr][idc]
            row_tmp.append(t)
        result.append(row_tmp)
    return result

# hieu 2 ma tran


def Hieu2MaTran(a, b):
    result = []
    rows = len(a)
    cols = len(a[0])
    for idr in range(rows):
        row_tmp = []
        for idc in range(cols):
            t = a[idr][idc]-b[idr][idc]
            row_tmp.append(t)
        result.append(row_tmp)
    return result
# Tích 2 ma trận


def Tich2MaTran(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for idra in range(rows_a):
        for idrb in range(cols_b):
            for idc in range(cols_a):
                result[idra][idrb] += a[idra][idc]*b[idc][idrb]
    return result


mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat_b = [[2, 4, 6], [1, 3, 5], [1, 0, 1]]
# tong 2 ma tran
print(f'Tổng: {Tong2MaTran(mat_a, mat_b)}')
print(f'Hiệu: {Hieu2MaTran(mat_a, mat_b)}')
print(f'Dot product: {Tich2MaTran(mat_a, mat_b)}')
