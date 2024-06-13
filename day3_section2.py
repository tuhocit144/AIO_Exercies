# Bài tập: Khởi tạo List và thao tác thêm xóa sửa trên List
# Câu 1: Tạo mới một List có tên là lst_data, gồm các số chẵn từ 1 đến 12.
lst_data = [2, 4, 6, 8, 10, 12]
# Câu 2: Xóa tất cả các số chia hết cho 3 trong lst_data vừa tạo
for x in lst_data:
    if x % 3 == 0:
        lst_data.remove(x)
print(lst_data)
# Câu 3: Thêm vào cuối lst_data các số từ 1 đến 3,
# và thêm vào vị trí index = 3 một chuỗi các số từ 6 đến 8
lst_data.extend([1, 2, 3])
for k in range(8, 5, -1):
    lst_data.insert(3, k)
print(lst_data)
# Câu 4: Nếu các số trong list lst_data chia hết cho 2
# hoặc chia hết cho 5 thì cập nhật thành số 0
lenght = len(lst_data)
for index in range(lenght):
    if lst_data[index] % 2 == 0 or lst_data[index] % 5 == 0:
        lst_data[index] = 0
print(lst_data)
