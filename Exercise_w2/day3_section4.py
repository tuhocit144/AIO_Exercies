# Cho một list và số extra_candies trả về boolean list.
def getBooleanList(lst_data, extra_candies):
    max_candies = max(lst_data)+extra_candies
    result = []
    lenght = len(lst_data)
    for index in range(lenght):
        result.append(lst_data[index]+extra_candies == max_candies)
        # if lst_data[index]+extra_candies == max_candies:
        #   result.append(True)
        # else:
        #    result.append(False)
    return result


# testcase
test_case_1 = [2, 3, 5, 1, 3]
extraCandies1 = 3
print(getBooleanList(test_case_1, extraCandies1))
test_case_2 = [4, 2, 1, 1, 2]
extraCandies2 = 1
print(getBooleanList(test_case_2, extraCandies2))
test_case_3 = [12, 1, 12]
extraCandies3 = 10
print(getBooleanList(test_case_3, extraCandies3))
