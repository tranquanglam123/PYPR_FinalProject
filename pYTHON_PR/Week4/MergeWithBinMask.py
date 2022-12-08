import numpy as np
def merge_with_binary_mask(x,y,binary_mask):
    return x*[1 - binary_mask] + y*binary_mask
x=np.array([[4,2,3,6],[7,6,8,9],[8,1,4,5]])
y=np.array([[0,9,4,1],[3,5,3,2],[4,7,9,0]])
binary_mask=np.array([[0,1,1,0],[1,0,1,0],[0,0,1,1]])
print(merge_with_binary_mask(x,y,binary_mask))
