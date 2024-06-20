# Câu 1: Tạo mới một List có tên là lst_data, gồm các số từ 1 đến 10.
lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Câu 1:", lst_data)
# Câu 2: Tính giá trị trung vị từ lst_data vừa tạo. (Không sử dụng numpy)
lst_data.sort()
length = len(lst_data)
k = length//2
if length % 2 == 0:
    m = (lst_data[k-1]+lst_data[k])/2
else:
    k = (length+1)//2
    m = lst_data[k-1]
print('Câu 2. Median: ', m)
# Câu 3: Lọc các giá trị số lẻ trong lst_data và lưu ra list mới có tên là:
# lst_odd_filter với thứ tự giảm dần
# ( Sử dụng phương thức reverse=True trong hàm sort/sorted).
lst_odd_filter = []
for x in lst_data:
    if x % 2 != 0:
        lst_odd_filter.append(x)
lst_odd_filter.sort(reverse=True)
print('Câu 3:', lst_odd_filter)
