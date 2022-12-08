import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_copy = taxi.copy()
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
 
taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1
 
print(taxi_modified)
