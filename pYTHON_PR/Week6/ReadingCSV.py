import numpy as np
import csv
'''taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_shape = taxi.shape
print(taxi_shape)'''


f=open("nyc_taxis.csv","r")
taxis_list=list(csv.reader(f))
'''taxis_list=taxis_list[1:]
converted_taxis_list=[]
for row in taxis_list:
    converted_row=[]
    for item in row:
        converted_row.append(float(item))
    converted_taxis_list.append(converted_row)

taxis=np.array(converted_taxis_list)
'''
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_shape = taxi.shape

print(taxi)
print(taxi_shape)
