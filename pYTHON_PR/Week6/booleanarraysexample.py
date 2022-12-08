import numpy as np
'''print(type(3.5)==float)
'print(5>6)
print(np.array([2,4,6,8]) +10)
print(np.array([2,4,6,8]) <5)'''
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100
print(a_bool)
print(b_bool)
print(c_bool)
