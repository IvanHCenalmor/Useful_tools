import numpy as np
import torch
device = torch.device("cuda:0")
for i in range(20):
    a[str(i)] = torch.tensor(list(np.random.random((100, 2500, 1000)).astype(np.float32)), device=device)
