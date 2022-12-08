import numpy as np
import csv
'''c=np.array([80.0,103.4,96.9,200.3])
c_bool=c>100
result=c[c_bool]
print(result)'''
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
pickup_month=taxi[:,1]
january_bool=pickup_month==1
january=pickup_month[january_bool]
january_rides=january.shape[0]
february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]
print(february_rides)
