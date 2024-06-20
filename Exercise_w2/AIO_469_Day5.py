# Ham tao Bag of Words
def getVocabul(data):
    aText = ""
    lenght = len(data)
    for x in data:
        aText = aText + x+" "
    aText = aText.replace(",", "")
    aText = aText.replace(".", "")
    aText = aText.replace("_", " ")
    aText = aText.replace("-", " ")
    aText = aText.split()
    aSet = set(aText)
    aText = list(aSet)
    aText.sort()
    return aText
# Lay so lan xuat hien cua cac tu trong data


def getOccur(data, aVocalbu):
    result = []
    lenght = len(aVocalbu)
    for idx in range(lenght):
        result.append(data.count(aVocalbu[idx]))
    return result


# my main
corpus = ["Tôi thích môn Toán.", "Tôi thích AI", "Tôi thích âm nhạc"]
myVocal = getVocabul(corpus)
myText = "Tôi thích AI thích Toán"
mylist = myText.split()
print(f"- {myText}: {getOccur(mylist, myVocal)}")
print(f"- Bag-of-Words:{myVocal}")
