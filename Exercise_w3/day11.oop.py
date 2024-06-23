import torch
from torch import nn
import math


class ReLUActivateFunction(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        zeros = torch.zeros_like(x)
        print('zeros:',zeros)
        return torch.maximum(x, zeros)


class SigmoidActivateFunction(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return (1/(1+torch.exp(-x)))


    # test
Relua = ReLUActivateFunction()
print(f'Relua: {Relua(torch.Tensor([1, -5, 1.5, 2.7, -5]))}')
Sigmoid = SigmoidActivateFunction()
print(f'Sigmoid: {Sigmoid(torch.Tensor([1, -5, 1.5, 2.7, -5]))}')
