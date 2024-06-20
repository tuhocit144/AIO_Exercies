# exercise 3: viet ham doc file text và tra ve dictionary tra ve so luong tu xuat hien trong 1
# chuoi voi key la tu, value la so lan xuat hien
# input: duong dan den file
# output: dictionary dem so tu
# ham doc file text
import gdown


def count_word(filePath):
    counter = {}
    f = open(filePath, 'r')
    data = f.read()
    listData = data.split()
    tmp = set(listData)
    myList = list(tmp)
    myList.sort()
    for x in myList:
        counter[x] = listData.count(x)
    return counter


# ham main
url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
file_path = 'content/P1_data01.txt'
gdown.download(url, file_path, quiet=False)

result = count_word(file_path)
print(f'result= {result}')
