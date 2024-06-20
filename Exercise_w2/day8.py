import math
# Cosine Similarity


def CosineSimilarity(A, B):
    # tinh tich vo thuong
    length = len(A)
    tmp = 0
    length_A = 0
    length_B = 0
    for idx in range(length):
        # tinh A.B
        tmp += A[idx]*B[idx]
        # tinh do lon cua A, B
        length_A += A[idx]**2
        length_B += B[idx]**2
    length_A = math.sqrt(length_A)
    length_B = math.sqrt(length_B)
    return tmp/(length_A*length_B)


# main
vector_a = [1, 2]
vector_b = [4, 5]
print(f'{CosineSimilarity(vector_a, vector_b)}')
