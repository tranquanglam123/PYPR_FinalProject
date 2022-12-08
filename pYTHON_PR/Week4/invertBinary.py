import numpy as np
def invert_binary(x):
    return 1-x
x=np.array([
            [1,0,0,1],
            [0,0,1,1],
            [0,0,1,1]])
print(invert_binary(x))
