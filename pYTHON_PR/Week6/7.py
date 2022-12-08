import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_copy = taxi.copy()
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
jfk = taxi[taxi[:,6] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:,6] == 3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

cleaned_taxi = taxi[trip_mph < 100]

mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()
print(mean_distance)
print(mean_length)
print(mean_total_amount)
