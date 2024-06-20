stop_words = ["I", "love", "and", "to"]
input = "I love AI and listen to music"
data = input.split(' ')
# cách 1
result = [item for item in data if stop_words.count(item) == 0]
print(result)
# cách 2
result = []
for item in data:
    if stop_words.count(item) == 0:
        result.append(item)
print(result)
