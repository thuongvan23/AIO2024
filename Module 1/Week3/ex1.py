import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x, dim=-1, keepdim=True)

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_x = torch.max(x, dim=-1, keepdim=True).values
        exp_x = torch.exp(x - max_x)
        return exp_x / torch.sum(exp_x, dim=-1, keepdim=True)

# Kiểm tra với ví dụ cụ thể
x = torch.tensor([2.0, 1.0, 0.1])

# Khởi tạo các lớp
softmax = Softmax()
softmax_stable = SoftmaxStable()

# In kết quả
print("Softmax:", softmax(x))
print("Softmax ổn định:", softmax_stable(x))
