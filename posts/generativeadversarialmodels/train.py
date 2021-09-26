# check python --version, conda --version

import torch
from torch import nn ## neural network module, custom layers for deep learning

class LogisticRegression(nn.Module):
    def __init__(self, input): #__init__: constructor; input: input variables for LR 
        super().__init__()
        self.log_reg = nn.Sequential(
            nn.Linear(input, 1),
            nn.Sigmoid()
            )
    def forward(self, x):
        return self.log_reg(x)


