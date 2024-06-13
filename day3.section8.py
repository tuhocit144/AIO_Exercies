
# tìm vị trí None đầu tiên, nếu không thấy trả về -1

def search_first(data, x):
    for a in data:
        if a == x:
            return data.index(a)
    return -1

# tìm tất cả vị trí None, nếu không thấy trả về list rỗng


def search_all(data, x):
    result = []
    length = len(data)
    for index in range(length):
        if (data[index] == x):
            result.append(index)
    return result


# ham main
# tạo list data
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
print(f'Vị trí None đầu tiên: {search_first(lst_data, None)} - ', end=' ')
print(f'Danh sách vị trí có giá trị None: {search_all(lst_data, None)}')
