import numpy as np
def alternate_ones_zeros(num_rows, num_cols):
    x=np.zeros((num_rows, num_cols))
    x[::2, ::2] = 1
    x[1::2,1::2]=1
    return x
x = alternate_ones_zeros(5,6)
print(x)
