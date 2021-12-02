import torch
import numpy as np
A=np.array([1,2,2,3])
print(A)
A=torch.tensor(A)
print(A)
B=np.array([1,2,3,3])
B=torch.from_numpy(B)
ALL= (A==B).sum()
ALLA= ALL.item()
print(ALL)
print(ALLA)
C=torch.tensor([1,1,1,1,1],dtype=torch.float32)
print(C)