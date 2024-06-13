def find_squared_root(a):
    # khoi tao
    x = a
    n = 0
    EPSILON = 0.001
    # tính f(x)
    f = x**2-a
    # cải thiện xn+1 theo xn
    x_1 = x-f/(2*x)
    while (abs(x-x_1) >= EPSILON):
        x = x_1
        f = x**2-a
        x_1 = x-f/(2*x)
    return x_1


# hàm main
print(find_squared_root(2))
print(find_squared_root(3))
