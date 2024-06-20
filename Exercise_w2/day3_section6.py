def getMedian(data):
    data.sort()
    length = len(data)
    k = length//2
    if length % 2 == 0:
        m = (data[k-1]+data[k])/2
    else:
        k = (length+1)//2
        m = data[k-1]
    return m


# Câu 1: Tạo mới một List có tên là lst_data, gồm các số từ 1 đến 10.
lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Câu 1:", lst_data)
# Câu 2: Tính giá trị trung bình cho các số lẻ và số chẵn từ lst_data vừa tạo.
# (Không sử dụng numpy)
lst_odd = [x for x in lst_data if x % 2 != 0]
lst_even = [x for x in lst_data if x % 2 == 0]
meanEven = sum(lst_even)/len(lst_even)
meanOdd = sum(lst_odd)/len(lst_odd)
print(f'Câu 2: Mean lẻ:{meanOdd} - Mean chẵn: {meanEven}')
# Câu 3: Tính giá trị trung bình và trung vị cho tất cả
# dữ liệu trong lst_data và cho nhận xét.
mean = sum(lst_data)/len(lst_data)
median = getMedian(lst_data)
if (mean == median):
    print('Câu 3: Mean = Median =', mean)
else:
    print(f'Câu 3: Mean {mean} != Median ={median}')
