# Bước 1: Viết hàm xét số Armstrong, hàm trả về 1 nếu phần tử đang xét là số Armstrong,
# ngược lại trả về 0.
def checkArmstrong(x):
    t = x
    sum = 0
    while (t > 0):
        k = t % 10
        sum = sum+k**3
        t = t//10
    if sum == x:
        return 1
    else:
        return 0

# Bước 2: Chạy vòng lặp qua tất cả các phần tử của list.
test_case1 = [130, 270, 153, 407, 177, 371, 1000, 1634, 370]
result = []
# Bước 3: Xét điều kiện nếu phần từ là số Armtrong thì lưu vào 1 list khác.
for x in test_case1:
    if checkArmstrong(x):
        result.append(x)
# Bước 4: In ra list kết quả chứa các số Armstrong đã xét.
print('Các số Armstrong có trong list là: ', result)
