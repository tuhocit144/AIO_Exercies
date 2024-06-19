# calculte distance of 2 points
import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance_to_origin(self, a):
        d = (self.__x-a.__x)**2+(self.__y-a.__y)**2
        return math.sqrt(d)

    def __str__(self):
        return '({},{})'.format(self.__x, self.__y)


# main
O = Point(0, 0)
A = Point(1, 2)
B = Point(4, 5)
print(f'Distance from A{A} to O(0,0) is : {A.distance_to_origin(O)}')
print(f'Distance from B{B} to O(0,0) is : {B.distance_to_origin(O)}')
