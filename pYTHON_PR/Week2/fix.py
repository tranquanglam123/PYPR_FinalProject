import numpy as np
'''def framed_zeros(num_rows, num_cols):
        x=np.ones((num_rows, num_cols))
        x[1:-1, 1:-1] = 0
        return x
x = framed_zeros(6,5)
print(x)'''
'''def alternate_ones_zeros(num_rows, num_cols):
        x =np.zeros((num_rows, num_cols))
        x[::2, ::2]=1
        x[1::2,1::2]=1
        return x
x = alternate_ones_zeros(5,6)'''
'''def invert_binary(x):
        return 1-x
x=np.array([
        [1,0,0,1],
        [0,0,1,1],
        [0,0,1,1]
        ])
print(invert_binary(x))'''
def merge_with_binary_mask(x, y, binary mask):
        return x * (1-binary_mask) + y * binary_mask

x = np.aray([[4,2,3,6],[7,6,8,9],[8,1,4,5]])
y=np.array([[0,9,4,1],[3,5,3,2],[4,7,9,0]])
binary_mask=np.array([[0,1,1,0],[1,0,1,0]
        
