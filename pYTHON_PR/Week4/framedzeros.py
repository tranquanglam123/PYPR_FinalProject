import numpy as np
def framed_Zeros(num_rows, num_cols):
    x=np.ones((num_rows, num_cols))
    x[1:-1,1:-1]=0
    return x
x= framed_Zeros(6,5)
print(x)
