import torch
b=0.05
tensor = torch.ones(4, 4)
tensor[:,3] = 0
print(tensor, "\n")
tensor.add_(5,alpha=-1)
print(tensor)