lst_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(lst_data)
cols = len(lst_data[0])
sub_list = []
for idr in range(rows):
    sub_row = []
    for idc in range(cols):
        if (idc == 0 or idc == 2):
            sub_row.append(lst_data[idr][idc])
    sub_list.append(sub_row)
print(sub_list)
