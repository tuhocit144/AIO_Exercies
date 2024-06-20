# exercise 2: viet ham tra ve dictionary tra ve so luong chu xuat hien trong 1 tu
# voi key la chu cai, value la so lan xuat hien
def count_chars(data):
    character_statistic = {}
    my_list = list(data)
    for x in my_list:
        character_statistic[x] = my_list.count(x)
    return character_statistic


# ham main
string = "Happiness"
print(count_chars(string))
string = "smiles"
print(count_chars(string))
