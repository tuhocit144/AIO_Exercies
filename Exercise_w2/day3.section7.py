def tokeNization(data):
    result = []
    rows = len(data)
    for id in range(rows):
        words = data[id].split(' ')
        result.extend(words)
    # loại bỏ từ trùng nhau
    vocabulary = []
    [vocabulary.append(x) for x in result if x not in vocabulary]
    vocabulary.sort()
    return vocabulary


def getVector(data, voca):
    result = []
    lst = data.split(' ')
    len_voca = len(voca)
    for index in range(len_voca):
        result.append(lst.count(voca[index]))
    return result


corpus = ['Tôi thích Toán', 'Tôi thích AI', 'Tôi thích âm nhạc']
lst_vocabulary = tokeNization(corpus)
inputText = 'Tôi thích AI thích Toán'
print(f'{inputText}: {getVector(inputText, lst_vocabulary)}')
print(f'Bag-of-Words:{lst_vocabulary}')
