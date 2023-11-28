import numpy as np
import torch

torch.cuda.is_available()
torch.cuda.device_count()
torch.cuda.current_device()
torch.cuda.device(0) 
torch.cuda.get_device_name(0)

device = torch.device("cuda:0")
for i in range(20):
    a[str(i)] = torch.tensor(list(np.random.random((100, 2500, 1000)).astype(np.float32)), device=device)
