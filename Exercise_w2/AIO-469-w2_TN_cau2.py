# exercise 2: viet ham tra ve dictionary tra ve so luong chu xuat hien trong 1 tu
# voi key la chu cai, value la so lan xuat hien
def character_count(data):
    character_statistic = {}
    my_list = list(data)   
    for x in my_list:
        character_statistic[x] = my_list.count(x)
    return character_statistic


# ham main
assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
