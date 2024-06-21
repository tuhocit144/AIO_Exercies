import torch.nn as nn
import math


class ReLUActivateFunction(nn.Module):
    def __init__(self, x):
        self.__x = x

    def __call__(self):
        a = []
        length = len(self.__x)
        for idx in range(length):
            if (self.__x[idx] > 0):
                a.append(self.__x[idx])
            else:
                a.append(0)
        return a


class SigmoidActivateFunction(nn.Module):
    def __init__(self, x):
        self.__x = x

    def __call__(self):
        a = []
        length = len(self.__x)
        for idx in range(length):
            a.append(round(1/(1+math.exp(-self.__x[idx])), 4))
        return a


    # test
Relua = ReLUActivateFunction([1, -5, 1.5, 2.7, -5])
print(Relua())
Sigmod = SigmoidActivateFunction([1, -5, 1.5, 2.7, -5])
print(Sigmod())
