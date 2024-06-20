# cau 1: tạo list có 10 phần tử từ 1 đến 10
lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cau 2: in ra ket qua 5 phan tu dau tien
print('Câu 2:', end=" ")
for index in range(0, 6):
    print(lst_data[index], end=" ")
# câu 3: in ra kết quả phần tử có giá trị không chia hết cho 2 (kết hợp for)
print('\nCâu 3: ', end=" ")
for x in lst_data:
    if x % 2 != 0:
        print(x, end=" ")
# câu 4: In ra kết quả tổng các giá trị trong list (dùng kết hợp với vòng lặp for)
print('\nCâu 4: ', end="")
sum = 0
for x in lst_data:
    sum = sum+x
print(sum)
