import math
my_tuple1 = (2, 3)
my_tuple2 = (3, 6)
tong_vector = (my_tuple1[0]+my_tuple2[0], my_tuple1[1]+my_tuple2[1])
tich_vector = my_tuple1[0]*my_tuple2[0]+my_tuple1[1]*my_tuple2[1]
print(tong_vector)
print(tich_vector)
# khoảng cách của 2 vector

distance = math.sqrt((my_tuple1[0]-my_tuple2[0])** 2 + (my_tuple1[1]-my_tuple2[1])**2)
print('Khoảng cách: ', distance)
my_tuple=my_tuple1+my_tuple2
print(my_tuple.index(3))