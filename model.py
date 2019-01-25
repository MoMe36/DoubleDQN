import torch 
import torch.nn as nn 
import torch.nn.functional as F 
import torch.optim as optim 
from torch.distributions import Categorical 


class QNetwork(nn.Module): 

    def __init__(self, obs, ac): 

        super().__init__()

        self.model = nn.Sequential(nn.Linear(obs, 128), 
                                   nn.ReLU(), 
                                   nn.Linear(128,128), 
                                   nn.ReLU(), 
                                   nn.Linear(128, ac))

    def forward(self, x): 

        return self.model(x)