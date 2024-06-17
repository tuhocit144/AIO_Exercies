# khoi tao ma tran D
def levenshtein_distance(source, target):
    D = []
    M = len(source)+1  # M hang
    N = len(target)+1  # N cot
    D = [[0]*N for i in range(M)]
    # B2: cap nhat hang dau tien
    a = 0
    b = 0
    c = 0
    for k in range(N):
        D[0][k] = k
        if k < M:
            D[k][0] = k
    # B3 tinh toan cac gia tri bat dau tu D(1,1)
    for t1 in range(1, M):
        for t2 in range(1, N):
            if (source[t1-1] == target[t2-1]):
                D[t1][t2] = D[t1-1][t2-1]
            else:
                a = D[t1][t2-1]
                b = D[t1-1][t2]
                c = D[t1-1][t2-1]
                if (a <= b and a <= c):
                    D[t1][t2] = a+1
                elif (b <= a and b <= c):
                    D[t1][t2] = b+1
                else:
                    D[t1][t2] = c+1
    return D[M-1][N-1]


# ham main
assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hola", "hello"))
